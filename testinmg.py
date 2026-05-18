import requests
from bs4 import BeautifulSoup
import re

def scraping():
    r = requests.get('https://somedina7.com/bg/price')
    soup = BeautifulSoup(r.text,'lxml')
    th=soup.find('th',{'class':'text-right'})
    find = (re.search(r'\d\d.\d\d', th.get_text()).group()) 
    data = (float(find))
    print(data)
    return(data)



def scraping_met():
    r = requests.get('https://somedina7.com/bg/price/index/4/')
    soup = BeautifulSoup(r.text,'lxml')
    data = []
    for el in soup.find_all('th',{'class':'text-right'}):
        data.append(float(re.search(r'\d\d.\d\d', el.get_text()).group()))
    print(data)
    return(data)

scraping_met()