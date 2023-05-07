import os


def read_file():
    with open("ekstre.txt","r",encoding="cp1254") as f:
        print("dosya okunuyor")
        icerik=f.read()
        print(icerik)
        print("dosya içeriği okundu")
        liste1=icerik.split(",")
        print(liste1)
read_file()
def read_folder():
     with os.scandir("C:/Users/HP/OneDrive/Masaüstü/dosya_okuma/Faturalar") as tarama:
         for belge in tarama:
             if belge.is_file():
                 print(belge.name)
read_folder()


# for dosya in os.listdir():
#     if dosya.is_file():
#         print(dosya.name)

# print(os.listdir())

with open("C:/Users/HP/OneDrive/Masaüstü/dosya_okuma/Faturalar/a001.txt","r") as f:
    print("dosya okunuyor")
    icerik=f.read()
    print("a001 "+icerik)