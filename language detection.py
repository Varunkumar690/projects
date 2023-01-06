#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
df = pd.read_csv("dataset.csv")
print(df.head())


# In[2]:


df = pd.read_csv("dataset.csv")


# In[3]:


df.info()


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.isnull().count()


# In[7]:


df["language"].value_counts()


# In[8]:


x = np.array(df["Text"])
y = np.array(df["language"])

cv = CountVectorizer()
X = cv.fit_transform(x)
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.33, 
                                                    random_state=42)


# In[9]:


model = MultinomialNB()
model.fit(X_train,y_train)
model.score(X_test,y_test)


# In[10]:


user = input("Enter a Text: ")
df = cv.transform([user]).toarray()
output = model.predict(df)
print(output)


# In[ ]:




