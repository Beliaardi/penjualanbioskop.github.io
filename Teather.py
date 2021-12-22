widht_console = 45
def br(jenis):
    s = ""
    for a in range(widht_console):
        s += jenis
    print (s)

def Pesan(data):
    br("=")
    print (str.center("TEATER 31 DEWI SARTIKA", widht_console))
    br("=")
    print ("{: <10}{: <15}".format("Teater", "Film"))
    print ("{: <10}{: <15}".format("1", "Luca"))
    print ("{: <10}{: <15}".format("2", "Happiness"))
    print ("{: <10}{: <15}".format("3", "Sweet 20"))

    br("=")

    waktutayang = input ("{: <30} : ".format("Pilih Waktu Tayang [K|L]"))
    teater = input ("{: <30} : ".format("Pilih Teater [1|2|3]"))
    jumlah_tiket = int(input ("{: <30} : ".format("Jumlah Tiket")))
    makanan = input ("{: <30} : ".format("Pilih Jenis Makanan [A|B|C]"))
    jumlah_makanan = int(input ("{: <30} : ".format("Jumlah Makanan")))
    minuman = input ("{: <30} : ".format("Pilih Jenis Minuman [X|Y|Z]"))
    jumlah_minuman = int(input ("{: <30} : ".format("Jumlah Minuman")))

    br("=")

    if (waktutayang == "K"): 
        kunjungan = "Hari Kerja"
        harga_kunjungan = 35000
    else: 
        kunjungan = "Hari Libur"
        harga_kunjungan = 55000
    print ("{: <25} : {}".format("Waktu Kunjungan", kunjungan))
    print ("{: <25} : {}".format("Harga Tiket", harga_kunjungan))
    print ("{: <25} : Teater {}".format("Teater", teater))
    print ("{: <25} : {}".format("Teater", data[teater]))
    print ("{: <25} : {}".format("Jumlah Tiket", jumlah_tiket))
    print ("{: <25} : {}".format("Makanan Yang Di Pilih", data[makanan]['nama']))
    harga_makanan = data[makanan]['harga'] * jumlah_makanan
    print ("{: <25} : {}".format("Harga Makanan", harga_makanan))
    print ("{: <25} : {}".format("Makanan Yang Di Pilih", data[minuman]['nama']))
    harga_minuman = data[minuman]['harga'] * jumlah_minuman
    print ("{: <25} : {}".format("Harga Makanan", harga_minuman))

    br("=")

    total = (jumlah_tiket * harga_kunjungan) + harga_makanan + harga_minuman
    print ("{: <25} : {}".format("Total", total))


    
menu = {
    '1': "Luca",
    '2': "Happiness",
    '3': "Sweet 20",

    'A': {'nama': 'Pizza', 'harga': 35000},
    'B': {'nama': 'Popcorn', 'harga': 25000},
    'C': {'nama': 'Tidak Pilih', 'harga': 0},

    'X': {'nama': 'Colla', 'harga': 15000},
    'Y': {'nama': 'Lemon Tea', 'harga': 12500},
    'Z': {'nama': 'Tidak Pilih', 'harga': 0}
}

Pesan(menu)