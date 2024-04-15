import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login():
    driver = webdriver.Edge()  # Use the browser driver of your choice
    driver.get('https://gateway.iitk.ac.in:1003/login?')

    try:
        username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
        password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))

        username_field.send_keys('usrnm')  # Replace with your username
        password_field.send_keys('pwd')  # Replace with your password

        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.primary')))
        submit_button.click()

        time.sleep(10)  # Wait for 5 seconds before closing
    finally:
        driver.quit()

while True:
    login()
    time.sleep(2000)  # Wait for 2000 seconds before logging in again
