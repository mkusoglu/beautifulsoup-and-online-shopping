from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
#telefon,laptop,beyaz eşya,bayan giyim,erkek giyim,mobilya,oyuncal,spor malzemeleri,kozmetik,kitap

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y")
siteler=['https://www.hepsiburada.com/cep-telefonlari-c-371965?siralama=coksatan',
         'https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98?siralama=coksatan',
         'https://www.hepsiburada.com/beyaz-esya-ankastreler-c-235604?siralama=coksatan',
         'https://www.hepsiburada.com/bayan-giyim-modelleri-c-12087178?siralama=coksatan',
         'https://www.hepsiburada.com/erkek-giyim-modelleri-c-12087177?siralama=coksatan',
         'https://www.hepsiburada.com/mobilyalar-c-18021299?siralama=coksatan',
         'https://www.hepsiburada.com/oyuncaklar-c-23031884?siralama=coksatan',
         'https://www.hepsiburada.com/spor-malzemeleri-kiyafetleri-c-369685?siralama=coksatan',
         'https://www.hepsiburada.com/kozmetik-c-2147483603?siralama=coksatan',
         'https://www.hepsiburada.com/kitaplar-c-2147483645?siralama=coksatan']

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

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}
liste=[]
sayac=1
for site in siteler:
    print(site)
    r= requests.get(site,headers=headers)
    soup = BeautifulSoup(r.content,'lxml')
    st1 = soup.find("div",attrs={"class":"productListContainer-root"})
    st2 = st1.find("ul",attrs={"class":"productListContainer-wrapper productListContainer-grid-0"})
    st3 = st2.find("li",attrs={"class":"productListContainer-item"})
    a=1
    while a<=1:
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}
        r= requests.get(site+"&sayfa="+str(a)+"",headers=headers)
        soup = BeautifulSoup(r.content,'lxml')
        st1 = soup.find("div",attrs={"class":"productListContainer-root"})
        st2 = st1.find("ul",attrs={"class":"productListContainer-wrapper productListContainer-grid-0"})
        st3 = st2.find_all("li",attrs={"class":"productListContainer-item"})
        for icerik in st3:
            link=icerik.a.get("href")
            r1=requests.get(link,headers=headers)
            soup1=BeautifulSoup(r1.content,"lxml")
            urunAdi = soup1.find("span",attrs={"class":"product-name"}).text
            print (urunAdi)
            kategori=kategoriler[sayac]
            urunMarkasi = soup1.find("a",attrs={"data-bind":"attr: {'data-hbus': userInformation() && userInformation().userId && isEventReady()? productDetailHbus('BrandClick') : '' }"}).text
            originalPrice = soup1.find("del",attrs={"id":"originalPrice"}).text
            try:
                simdikiFiyat = soup1.find("span",attrs={"data-bind":"markupText:'currentPriceBeforePoint'"}).text
            except:
                simdikiFiyat = originalPrice
            try:
                simdikiFiyat_kurus = soup1.find("span",attrs={"data-bind":"markupText:'currentPriceAfterPoint'"}).text
            except:
                simdikiFiyat_kurus = "00"
            try:
                puan = soup1.find("span",attrs={"class":"rating-star"}).text
            except:
                puan="NaN"
            try:
                degerlendirme = soup1.find("div",attrs={"id":"comments-container"}).text
            except:
                degerlendirme= "NaN"
            
            liste.append([link,urunAdi,urunMarkasi,kategori,originalPrice,simdikiFiyat,simdikiFiyat_kurus,puan,degerlendirme])
        a=a+1
    pd.DataFrame(liste)
    df = pd.DataFrame(liste)
    df.columns = ("link","urunAdi","urunMarkasi","kategori","originalPrice","simdikiFiyat","simdikiFiyat_kurus","puan","degerlendirme")
    sayac=sayac+1
    #liste=[]
    #df.to_csv(timestampStr+".csv"+"")
    
    #df2=pd.read_csv("12-Oct-2021.csv")

"""--------------------------------------------------------------"""
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
trendyol=['https://www.trendyol.com/sr?wc=103498&sst=BEST_SELLER',
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

dateTimeObj1 = datetime.now()
timestampStr1 = dateTimeObj.strftime("%d-%b-%Y")

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}



liste_trendyol=[]
sayac_trendyol=1
for site_ in trendyol:
    print(site_)
    r_= requests.get(site_,headers=headers)
    soup_ = BeautifulSoup(r_.content,'lxml')
    st1_ = soup_.find("div",attrs={"class":"prdct-cntnr-wrppr"})
    st2_ = st1.find("div",attrs={"class":"p-card-chldrn-cntnr"})
    linkSonu=st2_.a.get("href")
    linkBasi="https://www.trendyol.com"
    link=linkBasi+linkSonu
    print(link)
    b=1
    while b<=1:
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}
        r= requests.get(site_+"&pi="+str(b)+"",headers=headers)
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
                print(degerlendirme)
            except:
                degerlendirme= "NaN"
                print(degerlendirme)
            liste_trendyol.append([link,urunAdi,urunMarkasi,originalPrice,simdikiFiyat,simdikiFiyat_kurus,puan,degerlendirme])
        b=b+1
    pd.DataFrame(liste)
    df_trendyol = pd.DataFrame(liste_trendyol)
    df_trendyol.columns = ("link","urunAdi","urunMarkasi","originalPrice","simdikiFiyat","simdikiFiyat_kurus","puan","degerlendirme")
    sayac_trendyol=sayac_trendyol+1