# get html to wep

import requests as re

response=re.get('https://fireliker.com/')
html=response.text
print(html)
