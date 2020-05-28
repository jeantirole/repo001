#!/usr/bin/env python
# coding: utf-8

# ### 구글 논문 검색 자동화
#  * 제목
#  * 논문 링크 가져오기
#  * 논문 요약 정보
#  * 저자 및 연도
#  * 인용 횟수 정보 가져오기

# ### 01 라이브러리 불러오기

# In[21]:


from bs4 import BeautifulSoup
from selenium import webdriver

import os
print( os.getcwd() )  # 현재 주피터 노트북 파일이 열린 기본 장소

driver = webdriver.Chrome('./chrome/chromedriver_246')
driver


# In[22]:


url = 'https://scholar.google.co.kr/'
driver.get(url)

# input  : //*[@id="gs_hdr_tsi"]
# button : //*[@id="gs_hdr_tsb"]
inb = '//*[@id="gs_hdr_tsi"]'
btn ='//*[@id="gs_hdr_tsb"]'

input_blank = driver.find_element_by_xpath(inb)
button = driver.find_element_by_xpath(btn)

print(input_blank, button)


# ### 02 논문 검색

# In[23]:


url = 'https://scholar.google.co.kr/'
driver.get(url)

# input  : //*[@id="gs_hdr_tsi"]
# button : //*[@id="gs_hdr_tsb"]
inb = '//*[@id="gs_hdr_tsi"]'
btn ='//*[@id="gs_hdr_tsb"]'

input_blank = driver.find_element_by_xpath(inb)
button = driver.find_element_by_xpath(btn)


# In[24]:


### 검색할 단어 입력
#%% 논문 검색
# keyword = 'text mining'
keyword = 'generative adversarial networks'  # GAN은 kewword의 약자.
input_blank.clear()
input_blank.send_keys(keyword)
button.click()


# In[25]:


import time 

title = []
des = []
title_url = []
ref_cnt = []
author_year = []

time_lay = [2,3,4,5,6,7]
cnt = 0
for i in range(0, 100, 10):
    cnt =  cnt + 1
    url1 = 'https://scholar.google.co.kr/scholar?start='+ str(i) + '&q=' + keyword + '&hl=ko&as_sdt=0,5'
    driver.get(url1)
    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')
    print( soup.title )
    
    all_dat = soup.find('div', id='gs_res_ccl_mid').find_all("div", class_='gs_r gs_or gs_scl')
    for item in all_dat:
        time.sleep(1)
        # 제목
        temp1 = item.find("div", class_='gs_ri').find('a')
        if temp1 is not None:
            tmp_txt = temp1.text
            title.append(tmp_txt)
        else:
            title.append("")
          
        # 요약 정보
        # __________
            
        # 논문 링크 가져오기
        # __________
            
        # 저자 및 연도
        t4 = item.find("div", class_='gs_a')
        if t4 is not None:
            tmp_txt = t4.text
            author_year.append(tmp_txt)
        else:
            author_year.append("")

    # 인용횟수 정보 가져오기
    # //*[@id="gs_res_ccl_mid"]/div[2]/div[2]/div[3]/a[3]
    des_all = driver.find_elements_by_partial_link_text("인용")
    for item in des_all:
        # 링크
        temp1 = item.text
        # print(temp1)
        ref_cnt.append(temp1)

    print(len(title), len(ref_cnt), len(author_year) )
    time.sleep(time_lay[cnt%6])
    
print("정보 수집 완료")


# ### 위에서 가져오지 못한 나머지 부분 이용

# In[27]:


import time 

title = []
des = []
title_url = []
ref_cnt = []
author_year = []

time_lay = [2,3,4,5,6,7]
cnt = 0
for i in range(0, 100, 10):
    cnt =  cnt + 1
    url1 = 'https://scholar.google.co.kr/scholar?start='+ str(i) + '&q=' + keyword + '&hl=ko&as_sdt=0,5'
    driver.get(url1)
    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')
    print( soup.title )
    
    all_dat = soup.find('div', id='gs_res_ccl_mid').find_all("div", class_='gs_r gs_or gs_scl')
    for item in all_dat:
        # 제목
        temp1 = item.find("div", class_='gs_ri').find('a')
        if temp1 is not None:
            tmp_txt = temp1.text
            title.append(tmp_txt)
        else:
            title.append("")
          
        # 요약 정보
        t2 = item.find('div', class_="gs_rs")
        if t2 is not None:
            temp2 = item.find('div', class_="gs_rs").text
            des.append(temp2)
        else:
            des.append("")
            
        # 논문 링크 가져오기
        t3 = item.find("div", class_='gs_ri').find('a')
        if t3 is not None:
            temp3 = item.find("div", class_='gs_ri').find('a')['href']
            title_url.append(temp3)
        else:
            title_url.append("")
            
        # 저자 및 연도
        t4 = item.find("div", class_='gs_a')
        if t4 is not None:
            tmp_txt = t4.text
            author_year.append(tmp_txt)
        else:
            author_year.append("")

    # 인용횟수 정보 가져오기
    # //*[@id="gs_res_ccl_mid"]/div[2]/div[2]/div[3]/a[3]
    des_all = driver.find_elements_by_partial_link_text("인용")
    for item in des_all:
        # 링크
        temp1 = item.text
        # print(temp1)
        ref_cnt.append(temp1)

    print(len(title), len(des), len(title_url), len(ref_cnt), len(author_year) )
    time.sleep(time_lay[cnt%6])
    
print("정보 수집 완료")


# In[28]:


#%% excel 파일로 정리
import pandas as pd

dat = { "title":title, "description":des, "인용횟수":ref_cnt, "논문링크":title_url, "저자및년도":author_year }
excel_dat = pd.DataFrame(dat)

excel_dat.to_csv("data.csv", index=False)
excel_dat.to_excel("data.xlsx", index=False)


# In[29]:


import os


# In[31]:


path = "./"
file_list = os.listdir(path)
print(file_list)


# ### pandas를 이용한 데이터 가져오기

# In[32]:


import pandas as pd
dat = pd.read_csv("data.csv")
dat


# In[37]:


dat['인용횟수'] = dat['인용횟수'].str.replace("회", "")
dat['인용횟수'] = dat['인용횟수'].str.replace("인용", "")
dat


# In[39]:


### 논문의 요약값 확인
print(dat.columns)
print(dat.description)


# ### 언제 쓰여진 논문일까? 연도만 추출

# In[40]:


tmp_year = dat['저자및년도']
tmp_year


# In[41]:


### 숫자만 추출
tmp_year.str.extract( '(\d{4}\s)' )  # 숫자만 추출


# In[42]:


year = tmp_year.str.extract( '(\d{4}\s)' ) # 숫자만 추출
dat['년도'] = year
dat


# ### 년도별 논문 횟수를 시각화 해보기

# In[50]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[51]:


sns.countplot(x='년도', data=dat)
plt.xlabel("year")


# In[52]:


sns.countplot(y='년도', data=dat)
plt.ylabel("year")


# In[53]:


myyear = sns.countplot(y='년도', data=dat)
fig = myyear.get_figure()
fig.savefig("output_gan.png")
plt.ylabel("year")

