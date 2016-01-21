'''
Created on 12 січ. 2016

@author: chmel
'''
from engine.BaseWebPage import BaseWebPage

class PanelOfInstruments(BaseWebPage):
    '''
    classdocs
    '''
    webdriver = None

    def __init__(self, webdriver):
        '''
        Constructor
        '''
        self.webdriver = webdriver
        super().__init__(self.webdriver)
        