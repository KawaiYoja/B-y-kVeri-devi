import sqlite3 as sql


baglanti = sql.connect("yazar.db")

def baglan(): 
 komut="CREATE TABLE IF NOT EXISTS yazar(id PRIMARY KEY AUTOINCREMENT,ad TEXT)"
 baglanti.execute(komut)
 baglanti.commit()

def yazarEkle(ad):
 baglanti.execute("INSERT OR REPLACE INTO yazar VALUES(null,?);",(ad,))
 baglanti.commit()
 print("Yazar Eklendi")

def scnk():
    print("1.Yazar Listesi Getir")
    print("2.Yazar Ekle")    
    cevap = input("Seçim: ")
    if cevap == 1:
     liste= baglanti.execute("SELECT * FROM kab")

     print("|[ID]|[  AD  ]|")

     for veri in liste:         
        print(
            "|",veri[0],
            "|",veri[1],
            "|"
            )
     scnk()
    elif cevap == 2:        
        isim = input("Yazar Adını Giriniz: ")
        yazarEkle(isim)
        scnk()




