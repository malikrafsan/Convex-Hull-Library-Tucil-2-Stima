from scipy.spatial import ConvexHull
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from MyConvexHull import MyConvexHull
from CustomDataset import CustomDataset

datasets_dict = {
    'iris': datasets.load_iris(),
    'wine': datasets.load_wine(),
    'cancer': datasets.load_breast_cancer(),
    'custom': CustomDataset({
        'data': [[0, 0], [1, 0], [0, 1], [1, 1], [0, 0], [1, 0], [0, 1], [1, 1], [0.5, 0.5], [0.5, 0.5], [-1, -1]],
        'target': [0 for i in range(11)],
        'target_names': ['uniform'],
        'feature_names': ['X', 'Y'],
    }),
    'custom1': CustomDataset({
        'data': [[0, 0], [1, 1], [2, 1]],
        'target': [0 for i in range(3)],
        'target_names': ['uniform'],
        'feature_names': ['X', 'Y'],
    }),
}

def choose_dataset():
    print("Dataset that can be used:")
    lst_datasets = [x for x in datasets_dict]
    for i in range(len(lst_datasets)):
        print(f"{i+1}. {lst_datasets[i]}")
    
    idx = input("Choose dataset: ")
    return lst_datasets[int(idx)-1]

def choose_colums(feature_names):
    print("Columns that can be used:")
    for i in range(len(feature_names)):
        print(f"{i+1}. {feature_names[i]}")
    
    idx1 = input("Choose first column: ")
    idx2 = input("Choose second column: ")
    return (int(idx1)-1, int(idx2)-1)

def main():
    dataset = choose_dataset()
    data = datasets_dict[dataset]
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
    
    print(f"Dataset {dataset}:")
    print(df.shape)
    print(df.head())

    COLUMNS_USED = choose_colums(data.feature_names)

    plt.figure(figsize=(10, 6))
    colors = ['b', 'r', 'g', 'c', 'm', 'y', 'k', 'w']
    plt.title(
        f'{data.feature_names[COLUMNS_USED[0]]} vs {data.feature_names[COLUMNS_USED[1]]}')
    plt.xlabel(data.feature_names[COLUMNS_USED[0]])
    plt.ylabel(data.feature_names[COLUMNS_USED[1]])
    for i in range(len(data.target_names)):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:, [COLUMNS_USED[0], COLUMNS_USED[1]]].values
        hull = MyConvexHull(bucket)
        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
        for simplex in hull.simplices:
            plt.plot(bucket[simplex, 0], bucket[simplex, 1],
                     colors[i % len(colors)])
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
