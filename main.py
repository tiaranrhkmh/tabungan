#JAWABAN A: membuat dictionary pemasukan dan pengeluaran
#Membuat variabel yang akan diinput oleh user
def input_data(a:dict,b:dict): #fungsi input data untuk pembuatan sekaligus mengolah data input yang selanjutnya akan direkap di file pengeluaran/pemasukan
    while True: #perulangan yang tidak ada batas kecuali kondisi tertentu
        bulan = input("Bulan dan Tahun (Juli 2020) :") #input waktu mencakup bulan dan tahun
        bulan = bulan.strip() #hapus spasi
        uang = input("Akumulasi Uang(+/-): ")#input akumulasi uang +(pemasukan) -(pengeluaran)
        uang= uang.strip() #hapus spasi
        if (uang.find('+') == 0): #jika pada input uang terdapat nilai +
            rekap_pemasukan = open("pemasukan.txt","+a") #maka dibuatkan atau dibuka kembali file pemasukan jika sudah dimasukkan nilainya 
            a[bulan] = uang #input dictionary sesuai dengan key : value
            nilai = uang[uang.find('+')+1:] #pengambilan tanpa tanda +
            hasil = bulan + " IDR %s" %nilai # output hasil pada file pemasukan
            rekap_pemasukan.write("%s\r" %hasil) # untuk menyalin, %s karna string
            rekap_pemasukan.close() #menutup folder (ini wajib ketika mengakses file)
            continue # untuk melanjutkan proses input data
        elif (uang.find('-') == 0): #jika pada input uang terdapat nilai -
            rekap_pengeluaran = open("pengeluaran.txt","+a")#maka dibuatkan atau dibuka kembali file pengeluaran jika sudah dimasukkan nilainya 
            b[bulan] = uang #input dictionary pengeluaran sesuai dengan key : value
            nilai = uang[uang.find('-')+1:] #pengambilan tanpa tanda -
            hasil = bulan + " IDR %s" %nilai  # output hasil pada file pengeluaran
            rekap_pengeluaran.write("%s\r" %hasil)# untuk menyalin, %s karna string
            rekap_pengeluaran.close() #menutup folder (ini wajib ketika mengakses file)
            continue # untuk melanjutkan proses input data
        elif (uang == "" or bulan =="" or uang == "STOP" or bulan == "STOP"): #jika diisi spasi atau STOP
            print(a,b) #menampilkan a dan b
            print("\n STOP") # diakhiri STOP
            tertinggi(a,b) # memanggil fungsi nilai tertinggi dari pemasukan(a) dan pengeluaran (b)
            rerata(a,b) #memanggil fungsi nilai rerata dari pemasukan (a) dan pengeluaran (b)
        break
    return a,b
        

#JAWABAN B Fungsi rerate untuk mengembalikan nilai rata-rata besarnya pemasukan dan pengeluaran
def rerata (a:dict, b:dict): #parameter pada fungsi yang sama pada a hanya saja untuk menghitung rata-rata
    nilai = {} #sebuah dictioncary untuk perulangan for yang akan di cek satu per satu
    a = {key.strip(): item.strip("+") for key, item in a.items()} #menghapus nilai yang masih punya tanda + untuk mendapatkan nilai tertinggi pada value
    b = {key.strip(): item.strip("-") for key, item in b.items()} #menghapus nilai yang masih punya tanda - untuk mendapatkan nilai tertinggi pada value
    for j, k in a.items(): #untuk mengecek dan mengelompokkan jumlah dan bulan yang sama
        rerata = sum(nilai[k])/len(nilai[j]) #proses perhitungan rata rata pemasukan per bulan
        print ("Rata-rata pemasukan bulan" + nilai[j]+"sebesar IDR"+ rerata) # proses menampilkan rata-rata pemasukan
    for i, h in b.items(): #untuk mengecek dan mengelompokkan jumlah dan bulan yang sama
        rerata = sum(nilai[h])/len(nilai[i]) #proses perhitungan rata rata pengeluaran per bulan
        print ("Rata-rata pengeluaran bulan" + nilai[i]+ "sebesar IDR"+ rerata) # proses menampilkan rata-rata pengeluaran
    return rerata #pengembalian nilai rerata

#JAWABAN C Fungsi tertinggi untuk mengembalikan nilai bulan dan tahun dengan pemasukan tertinggi
def tertinggi (c:dict,d:dict):#fungsi untuk mencari nilai tertinggi
    c = {key.strip(): item.strip("+") for key, item in c.items()} #menghapus nilai yang masih punya tanda + untuk mendapatkan nilai tertinggi pada value
    d = {key.strip(): item.strip("-") for key, item in d.items()} #menghapus nilai yang masih punya tanda - untuk mendapatkan nilai tertinggi pada value
    bulan_pemasukan = max(c,key=c.get) #mendapatkan dibulan mana pemasukan terbesar
    bulan_pengeluaran = max(d,key=d.get) #mendapatkan dibulan mana pengeluaran terbesar
    uang_pemasukan = max(c.values()) #mendapatkan nilai dari yang bulan pemasukan terbesar
    uang_pengeluaran = max(d.values()) #mendapatkan nilai dari yang bulan pengeluaran terbesar
    print("Pemasukan terbesar pada ",bulan_pemasukan,"sebesar IDR ",uang_pemasukan) #menampilkan output pada pemasukan terbesar
    print("Pengeluaran terbesar pada ",bulan_pengeluaran,"sebesar IDR ",uang_pengeluaran) #menampilkan output pada pengeluaran terbesar
    
    return c,d #pengembalian dict pemasukan dan pengeluaran
    
#JAWABAN D menampilkan pada satu fungsi yang akan menjalankan fungsi lainnya
pemasukan = dict()  #dictionary pemasukan sesuai JAWABAN A
pengeluaran = dict() #dictionary pengeluaran sesuai JAWABAN B
hasil= input_data(pemasukan,pengeluaran) # hasil dari fungsi input_data



