from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
#chrome_options.add_argument('--headless')  # You need to add the argument --headless to invoke Chrome in headless mode
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument('--disable-gpu')


driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
#open window max size
driver.maximize_window()

# open browser
driver.get("https://www.quora.com/")

# find email input by selector
email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "form.inline_login_form input[name=email]")))

# find password input by selector
password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "form.inline_login_form input[name=password]")))

# set value to email input
email.send_keys('mygmail@gmail.com')

# set value to password input
password.send_keys('123456')

#find submit button
button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "form.inline_login_form input[name=submit]")))


#click submit button
button.click()

#close browser
driver.close()
