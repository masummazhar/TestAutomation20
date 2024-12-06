from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.select import  Select
driver = webdriver.Firefox()
driver.get("https://muntasir101.github.io/Conference-Room-Booking/")
driver.implicitly_wait(20)
Select_room = driver.find_element((By.CSS_SELECTOR, "select#room"))
room_type = Select(Select_room)
room_type.select_by_value("Small Room")