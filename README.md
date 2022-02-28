## Tugas Kecil 2 Strategi Bandung

## Description

> MyConvexHull library: program ini merupakan progam yang berisi modul MyConvexHull untuk membantu mengklasifikasikan dataset yang diberikan dengan cara menentukan titik mana saja yang membentuk sisi terluar dari suatu kategori dataset. Program ini juga menyediakan driver untuk menjalankan program serta kelas pembantu untuk membuat dataset tersendiri. Program ini dibuat untuk memenuhi tugas kecil 2 mata kuliah Strategi Algoritma semester genap tahun 2021/2022

## Setup
- Secara default, program ini akan menggunakan dataset iris
- Namun, Anda dapat mengganti dataset serta kolom yang digunakan dengan cara mengganti baris berikut pada `main.py`
  ```python
  data = datasets_dict['iris']
  ```
  sesuai dengan dataset yang disediakan:
  ```py
  ['iris', 'wine', 'cancer', 'custom']
  ```
- Anda juga dapat membuat dataset sendiri sesuai template pada `datasets_dict['custom']`
- Anda juga dapat menyesuaikan column apa yang ingin dibandingkan dengan cara mengganti baris berikut pada `main.py`
  ```py
  COLUMNS_USED = (0, 1)
  ```

## How to Run
- Program ini dapat langsung dijalankan dengan cara menjalankan program utama (`main.py`) dengan cara sebagai berikut.
  ```python
  py src/main.py
  ```
  - Note: jika tidak bisa dijalankan, maka ganti command `py` dengan command yang sesuai pada operating system dan versi Python Anda

## Project Status
- Program ini sudah selesai dikembangkan dan dites baik pada beberapa dataset yang disediakan, maupun dataset yang dibuat sendiri.
  | Poin | Ya | Tidak |
  |---|---|---|
  | Pustaka myConvexHull berhasil dibuat dan tidak ada kesalahan | V | |
  | Convex hull yang dihasilkan sudah benar | V | |
  | Pustaka myConvexHull dapat digunakan untuk menampilkan convex hull setiap label dengan warna yang berbeda. | V | |
  | Bonus: program dapat menerima input dan menuliskan output untuk dataset lainnya. | V | |

## Developed by

- Malik Akbar Hashemi Rafsanjani
- 13520105
- Teknik Informatika 2020
