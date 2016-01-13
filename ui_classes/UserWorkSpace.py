'''
Created on 11 січ. 2016

@author: chmel
'''
from ui_classes.PageTemplate import PageTemplate
from selenium import webdriver

class UserWorkSpace(PageTemplate):
    '''
    classdocs
    '''


    def __init__(self, browser_val, booking_url):
        '''
        Constructor
        '''
        super().__init__(browser_val, booking_url)
    
    
    def get_user_firstname(self):
        return self.webdriver.find_element_by_xpath('//span[@class="header_name user_firstname"]')
    
    def get_user_surname(self):
        return self.webdriver.find_element_by_xpath('//span[@class="header_name user_lastname"]')
        