import requests
from bs4 import BeautifulSoup
import re

url = "https://minfin.com.ua/currency/nbu/"
req = BeautifulSoup(requests.get(url).text)

# f_num - current value
f_num = req.findAll("td",{"class":"responsive-hide td-collapsed mfm-text-nowrap mfm-text-right"})
f_num = re.findall("\d+",str(f_num))

list_num = []
j=0
for i in range(len(f_num)):
    j+=1
    if i%5!=0:
        j = 0
    if j==1:
        str_1 = f_num[i]+"."+f_num[i+1]
        list_num.append(str_1)

#f_text - name of money
list_text = []
f_text = req.findAll("a",{"class":"link-icon"})

for i in range(len(f_text)):
    str_2 = str(f_text[i])
    list_text.append(str_2[47:-4])

kurs_grivny = dict(zip(list_text,list_num))

for key,value in kurs_grivny.items():
    print(key," - ",value)
