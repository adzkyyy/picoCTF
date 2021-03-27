#!/usr/bin/python

import requests 
url = 'https://jupiter.challenges.picoctf.org/problem/36474/'

p = requests.get(url + 'robots.txt').text[24:35]
flag = requests.get(url + p).text

print flag[351:386]
