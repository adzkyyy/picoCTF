#!/usr/bin/python
import requests

url = 'https://jupiter.challenges.picoctf.org/problem/26704/flag'
UG = 'picobrowser'
p = requests.get(url, headers={'User-Agent':UG})
print(p.text)[1634:1669]
