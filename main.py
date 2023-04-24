# get html of webpage

import requests as re

response = re.get('https://zefoy.com/')
lol = response.text
print(lol)
