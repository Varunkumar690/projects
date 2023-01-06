#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import missingno as ms
import plotly.express as px


# In[ ]:





# In[2]:


df=pd.read_csv("WHO-COVID-19-global-data.csv.xls")


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.info("Japan")


# In[6]:


df.isnull().sum()


# In[7]:


df.describe()


# In[8]:


fig= px.area(df,x="Date_reported",y="Cumulative_cases",color="Country" )
fig.show()


# In[9]:


fig= px.area(df,x="Date_reported",y="Cumulative_deaths",color="Country" )
fig.show()


# In[13]:


fig= px.area(df,x="Date_reported",y="Cumulative_deaths",color="Country",line_group="Country" )
fig.show()

