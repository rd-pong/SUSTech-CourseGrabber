from bs4 import BeautifulSoup
import random
import time
import requests

# 参数
jwxtCASUrl = 'https://cas.sustc.edu.cn/cas/login?service=http%3A%2F%2Fjwxt.sustc.edu.cn%2Fjsxsd%2F'
jrxkUrl2 = 'http://jwxt.sustc.edu.cn/jsxsd/xsxk/xsxk_index?jx0502zbid=3A1BF4389B934C97892839429A1528F5'

class_id = [
    ["201820192000615", "艺术与科学大讲堂[中文班]"],
    ["201820191000712", "形势与政策[中文6班]"]
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
            "http://jwxt.sustc.edu.cn/jsxsd/xsxkkc/fawxkOper?jx0404id=" + i[0] + "&xkzy=&trjf=")
        print(i[1], res.json()["message"])
        time.sleep(random.random())
