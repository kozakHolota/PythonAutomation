'''
Created on 12 січ. 2016

@author: chmel
'''
from engine.BaseWebPage import BaseWebPage
from ui_classes.ApartDetails import ApartDetails

class ApartSearchResultPage(BaseWebPage):
    '''
    classdocs
    '''
    
    webdriver = None
    current_block = None


    def __init__(self, webdriver):
        '''
        Constructor
        '''
        self.webdriver = webdriver
        super().__init__(self.webdriver)
        self.get_countries_block()
    
    def get_countries_block(self):
        self.current_block = "//*[@id='disambBlock_country']"
        return self
    
    def get_regions_block(self):
        self.current_block = "//*[@id='disambBlock_region']"
        return self
    
    def get_cities_block(self):
        self.current_block = "//*[@id='disambBlock_city']"
        return self
    
    def get_hotels_block(self):
        self.current_block = "//*[@id='disambBlock_hotel']"
        return self
    
    def get_landmarks_block(self):
        self.current_block = "//*[@id='disambBlock_landmark']"
        return self
    
    def verify_item(self, item_value):
        try:
            self.webdriver.find_element_by_xpath("%s//a[text()='%s']" %(self.current_block, item_value))
            return True
        except:
            return False
    
    def go_to_hotel(self, hotel_name):
        context_menu = "//*[@id='maxotel_table_header']"
        self.click(self.webdriver.find_element_by_link_text(hotel_name)).wait_for(context_menu, 40)
        return ApartDetails(self.webdriver)
        