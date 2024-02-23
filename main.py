#importing the required libraries
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

# Create an ActionChains object


#Opening the browser
driver = webdriver.Chrome()
action = ActionChains(driver)
driver.get("https://www.instagram.com/")
time.sleep(2)
email = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
email.send_keys("kushagrakk2008@outlook.com")
password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys("Sudhir1!Shalini")
loginbutton = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
loginbutton.click()
time.sleep(5)
driver.back()
time.sleep(5)

Notification= driver.find_element(By.XPATH, "//*[text()='Not Now']")
Notification.click()

time.sleep(2)
reel = driver.find_element(By.XPATH, '//*[@aria-label="Reels"]')
reel.click()
time.sleep(2)

while True:
    # Perform the action
    time.sleep(5)
    send_real = driver.find_element(By.XPATH,'//*[@id="mount_0_0_UE"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div[3]/div/div/svg/polygon')
    send_real.click()

    action.send_keys(Keys.DOWN).perform()

    # Wait for 5 seconds
    time.sleep(20)




time.sleep(10000)

