import requests
from bs4 import BeautifulSoup
import pandas as pd

books=[]
for i in range(1,5):
    url=f"https://books.toscrape.com/catalogue/page-{i}.html"
    response=requests.get(url)
    response=response.content
    #print(response)

    soup=BeautifulSoup(response,'html.parser')
    #print(soup)

    ol=soup.find('ol')
    articles=ol.find_all('article',class_='product_pod')
    #print(articles)


    for article in articles:
        image=article.find('img')
        title=image.attrs['alt']
        #print(title)
        star=article.find('p')
        star=star['class'][1]
        #print(star)
        price=article.find('p',class_='price_color').text
        price=float(price[1:])
        path=image.attrs['src']
        #print(price)
        books.append([title,price,star,path])
    #print(books)

df=pd.DataFrame(books,columns=['Title','Price','StarRating','ImagePath'])
df.to_csv('books.csv')
