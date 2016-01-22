'''
Created on 10 січ. 2016

@author: chmel
'''
from ui_classes.PageTemplate import PageTemplate
from ui_classes.LogIn import LogIn
from selenium import webdriver

class FirstPage(PageTemplate):
    '''
    classdocs
    '''


    def __init__(self, browser_val, booking_url):
        '''
        Constructor
        '''
        super().__init__(browser_val, booking_url)
    
    @property
    def register_button(self):
        return self.webdriver.find_element_by_xpath('.//*[@id="current_account"][1]/a')
    
    @property
    def login_button(self):
        return self.webdriver.find_element_by_xpath('.//*[@id="current_account"][2]/a')
    
    def login(self):
        self.click(self.login_button)
        return LogIn(self.webdriver)
        