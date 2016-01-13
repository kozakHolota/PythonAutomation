'''
Created on 10 січ. 2016

@author: chmel
'''

from selenium import webdriver
from engine.WebDriverHelper import WebDriverHelper
from ui_classes.ApartSearch import ApartSearch

class PageTemplate(object):
    '''
    classdocs
    '''
    webdriver = None
    browser_val = None


    def __init__(self, browser_val, booking_url):
        '''
        Constructor
        '''
        if isinstance(browser_val, str):
            self.webdriver = WebDriverHelper.return_webdriver(browser_val)
            self.browser_val = browser_val
            self.webdriver.maximize_window()
        else:
            self.webdriver = browser_val
        
        
        if booking_url:
            self.webdriver.get(booking_url)
    
    def go_to_search_apartaments(self):
        self.webdriver.find_element_by_xpath("//*[@id='frm']")
        return ApartSearch(self.webdriver)