from dotenv import load_dotenv
load_dotenv()
from woocommerce import API
import os
import json

url="https://shop-staging.ilkeczane.com"
if os.environ["ENV"] in ["PRODUCTION","TESTING"]:
  url="https://shop.ilkeczane.com"
    


wcapi= API(
        url=url,
        consumer_key=os.getenv("WOOCOMMERCE_API_KEY"),
        consumer_secret=os.getenv("WOOCOMMERCE_API_SECRET_KEY"),
        version="wc/v3",
)

category_data={
    "name":"Clothing",
    "description": "Just a category example"
}

product_data = {
    "name": "Simple example product",
    "type": "simple",
    "regular_price": "22.50",
    "stock_quantity": 10,
    "short_description": "just an example product",
    "description": "This is just an example product, created with the Woocommerce REST API",
    "categories": [
      {
        "id": 17
      }
    ],

    "images": [
        {
            "src": "https://linuxconfig.org/images/linuxconfig_logo.png",
            "alt": "example-image"
        }
    ]
}


response=wcapi.get("products")
response_ls=response.json()

#print(json.dumps(response_ls, indent = 4, sort_keys=True))

#print(type(response_ls))
dosya=open("data.txt","w")
for i in range(len(response_ls)):
   id=response_ls[i]["id"]
   name=response_ls[i]["name"]
   price=response_ls[i]["price"]
   result=f"{id} , {name} : {price}"
   print(result) 
   dosya.writelines(result)
dosya.close()  


with open("data-2.txt","wb") as f:
   f.write(b"a")



X = input("a")
print("tamam")
      




















# def data_extraction():
      
#         response=requests.get(url,
#                                 headers={
#                                 # "user_agent":"HP",
#                                         "content_type":"application/json"
#                                         },
#                                 params={
#                                         "api_key":api_key,
#                                         # "q":price
#                                                 }
#                                 )
#         return response.text   

# data_extraction()
# print(response.status_code)
# # data=response.text
# data=json.loads(response.text)
# # # result=response.json()
# print(data)

