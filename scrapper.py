from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import csv

url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
page = requests.get(url)
soup = bs(page.text,'html.parser')

star_table = soup.find('table')

temp_list= []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

headers = ['name','distance','mass','radius','luminosity']
name = []
distance =[]
mass = []
radius =[]
luminosity = []

for i in range(1,len(temp_list)):
    name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    luminosity.append(temp_list[i][7])

df = pd.DataFrame(list(zip(name,distance,mass,radius,luminosity)),columns=headers)
df.to_csv('file.csv')