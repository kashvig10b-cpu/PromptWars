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
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys("recruiter@techhire.com")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("recruiter123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(4)

    links = driver.find_elements(By.TAG_NAME, "a")
    for l in links:
        href = l.get_attribute("href")
        if href and "/passport/" in href:
            print("Candidate link:", href)
finally:
    driver.quit()
