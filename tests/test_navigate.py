import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait

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
    expectedResult = 'file:///Users/GDC02/Documents/Automated%20Tester%20Reskill%20Bootcamp%202021/week%203/testing/testcafe-quicklab-practice/src/practice_page.html'

    assert home_location == expectedResult

def find(driver):
    qa = driver.find_element_by_id("qa")
    if qa:
        return qa
    else:
        return False

def test_navigate():

    driver.get('file:///Users/GDC02/Documents/Automated%20Tester%20Reskill%20Bootcamp%202021/week%203/testing/testcafe-quicklab-practice/src/practice_page.html')

    bbc = driver.find_element_by_id("bbc")
    qa = driver.find_element_by_id("qa")

    bbc_expected_url = bbc.get_attribute('href')
    qa_expected_url = qa.get_attribute('href')
    
    bbc.click()

    current_page = driver.current_url

    assert current_page == bbc_expected_url

    driver.get('file:///Users/GDC02/Documents/Automated%20Tester%20Reskill%20Bootcamp%202021/week%203/testing/testcafe-quicklab-practice/src/practice_page.html')
    
    qa = WebDriverWait(driver, 1).until(find)

    qa.click()

    current_page = driver.current_url
    
    assert current_page == qa_expected_url







    





