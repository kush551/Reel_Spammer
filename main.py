# importing the required libraries
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Taking the user input
user_name = input("Enter the username of the person you want to send the reels to: ")
Email_Input = input("Enter your Instagram email or username: ")
Password_Input = input("Enter your Instagram password: ")

# Locating path of the website
Email_Path = "//*[@id='loginForm']/div/div[1]/div/label/input"
Password_Path = "//*[@id='loginForm']/div/div[2]/div/label/input"
Login_Button_Path = "//*[@id='loginForm']/div/div[3]"
Not_Now_Path = "//*[text()='Not Now']"
Reels_Path = "//*[@aria-label='Reels']"
Direct_Message_Path = "svg[aria-label='Direct'].x1lliihq.x1n2onr6.xyb1xck"
Send_Button_Path = "//*[text()='Send']"
User_Path = "//span[contains(text()"

# Opening the browser
driver = webdriver.Chrome()
action = ActionChains(driver)
driver.get("https://www.instagram.com/")
time.sleep(2)

# Logging in
email = driver.find_element(By.XPATH, f'{Email_Path}')
email.send_keys(Email_Input)
password = driver.find_element(By.XPATH, f'{Password_Path}')
password.send_keys(Password_Input)
login_button = driver.find_element(By.XPATH, f'{Login_Button_Path}')
login_button.click()
time.sleep(2)

# Removing the notification
driver.back()
time.sleep(2)
Not_Now = driver.find_element(By.XPATH, f"{Not_Now_Path}")
Not_Now.click()
time.sleep(2)

# Clicking on the reels
reel = driver.find_element(By.XPATH, f'{Reels_Path}')
reel.click()
time.sleep(5)


# creating a loop to keep scrolling and keep sharing the reels
while True:
    try:
        # Your actions to send reels

        # Wait for the direct message modal to appear
        direct_modal = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f'{Direct_Message_Path}')))
        direct_modal.click()

        # Find the user to send the reel
        person = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//span[contains(text(), "{user_name}")]')))
        person.click()

        # Click the send button
        send_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"{Send_Button_Path}")))
        send_button.click()

        print("Reel sent successfully.")

        time.sleep(1)

        # Add a short delay before the next iteration


    except Exception as e:
        print(f"Error: {str(e)}")
        # Handle error as needed

    # Add a break condition if needed to exit the loop under certain conditions

















