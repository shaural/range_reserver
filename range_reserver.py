from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
from selenium.webdriver.support.ui import Select
from datetime import timedelta
from datetime import datetime

# Set env vars from .env file (for password)
load_dotenv('.env')

# Rentcafe credentials
username = os.getenv("RENTCAFE_USERNAME")
password = os.getenv("RENTCAFE_PASSWORD")

# initialize the Chrome driver
driver = webdriver.Chrome("chromedriver")
# head to github login page
driver.get("https://www.rentcafe.com/residentservices/apartmentsforrent/conciergereservations.aspx#tab_MakeAReservation")
# find username/email field and send the username itself to the input field
driver.find_element(By.ID, "Username").send_keys(username)
# find password input field and insert password as well
driver.find_element(By.ID, "Password").send_keys(password)
# click login button
driver.find_element(By.NAME, "SignIn").click()
# wait the ready state to be complete
WebDriverWait(driver, 10).until(
    lambda x: x.find_element(By.ID, "LoggedInAsName")
)
# navigate to reservation page
driver.get("https://www.rentcafe.com/residentservices/apartmentsforrent/conciergereservations.aspx#tab_MakeAReservation")
# wait the ready state to be complete
WebDriverWait(driver, 10).until(
    lambda x: x.find_element(By.ID, "ResourceId")
)
# Select Amenity
Select(driver.find_element(By.ID, "ResourceId")).select_by_visible_text('Capstone Range') # can also select by value = 234
# Set date
next_week = datetime.now() + timedelta(weeks=1)
start_date_element = driver.find_element(By.ID, "StartDate")
start_date_element.clear()
start_date_element.send_keys(next_week.strftime("%m/%d/%Y"))
# Set time
Select(driver.find_element(By.ID, "AmPmStart")).select_by_visible_text('PM') # if this works convert top^
Select(driver.find_element(By.ID, "HoursStart")).select_by_visible_text('7')
# Create Reservation (first submit button)
driver.find_element(By.ID, "btnCreateReservation").click()
# Maybe add verification that cost is 0?
driver.find_element(By.ID, "btnPayNow").click()

# close the driver
driver.close()