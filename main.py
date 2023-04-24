# get html of webpage

import requests as re

response = re.get('https://fireliker.com/login.php')
lol = response.text
print(lol)
