'''
Created on 10 січ. 2016

@author: chmel
'''
from engine.BaseWebPage import BaseWebPage
from ui_classes.UserWorkSpace import UserWorkSpace

class LogIn(BaseWebPage):
    '''
    classdocs
    '''


    def __init__(self, webdriver):
        '''
        Constructor
        '''
        super().__init__(webdriver)
    
    @property
    def username_field(self):
        return self.webdriver.find_element_by_xpath("//*[@name='username']")
    
    @property
    def password_field(self):
        return self.webdriver.find_element_by_xpath("//*[@name='password']")
    
    @property
    def send_button(self):
        return self.webdriver.find_element_by_xpath("//form[@target='log_tar']/input[@type='submit']")
    
    def login_as_user(self, username, password):
        self.enter_text(username, self.username_field).\
        enter_text(password, self.password_field).\
        click(self.send_button).\
        wait_for("//ul[@class='profile-area__nav']")
        return UserWorkSpace(self.webdriver, None)

    def login_from_facebook(self):
        pass