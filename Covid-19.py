#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


# In[3]:


df= pd.read_csv(r'C:\Users\dilee\Downloads\covid_19_data.csv.zip')


# In[4]:


df.head()


# In[5]:


df.drop(['SNo','Last Update'],axis=1,inplace=True)


# In[6]:


df.head()


# In[7]:


df.rename(columns={'ObservationDate':'Date','Province/State':'State','Country/Region':'Country'},inplace=True)


# In[8]:


df.head()


# In[9]:


df['Date']=pd.to_datetime(df['Date'])


# In[10]:


df.head()


# In[11]:


imputer=SimpleImputer(strategy='constant')
df2=pd.DataFrame(imputer.fit_transform(df),columns=df.columns)


# In[13]:


df2.head()


# In[15]:


df3 = df2.groupby(['Date', 'Country'])[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()


# In[16]:


df3


# In[17]:


df3 = df2.groupby(['Country', 'Date'])[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()


# In[18]:


df3


# In[19]:


df3.head(10)


# In[20]:


countries = df3['Country'].unique()
len(countries)


# In[22]:


for idx in range(0,len(countries)):
    C=df3[df3['Country']==countries[idx]].reset_index()
    plt.scatter(np.arange(0,len(C)),C['Confirmed'],color='blue',label='Confirmed')
    plt.scatter(np.arange(0,len(C)),C['Recovered'],color='green',label='Recovered')
    plt.scatter(np.arange(0,len(C)),C['Deaths'],color='red',label='Deaths')
    plt.title(countries[idx])
    plt.xlabel('Days since the first suspect')
    plt.ylabel('Number of cases')
    plt.legend()
    plt.show()


# In[ ]:




