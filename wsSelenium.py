# from selenium import webdriver

# PATH = 'C:\Program Files (x86)\chromedriver.exe'
# driver = webdriver.Chrome(PATH)

# driver.get("https://www.google.com/")


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By # need this in newer version of selenium to access the name, id , etc attributes

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
# chrome_options.add_experimental_option("detach", True) # for not letting the browser quit on its own
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # put options = chrome_options as second para
driver.get("https://techwithtim.net")
print(driver.title)
search = driver.find_element(By.NAME, "s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

time.sleep(7)
driver.quit()

