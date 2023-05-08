
from woocommerce import API

wcapi= API(
        url="https://shop-staging.ilkeczane.com/",
        consumer_key="ck_2c044dfc1270fe58a29037abcfb4d94685328737",
        consumer_secret="cs_225059c9d99c62e3cc9671d463103183c1f63080",
        timeout=50
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


response=wcapi.get("product")
print(response)






















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

