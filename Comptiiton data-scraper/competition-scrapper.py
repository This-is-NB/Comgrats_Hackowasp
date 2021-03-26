import requests
from bs4 import BeautifulSoup
import json

url = r"https://clist.by/"

data = {}
clean_d= {}
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

i = 0
for event in soup.find_all('a',attrs = {"class":'data-ace'}):
    try:
        temp = event.attrs.get('data-ace', None).replace("\n          ","")
        data[i+1] = eval(temp)
    except Exception:
        continue
    i += 1
    
with open('data.json','w') as f:
    json.dump(data, f, indent=4)
    