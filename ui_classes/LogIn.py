'''
Created on 10 січ. 2016

@author: chmel
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui_classes.UserWorkSpace import UserWorkSpace

class LogIn(object):
    '''
    classdocs
    '''
    webdriver = None


    def __init__(self, webdriver):
        '''
        Constructor
        '''
        self.webdriver = webdriver
    
    def get_username_field(self):
        return self.webdriver.find_element_by_xpath("//*[@name='username']")
    
    def get_password_field(self):
        return self.webdriver.find_element_by_xpath("//*[@name='password']")
    
    def get_send_button(self):
        return self.webdriver.find_element_by_xpath("//form[@target='log_tar']/input[@type='submit']")
    
    def login_as_user(self, username, password):
        self.get_username_field().send_keys(username)
        self.get_password_field().send_keys(password)
        self.get_send_button().click()
        element = WebDriverWait(self.webdriver, 30).until(EC.presence_of_element_located((By.XPATH, "//ul[@class='profile-area__nav']")))
        return UserWorkSpace(self.webdriver, None)

    def login_from_facebook(self):
        pass