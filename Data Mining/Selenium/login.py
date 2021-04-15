import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('http://quotes.toscrape.com/')

driver.find_element_by_css_selector('.header-box p a').click()

username = driver.find_element_by_css_selector('#username')
username.send_keys('user')
time.sleep(3)

password = driver.find_element_by_css_selector('#password')
password.send_keys('password')
time.sleep(3)

driver.find_element_by_css_selector('[value="Login"]').click()

driver.quit()