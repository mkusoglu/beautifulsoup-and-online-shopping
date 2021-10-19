# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 22:58:06 2021

@author: MustafaKuşoğlu
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
dateTimeObj1 = datetime.now()
timestampStr1 = dateTimeObj1.strftime("%d-%b-%Y")

siteler=['https://www.n11.com/telefon-ve-aksesuarlari/cep-telefonu?srt=SALES_VOLUME&pg=',
         'https://www.n11.com/bilgisayar/dizustu-bilgisayar?srt=SALES_VOLUME&pg=',
         'https://www.n11.com/beyaz-esya?srt=SALES_VOLUME&pg=',
         'https://www.n11.com/beyaz-esya?srt=SALES_VOLUME&pg=',
         'https://www.n11.com/beyaz-esya?srt=SALES_VOLUME&pg=',
         'https://www.n11.com/mobilya?srt=SALES_VOLUME&pg=',
         'https://www.n11.com/cocuk-oyuncaklari-ve-parti?srt=SALES_VOLUME&pg=',
         'https://www.n11.com/outdoor-ve-kamp?srt=SALES_VOLUME&pg=',
         'https://www.n11.com/parfum-ve-deodorant?srt=SALES_VOLUME&pg=',
         'https://www.n11.com/kitap?srt=SALES_VOLUME&pg=']

kategoriler=["",
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
platform="n11"
kategori_s=1
liste=[]
for site in siteler:
    print(site)
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}
    r=requests.get("https://www.n11.com/telefon-ve-aksesuarlari/cep-telefonu?srt=SALES_VOLUME",headers=headers)
    soup=BeautifulSoup(r.content,"lxml")
    print(r)
    orjinaller_oldPrice=[""]
    orjinaller_newPrice=[""]
    a=1
    sayac=1
    while a<=1:
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}
        r=requests.get(site+str(a)+"",headers=headers)
        soup=BeautifulSoup(r.content,"lxml")
        st1=soup.find("section",attrs={"class":"group listingGroup resultListGroup import-search-view"})
        st2=st1.find_all("li",attrs={"class":"column"})
        for lis in st2:
            x=lis.find_all('del')
            if x == []:
                x=lis.find_all('ins')
                for op in x:
                    orjinaller_oldPrice.append(op.text)
            else:
                for op in x:
                    orjinaller_oldPrice.append(op.text)
        for newP in st2:
            anlik=newP.find_all('ins')
            for herAnlik in anlik:
                orjinaller_newPrice.append(herAnlik.text)
        """Yukarıdak for ile başlayan kısımla yapılmak istenilen:
        indirimi olmayan ürünlerde fiyat newPrice divinde ins altında yazılıdır.
        indirimli ürünlerde ise orjinal fiyat oldprice divinde del içinde yazılıdır.
        yukarıdaki işlemlerde, orjinal fiyat değeri için indirim varsa oldprice içindeki veri, 
        indirim yoksa newprice içindeki değer alınması sağlanmıştır"""
        for icerik in st2:
            link=icerik.a.get("href")
            r1=requests.get(link,headers=headers)
            soup1=BeautifulSoup(r1.content,"lxml")
            urunAdi=soup1.find("h1",attrs={'class':"proName"}).text.replace("\n","")
            urunAdi=urunAdi.replace("                    ","")
            print(urunAdi)
            urunMarkasi="bulunamıyor"
            kategori=kategoriler[kategori_s]
            originalPrice=orjinaller_oldPrice[sayac]
            simdikiFiyat=orjinaller_newPrice[sayac]
            simdikiFiyat_kurus=simdikiFiyat[-6]+simdikiFiyat[-5]
            puan_sinif=soup1.find("div",attrs={"class":"ratingCont"})
            classes = []
            for element in puan_sinif.find_all(class_=True):
                classes.extend(element["class"])
            for cla in classes:
                if cla =='r100':
                    puan ='5'
                elif cla == 'r90':
                    puan = '4.5'
                elif cla =='r80':
                    puan = '4'
                elif cla =='r70':
                    puan = '3.5'
                elif cla =='r60':
                    puan = '3.0'
                elif cla =='r50':
                    puan = '2.5'
                elif cla =='r40':
                    puan = '2.0'
                elif cla =='r30':
                    puan = '1.5'
                elif cla =='r20':
                    puan = '1.0'
                elif cla =='r10':
                    puan = '0.5'
                elif cla =='r0':
                    puan = 'NaN'
            try:
                degerlendirmeSayisi=soup1.find("span",attrs={"class":"reviewNum"}).text
            except:
                degerlendirmeSayisi="0"
            sayac=sayac+1
            liste.append([link,platform,urunAdi,urunMarkasi,kategori,originalPrice,simdikiFiyat,simdikiFiyat_kurus,puan,degerlendirmeSayisi])
        a=a+1
        pd.DataFrame(liste)
        df = pd.DataFrame(liste)
        df.columns = ("link","platform","urunAdi","urunMarkasi","kategori","originalPrice","simdikiFiyat","simdikiFiyat_kurus","puan","degerlendirmeSayisi")
        kategori_s=kategori_s+1