'''
Created on 10 січ. 2016

@author: chmel
'''
import unittest
from selenium import webdriver
from ui_classes.FirstPage import FirstPage


class TestSetupTeardown(unittest.TestCase):
    booking_base_page = None
    booking_user = None
    booking_password = None
    
    def setup_env(setup):
        def setup_wrap(self):
            import configparser
            conf_reader = configparser.ConfigParser()
            conf_reader.read('../etc/config.ini')
            browser_val = conf_reader['Selenium']['browser']
            booking_url = conf_reader['Booking.com']['url']
            self.booking_user = conf_reader['Booking.com']['login']
            self.booking_password = conf_reader['Booking.com']['password']
            
            self.booking_base_page = FirstPage(browser_val, booking_url)
            try:
                res = setup(self)
            except Exception as e:
                self.booking_base_page.webdriver.close()
                raise ValueError("Test failed\n. Exception: %s" %str(e))
            return res
        return setup_wrap
    
    def teardown_env(teardown):
        def teardown_wrap(self):
            try:
                res = teardown(self)
            except Exception as e:
                self.booking_base_page.webdriver.close()
                raise ValueError("Test failed\n. Exception: %s" %str(e))
            self.booking_base_page.webdriver.close()
            return res
        return teardown_wrap
    
    def ui_test(test):
        def ui_test_wrapper(self):
            try:
                res = test(self)
                return res
            except Exception as e:
                #self.booking_base_page.webdriver.close()
                raise ValueError("Test failed\n. Exception: %s" %str(e))
        return ui_test_wrapper


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()