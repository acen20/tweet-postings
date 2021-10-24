#!/usr/bin/env python
# coding: utf-8

# In[682]:


#pandas lib for manipulation of data
import pandas as pd 


# In[683]:


#loading file
file_ = open('smalltweets.txt', 'r').read()


# In[684]:


lines_ = file_.split("\n") #splitting into lines on "\n" delimeter
tweets = [] #list to hold all tweets as objects
postings = [] #final positings will be appended to this list
match_ltr = 'a'


# In[685]:


#following loop is splitting each line into separate columns i.e. ID & Text 
for line in lines_:
    arr = line.split("\t")
    try:
        tweets.append({
            'ID': arr[0],
            'Text': arr[1].lower() #to match in lowercase letters
        })
    except:
        continue


# In[686]:


for tweet in tweets:
    txt = tweet['Text'].split(" ")
    txt = filter(lambda x: x.startswith(match_ltr),txt)
    occurrence = list(txt)
    
    #each occurrence is stored in a list
    postings.append({
        'ID':tweet['ID'],
        'Postings': occurrence
    })


# In[687]:


postings = pd.DataFrame(postings)


# In[688]:


postings['Entries'] = [len(i) for i in postings.Postings]
postings.sort_values(by = ['Entries'], ascending = False, inplace = True)
print(f'\n\n=============TERMS STARTING with "A"==============\n')
print(postings)


# In[689]:


terms = [] #to store all terms

for posting in postings['Postings']:#Union of all
    terms += posting


# In[690]:


terms = list(dict.fromkeys(terms)) #Remove duplicate words


# In[691]:


print(f'\n\n=============UNIQUE TERMS IN ALL DOCS=============\n')
print(terms)


# In[692]:


final_postings = {}
for term in terms:
    final_postings[term] = {
        'Frequency': 0, 
        'Docs': []
    }


# In[693]:


final_postings


# In[694]:


print(f'\n\n=============FINAL POSTINGS LIST============\n')

for term in terms:
    for tweet in tweets:
        if term in tweet['Text'].split(" "):
            final_postings[term]['Frequency'] += 1
            final_postings[term]['Docs'].append(tweet['ID'])
final = pd.DataFrame(final_postings).transpose().sort_values(by = ['Frequency'], ascending = False)

print(final)


# In[695]:


#MERGING
w1 = 'egg'
w2 = 'cheese'
answer = []
print(f'\n\n=============DOCS: {w1} AND {w2}============\n')

try:
    w1 = final_postings[w1]
    w2 = final_postings[w2]

    answer = w1['Docs'] + w2['Docs']
    answer = list(dict.fromkeys(answer))
    print(answer)
except:
    print("The word does not exist")


# In[696]:


#MERGING
w1 = 'chocolate'
w2 = 'strawberry'
answer = []
print(f'\n\n=============DOCS: {w1} AND {w2}============\n')

try:
    w1 = final_postings[w1]
    w2 = final_postings[w2]

    answer = w1['Docs'] + w2['Docs']
    answer = list(dict.fromkeys(answer))
    print(answer)
except:
    print("The word does not exist")


# In[697]:


#MERGING
w1 = 'egg'
w2 = 'cheese'
w3 = 'bacon'
answer = []
print(f'\n\n=============DOCS: {w1} AND {w2} AND {w3}============\n')

try:
    w1 = final_postings[w1]
    w2 = final_postings[w2]
    w3 = final_postings[w3]

    answer = w1['Docs'] + w2['Docs'] + w3['Docs']
    answer = list(dict.fromkeys(answer))
    print(answer)
except:
    print("The word does not exist")

