#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("Games.csv")


# In[3]:


df


# In[4]:


df.shape


# In[5]:


df.head()


# In[6]:


df.tail()


# In[7]:


df.info()


# In[8]:


df.isnull()


# In[9]:


df.isnull().sum()


# In[10]:


df.describe()


# In[11]:


df["Sales"].value_counts()


# In[12]:


df["Sales"].value_counts().sum()


# In[13]:


import missingno as ms


# In[ ]:





# In[14]:


ms.bar(df,color="red")


# In[15]:


ms.matrix(df)


# In[16]:


ms.heatmap(df)


# In[17]:


ms.dendrogram(df)


# In[18]:


import seaborn as sns


# In[19]:


sns.displot(df["Sales"])


# In[20]:


sns.distplot(df["Sales"])


# In[21]:


sns.distplot(df["Sales"],hist_kws = dict(linewidth=2,edgecolor="r"))


# In[22]:


sns.distplot(df["Sales"],hist = False)


# In[23]:


sns.set_style("whitegrid")


# In[24]:


sns.distplot(df["Sales"])


# In[25]:


sns.distplot(df["Sales"],hist = False)


# In[26]:


x,y = plt.subplots(figsize=(8,8))
sns.distplot(df["Sales"],hist=False,ax=y)
y.axvline(df["Sales"].mean(),color="r",ls="--")


# In[27]:


uniquename=[]
for i in df.columns:
    x= df[i].value_counts().count()
    uniquename.append(x)
    
    

pd.DataFrame(uniquename,index=df.columns,columns=["Total Unique Names"])    


# In[28]:


ms.bar(df)


# In[29]:


correlation = df.drop(['Genre'],axis=1).corr()
plt.figure(figsize=(10,10))
sns.heatmap(correlation,annot=True)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




