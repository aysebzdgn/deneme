with open("img.jpg","rb") as f:
   img = f.read()
  
# print(img)

url = "https://www.kayserieo.org.tr/dosyalar/image/uresim/havan-5.jpg"

import requests

response = requests.get(url)

img_from_net = response.content

print(img_from_net)