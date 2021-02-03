import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome('/Users/GDC02/bin/chromedriver')  
# Optional argument, if not specified will search path.
#driver = webdriver.Chrome()
driver.get('file:///Users/GDC02/Documents/Automated Tester Reskill Bootcamp 2021/week 3/testing/getting-setup/simple_page.html')
input_field = driver.find_element_by_id("message")
input_field.send_keys("help me!")
submitBtn = driver.find_element_by_id("submit-button")
time.sleep(2) # Let the user actually see something!

submitBtn.click()
time.sleep(3)

alert = Alert(driver)
alert.accept()
time.sleep(3)

driver.get('http://www.google.com/')
time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!

driver.quit()