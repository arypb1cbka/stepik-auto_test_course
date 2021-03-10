from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    browser.find_element_by_tag_name("button").click()
    browser.switch_to.alert.accept()
    value=browser.find_element_by_id("input_value").text
    browser.find_element_by_id("answer").send_keys(calc(value))
    browser.find_element_by_css_selector("[type='submit']").click()
finally:
    time.sleep(10)
    browser.quit()
