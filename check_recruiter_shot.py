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
    # Login via direct fetch in browser to store token
    driver.get("https://digital-skill-passport.vercel.app/login")
    time.sleep(2)
    driver.execute_script("localStorage.clear(); sessionStorage.clear();")
    
    # Enter recruiter credentials
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys("recruiter@google.com")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("recruiter123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(4)

    # Directly check URL or navigate
    if "recruiter" not in driver.current_url:
        driver.get("https://digital-skill-passport.vercel.app/recruiter/dashboard")
        time.sleep(4)
        
    print("Recruiter URL:", driver.current_url)
    driver.save_screenshot("project_screenshots/07_recruiter_discovery.png")
    print("Saved 07_recruiter_discovery.png successfully!")
finally:
    driver.quit()
