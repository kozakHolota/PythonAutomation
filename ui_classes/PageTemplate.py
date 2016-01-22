'''
Created on 10 січ. 2016

@author: chmel
'''

from selenium import webdriver
from engine.WebDriverHelper import WebDriverHelper
from engine.BaseWebPage import BaseWebPage
from ui_classes.ApartSearch import ApartSearch


class PageTemplate(BaseWebPage):
    '''
    classdocs
    '''
    browser_val = None


    def __init__(self, browser_val, booking_url):
        '''
        Constructor
        '''
        driver = None
        if isinstance(browser_val, str):
            driver = WebDriverHelper.return_webdriver(browser_val)
            super().__init__(driver)
            self.browser_val = browser_val
            self.webdriver.maximize_window()
        else:
            super().__init__(browser_val)
        
        if booking_url:
            self.webdriver.get(booking_url)
    
    def go_to_search_apartaments(self):
        self.webdriver.find_element_by_xpath("//*[@id='frm']")
        return ApartSearch(self.webdriver)
    