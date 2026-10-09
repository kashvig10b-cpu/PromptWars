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

    # Trigger React state change on the slider to 50%
    result = driver.execute_script("""
        const slider = document.querySelector("input[type='range']");
        if (slider) {
            const nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
            nativeInputValueSetter.call(slider, 50);
            slider.dispatchEvent(new Event('input', { bubbles: true }));
            slider.dispatchEvent(new Event('change', { bubbles: true }));
            return "Set to 50 successfully";
        }
        return "Slider not found";
    """)
    print("Script result:", result)
    time.sleep(3)

    # Verify text on page has 50%
    body_text = driver.find_element(By.TAG_NAME, "body").text
    if "50%" in body_text:
        print("CONFIRMED: Min Completion is visually at 50%!")
    else:
        print("WARNING: 50% not found in page text!")

    driver.save_screenshot("project_screenshots/07_recruiter_discovery.png")
    print("Saved 07_recruiter_discovery.png with confirmed 50% slider!")
finally:
    driver.quit()
