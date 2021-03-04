
"""Q1:Output a file with list of US states in order, by:
a)
Alphabetical
b)
Number of letters in name
c)
Reverse Alphabetical order"""


states=['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan',
        'Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina',
        'South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']

#list in alphabetical order
l1_alphabetical=sorted(states)
f1=open("ListofUSStates_Alphabetical",'w')
for i in l1_alphabetical:
    f1.write(i+'\n')
print(l1_alphabetical)
# sorted list based on length of element
states.sort(key=len)
l2_len_order = states
f2 = open("ListofUSStates_len_state", 'w')
for i1 in l2_len_order:
    f2.write(i1 + '\n')
print(l2_len_order)
# sorted list reverse alphabetical
states.sort(reverse=True)
l3_reverse_alphabetical = states

f3=open("ListofUSStates_Rev_Alphabetical",'w')
for i2 in l3_reverse_alphabetical:
    f3.write(i2+'\n')
print(l3_reverse_alphabetical)



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
print(state_doubleletter)


"""Q3:Output a file with list of US states , in alphabetical order, that have Capitol names
of less than 10 characters length"""
list1=[]
stateandcapitals={'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
                  'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
                  'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for key,value in stateandcapitals.items():
    if len(value)<10:
        list1.append(key)
    else:
        continue
f=open("ListofUSStates_capital_len",'w')
for i in list1:
    f.write(i+'\n')
print(list1)




