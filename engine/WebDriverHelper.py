'''
Created on 11 січ. 2016

@author: chmel
'''
from selenium import webdriver

class WebDriverHelper(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    @staticmethod
    def return_webdriver(browser_val):
        if browser_val == 'Chrome':
                return webdriver.Chrome()
        elif browser_val == 'Firefox':
                return webdriver.Firefox()
        elif browser_val == 'Ie':
                return webdriver.Ie()
        else:
                raise ValueError('Incorrect browser is choosen')