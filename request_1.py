import requests
from bs4 import BeautifulSoup

url = "https://minfin.com.ua/currency/nbu/"

req = BeautifulSoup(requests.get(url).text)

'''some_t = requests.get(url)
html_1 = some_t.text
soup = BeautifulSoup(html_1)'''

table = req.find("table",{"class":"table-auto"})
tr = table.find("td",{"class":"js-ex-rates"})
tr = tr.text
tr = tr[2:8]
print(tr)
