deklarasi matiriks 3×3
a = [[2,2,3],[3,1,2],[1,3,4]]
b = [[2,4,1],[4,3,5],[4,1,2]]

#inisiasi variabel untuk hasil
c = []
d = []
e = []
f = []
g = []
h = []
i = []
j = []
k = []

#menentukan baris dan kolom matriks a dan b
baris_a = len(a)
kolom_a = len(a[0])

baris_b = len(b)
kolom_b = len(b[0])

#cetak kolom dan baris a
print (a)
print ("baris matriks a adalah ", baris_a)
print ("kolom matriks a adalah ", kolom_a)

#cetak kolom dan baris b
print (b)
print ("baris matriks b adalah ", baris_b)
print ("kolom metriks b adalah ", kolom_b)
#kondisi
if (kolom_a !=baris_b):
    print ("martriks a dan b tidak dapat dikalikan")
else:
    print("martiks a dan b dapat dikalikan")
   
#Rumus matriks 3×3
    c = (a[0][0]*b[0][0])+(a[0][1]*b[1][0])+(a[0][2]*b[2][0])
    d = (a[0][0]*b[0][1])+(a[0][1]*b[1][1])+(a[0][2]*b[2][1])
    e = (a[0][0]*b[0][2])+(a[0][1]*b[1][2])+(a[0][2]*b[2][2])
#cetak hasil matrik c,d,e
    print (f"[{c} {d} {e}]")
    f = (a[1][0]*b[0][0])+(a[1][1]*b[1][0])+(a[1][2]*b[2][0])
    g = (a[1][0]*b[0][1])+(a[1][1]*b[1][1])+(a[1][2]*b[2][1])
    h = (a[1][0]*b[0][2])+(a[1][1]*b[1][2])+(a[1][2]*b[2][2])
#cetak hasil matriks 3×3
    print (f"[{f} {g} {h}]")
    i = (a[2][0]*b[0][0])+(a[2][1]*b[1][0])+(a[2][2]*b[2][0])
    j = (a[2][0]*b[0][1])+(a[2][1]*b[1][1])+(a[2][2]*b[2][1])
    k = (a[2][0]*b[0][2])+(a[2][1]*b[1][2])+(a[2][2]*b[2][2])
#cetak matriks 3×3
    print (f"[{i} {j} {k}]")
