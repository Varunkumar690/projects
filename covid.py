#!/usr/bin/env python
# coding: utf-8

# In[4]:


import seaborn as sns
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


# In[5]:


df = pd.read_csv("covid.csv.xls")


# In[6]:


df.head()


# In[7]:


df.info()
df.shape


# In[8]:


df.isnull().sum()


# In[9]:


df.describe()


# In[10]:


df=df.drop("Date",axis=1)


# In[11]:


import plotly.express as px


# In[12]:


fig = px.bar(df,x="Date_YMD",y="Daily Confirmed")
fig.show()


# In[13]:


cases = df["Daily Confirmed"].sum()
deceased=df["Daily Deceased"].sum()

labels = ["confimed","Deceased"]
values = [cases,deceased]

fig = px.pie(df,values=values,
             names=labels,
             title="Daily Confirmed Cases vs Daily Deaths",hole=0.5)
fig.show()


# In[11]:


death_rate=(df["Daily Deceased"].sum()/df["Daily Confirmed"].sum())*100
print(death_rate)


# In[12]:


get_ipython().system('pip install autots')


# In[14]:


import autots 
from autots import AutoTS


# In[15]:


model =AutoTS(forecast_length=30,frequency="infer",ensemble="simple")
model= model.fit(df,date_col="Date_YMD",value_col="Daily Deceased",id_col=None)
prediction= model.predict()
forecast= prediction.forecast
print(forecast)


# In[ ]:


df.loc[df["Country"]=="Japam",:]

