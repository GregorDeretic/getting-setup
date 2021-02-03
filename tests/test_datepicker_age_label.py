import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

driver = object

def setup_module():
    global driver

    driver = webdriver.Chrome('/Users/GDC02/bin/chromedriver')  
    # Optional argument, if not specified will search path.
    #driver = webdriver.Chrome()

def teardown_module():
    driver.close()
    driver.quit()

def test_label_empty_on_page_load():
    
    driver.get('file:///Users/GDC02/Documents/Automated Tester Reskill Bootcamp 2021/week 3/testing/getting-setup/practice_page.html')
    age_label = driver.find_element_by_id("age")
    date_picker = driver.find_element_by_id("birthday")
    date_picker.send_keys("04-07-1984")


    assert age_label.get_attribute("innerText") == "36"