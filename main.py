import requests,bs4,json,os,sys,random,datetime,time,re
import threading
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col

x = '\33[m' # DEFAULT

k = '\033[93m' # KUNING +

h = '\x1b[1;92m' # HIJAU +

hh = '\033[32m' # HIJAU -

u = '\033[95m' # UNGU

kk = '\033[33m' # KUNING -

b = '\33[1;96m' # BIRU -

p = '\x1b[0;34m' # BIRU +

P = '\033[0;00m'

J = '\033[0;33m'

S = '\033[0;00m'

N = '\x1b[0m'

I ='\033[0;32m'

C ='\033[0;36m'

M ='\033[0;31m'

U ='\033[0;35m'

K ='\033[0;33m'

P='\033[00m'

h='\033[0;90m'

Q="\033[00m"

kk='\033[0;32m'

ff='\033[0;36m'

G='\033[0;36m'

p='\033[00m'

h='\033[0;90m'

Q="\033[00m"

I='\033[0;32m'

II='\033[0;36m'

m='\033[0;31m'

O ='\033[0;33m'

H='\033[0;33m'

b = '\033[0;36m'

war = "[•]"

B = random.choice([U,I,K,b,M])


dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}

dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}

tgl = datetime.datetime.now().day

bln = dic[(str(datetime.datetime.now().month))]

thn = datetime.datetime.now().year

okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

os.system('clear')

def back():
	os.system('git pull')
os.system('clear')

def banner():
	print('''%s
	_______           ______   _______  _                 ______  
       (  ____ )|\     /|(  __  \ (  ___  )( \      |\     /|(  __  \ 
       | (    )|| )   ( || (  \  )| (   ) || (      ( \   / )| (  \  )
       | (____)|| |   | || |   ) || (___) || | _____ \ (_) / | |   ) |
       |     __)| |   | || |   | ||  ___  || |(_____) ) _ (  | |   | |
       | (\ (   | |   | || |   ) || (   ) || |       / ( ) \ | |   ) |
       | ) \ \__| (___) || (__/  )| )   ( || (____/\( /   \ )| (__/  )
       |/   \__/(_______)(______/ |/     \|(_______/|/     \|(______/ 
                                                               
───────────────────────────────────────────────────────
 [\x1b[1;96m+%s] Author   : Rudal-XD
 [\x1b[1;96m+%s] Github   : https://github.com/Rudal-XD
 [\x1b[1;96m+%s] Facebook : Fanky
───────────────────────────────────────────────────────\n'''%(hh,hh,hh,hh))

#login

balmond = O+"["+J+"•"+O+"]"

class menu:
	banner()
	print('[bold green]1.open\n2.exit')
	lol=input('choose:')
	if lol == ['1']:
		from assets import json
	elif lol == ['2']:
		exit()

			
if __name__=='__main__':
	menu()
	
	
	
	
	
	
	
	
	
	
	
	
