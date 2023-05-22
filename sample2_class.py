
from datetime import datetime

class Personel():
    def __init__(self,isim,yas,maas,baslangic_tarihi):
        print("*"*10)
        print("Yeni Personel: ",isim)
        self.isim=isim
        self.yas=yas
        self.maas=maas
        self.baslangic_tarihi=baslangic_tarihi
       


    def personel_bilgisi(self):
        print("Personelin ismi: ",self.isim)
        print("Personelin yaşı: ",self.yas)
        print("Personelin Maaşı: ",self.maas)
        baslama=datetime.strptime(self.baslangic_tarihi,"%d.%m.%Y")
        simdi=datetime.now()
        sure=simdi-baslama
        print("Personelin Çalışma Süresi: ",sure)


    def bilgileri_kaydet(self,dosya_Adi):
        dosya_ismi=f"{self.isim}/{dosya_Adi}"
        print(f"kaydediliyor {dosya_ismi}...")
        print("*"*10)




p1=Personel("Ayşe Bozdoğan",24,5000,"01.08.2021")
p1.personel_bilgisi()
p1.bilgileri_kaydet("bilgiler.txt")

p2=Personel("Melek Kaya", 21,5000,"01.06.2021")
p2.personel_bilgisi()
p2.bilgileri_kaydet("bilgiler.txt")

p3=Personel("Durmuş Türkmen",33,5000,"01.01.2012")
p3.personel_bilgisi()
p3.bilgileri_kaydet("bilgiler.txt")