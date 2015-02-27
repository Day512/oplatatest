from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.oplata.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled(self):
        driver = self.driver
        # open | / |
        driver.get(self.base_url + "/")
        # click | link=Подключиться |
        driver.find_element_by_link_text(u"Подключиться").click()
        # type | id=signup_email | test@gmail.com
        driver.find_element_by_id("signup_email").clear()
        driver.find_element_by_id("signup_email").send_keys("test@gmail.com")
        # type | id=merchant_url | test.com
        driver.find_element_by_id("merchant_url").clear()
        driver.find_element_by_id("merchant_url").send_keys("test.com")
        # type | id=merchant_refund_number | 0000000000000000
        driver.find_element_by_id("merchant_refund_number").clear()
        driver.find_element_by_id("merchant_refund_number").send_keys("0000000000000000")
        # type | id=merchant_mfo | 000000
        driver.find_element_by_id("merchant_mfo").clear()
        driver.find_element_by_id("merchant_mfo").send_keys("000000")
        # type | id=merchant_okpo | 000000000000
        driver.find_element_by_id("merchant_okpo").clear()
        driver.find_element_by_id("merchant_okpo").send_keys("000000000000")
        # type | id=merchant_off_name | Testmain
        driver.find_element_by_id("merchant_off_name").clear()
        driver.find_element_by_id("merchant_off_name").send_keys("Testmain")
        # click | id=merchant_submit |
        driver.find_element_by_id("merchant_submit").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
