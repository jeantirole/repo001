#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np
import plotly.express as px


# In[25]:


plt.rc('font', family='Malgun Gothic')


# In[3]:


death = pd.read_excel("C:\\Eric_work\\Github\\repo001\\1518_death.xlsx", encoding="utf-8")


# In[36]:


death.dtypes

#데이터 타입 확인 
#각 Feature 별로 데이터 타입을 확인해 보았다. 
#데이터의 내용에 따라 아래와 같이 분류해 보았다. 
#### 결측치 빼는거 확인 해봐야함 


# 1) Category Type, 
# 발생일, 발생시간, 주야, 요일 
# 발생지_시도, 발생지_시군구, 
# 기상상태, 노면상태_대분류, 노면상태
# 사고내용
# 도로종류, 도로형태_대분류, 도로형태
# 교차로형태_대분류, 교차로형태
# 도로선형_대분류 
# 도로선형

# 2)Numerical Type  
# 사망자수, 중상자수, 경상자수, 부상신고자수
# 경도, 위도 


# In[126]:


## 요일(3) & 사망자수 

death1 = death.iloc[:,[3,10]]
death1 = pd.DataFrame(death1)
death1_grouped = death1["사망자수"].groupby(death1["요일"])
death_grouped_sum =death1_grouped.sum().sort_index(ascending=True)
b1 = pd.DataFrame(data=death_grouped_sum, columns=['사망자수'], index=['금','목','수','월','일','토','화'])
b2 = b1.loc[['월','화','수','목','금','토','일'],:]

## 발생일(0) & 사망자수 
death2 = death.iloc[:,[0,10]]
death2 = pd.DataFrame(death2)
death2_grouped = death2["사망자수"].groupby(death2["발생일"])
death2_grouped_sum =death2_grouped.sum()
de2 = pd.DataFrame(death2_grouped_sum)
de2 =de2.reset_index()

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


# In[133]:


b3 = b2.reset_index()
b3.columns =['요일','사망자수']
b3


# In[138]:


## EDA 과정.. 시계열로 간다 후 가즈아 
##datetime -> year, month, day 로 쪼개보기 

de2['발생일']= pd.to_datetime(de2['발생일'], format = "%Y%m%d", errors='raise')
de2['년 단위'] = de2['발생일'].dt.year
de2['월 단위'] = de2['발생일'].dt.month
de2['시간 단위'] = death['발생시간']

fig,(ax1,ax2,ax3,ax4)= plt.subplots(nrows=4)
fig.set_size_inches(12,20)

monthgroup = pd.DataFrame(de2.groupby("월 단위")["사망자수"].mean()).reset_index()
sns.barplot(data=monthgroup,x="월 단위",y="사망자수", ax=ax1)

yeargroup = pd.DataFrame(de2.groupby("년 단위")["사망자수"].mean()).reset_index()
sns.barplot(data=yeargroup,x="년 단위",y="사망자수", ax=ax2)

sns.pointplot(data=b3,x="요일",y="사망자수", ax=ax3)

timegroup = pd.DataFrame(de2.groupby("시간 단위")["사망자수"].mean()).reset_index()
sns.barplot(data=de2,x="시간 단위",y="사망자수", ax=ax4)


# In[53]:


## EDA 과정.. Category 로 안바꿔서 밑에 그래프가 깨지는 건가.. 혹은 폰트 문제인가.. 어쨌든 둘다 해보도록 하자! 

categoryVariableList = ["주야","요일","기상상태","노면상태","도로종류","도로선형"]
for var in categoryVariableList: 
    death[var] = death[var].astype("category")


# In[63]:


## 주요변수들을 Box Plot 형태로 출력해보기. 근데 그래프가 깨지고 있음 ㅠㅠ 
## 이상치들이 많은지 확인도 해보고.. 많으면삭제도 하고 해야하는데.. 
## 시간대별 사고량 빼먹음 


fig,axes = plt.subplots(nrows=3,ncols=2)
fig.set_size_inches(12, 10)

sns.boxplot(data=death,y="사망자수",x="주야",ax=axes[0][0])
sns.boxplot(data=death,y="사망자수",x="요일",orient="v",ax=axes[0][1])
sns.boxplot(data=death,y="사망자수",x="발생지_시도",orient="v",ax=axes[1][0])
sns.boxplot(data=death,y="사망자수",x="기상상태",orient="v",ax=axes[1][1])
sns.boxplot(data=death,y="사망자수",x="노면상태",orient="v",ax=axes[2][0])
sns.boxplot(data=death,y="사망자수",x="도로종류",orient="v",ax=axes[2][1])


# In[82]:


## Correlation Analysis
## 해당 death 자료에는.. numerical 한 데이터가 거의 없기 때문에 변수 분석이 쉽지 않다. 
CorrMatt = death[["주야","요일","발생지_시도","기상상태","노면상태","도로종류","사망자수"]].corr()
mask = np.array(CorrMatt)
mask[np.tril_indices_from(mask)] = False
#fig,ax= plt.subplots()
#fig.set_size_inches(20,10)
#sns.heatmap(CorrMatt, mask=mask,vmax=.8, square=True,annot=True) 


# In[84]:


death["사망자수"].dtype.astype()


# In[80]:


from scipy import stats
fig,axes = plt.subplots(ncols=2,nrows=2)
fig.set_size_inches(12, 10)

sns.distplot(out_death,ax=axes[0][0])
stats.probplot(death["사망자수"], dist='norm', fit=True, plot=axes[0][1])
sns.distplot(np.log(death["사망자수"]),ax=axes[1][0])
stats.probplot(np.log1p(death["사망자수"]), dist='norm', fit=True, plot=axes[1][1])


# In[32]:


plt.bar(de3["기상상태"],de3["사망자수"],color="blue")
plt.show()


# In[62]:


sns.boxplot(x="기상상태", y="사망자수",
            palette=["m", "g"],
            data=de3)


# In[27]:


#tips = sns.load_dataset("tips")
sns.barplot(x="기상상태", y="사망자수",data=de3)


# In[28]:


plt.bar(de4["노면상태"],de4["사망자수"],color="blue")
plt.show()


# In[29]:


plt.bar(de5["도로종류"],de5["사망자수"],color="blue")
plt.show()


# In[30]:


plt.bar(de6["도로형태"],de6["사망자수"],color="blue")
plt.show()


# In[31]:


plt.bar(de7["도로선형"],de7["사망자수"],color="blue")
plt.show()


# In[33]:


de7


# In[ ]:




