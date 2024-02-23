#importing the required libraries
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

#Opening the browser
driver = webdriver.Chrome()
action = ActionChains(driver)
driver.get("https://www.instagram.com/")
time.sleep(2)

#Logging in
email = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
email.send_keys("kushagrakk2008@outlook.com")
password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys("Sudhir1!Shalini")
loginbutton= driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
loginbutton.click()
time.sleep(5)

#Removing the notification
driver.back()
time.sleep(2)
Notification = driver.find_element(By.XPATH, "//*[text()='Not Now']")
Notification.click()
time.sleep(2)

#Clicking on the reels
reel = driver.find_element(By.XPATH, '//*[@aria-label="Reels"]')
reel.click()
time.sleep(2)


#creating a loop to keep scrolling and keep sharing the reels
while True:
    # Perform the action
    time.sleep(5)
    send_real = driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="Direct"].x1lliihq.x1n2onr6.xyb1xck')
    send_real.click()

    action.send_keys(Keys.DOWN).perform()

    # Wait for 5 seconds
    time.sleep(20)




time.sleep(10000)

