#importing the required libraries
import selenium
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

#Opening the browser
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")
time.sleep(2)

#Entering the username and password
username = driver.find_element(By.NAME, "kushagrakk2008@outlook.com")
username.send_keys("username")
password = driver.find_element(By.NAME, "Sudhir1!Shalini")
password.send_keys("password")

#Clicking the login button
login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
login.click()
time.sleep(2)

#Clicking the not now button
not_now = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
not_now.click()
time.sleep(2)

#Clicking the not now button
not_now = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]')
not_now.click()

#Open the real tab

