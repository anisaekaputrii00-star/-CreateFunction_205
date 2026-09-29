def konversi_suhu (nilai, satuan):
    if satuan == "C":
        hasil = ( nilai * 9/5) + 32
        return hasil
    elif satuan == "F":
        hasil = (nilai - 32 ) * 5/9
        return hasil 
    else:
        return "Satuan tidak valid"

suhu = float(input (" Masukan Nilai suhu: "))
satuan = input("Masukan Satuannya (C/F): ").upper()

hasil = konversi_suhu(suhu, satuan)
print("Hasil konversi: ", hasil)