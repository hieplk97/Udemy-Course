from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('http://quotes.toscrape.com/')

while True:
    for div in driver.find_elements_by_css_selector('.quote'):
        print(div.find_element_by_css_selector('.text').text)
        print(div.find_element_by_css_selector('.author').text)
        for tag in div.find_elements_by_css_selector('.tag'):
            print(tag.text)
        print('---------')
    try:
        driver.find_element_by_css_selector('.next a').click()
    except:
        print('End')
        break
driver.quit()
