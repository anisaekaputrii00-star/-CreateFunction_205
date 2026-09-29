import math

luas_lingkaran = lambda r : math.pi * r * r
jari_jari = float(input("Masukan jari-jari lingkaran: "))
hasil = luas_lingkaran(jari_jari)
print("Luas lingkaran: ", hasil)