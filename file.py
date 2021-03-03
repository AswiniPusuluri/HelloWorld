#f=open("C:\\Users\\aswin\\PythonPractice\\usa.states.txt","r")
#print(f.read())

import ssl
#import urllib.request
#with urllib.request.urlopen('https://www.britannica.com/topic/list-of-state-capitals-in-the-United-States-2119210')

# import requests
# import pandas as pd
# import urllib.request
# import time
# from bs4 import BeautifulSoup
# products=[]
# #url = 'https://codegolf.stackexchange.com/questions/64254/states-and-capitals'
# url = 'https://www.britannica.com/topic/list-of-state-capitals-in-the-United-States-2119210'
# response = requests.get(url)
# soup = BeautifulSoup(response.content,"html.parser")
# soup = soup.findAll('a',attrs={'class': 'md-crosslink'})
# list_capitals = []
# for item in soup:
#     list_capitals.append(item.text)
# print(list_capitals)
# gdp_table = soup.find("table")
# gdp_table_data = gdp_table.tbody.find_all("tr")
# for item in gdp_table_data:
#     for item1 in item.find_all("td"):
#         print(item1.text)


#soup.findAll('code')
#capitals=list(soup.find('code').findNext('code').findNext('code'))
# converting to string
#capitals=str(capitals)
#capitals=capitals.replace(',',':').replace('\\n',',')
#print(capitals)
#dataframe=pd.DataFrame([i for i in capitals.split(',')])
#dataframe.to_csv('Capitals.csv', index=False, encoding='utf-8')

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

import requests
from bs4 import BeautifulSoup
url = "https://www.britannica.com/topic/list-of-state-capitals-in-the-United-States-2119210"
soup = BeautifulSoup(requests.get(url).content, "html.parser")
dic_state = {}
for row in soup.findAll('table')[0].tbody.findAll('tr'):
    first_column = row.findAll('td')[0].text
    second_column = row.findAll('td')[1].text
    dic_state[first_column] = second_column

f = open("C:\\Users\\aswin\\PythonPractice\\usa.states.txt","r")
for line in f:
    line = line.rstrip("\n")
    print("{}, {}".format(line, dic_state[line]))


