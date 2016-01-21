'''
Created on 21 січ. 2016

@author: chmel
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class BaseWebPage(object):
    '''
    classdocs
    '''
    
    webdriver = None


    def __init__(self, webdriver):
        '''
        Constructor
        '''
        
        self.webdriver = webdriver
    
    #Methods to deal with Web elements
    
    def click(self, web_element):
        '''
        Click Element
        '''
        web_element.click()
        return self
    
    def enter_text(self, text, web_element):
        '''
        Enter text into element
        '''
        web_element.send_keys(text)
        return self
    
    def wait_for(self, xpath, timeout=30):
        '''
        Wait until element set by "xpath" is shown under timeout "timeout"
        '''
        WebDriverWait(self.webdriver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return self
    
    def select_value_from_dropdown_menu(self, value, web_element, error_message='Incorrect value'):
        '''
        Select from dropdown menu located by xpath "xpath" element with value "value".
        '''
        
        select = Select(web_element)
        try:
            select.select_by_value('%s' %value)
        except:
            raise ValueError(error_message)
        
        return self
        