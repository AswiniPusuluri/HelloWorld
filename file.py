import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://www.britannica.com/topic/list-of-state-capitals-in-the-United-States-2119210"
soup = BeautifulSoup(requests.get(url).content, "html.parser")
dic_state = {}
for row in soup.findAll('table')[0].tbody.findAll('tr'):
    first_column = row.findAll('td')[0].text
    second_column = row.findAll('td')[1].text
    dic_state[first_column] = second_column

f = open("C:\\Users\\aswin\\PythonPractice\\usa.states.txt","r")
capitals = []
for line in f:
    line = line.rstrip("\n")
    capital = "{}, {}".format(line, dic_state[line])
    capitals.append(capital)
    print("{}, {}".format(line, dic_state[line]))

df = pd.DataFrame({"State, Capital":capitals})
df.to_csv('Capitals.csv', index=False, encoding='utf-8')

