#f=open("C:\\Users\\aswin\\PythonPractice\\usa.states.txt","r")
#print(f.read())

import ssl
#import urllib.request
#with urllib.request.urlopen('https://www.britannica.com/topic/list-of-state-capitals-in-the-United-States-2119210')

import requests
import pandas as pd
import urllib.request
import time
from bs4 import BeautifulSoup
products=[]
url = 'https://codegolf.stackexchange.com/questions/64254/states-and-capitals'
response = requests.get(url)
response.content
soup = BeautifulSoup(response.content,"html.parser")
soup.findAll('code')
capitals=list(soup.find('code').findNext('code').findNext('code'))
# converting to string
capitals=str(capitals)
capitals=capitals.replace(',',':').replace('\\n',',')
print(capitals)
dataframe=pd.DataFrame([i for i in capitals.split(',')])
dataframe.to_csv('Capitals.csv', index=False, encoding='utf-8')

#df = pd.DataFrame({'Capital Name':capitals})
#df.to_csv('products.csv', index=False, encoding='utf-8')
#print(soup.prettify())

#print(soup.title.string)
'''for a in soup:
    name = a.find('a', attrs={'class': 'md-crosslink'})
    products.append(name.text)
print(products)'''

'''for a in soup:
    name = a.find('a').text
    products.append(name)
print(products)'''



