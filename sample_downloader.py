class Downloader:
    ...

if __name__ == "__main__":
    d = Downloader(save_to_location="downloads")
    d.download(url = 'https://www.kayserieo.org.tr/dosyalar/image/uresim/havan-5.jpg')
    print(f"İndirilen son dosyanın boyutu: {len(d.last_content)}")