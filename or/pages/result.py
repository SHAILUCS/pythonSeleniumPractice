from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/home/shailu/eclipse-workspace/SeleniumPractice/driverBinary/chromedriver")

driver.maximize_window()

driver.get("https://www.google.com")

driver.find_element_by_name("q").send_keys("Selenium",Keys.ENTER)

print(driver.title)

driver.quit()