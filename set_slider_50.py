import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1600,1050")
options.add_argument("--force-device-scale-factor=1")
driver = webdriver.Chrome(options=options)

try:
    with open("recruiter_creds.json") as f:
        creds = json.load(f)

    driver.get("https://digital-skill-passport.vercel.app/login")
    time.sleep(2)
    driver.execute_script("localStorage.clear(); sessionStorage.clear();")
    driver.refresh()
    time.sleep(2)

    # Login as recruiter
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys(creds["email"])
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(creds["password"])
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(4)

    driver.get("https://digital-skill-passport.vercel.app/recruiter/dashboard")
    time.sleep(3)

    # Find the range input (Min Completion slider) and set its value to 50
    driver.execute_script("""
        const slider = document.querySelector("input[type='range']");
        if (slider) {
            slider.value = 50;
            slider.dispatchEvent(new Event('input', { bubbles: true }));
            slider.dispatchEvent(new Event('change', { bubbles: true }));
        }
    """)
    time.sleep(3)

    driver.save_screenshot("project_screenshots/07_recruiter_discovery.png")
    print("Successfully captured recruiter discovery with Min Completion at 50%!")
finally:
    driver.quit()
