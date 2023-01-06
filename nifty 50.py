#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import missingno as ms
import warnings 
warnings.filterwarnings("ignore")
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv("National_Stock_Exchange_of_India_Ltd.csv")


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.info()


# In[6]:


df["365 d % chng"].value_counts()


# In[7]:


df["365 d % chng"].value_counts().sum()


# In[8]:


ms.heatmap(df)


# In[23]:


ms.bar(df,color="pink")


# In[24]:


ms.matrix(df)


# In[ ]:





# In[9]:


sns.distplot(df["365 d % chng"],hist_kws = dict(linewidth=1,edgecolor="red"))


# In[10]:


df.isnull().sum()


# In[11]:


df.isnull()


# In[12]:


import seaborn as sns
import missingno as ms


# ms.bar(df)

# In[13]:


ms.bar(df)


# In[14]:


unique_number = []  
for i in df.columns:
    x = df[i].value_counts().count()
    unique_number.append(x)
        
pd.DataFrame(unique_number,index = df.columns,columns=["Total Unique Value"])
     


# In[15]:


sns.set_style("whitegrid")
sns.distplot(df["30 d % chng"], hist_kws = dict(linewidth = 1, edgecolor = 'g', color = 'r'))


# In[16]:


uniquename=[]
for i in df.columns:
    x= df[i].value_counts().count()
    uniquename.append(x)
    
    

pd.DataFrame(uniquename,index=df.columns,columns=["Total Unique Names"])  


# In[17]:


correlation = df.drop(['Open'],axis=1).corr()
plt.figure(figsize=(10,10))
sns.heatmap(correlation,annot=True)
plt.show()


# In[18]:


df.info(int)


# In[19]:


numerical = ["Chng","Volume (lacs)","% Chng"]
numerical_axis = ["change","Vol","%C"]
list(zip(numerical,numerical_axis))
[("Chng","change"),("Volume (Lacs)","Vol"),("% Chng","%C")]


# In[ ]:





# In[20]:


title_font = {"family":"arial","color":"darkblue","weight":"bold","size":15}
axis_font = {"family":"arial","color":"darkred","weight":"bold","size":10}
for i,z in list(zip(numerical,numerical_axis)):
    plt.figure(figsize=(8,8),dpi = 90)
    sns.distplot(df[i], hist_kws=dict(linewidth=1,edgecolor="r"))
    
    plt.title(i,fontdict = title_font)
    plt.xlabel(z,fontdict=axis_font)
    plt.ylabel("Density",fontdict=axis_font)
    
    plt.tight_layout()
    plt.show()


# In[21]:


fig , (axis1,axis2,axis3,axis4) = plt.subplots(1,4,figsize=(20,10))
axis1.boxplot(df["30 d % chng"])
axis1.set_title("30 d % chng")

axis2.boxplot(df["365 d % chng"])
axis2.set_title("365 d % chng")

axis3.boxplot(df["Volume (lacs)"])
axis3.set_title("Volume (lacs)")

]-
axis4.boxplot(df["% Chng"])
axis4.set_title("% Chng")

plt.show()


# In[22]:


title_font = {"family": "arial", "color":"darkblue","weight":"bold","size":15}
axis_font = {"family": "arial", "color":"darkred","weight":"bold","size":10}
for i,z in list(zip(numerical,numerical_axis)):
    fig, axis = plt.subplots(figsize=(8,6))
    
    observational_values = list(df[i].value_counts().index)
    toatl_observation_values = list(df[i].value_counts())
    
    axis.pie(toatl_observation_values,labels= observational_values, autopct = "%1.1f%%",startangle = 110 , labeldistance = 1.1)
    axis.axis("equal")
    
    plt.title((i+ "(" + z + ")"), fontdict = title_font)
    plt.legend()
    plt.show()


# In[ ]:




