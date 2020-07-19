#!/usr/bin/env python
# coding: utf-8

# In[62]:


import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np
import plotly.express as px

plt.rc('font', family='Malgun Gothic')


# In[2]:


death = pd.read_excel("E:\\Eric_Github\\repo001\\Sample_Data\\1518_death.xlsx", encoding="utf-8")


# In[3]:


death.head()


# In[157]:


## 요일(3) & 사망자수 

death1 = death.iloc[:,[3,10]]
death1 = pd.DataFrame(death1)
death1_grouped = death1["사망자수"].groupby(death1["요일"])
death_grouped_sum =death_grouped.sum().sort_index(ascending=True)
b1 = pd.DataFrame(data=death_grouped_sum, columns=['사망자수'], index=['금','목','수','월','일','토','화'])
b2 = b1.loc[['월','화','수','목','금','토','일'],:]

## 발생일(0) & 사망자수 
death2 = death.iloc[:,[0,10]]
death2 = pd.DataFrame(death2)
death2_grouped = death2["사망자수"].groupby(death2["발생일"])
death2_grouped_sum =death2_grouped.sum()
de2 = pd.DataFrame(death2_grouped_sum)

## 기상상태(6) & 사망자수 
death3 = death.iloc[:,[6,10]]
death3 = pd.DataFrame(death3)
death3_grouped = death3["사망자수"].groupby(death3["기상상태"])
death3_grouped_sum = death3_grouped.sum()
de3 = pd.DataFrame(death3_grouped_sum)
de3 =de3.reset_index()

## 노면상태(8) & 사망자수 
death4 = death.iloc[:,[8,10]]
death4 = pd.DataFrame(death4)
death4_grouped = death4["사망자수"].groupby(death4["노면상태"])
death4_grouped_sum = death4_grouped.sum()
de4 = pd.DataFrame(death4_grouped_sum)
de4 =de4.reset_index()

## 도로종류(14) & 사망자수

death5 = death.iloc[:,[14,10]]
death5 = pd.DataFrame(death5)
death5_grouped = death5["사망자수"].groupby(death5["도로종류"])
death5_grouped_sum = death5_grouped.sum()
de5 = pd.DataFrame(death5_grouped_sum)
de5 =de5.reset_index()

## 도로형태(16) & 사망자수

death6 = death.iloc[:,[16,10]]
death6 = pd.DataFrame(death6)
death6_grouped = death6["사망자수"].groupby(death6["도로형태"])
death6_grouped_sum = death6_grouped.sum()
de6 = pd.DataFrame(death6_grouped_sum)
de6 =de6.reset_index()

## 도로선형(20) & 사망자수

death7 = death.iloc[:,[20,10]]
death7 = pd.DataFrame(death7)
death7_grouped = death7["사망자수"].groupby(death7["도로선형"])
death7_grouped_sum = death7_grouped.sum()
de7 = pd.DataFrame(death7_grouped_sum)
de7 =de7.reset_index()


# In[153]:


print(death7)


# In[142]:


plt.bar(de3["기상상태"],de3["사망자수"],color="blue")
plt.show()


# In[145]:


plt.bar(de4["노면상태"],de4["사망자수"],color="blue")
plt.show()


# In[148]:


plt.bar(de5["도로종류"],de5["사망자수"],color="blue")
plt.show()


# In[155]:


plt.bar(de6["도로형태"],de6["사망자수"],color="blue")
plt.show()


# In[156]:


plt.bar(de7["도로선형"],de7["사망자수"],color="blue")
plt.show()


# In[106]:


type(de2)


# In[107]:


de2.plot()


# In[81]:


print(death_grouped_sum)


# In[65]:


death.columns


# In[49]:


death1_grouped = death1["사망자수"].groupby(death1["요일"])
b =death_grouped.sum().sort_index(ascending=True)


# In[79]:


type(b)
b


# In[52]:


b2 = pd.DataFrame(data=b, columns=['사망자수'], index=['금','목','수','월','일','토','화'])


# In[55]:


b2


# In[60]:


#b3 = pd.DataFrame(data=b2, rows=['월','화','수','목','금','토','일'])

b3 = b2.loc[['월','화','수','목','금','토','일'],:]
b3


# In[63]:


b3.plot()


# In[ ]:




