•flowchart
https://drive.google.com/file/d/1maBTEmwNryAotEHEir8Q9fcwGcdaKPT6/view?usp=sharing

•pseudocode
// Definisikan matriks a dan b
a = [[1, 2, 3], [3, 2, 1], [2, 1, 3]]
b = [[2, 3, 4], [4, 3, 2], [4, 3, 2]]

// Cek ukuran matriks
IF (jumlah_kolom_a != jumlah_baris_b) THEN
PRINT "Matriks tidak dapat dikalikan"
ELSE
// Hitung hasil perkalian baris pertama
c = a[0][0]*b[0][0] + a[0][1]*b[1][0] + a[0][2]*b[2][0]
d = a[0][0]*b[0][1] + a[0][1]*b[1][1] + a[0][2]*b[2][1]
e = a[0][0]*b[0][2] + a[0][1]*b[1][2] + a[0][2]*b[2][2]

// Tampilkan hasil
PRINT "[" + c + ", " + d + ", " + e + "]"
