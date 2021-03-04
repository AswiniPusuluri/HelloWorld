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
print(dic_state)

print("In-Class US States Assignment2")

"""Q1:Output a file with list of US states in order, by:
a)
Alphabetical
b)
Number of letters in name
c)
Reverse Alphabetical order"""


states=list(dic_state.keys())

#list in alphabetical order
l1_alphabetical=sorted(states)
f1=open("ListofUSStates_Alphabetical",'w')
for i in l1_alphabetical:
    f1.write(i+'\n')
print(f'Alphabetical={l1_alphabetical}')
# sorted list based on length of element
states.sort(key=len)
l2_len_order = states
f2 = open("ListofUSStates_len_state", 'w')
for i1 in l2_len_order:
    f2.write(i1 + '\n')
print(f'Number of letters in name={l2_len_order}')
# sorted list reverse alphabetical
states.sort(reverse=True)
l3_reverse_alphabetical = states

f3=open("ListofUSStates_Rev_Alphabetical",'w')
for i2 in l3_reverse_alphabetical:
    f3.write(i2+'\n')
print(f'Reverse Alphabetical order={l3_reverse_alphabetical}')



"""Q2:Output a file with list of US states with double letter sequence ( e.g. Hawaii)"""
state_doubleletter=[]

for state in states:
    for j in range(len(state)-1):
        if state[j]==state[j+1]:
            if state not in state_doubleletter:
                state_doubleletter.append(state)

        else:
            continue
f=open("ListofUSStates_Double_let_seq",'w')
for i in state_doubleletter:
    f.write(i+'\n')
print(f'list of US states with double letter sequence={state_doubleletter}')


"""Q3:Output a file with list of US states , in alphabetical order, that have Capitol names
of less than 10 characters length"""
list1=[]

for key,value in dic_state.items():
    if len(value)<10:
        list1.append(key)
    else:
        continue
f=open("ListofUSStates_capital_len",'w')
for i in list1:
    f.write(i+'\n')
print(f'States that have Capitol names of less than 10 characters length={sorted(list1)}')






