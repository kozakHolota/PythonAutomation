'''
Created on 13 січ. 2016

@author: chmel
'''
from engine.BaseWebPage import BaseWebPage

class ApartDetails(BaseWebPage):
    '''
    classdocs
    '''


    def __init__(self, webdriver):
        '''
        Constructor
        '''
        super().__init__(webdriver)
    
    def get_apartment_details(self):
        apart_dict = {"apartment type": [], "price": [], "cases": [],"booking": [] }
        for apart_type in self.webdriver.find_elements_by_xpath('//tr[@id="price_highlight_space"]/td'):
            apart_dict["apartment type"].append(apart_type)
        
        return apart_dict
        