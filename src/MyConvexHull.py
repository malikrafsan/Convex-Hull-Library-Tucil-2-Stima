import sys
import math


class MyConvexHull:
    """A class for solving the convex hull classification problem using 
    divide and conquer algorithm.

    Attributes
    ----------
    simplces : list
        list of simplices, list of lists of two elements, containing the 
        indices of the two connected points on convex hull
    _points : list
        list of points for classification, list of lists of two 
        elements, containing the x and y coordinates of the point
    _sorted_points : list
        list of points sorted ascending by x coordinate then by y 
        coordinate, list of lists of two elements, containing the x and 
        y coordinates of the points
    """

    simplices = []
    _points = []
    _sorted_points = []

    def __init__(self, points):
        """Constructor for MyConvexHull class

        @type points: list
        @param points: list of points for classification
        """
        
        if (len(points) <= 1):
            raise Exception("The number of points must be greater than 1")

        self.simplices = []
        self._sorted_points = []

        # add index to points
        self._points = [[x[0], x[1], idx] for idx, x in enumerate(points)]
        
        self._sorted_points = self._qsort(self._points)
        self._solve_convex_hull()

    def _solve_convex_hull(self):
        """Solve the convex hull classification using divide and conquer 
        algorithm. 

        For more details about the algorithm, see:
        https://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2021-2022/Algoritma-Divide-and-Conquer-(2022)-Bagian4.pdf
        """

        n = len(self._sorted_points)
        p1 = self._sorted_points[0]
        pn = self._sorted_points[n - 1]

        upper_points = []
        lower_points = []

        for i in range(1, n-1):
            det = self._compare(p1, pn, self._sorted_points[i])

            if (det > 0):
                upper_points.append(self._sorted_points[i])
            elif (det < 0):
                lower_points.append(self._sorted_points[i])

        self._create_hull(upper_points, p1, pn, False)
        self._create_hull(lower_points, p1, pn, True)

    def _get_dist(self, p1, pn, point):
        """Calculate the distance between a point and the line defined 
        by two points

        @type p1: list
        @param p1: first point of the line
        @type pn: list
        @param pn: second point of the line
        @type point: list
        @param point: a point whose distance is calculated from the line
        @rtype: list
        @returns: distance between the point and the line
        """

        num = abs((pn[0] - p1[0])*(p1[1] - point[1]) -
                  (p1[0] - point[0]) * (pn[1] - p1[1]))
        denom = ((pn[0] - p1[0])**2 + (pn[1] - p1[1])**2) ** 0.5

        if (denom <= sys.float_info.min and denom >= -sys.float_info.min):
            return num / denom
        else:
            # handle case where denom is very close to zero
            return (num + sys.float_info.min) / (denom + sys.float_info.min)

    def _length_square(self, p1, p2):
        """Calculate the square of the distance between two points

        @type p1: list
        @param p1: first point
        @type p2: list
        @param p2: second point
        @rtype: float
        @returns: square of the distance between the two points
        """

        xDiff = p1[0] - p2[0]
        yDiff = p1[1] - p2[1]
        return xDiff * xDiff + yDiff * yDiff

    def _calc_angle(self, p1, pn, point):
        """Calculate the angle on p1 between three point

        @type p1: list
        @param p1: point of whose angle is to be calculated
        @type p2: list
        @param p2: second point
        @type point: list
        @param point: third point
        @rtype: float
        @returns: angle between point, p1, and pn
        """

        a2 = self._length_square(pn, point)
        b2 = self._length_square(p1, pn)
        c2 = self._length_square(p1, point)

        b = math.sqrt(b2)
        c = math.sqrt(c2)

        try:
            alpha = math.acos((b2 + c2 - a2) / (2 * b * c))
        except ValueError:
            # handle case where angle is very close to 0 degree
            if ((b2 + c2 - a2) / (2 * b * c) > 1):
                alpha = math.acos(1)
            else:
                alpha = math.acos(-1)

        return alpha * 180 / math.pi

    def _create_hull(self, points, p1, pn, isLower):
        """Create the convex hull recursively. If points is empty, add 
        p1 and pn to simplices as solutions for convex hull.

        @type points: list
        @param points: list of points for classification
        @type p1: list
        @param p1: most left and bottom point
        @type pn: list
        @param pn: most right and top point
        """

        if (len(points) != 0):
            idx_extreme_point = 0
            cur_dist = self._get_dist(p1, pn, points[0])
            cur_angle = self._calc_angle(p1, pn, points[0])

            for i in range(1, len(points)):
                new_dist = self._get_dist(p1, pn, points[i])
                if (new_dist > cur_dist):
                    cur_dist = new_dist
                    idx_extreme_point = i
                elif (new_dist == cur_dist):
                    # compare angle (between current pmax with pmax candidate) and p1 and pn
                    new_angle = self._calc_angle(p1, pn, points[i])
                    if (new_angle > cur_angle):
                        cur_angle = new_angle
                        idx_extreme_point = i

            upper_points = []
            lower_points = []

            for i in range(len(points)):
                if i != idx_extreme_point:
                    det1 = self._compare(
                        p1, points[idx_extreme_point], points[i])
                    det2 = self._compare(
                        points[idx_extreme_point], pn, points[i])

                    if (isLower):
                        det1 = -1 * det1
                        det2 = -1 * det2

                    if det1 > 0:
                        upper_points.append(points[i])
                    elif det2 > 0:
                        lower_points.append(points[i])

            # solve recursively
            self._create_hull(upper_points, p1,
                              points[idx_extreme_point], isLower)
            self._create_hull(
                lower_points, points[idx_extreme_point], pn, isLower)

        else:
            self.simplices.append([p1[2], pn[2]])

    def _compare(self, a, b, c):
        """Calculate the determinant of the matrix from three points. 
        If the determinant is positive, point c is on the left side of
        the line defined by points a and b.

        @type a: list
        @param a: first point of the line
        @type b: list
        @param b: second point of the line
        @type c: list
        @param c: a point whose relative position from the line is calculated
        @rtype: float
        @returns: determinant of the matrix
        """

        return (a[0] * b[1] + b[0] * c[1] + c[0] * a[1]) - (a[1] * b[0] + b[1] * c[0] + c[1] * a[0])

    def _qsort(self, lst):
        """Sort the list of points using quick sort algorithm

        @type lst: list
        @param lst: list of points to be sorted
        @rtype: list
        @returns: sorted list of points
        """

        if len(lst) == 0:
            return []
        else:
            pivot = lst[0]
            lesser = self._qsort(
                [x for x in lst[1:]
                 if (x[0] < pivot[0])
                 or (x[0] == pivot[0] and x[1] < pivot[1])
                 ])
            greater = self._qsort(
                [x for x in lst[1:]
                 if (x[0] > pivot[0])
                 or (x[0] == pivot[0] and x[1] >= pivot[1])
                 ])
            return lesser + [pivot] + greater
