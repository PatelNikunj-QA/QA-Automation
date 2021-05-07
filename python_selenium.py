
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
driver.get("http://localhost:8080/webapp/")
assert driver.find_element_by_css_selector('h1').text == "Kruti & Shiven Patel Learning Academy"
# assert driver.find_element_by_tag_name('h1').text == "Kruti & Shiven Patel Learning Academy"
assert driver.current_url == "http://localhost:8080/webapp/"
driver.quit()

