from bs4 import BeautifulSoup
import random
import time
import requests

# 参数
jwxtCASUrl = 'https://cas.sustech.edu.cn/cas/login?service=http%3A%2F%2Fjwxt.sustech.edu.cn%2Fjsxsd%2F'
jrxkUrl2 = 'http://jwxt.sustech.edu.cn/jsxsd/xsxk/xsxk_index?jx0502zbid=3E90176099AB4B3DA057E81E0FBD5181'

class_id = [
    "201920201000314", "离散数学",
    "201920201000314", "离散数学",
]

userId = ''  # fill with 8 digits student ID number
password = ''  # password to your account

#
session = requests.session()
r = session.get(jwxtCASUrl)
loginSoup = BeautifulSoup(r.content, 'html.parser')
execution = loginSoup.find("input", attrs={"name": "execution"})["value"]
r = session.post(jwxtCASUrl,
                 data={"username": userId,
                       "password": password,
                       "execution": execution,
                       "_eventId": "submit",
                       "geolocation": " "})
r = session.get(jrxkUrl2)

while True:
    for i in class_id:
       res = session.get(
                "http://jwxt.sustech.edu.cn/jsxsd/xsxkkc/knjxkOper?jx0404id=" + class_id[i] + "&xkzy=&trjf=")
            print(class_id[i + 1], res.json()["message"])
        time.sleep(random.random())
