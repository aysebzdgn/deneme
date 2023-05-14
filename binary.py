import requests


url = 'https://www.kayserieo.org.tr/dosyalar/image/uresim/havan-5.jpg'
r = requests.get(url)

#open('img_data.txt', 'wb').write(r.content)

with open("img_data.jpg","wb") as f:
    f.write(r.content)


with open("img_data.txt","wb") as f:
    f.write(r.content)


print(r.content)