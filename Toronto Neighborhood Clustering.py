#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import the library we use to open URLs
import urllib.request


# In[2]:


url = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"


# In[3]:


page = urllib.request.urlopen(url)


# In[4]:


# import the BeautifulSoup library so we can parse HTML and XML documents
from bs4 import BeautifulSoup


# In[5]:


# parse the HTML from our URL into the BeautifulSoup parse tree format
soup = BeautifulSoup(page, "lxml")


# In[6]:


print(soup.prettify())


# In[7]:


soup.title


# In[8]:


soup.title.string


# In[9]:


all_tables = soup.find_all("table")
all_tables


# In[10]:


right_table=soup.find('table', class_='wikitable sortable')
right_table


# In[20]:


A=[]
B=[]
C=[]

for row in right_table.findAll('tr'):
    cells=row.findAll('td')
    if len(cells)==3:
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
       


# In[21]:


import pandas as pd
df=pd.DataFrame(A,columns=['PostalCode'])
df['Borough']=B
df['Neighborhood']=C
df


# In[22]:


df.shape


# In[23]:


df.head()


# In[32]:


df.tail(10)


# In[34]:


df.count()


# In[48]:


df_1=df.replace(to_replace ="Not assigned\n", 
                 value ="Borough")


# In[49]:


df_1.head(20)


# In[50]:


df_2=df_1.replace(to_replace ="North York\n", 
                 value ="North York")


# In[51]:


df_3=df_2.replace(to_replace ="Downtown Toronto\n", 
                 value ="Downtown Toronto")


# In[52]:


df_4=df_3.replace(to_replace ="Etobicoke\n", 
                 value ="Etobicoke")


# In[53]:


df_5=df_4.replace(to_replace ="Scarborough\n", 
                 value ="Scarborough")


# In[54]:


df_6=df_5.replace(to_replace ="East York\n", 
                 value ="East York")


# In[55]:


df_6.head(10)


# In[56]:


df_6.shape


# In[ ]:




