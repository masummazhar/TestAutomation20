from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://google.com")
time.sleep(10)
website_title = driver.title
print(website_title)
website_url = driver.current_url
print(website_url)

driver.close()