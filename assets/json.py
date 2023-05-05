import requests
from urllib.request import urlopen
url='https://fireliker.com'
response=urlopen(url)
print(response.read())
