from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

browser = webdriver.Chrome()
browser.get("https://my.clippings.io/#/login")
browser.implicitly_wait(5)

#username = credentials.GOODREADS_USERNAME
#password = credentials.GOODREADS_PASSWORD

username_input = browser.find_element_by_id("username")
password_input = browser.find_element_by_id("password")

username_input.send_keys("username")
password_input.send_keys("password")

#import_button = browser.find_element_by_id("")

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(2)
browser.close()