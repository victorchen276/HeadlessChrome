from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chrome_driver = os.getcwd() +"/chromedriver"

# https://www.realestate.co.nz/
driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
driver.get("https://www.realestate.co.nz/")
# lucky_button = driver.find_element_by_css_selector("[name=btnI]")
# lucky_button.click()

# capture the screen
driver.get_screenshot_as_file("capture.png")