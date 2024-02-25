# importing the required libraries
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



# Taking the user input
user_name = input("Enter the username of the person you want to send the reels to: ")


# Opening the browser
driver = webdriver.Chrome()
action = ActionChains(driver)
driver.get("https://www.instagram.com/")
time.sleep(2)

# Logging in
email = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
email.send_keys("the_game.news")
password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys("sudhir1!shalini")
loginbutton= driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
loginbutton.click()
time.sleep(5)

# Removing the notification
driver.back()
time.sleep(2)
Notification = driver.find_element(By.XPATH, "//*[text()='Not Now']")
Notification.click()
time.sleep(2)

# Clicking on the reels
reel = driver.find_element(By.XPATH, '//*[@aria-label="Reels"]')
reel.click()
time.sleep(5)


# creating a loop to keep scrolling and keep sharing the reels


while True:
    try:
        # Your actions to send reels

        # Wait for the direct message modal to appear
        direct_modal = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'svg[aria-label="Direct"].x1lliihq.x1n2onr6.xyb1xck')))
        direct_modal.click()

        # Find the user to send the reel
        person = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f'//span[contains(text(), "{user_name}")]')))
        person.click()

        # Click the send button
        send_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Send']")))
        send_button.click()

        print("Reel sent successfully.")

        time.sleep(1)

        # Add a short delay before the next iteration


    except Exception as e:
        print(f"Error: {str(e)}")
        # Handle error as needed

    # Add a break condition if needed to exit the loop under certain conditions

















