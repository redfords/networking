import requests
import os
from PIL import Image
from IPython.display import IFrame

url = 'https://www.ibm.com/'
r = requests.get(url)

print(r.status_code)
print(r.request.headers)
print("Request body:", r.request.body)

header = r.headers
print(header)
print(r.encoding)

# non-text request
url='https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png'

r = requests.get(url)

print(r.headers)
print(r.headers['Content-Type'])

# save the image using a file object
path = os.path.join(os.getcwd(), 'image.png')
with open(path, 'wb') as f:
    f.write(r.content)
Image.open(path)
