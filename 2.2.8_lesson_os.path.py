from selenium import webdriver
import os
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    for element in browser.find_elements_by_css_selector(".form-control"):
        element.send_keys("answer")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "text.txt")
    browser.find_element_by_id("file").send_keys(file_path)
    browser.find_element_by_css_selector("[type='submit']").click()
finally:
    time.sleep(5)
    browser.quit()

