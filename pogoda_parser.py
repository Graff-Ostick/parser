import requests
from bs4 import BeautifulSoup

url = "https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%83%D0%B6%D0%B3%D0%BE%D1%80%D0%BE%D0%B4/"

req = requests.get(url)
html = BeautifulSoup(req.content, "html.parser")

list_date = []
temp =[]

for el in html.select(".tabs"):
    title_date = el.select("p",{"class":"date"})

for el in html.select(".tabs"):
    title_min = el.select(".min > span")

for el in html.select(".tabs"):
    title_max = el.select(".max > span")

for i in range(len(title_date)):
    if i%3==0:
        date = title_date[i].text+" "+title_date[i+1].text + " " + title_date[i+2].text
        list_date.append(date)
    if i<7:
        title = "min " + title_min[i].text + " max" + title_max[i].text
        temp.append(title)


pogoda = dict(zip(list_date, temp))
for elem,value in pogoda.items():
    print(elem, " - ", value)
