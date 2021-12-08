import function
import sqlite3

Yol=sqlite3.connect("Kıyafet.db")

kmt="CREATE TABLE IF NOT EXISTS Kıyafet(Marka text, Model text, Renk text, fiyat int)"
yol=.commit()

komut="Insert INTO Kıyafet VALUES('Armani','Düz yaka','beyaz', 300)"
function.Kıyafet_ekle()
yol.commit()

komut2="DELETE from Kıyafet where Marka"
function.veri_silme()
yol.commit()

komut3="UPDATE Kıyafet where Marka= ?"
function.veri_güncelleme("Lacoste")
yol.commit()


ayıklama="Select * from Kıyafet where Marka = ?"
function.Kıyafet_getir("Fred Perry")
yol.commit()

yol.close()


