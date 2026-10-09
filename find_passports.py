import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1600,1000")
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://digital-skill-passport.vercel.app/login")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys("admin@dsp.gov")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(4)

    # Let's inspect text on admin dashboard or navigate to recruiter
    driver.get("https://digital-skill-passport.vercel.app/recruiter/dashboard")
    time.sleep(4)
    elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/passport/')]")
    for el in elements:
        print("Found passport link:", el.get_attribute("href"))
finally:
    driver.quit()
