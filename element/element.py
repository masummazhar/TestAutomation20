from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")

driver.implicitly_wait(20)

username = driver.find_element(By.NAME, "email")
password = driver.find_element(By.NAME, "password")
login_btn = driver.find_element(By.CSS_SELECTOR, "[action] .btn-primary")

username.send_keys("Admin")
password.send_keys('admin123')
login_btn.click()