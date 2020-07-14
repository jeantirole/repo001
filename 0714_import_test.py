import Module3rd

Module3rd.crawl_words()


result = []

url = "https://www.shilladfs.com/estore/kr/ko/fastshop"

driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)

time.sleep(2)
#############################################################
driver.find_element_by_tag_name('#facetCategoryL_3').click()
driver.find_element_by_tag_name('#facetCategoryS_3_2').click()
#############################################################
for page in range(1,3): #페이지 수 따로 입력하지 않고, end page 까지 적용시키는방법? 
    try:        
        driver.execute_script("javascript:facet.search(%s);"%str(page))
        time.sleep(2)

        shi_01=driver.find_elements_by_css_selector('.facet-product-list .product_off_wrap')

        print("*"*10 + str(page)+"*"*10)      
        for ele in shi_01:    
            brand_name = ele.find_element_by_css_selector('div.brand').text
            #product_name = ele.find_element_by_css_selector('div.name').text
            reg_number = ele.find_element_by_css_selector('div.ref_no').text
            dollar_price = ele.find_element_by_css_selector('div.price > span.sale').text
            won_price = ele.find_element_by_css_selector('div.price > span.won').text

            result.append([brand_name]+[reg_number]+[dollar_price]+[won_price])
    except Exception as e:
        print("오류", e)                                                 
print("*"*2) 
print(result)