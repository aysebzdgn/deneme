import os
from typing import Callable

directory_to_scan = "./FATURALAR"
file_name_extre = "ekstre.txt"

def read_file(file_name_extre):
    with open(file_name_extre,"r",encoding="cp1254") as f:
        print("dosya okunuyor")
        icerik=f.read()
        print(icerik)
        print("dosya içeriği okundu")
        liste1=icerik.split(",")
        print(liste1)

def parse_invoice(raw_text):
    return "okunmuş:" + raw_text

def read_invoice_file(file_name_invoice ,invoice_parser):
    with open(file_name_invoice,"r",encoding="cp1254") as f:
        print("fatura dosyası okunuyor")
        icerik=f.read()
        print(icerik)
        print("fatura içeriği okundu")
        if isinstance(invoice_parser,Callable):
            liste1=invoice_parser(icerik)
            print(liste1)
        else:
            print(f"parser function değil: {invoice_parser}")


def read_folder(directory_to_scan):
     with os.scandir(directory_to_scan) as tarama:
         for belge in tarama:
             if belge.is_file():
                 read_invoice_file(belge.path,parse_invoice)

if __name__ == "__main__":
    read_file(file_name_extre)
    read_folder(directory_to_scan)
