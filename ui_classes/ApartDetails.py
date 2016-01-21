'''
Created on 13 січ. 2016

@author: chmel
'''
from selenium import webdriver

class ApartDetails(object):
    '''
    classdocs
    '''
    
    webdriver = None


    def __init__(self, webdriver):
        '''
        Constructor
        '''
        self.webdriver = webdriver
    
    def get_apartment_details(self):
        apart_dict = {"apartment type": [], "price": [], "cases": [],"booking": [] }
        for apart_type in self.webdriver.find_elements_by_xpath('//tr[@id="price_highlight_space"]/td'):
            apart_dict["apartment type"].append(apart_type)
        
        return apart_dict
        