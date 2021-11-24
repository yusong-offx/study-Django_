from urllib.request import urlopen, Request
from urllib.parse import urlencode
import sys

# ob = urllib.request.urlopen("https://www.naver.com")
# print(ob.read(500).decode('utf-8'))

# data = "language=python&framework=django"
# url = "http://127.0.0.1:8000"
# ob = urlopen(url, bytes(data, encoding='utf-8'))
# print(ob.info())
# print(ob.read().decode('utf-8'))

url = "http://127.0.0.1:8000"
data = {
	'name': '송유진',
	'email': '42.4.yusong@gmail.com',
	'url': 'http://www.naver.com',
}
enData = urlencode(data, encoding='utf-8')
postData = bytes(enData, encoding='utf-8')
req = Request(url, data=postData)
#print(enData, postData, sep='\n')
#req.add_header('Content-Type', 'application/x-www-form-urlencoded')
req.remove_header('Content-Type')
f = urlopen(req)
print(f.headers)
#print(f.read().decode('utf-8'))