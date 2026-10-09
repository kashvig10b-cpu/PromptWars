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
    driver.get("https://digital-skill-passport.vercel.app/register")
    time.sleep(2)
    
    # Fill student registration
    driver.find_element(By.XPATH, "//input[@placeholder='e.g. Alex Johnson']").send_keys("Kashvi Garg")
    rand_email = f"kashvi_{int(time.time())}@dsp.edu"
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys(rand_email)
    
    college_inputs = driver.find_elements(By.XPATH, "//input[contains(@placeholder, 'Stanford') or contains(@placeholder, 'College') or contains(@placeholder, 'University')]")
    if college_inputs:
        college_inputs[0].send_keys("Sapthagiri NPS University")
        
    pw_inputs = driver.find_elements(By.XPATH, "//input[@type='password']")
    if len(pw_inputs) >= 2:
        pw_inputs[0].send_keys("password123")
        pw_inputs[1].send_keys("password123")
        
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    
    print("Post-registration URL:", driver.current_url)
    driver.get("https://digital-skill-passport.vercel.app/student/dashboard")
    time.sleep(4)
    
    driver.save_screenshot("project_screenshots/08_student_dashboard.png")
    print("Captured authentic student dashboard screenshot to project_screenshots/08_student_dashboard.png!")
finally:
    driver.quit()
