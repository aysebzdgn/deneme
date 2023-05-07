import requests
import json



api_key="ck_2c044dfc1270fe58a29037abcfb4d94685328737"
url="https://shop-staging.ilkeczane.com/"
response=requests.get(url,
                         headers={
                        #         "user_agent":"HP",
                                 "content_type":"application/json"
                                 },
                        params={
                                "api_key":api_key,
                                # "q":price
                                        }
                        )
        


print(response.status_code)
# data=response.text
data=json.loads(response.text)
# # result=response.json()
print(data)

