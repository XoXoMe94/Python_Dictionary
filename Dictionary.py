# -*- coding: utf-8 -*-
"""

@author: sara
"""

# list: a linear collection of values that stay in order
# Dictionary: a bag of values, each with its label ( messy)
# Ex :candy , tissue, money, perfume 
# dictionary is like list except they use key instead of number to
#   look up values



#ex1 
a=dict()
a['money']=10
a['candy']=2
a['perfume']=6
print(a) #{'money': 10, 'candy': 2, 'perfume': 6}


#ex2
a=dict()
a['money']=10
a['candy']=2
a['perfume']=6
print(a['candy']) #2



#ex3 
a=dict()
a['money']=10
a['candy']=2
a['perfume']=6
a['candy']=a['candy']+2
print(a)  #{'money': 10, 'candy': 4, 'perfume': 6}



#ex4 creat dic
count={'sara':2, 'Reid':3}
print(a) #{'sara:2', 'Reid:3'}

b={} 
print(b) #empty dic {}


#ex5
count=dict()
names=['b','c','c','e','y','y']
for name in names:
    if name not in count:
        count[name]=1
    else:
        count[name]=count[name]+1
print(count) #{'b': 1, 'c': 2, 'e': 1, 'y': 2}



#ex6 get
count=dict()
names=['b','c','c','e','y','y']
for name in names:
    count[name]=count.get(name,0) +1
print(count) #{'b': 1, 'c': 2, 'e': 1, 'y': 2}



#ex7 wordcount

count=dict() # make a dic
print('Enter:') #sara haghighi 27 iran sara
line=input('') #input a line of text 
words=line.split() #list of words
print('words:', words)  #words: ['sara', 'haghighi', '27', 'iran', 'sara']

for word in words:
    count[word]=count.get(word,0)+1
print('counts', count) #counts {'sara': 2, 'haghighi': 1, '27': 1, 'iran': 1}



#ex8 key
count={'sara':2, 'Alex':3}
for key in count:
    print(key, count[key]) #sara 2     Alex 3
    


#ex9 
count={'sara':2, 'Reid':3}
print(list(count)) #['sara', 'Reid']
print(count.keys()) #dict_keys(['sara', 'Reid'])
print(count.values())  #dict_values([2, 3])
print(count.items()) #dict_items([('sara', 2), ('Reid', 3)])



#ex10
count={'sara':2, 'Alex':3}
for a,b in count.items() :
    print(a,b) #sara 2   Alex 3


#ex11
name=input('Enter:') #input a file
handle=open(name)

count=dict() #make a dic
for i in handle :
    words=i.split() #list of words
    for word in words:
        count[word]=count.get(word,0) +1
print(count) #{'From': 3, 'sara@yahoo': 1, 'Sat': 1, 'Jan': 1, '2020': 2, 'Reid@yahoo': 1, 'Fri': 1, 'Feb': 1, 'Sara': 1, 'HEllo': 1, 'Med@yahoo': 1, 'Mon': 1, 'Apr': 1, '2022': 1}

bigcount= None
bigword= None
for word,count in count.items():
    if bigcount is None or count>bigcount :
        bigword=word
        bigcount=count
print(bigword, bigcount)      #From 3   

