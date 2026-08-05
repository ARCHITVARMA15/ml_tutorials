import pandas as pd
import requests 
from bs4 import BeautifulSoup
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
webpage =requests.get('https://www.ambitionbox.com/list-of-companies?page=1', headers=headers).text

print(webpage)
soup = BeautifulSoup(webpage, 'lxml')
print("using print prettify")
print(soup.prettify())
print(" --- IGNORE --- ")

print(soup.find_all('h1'))