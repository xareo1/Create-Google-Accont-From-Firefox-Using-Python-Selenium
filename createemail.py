from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import openpyxl

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to the Gmail sign up page
driver.get("https://accounts.google.com/signup")

# Fill in the form to create a new account
driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("John")
driver.find_element(By.XPATH, '//*[@id="lastName"]').send_keys("Doe")
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("johndoe123")
driver.find_element(By.XPATH, '//*[@id="passwd"]/div[1]/div/div[1]/input').send_keys("password123")
driver.find_element(By.XPATH, '//*[@id="confirm-passwd"]/div[1]/div/div[1]/input').send_keys("password123")

# Click the "Next" button
driver.find_element(By.XPATH, '//*[@id="accountDetailsNext"]').click()

# Wait for the verification page to load
time.sleep(5)

# Fill in the verification form
driver.find_element(By.XPATH, '//*[@id="phoneNumberId"]').send_keys("5551234567")

# Click the "Next" button
driver.find_element(By.XPATH, '//*[@id="view_container"]/form/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div/content/span').click()

# Wait for the account creation to complete
time.sleep(10)

# Get the newly created email address
email = driver.find_element(By.XPATH, '//*[@id="headingText"]/span').text

# Close the browser
driver.quit()

# Open the Excel file and write the email address and password to it
workbook = openpyxl.load_workbook('accounts.xlsx')
sheet = workbook.active
sheet.append(["Email", "Password"])
sheet.append([email, "password123"])
workbook.save('accounts.xlsx')

print("Account created successfully: " + email)
