import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1600,1050")
options.add_argument("--force-device-scale-factor=1")
driver = webdriver.Chrome(options=options)

try:
    # 1. Clear session and open login
    driver.get("https://digital-skill-passport.vercel.app/login")
    time.sleep(2)
    driver.execute_script("localStorage.clear(); sessionStorage.clear();")
    driver.refresh()
    time.sleep(2)
    
    # 2. Login as Recruiter
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys("recruiter@google.com")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("recruiter123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    
    print("Recruiter logged in, current URL:", driver.current_url)
    driver.get("https://digital-skill-passport.vercel.app/recruiter/dashboard")
    time.sleep(5)
    
    # Take screenshot of actual recruiter dashboard with candidate cards
    driver.save_screenshot("project_screenshots/07_recruiter_discovery.png")
    print("Successfully captured authentic Recruiter Candidate Discovery dashboard!")
finally:
    driver.quit()
