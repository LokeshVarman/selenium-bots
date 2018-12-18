# Note: For proper working of this Script Good and Uninterepted Internet Connection is Required
# Keep all contacts unique
# Can save contact with their phone Number

# Import required packages
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



# Driver to open a browser
driver = webdriver.Firefox()

#link to open a site
driver.get("http://results.paavai.edu.in")

# 10 sec wait time to load, if good internet connection is not good then increase the time
# units in seconds
# note this time is being used below also
wait = WebDriverWait(driver, 10)
wait5 = WebDriverWait(driver, 5)


username = driver.find_element_by_id('txtregno')
username.send_keys("16104053' --")
nextButton = driver.find_element_by_id('txtdate')
nextButton.click()

password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'txtdate')))
password.send_keys("hgf")

signInButton = driver.find_element_by_id('btnsubmit')
signInButton.click()

internalmark=driver.find_element_by_id('lnkiar')
internalmark.click()
