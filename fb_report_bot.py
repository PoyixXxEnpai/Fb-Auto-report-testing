from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Configure Chrome options for headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

# Load Facebook login page
driver.get("https://www.facebook.com/")

# Fetch email and password from environment variables
email = os.getenv('FB_EMAIL', 'your_facebook_email')
password = os.getenv('FB_PASSWORD', 'your_facebook_password')

try:
    # Log in to Facebook
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
    wait.until(EC.presence_of_element_located((By.ID, "pass"))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.NAME, "login"))).click()
    time.sleep(4)  # Wait for the page to load

    # Go to the profile page you want to report
    profile_url = 'https://www.facebook.com/profile.php?id=100089108025261'  # replace with target profile URL
    driver.get(profile_url)
    time.sleep(4)  # Wait for profile page to load

    # Click on the three dots for additional actions
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Actions for this Page"]/div'))).click()
    time.sleep(3)

    # Click on "Find Support or Report Profile"
    wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Find support or report profile"]'))).click()
    time.sleep(3)

    # Select "Fake Account" as the reason for the report
    wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Fake Account"]'))).click()
    time.sleep(3)

    # Submit the report
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Submit"]'))).click()
    time.sleep(3)

    # Proceed to the next step
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Next"]'))).click()
    time.sleep(3)

    # Confirm that the report is complete
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Done"]'))).click()
    print("Report submitted successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
￼Enter
