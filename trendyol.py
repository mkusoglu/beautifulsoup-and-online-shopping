# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 22:27:30 2021

@author: MustafaKuşoğlu
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
dateTimeObj1 = datetime.now()
timestampStr1 = dateTimeObj1.strftime("%d-%b-%Y")

trendyol=['https://www.trendyol.com/cep-telefonu-x-c103498?sst=BEST_SELLER',
         'https://www.trendyol.com/laptop-x-c103108?sst=BEST_SELLER',
         'https://www.trendyol.com/beyaz-esya-x-c103613?sst=BEST_SELLER',
         'https://www.trendyol.com/sr/kadin-giyim-x-g1-c82?sst=BEST_SELLER',
         'https://www.trendyol.com/erkek-giyim-x-g2-c82?sst=BEST_SELLER',
         'https://www.trendyol.com/mobilya-x-c1119?sst=BEST_SELLER',
         'https://www.trendyol.com/oyuncak-x-c90?sst=BEST_SELLER',
         'https://www.trendyol.com/spor-aletleri-x-c104192?sst=BEST_SELLER',
         'https://www.trendyol.com/kozmetik-x-c89?sst=BEST_SELLER',
         'https://www.trendyol.com/kitap-x-c91?sst=BEST_SELLER']

tr_kategoriler=["",
             'Telefon',
             'Laptop',
             'Beyaz Esya',
             'Kadın Giyim',
             'Erkek Giyim',
             'Mobilyalar',
             'Oyuncaklar',
             'Spor Malzemeleri',
             'Kozmetik',
             'Kitaplar']



headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}

liste_trendyol=[]
sayac_trendyol=1
for siteler in trendyol:
    r_trendyol= requests.get(siteler,headers=headers)
    soup_trendyol = BeautifulSoup(r_trendyol.content,'lxml')
    site1 = soup_trendyol.find("div",attrs={"class":"prdct-cntnr-wrppr"})
    site2 = site1.find("div",attrs={"class":"p-card-chldrn-cntnr"})
    linkSonu=site2.a.get("href")
    linkBasi="https://www.trendyol.com"
    link=linkBasi+linkSonu
    print(link)
    b=1
    while b<=1:
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}
        r= requests.get(siteler+"&pi="+str(b)+"",headers=headers)
        soup = BeautifulSoup(r.content,'lxml')
        st1 = soup.find("div",attrs={"class":"prdct-cntnr-wrppr"})
        st2 = st1.find("div",attrs={"class":"p-card-chldrn-cntnr"})
        for icerik in st2:
            linkSonu=st2.a.get("href")
            linkBasi="https://www.trendyol.com"
            link=linkBasi+linkSonu
            kategori=tr_kategoriler[sayac_trendyol]
            r1=requests.get(link,headers=headers)
            soup1=BeautifulSoup(r1.content,"lxml")
            urunAdi = soup1.find("h1",attrs={"class":"pr-new-br"}).text
            print(urunAdi)
            try:
                urunMarkasi =soup1.find("h1",attrs={"class":"pr-new-br"}).a.text
            except:
                urunMarkasi =soup1.find("h1",attrs={"class":"pr-new-br"}).text
            try:
                originalPrice = soup1.find("span",attrs={"class":"prc-slg prc-slg-w-dsc"}).text
            except AttributeError:
                originalPrice = soup1.find("div",attrs={"class":"pr-bx-nm"}).text
            except:
                originalPrice = soup1.find("span",attrs={"class":"prc-org"}).text
            try:
                simdikiFiyat_text = soup1.find("div",attrs={"style":"display:flex"}).text
                simdikiFiyat = simdikiFiyat_text[:-6]
            except:
                simdikiFiyat_text = originalPrice
                simdikiFiyat = simdikiFiyat_text[:-6]
            try:
                simdikiFiyat_kurus = simdikiFiyat_text[-5]+simdikiFiyat_text[-4]
            except:
                simdikiFiyat_kurus = "00"
            try:
                puan = soup1.find("span",attrs={"class":"tltp-avg-cnt"}).text
            except:
                puan="NaN"
            try:
                degerlendirme = soup1.find("a",attrs={"class":"rvw-cnt-tx"}).text
            except:
                degerlendirme= "NaN"
            liste_trendyol.append([link,urunAdi,urunMarkasi,originalPrice,simdikiFiyat,simdikiFiyat_kurus,puan,degerlendirme])
        b=b+1
    pd.DataFrame(liste_trendyol)
    df_trendyol = pd.DataFrame(liste_trendyol)
    df_trendyol.columns = ("link","urunAdi","urunMarkasi","originalPrice","simdikiFiyat","simdikiFiyat_kurus","puan","degerlendirme")
    sayac_trendyol=sayac_trendyol+1