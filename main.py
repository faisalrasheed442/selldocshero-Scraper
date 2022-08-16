from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
import time
os.system('cls')
url="https://selldocshero.com/test-banks"

doc=requests.get(url).text
result=BeautifulSoup(doc,'html.parser')
total_page=result.find('div',class_='count')
total_page=int(total_page.find_all('span')[2].string)
# print(total_page)
rows=result.find('div',class_='row mb-md-5 mb-4 mx-md-n2 mx-n1 no-gutters')
items=rows.find_all('div',class_="product-block text-center mb-md-3 mb-2 p-md-3 p-2 rounded trsn")
names=[]
prices=[]
links=[]
for page in range(1,total_page+1):
    try:
        time.sleep(5)
        url=f"https://selldocshero.com/test-banks?page={page}"
        doc=requests.get(url).text
        result=BeautifulSoup(doc,'html.parser')
        rows=result.find('div',class_='row mb-md-5 mb-4 mx-md-n2 mx-n1 no-gutters')
        items=rows.find_all('div',class_="product-block text-center mb-md-3 mb-2 p-md-3 p-2 rounded trsn")
        for item in items:
            href=item.find('div',class_="brand-name small trsn").a
            link=href['href']
            name=item.find('img',class_='img-fluid img-portfolio img-hover mb-2')['alt']
            price=item.find('div',class_="list-price").span.text
            names.append(name)
            prices.append(price)
            links.append(link)
        print(f'done {page}')
    except:
        print(f"page {page}  not done")
        

scrap={"Name":names,'Price':prices,"Link":links}

df = pd.DataFrame(scrap)
df.to_excel(f"resullt.xlsx")

print("completed data scraping check now")
