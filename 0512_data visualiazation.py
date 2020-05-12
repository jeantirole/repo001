#!/usr/bin/env python
# coding: utf-8

# In[3]:


## data loading 
## exploting 
## visualization 


# In[4]:


import pandas as pd


# In[19]:


import pandas as pd
data_train = pd.read_csv('E:\\Eric_Github\\repo001\\train.csv')
data_test = pd.read_csv('E:\\Eric_Github\\repo001\\test.csv')


# In[21]:


print(data_train.shape)
print(data_test.shape)


# In[22]:


print(data_train.columns)
print(data_test.columns)


# In[39]:


import seaborn as sns 
import matplotlib as plt 


# In[28]:


sns.distplot(data_train["count"])


# In[30]:


sns.boxplot(x='season',y='count',data=data_train)


# In[51]:


plt.pyplot.figure(figsize=(10, 2))

sns.boxplot(x='weather',y='count',data=data_train)


# In[55]:


plt.pyplot.figure(figsize=(19, 15))
plt.pyplot.subplot(2,2,1)
sns.boxplot(x='season',y='count',hue='holiday',data=data_train)
plt.pyplot.subplot(2,2,2)
sns.boxplot(x='weather',y='count',data=data_train)
plt.pyplot.subplot(2,2,3)
sns.boxplot(x='workingday',y='count',data=data_train)
plt.pyplot.subplot(2,2,4)
sns.boxplot(x='holiday',y='count',data=data_train)


# In[56]:


plt.pyplot.figure(figsize=(19, 15))
sns.lmplot(x='temp',y='count',data=data_train, hue='holiday')


# In[58]:


tr_sub = data_train.copy()


# In[59]:


tr_sub.loc[tr_sub['season']==1, 'season_str'] = 'spring'
tr_sub.loc[tr_sub['season']==2, 'season_str'] = 'summer'
tr_sub.loc[tr_sub['season']==3, 'season_str'] = 'fall'
tr_sub.loc[tr_sub['season']==4, 'season_str'] = 'winter'


# In[60]:


tr_sub


# In[68]:


#각각의 값들의 개수 

tr_sub['season_str'].value_counts()


# In[70]:


sns.pairplot(tr_sub)


# In[73]:


sel = ['temp','atemp','humidity','windspeed','count','season']
tr_sub = tr_sub[sel]
## tr_sub.loc[:,sel]
sns.pairplot(tr_sub,hue='season')


# In[72]:


tr_sub.columns


# In[77]:


f_names = ['temp','atemp']
x_train = data_train[f_names]     #공부시킬 입력 데이터 
x_test = data_test[f_names]

label_name = 'count'         #렌탈 대수 
y_train = data_train[label_name]  #렌탈 대수 변수 값 선택 


# In[78]:


from sklearn.linear_model import LinearRegression 


# In[79]:


# 모델 선택, 학습, 예측 
model = LinearRegression()
model.fit(x_train, y_train)
pred = model.predict(x_test)


# In[92]:


omr = pd.read_csv('E:\\Eric_Github\\repo001\\sampleSubmission.csv')
omr['count']= pred
omr.to_csv('E:\\Eric_Github\\repo001\\firt_sub.csv',index=False)


# In[93]:


check = pd.read_csv('E:\\Eric_Github\\repo001\\firt_sub.csv')


# In[94]:


check


# In[96]:


myhobby =['swimming','game','soccer','baseketball']
myhobby


# In[98]:


for x in myhobby:
    print(x)


# In[105]:


myhobby =['swimming','game','soccer','baseketball']

first_q = input("what is your hobby?: ")
for x in myhobby:
    if first_q != x:
        print("우리는 다른 취미를 가지고 있다.")


# In[106]:


print("pandas 버전:", pd.__version__)


# In[109]:


for value in score.values: 
    print(values)
    
    


# In[110]:


from pandas import Series


# In[111]:


gildong = Series([1500,3000,2500],
                 index = ['a','b','c'])
toto = Series([3000,3000,2000],
              index = ['a','b','c'])


# In[114]:


for x in gildong: 
    print(x)


# In[116]:


count = 0
for value in gildong.values:
    if value >= 2500:
        count = count +1
        
for balue in toto.values: 
    if value >= 2500:
        count = count +1

print("최종 2500이상의 데이터 개수는:", count)


# In[118]:


gildong.values


# In[119]:


dat = {'col1':[1,2,3,4],
       'col2': [10,20,30,40],
       'col3':['A','B','C','D']}
df = pd.DataFrame(dat)


# In[121]:


df


# In[ ]:


team_df = DataFrame()

