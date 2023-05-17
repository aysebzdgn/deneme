import requests



class Downloader:
    def __init__(self,url):
        self.url=url
        response=requests.get(url)
        with open("download.txt","wb") as f:
            f.write(response.content)
    
d1=Downloader( url='https://www.kayserieo.org.tr/dosyalar/image/uresim/havan-5.jpg')

if __name__ == "__main__":
    ...
    # d = Downloader(save_to_location="downloads")
    # d.download(url = 'https://www.kayserieo.org.tr/dosyalar/image/uresim/havan-5.jpg')
    # print(f"İndirilen son dosyanın boyutu: {len(d.last_content)}")



class kisi:
    def __init__(self,isim,yas):
        self.isim=isim
        self.yas=yas

kisi1=kisi(isim= "ayse", yas=20)
