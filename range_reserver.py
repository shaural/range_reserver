from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
load_dotenv('.env')

# Rentcafe credentials
username = "shaural@live.com"
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
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
# navigate to reservation page
driver.get("https://www.rentcafe.com/residentservices/apartmentsforrent/conciergereservations.aspx#tab_MakeAReservation")
# Select Amenity
# driver.find_element(By.ID("ResourceID")).click()

# close the driver
driver.close()