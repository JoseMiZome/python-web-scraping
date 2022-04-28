# Add Geckodriver to PATH
# Linux /usr/local/bin
from selenium import webdriver
import datetime
import os
from pathlib import Path
from pushbullet import Pushbullet
from selenium.webdriver.firefox.options import Options
from io import BytesIO
import time
from PIL import Image
options = Options()
#options.add_argument('--headless')
browser = webdriver.Firefox(options=options)
home = str(Path.home())
Directorio = os.path.dirname(home)
URL = "https://www.skyscanner.com/transport/flights/bcn/nrt/190504/190524/?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&ref=home"
browser.get(URL)
pb = Pushbullet("o.EQBAkbhv6TPg8ImEfKjKJMTTmERQwn2P") # Add Pushbullet API 
# Aceptar Cookies
try:
	browser.find_element_by_class_name("CookieBanner_CookieBanner__wrapper__173Hh").click()
	browser.implicitly_wait(3)
	browser.find_element_by_class_name("bpk-button_bpk-button__3RA2Q").click()
except:
	pass # There's no cookies banner

# Filters
browser.implicitly_wait(3)
# Don't allow different company roundtrip
VariasAero = browser.find_element_by_xpath("//li[@data-id='multi']//label").click()
browser.implicitly_wait(3)
# Don't allow 2 scales
Escalas2 = browser.find_element_by_xpath("//li[@data-id='two_plus_stops']//label").click()
browser.execute_script("window.scrollTo(0,525);")
time.sleep(20)

# Cut the entire image of browser to what we want and store it as PNG
png = browser.get_screenshot_as_png()
im = Image.open(BytesIO(png))
# Adjust if results are cut in the image
# It happens when you switch languages on SkyScanner you have to modify the left,top,right,bottom values until it matches the first 3 results
left = 284
top = 36
right = 924
bottom = 740
im = im.crop((left, top, right, bottom))
im.save(home + "//Documents//ImagenSkyScanner.png")

# Send to Pushbullet Phone's App (Channel)
SkyScanner = pb.get_channel('rjyfcerygf3rfh80qyti3q78cujrhhd987325426triyfkjfhndjjkg4264726r7w65r8425yje43545768jfr6tfhg654') # Add SkyScanner Channel TAG
with open(home + "//Documents//ImagenSkyScanner.png", "rb") as pic:
    file_data = pb.upload_file(pic, "ImagenSkyScanner.png")
	
push = pb.push_file(**file_data)
push = pb.push_file(file_url=push["file_url"], file_name=datetime.datetime.now().strftime("%d-%m-%y %H:%Mh"), file_type=push["file_type"], channel=SkyScanner)
browser.close()
browser.quit()
raise SystemExit
