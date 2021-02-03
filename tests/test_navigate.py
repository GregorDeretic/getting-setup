import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

import http.client

driver = object

def setup_module():
    global driver

    driver = webdriver.Chrome('/Users/GDC02/bin/chromedriver')  
    # Optional argument, if not specified will search path.
    #driver = webdriver.Chrome()

def teardown_module():
    driver.close()
    driver.quit()

def test_current_location():
    
    driver.get('file:///Users/GDC02/Documents/Automated%20Tester%20Reskill%20Bootcamp%202021/week%203/testing/testcafe-quicklab-practice/src/practice_page.html')
    home_location = driver.current_url

    assert home_location == 'file:///Users/GDC02/Documents/Automated%20Tester%20Reskill%20Bootcamp%202021/week%203/testing/testcafe-quicklab-practice/src/practice_page.html'

def test_navigate():

    driver.get('file:///Users/GDC02/Documents/Automated%20Tester%20Reskill%20Bootcamp%202021/week%203/testing/testcafe-quicklab-practice/src/practice_page.html')

    bbc = driver.find_element_by_id("bbc")
    qa = driver.find_element_by_id("qa")

    bbc_expected_url = bbc.get_attribute('href')
    qa_expected_url = qa.get_attribute('href')
    
    
    bbc.click()

    current_page_bbc = driver.current_url

    assert current_page_bbc == bbc_expected_url

    driver.set_page_load_timeout(5)
    driver.get('file:///Users/GDC02/Documents/Automated%20Tester%20Reskill%20Bootcamp%202021/week%203/testing/testcafe-quicklab-practice/src/practice_page.html')

    qa.click()

    current_page_qa = driver.current_url

    assert current_page_qa == qa_expected_url







    





