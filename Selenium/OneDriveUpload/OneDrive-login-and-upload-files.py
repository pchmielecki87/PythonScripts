from time import sleep
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.goodreads.com/")

username = credentials.GOODREADS_USERNAME
password = credentials.GOODREADS_PASSWORD

username_input = browser.find_element_by_xpath(//*[@id="userSignInFormEmail"])
password_input = browser.find_element_by_xpath(//*[@id="user_password"])



username_input.send_keys(username)
username_input.send_keys(password)

login_button = browser.find_element_by_xpath(//*[@id="sign_in"]/div[3]/input[1])0
login_button.click()

sleep(2)
browser.close()