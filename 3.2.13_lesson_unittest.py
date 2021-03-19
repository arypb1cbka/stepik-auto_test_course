import unittest

class test_unit(unittest.TestCase):
    def test_reg_1(self):
        from selenium import webdriver
        import time
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector(
            """[class="first_block"] [class="form-group first_class"] input""")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(
            """[class="first_block"] [class="form-group second_class"] input""")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(
            """[class="first_block"] [class="form-group third_class"] input""")
        input3.send_keys("petrovivan@yahoo.com")
        button = browser.find_element_by_css_selector("""[type="submit"]""")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Wrong")

    def test_reg2(self):
        from selenium import webdriver
        import time
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector("""[class="first_block"] [class="form-group first_class"] input""")
        input1.send_keys("Ivan")
        input3 = browser.find_element_by_css_selector("""[class="first_block"] [class="form-group third_class"] input""")
        input3.send_keys("petrovivan@yahoo.com")
        button = browser.find_element_by_css_selector("""[type="submit"]""")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Wrong")

if __name__=="__main__":
    unittest.main()