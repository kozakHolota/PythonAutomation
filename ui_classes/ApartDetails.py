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
        for apart_type in self.webdriver.find_elements_by_xpath('//td[@class="roomType room-type-container rt__room-detail"]'):
            apart_dict["apartment type"].append(apart_type.text)
        
        return apart_dict
        