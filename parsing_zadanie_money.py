# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 00:18:15 2019

@author: Dell
"""

import requests
from bs4 import BeautifulSoup


def get_html(url):
 	r = requests.get(url)
    
 	return r.text

def get_data(html):
    soup = BeautifulSoup(html,'lxml')
    h1 = soup.text
    return h1


def getting_money():
    url = "http://www.nbrb.by/API/ExRates/Rates/145"
    data1 =get_data(get_html(url))
    dct1 = {}
    dct1 = eval(data1)
    url2 = "http://www.nbrb.by/API/ExRates/Rates/292"
    data2 =get_data(get_html(url2))
    dct2 = {}
    dct2 = eval(data2)
    
    GreateDate = dct1["Date"]
    Today = GreateDate[8:10]+'.' + GreateDate[5:7] + '.' + GreateDate[:4]
    #rez = 'За ' + Today +  ' курс ' + dct2["Cur_OfficialRate"] + ' рублей за 1 Евро, ' + dct1["Cur_OfficialRate"] + ' за 1 доллар'
    #print(rez)
    #print('За ',Today, ' курс ',dct2["Cur_OfficialRate"],' рублей за 1 Евро, ',dct1["Cur_OfficialRate"],' за 1 доллар')
    return[Today,dct2["Cur_OfficialRate"],dct1["Cur_OfficialRate"]]
#getting_money()

'''
if __name__ == '__main__':
 	main()
'''
