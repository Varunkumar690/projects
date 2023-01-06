#!/usr/bin/env python
# coding: utf-8

# In[2]:


import seaborn as sns
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import missingno as ms
import plotly.express as px


# In[3]:


df = pd.read_csv("Google-Playstore.csv")


# In[4]:


df.describe()


# In[5]:


df.head()


# In[4]:


df.tail()


# In[6]:


df.info()


# In[7]:


df.isnull().sum()


# In[8]:


df.isnull().sum().sort_values(ascending = False)


# In[9]:


df.shape


# In[10]:


df.columns


# In[11]:


ms.heatmap(df)


# In[12]:


ms.bar(df)


# In[13]:


ms.matrix(df)


# In[14]:


missing_percentage=df.isnull().sum().sort_values(ascending = False)/len(df)
missing_percentage=missing_percentage[missing_percentage!=0]
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"]=(20,10)
missing_percentage.plot(kind="barh")


# In[15]:


df.dropna(subset=["App Name", "Size", "Currency","Installs", "Minimum Installs","Developer Id","Developer Email"],inplace=True)


# In[16]:


df.isnull().sum().sort_values(ascending = False)


# In[17]:


boolean=df["App Name"].duplicated().any()
boolean


# In[18]:


df["App Name"].value_counts()


# In[19]:


df["App Id"].duplicated().any()


# In[20]:


df["App Id"].value_counts()


# In[21]:


df["Installs"].unique()


# In[22]:


df["Installs"] = df["Installs"].str.split("+").str[0]
df["Installs"].replace(',','',regex=True, inplace=True)
df["Installs"] = df["Installs"].astype(np.int64) 


# In[23]:


df["Installs"].unique()


# In[24]:


df["Currency"].unique()


# In[25]:


df["Size"].unique()


# In[26]:


df["Size"] = df["Size"].apply(lambda x:str(x).replace("M","") if 'M' in str(x) else x)
df["Size"] = df['Size'].apply(lambda x:str(x).replace(',','.') if ',' in str(x) else x)
df["Size"] = df['Size'].apply(lambda x:float(str(x).replace('k',''))/1000 if 'k' in str(x) else x)


# In[27]:


df['Size'] = df["Size"].apply(lambda x:float(x))


# In[28]:


df["Size"] =df["Size"].apply(lambda x: str(x).replace("Varies with device","0")if 'Varies with device' in str(x) else(x))


# In[29]:


df['Size'] = df['Size'].apply(lambda x:float(x))


# In[30]:


df['Size'] = df['Size'].apply(lambda x:float(str(x).replace('G',''))*1000 if 'G' in str(x) else x)


# In[31]:


df['Size'] = df['Size'].apply(lambda x:float(x))


# In[32]:


df.dtypes['Size']


# In[33]:


df['Minimum Android']


# In[34]:


df['Content Rating']


# In[35]:


df['Released']


# In[37]:


df['Last Updated']


# In[38]:


df['Privacy Policy']


# In[39]:


df['Scraped Time']


# In[40]:


df['Type'] = np.where(df['Free'] == True, 'Free','Paid')
df.drop(['Free'], axis = 1, inplace=True)


# In[41]:


df.describe()


# In[42]:


df['Content Rating'].unique()


# In[44]:


df['Content Rating']=df['Content Rating'].replace('Everyone 10+','Everyone')
df['Content Rating']=df['Content Rating'].replace('Unrated','Teen')
df['Content Rating']=df['Content Rating'].replace('Adults only 18+','Adults')
df['Content Rating']=df['Content Rating'].replace('Mature 17+ ','Adults')


# In[45]:


df['Content Rating'].unique()


# In[46]:


df.info()


# In[47]:


df['Rating'].unique()


# In[48]:


df['Rating Count'].max()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       


# In[49]:


df['Rating Type'] = 'NoRatingProvided'
df.loc[(df['Rating Count'] > 0) & (df['Rating Count'] <= 10000.0),'RatingType'] = 'Less than 10K'
df.loc[(df['Rating Count'] > 10000) & (df['Rating Count'] <= 500000.0),'RatingType'] = 'Between 10K and 500K'
df.loc[(df['Rating Count'] > 500000) & (df['Rating Count'] <= 138557570.0),'RatingType'] = 'More than 500K'
df.RatingType.value_counts()


# In[53]:


df.info()


# In[50]:


df['Category'].unique()


# In[51]:


top_Category = df.Category.value_counts().reset_index().rename(columns={'Category':'Count','index':'Category'})


# In[52]:


top_Category 


# In[54]:


Category_installs = df.groupby(['Category'])[['Installs']].sum()


# In[55]:


Category_installs


# In[56]:


top_Category_installs = pd.merge(top_Category, Category_installs, on='Category')
top_Category_installs.head(5)


# In[58]:


top_10_Categories_installs = top_Category_installs.head(10).sort_values(by = ['Installs'],ascending = False)


# In[59]:


import matplotlib.pyplot as plt
plt.figure(figsize=(14,7))
plt.xticks(rotation=60)
plt.xlabel("Category")
plt.ylabel("Number of applications")
plt.title("Top 10 Installed Categories")
sns.barplot(top_10_Categories_installs.Category, top_10_Categories_installs.Installs)


# In[ ]:




