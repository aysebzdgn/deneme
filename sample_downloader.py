import requests
import os
class Downloader:
    def __init__(self, save_to_location):
        self.download_location = save_to_location
        print("inner",self.download_location)
    
    def download(self, url, file_name):
        self.url = url
        response = requests.get(self.url)
        save_to_file_name = f"{self.download_location}/{file_name}"
        print(f"saving to {save_to_file_name}...")
        # if not os.path.exists(self.download_location):
        os.makedirs(self.download_location,exist_ok=True)
        with open(save_to_file_name,"wb") as f:
            f.write(response.content)
        print(f"saved to {save_to_file_name}!")
        self.last_content = response.content

if __name__ == "__main__":
    d1 = Downloader(save_to_location="downloads")
    d2 = Downloader(save_to_location="indirilenler")
    d3 = Downloader(save_to_location="images/havan/web")
    print("1",d1.download_location)
    print("2",d2.download_location)
    print("3",d3.download_location)
    
    # d1.download(url = 'https://www.kayserieo.org.tr/dosyalar/image/uresim/havan-5.jpg',file_name="5.jpg")
    d2.download(url = 'https://www.kayserieo.org.tr/dosyalar/image/uresim/havan-5.jpg',file_name="6.jpg")
    # d3.download(url = 'https://www.kayserieo.org.tr/dosyalar/image/uresim/havan-5.jpg',file_name="7.jpg")
    
    # print(f"İndirilen son dosyanın boyutu 1: {len(d1.last_content)}")
    print(f"İndirilen son dosyanın boyutu 2: {len(d2.last_content)}")
    print(hasattr(d2,"last_content"))
    lc = getattr(d2,"last_content")
    print("len(lc) = ",len(lc))
    delattr(d2,"last_content")
    print(hasattr(d2,"last_content"))
    setattr(d2,"last_content",lc)
    print(f"İndirilen son dosyanın boyutu 2: {len(d2.last_content)}")