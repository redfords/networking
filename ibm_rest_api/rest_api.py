import requests

""" GET """

url = 'https://www.ibm.com'
r = requests.get(url)

print(r.status_code)
print(r.request.headers)

header = r.headers

print(header)
print(header['date'])
# 'Thu, 19 Nov 2020 15:21:47 GMT'

print(header['Content-Type'])
# 'text/html; charset=UTF-8'

print(r.encoding)
# 'UTF-8'

print(r.text[0:100])
# <!DOCTYPE html>
# <html lang="es-ar" dir="ltr">
#   <head>
#     <meta charset="utf-8" />
# <script>digitalD

url_get = 'http://httpbin.org/get'
payload = {'name': 'Joseph', 'ID': '123'}
r = requests.get(url_get, params = payload)

print(r.url)
# 'http://httpbin.org/get?name=Joseph&ID=123'

print(r.text)
# {
#   "args": {
#     "ID": "123", 
#     "name": "Joseph"
#   }, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.25.1", 
#     "X-Amzn-Trace-Id": "Root=1-6092ca07-53bf10890d2470bf05063405"
#   }, 
#   "origin": "181.46.160.75", 
#   "url": "http://httpbin.org/get?name=Joseph&ID=123"
# }

print(r.headers['Content-Type'])
# application/json

print(r.json()['args'])
# {'ID': '123', 'name': 'Joseph'}

""" POST """

url_post = "http://httpbin.org/post"

payload = {'name': 'Joseph', 'ID': '123'}

r_post = requests.post(url_post, data = payload)

print("POST request URL:", r_post.url)
# POST request URL: http://httpbin.org/post
print("GET request URL:", r.url)
# GET request URL: ttp://httpbin.org/get?name=Joseph&ID=123

print("POST request body:", r_post.request.body)
# POST request body: name=Joseph&ID=123
print("GET request body:", r.request.body)
# GET request URL: None
