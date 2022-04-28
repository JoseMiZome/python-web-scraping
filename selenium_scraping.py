# Libraries

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import pandas as pd

#Navigation options
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\josem\\Downloads\\chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options=options)

# Initialize on second screen
driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)

# Initialize the navigator
driver.get('https://eltiempo.es')