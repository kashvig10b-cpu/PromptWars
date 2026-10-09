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
    # Try logging in as student or registering a clean student account
    driver.get("https://digital-skill-passport.vercel.app/login")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys("kashvi@dsp.edu")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("password123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(4)

    # If login fails, let us register a clean student account
    if "dashboard" not in driver.current_url:
        print("Registering fresh student...")
        driver.get("https://digital-skill-passport.vercel.app/register")
        time.sleep(2)
        # Register form fields
        inputs = driver.find_elements(By.TAG_NAME, "input")
        if len(inputs) >= 3:
            inputs[0].send_keys("Kashvi Garg")
            inputs[1].send_keys(f"kashvi_{int(time.time())}@dsp.edu")
            inputs[2].send_keys("password123")
            # Click submit
            btn = driver.find_element(By.XPATH, "//button[@type='submit']")
            btn.click()
            time.sleep(4)

    print("Current URL:", driver.current_url)
    # Scroll slightly if needed and capture screenshot
    driver.save_screenshot("project_screenshots/08_student_dashboard.png")
    print("Student dashboard captured successfully!")
finally:
    driver.quit()
