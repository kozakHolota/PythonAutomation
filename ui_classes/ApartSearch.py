'''
Created on 12 січ. 2016

@author: chmel
'''
from datetime import date
from engine.BaseWebPage import BaseWebPage
from ui_classes.ApartSearchResultPage import ApartSearchResultPage

class ApartSearch(BaseWebPage):
    '''
    classdocs
    '''
    webdriver = None
    form_xpath = None


    def __init__(self, webdriver):
        '''
        Constructor
        '''
        self.webdriver = webdriver
        
        super().__init__(self.webdriver)
        
        self.form_xpath = "//*[@id='frm']"
    
    def get_name_field(self):
        return self.webdriver.find_element_by_xpath("%s//input[@name='ss']" %self.form_xpath)
    
    def enter_country_city_name(self, name, hint_to_select=None):
        context_menu = "//*[@id='destinationSearch']"
        self.enter_text(name, self.get_name_field()).wait_for(context_menu)
        #self.get_name_field().send_keys(name)
        
        #element = WebDriverWait(self.webdriver, 30).until(EC.presence_of_element_located((By.XPATH, context_menu)))
        
        if hint_to_select and hint_to_select != '':
            self.webdriver.find_element_by_xpath("%s/b[contains(text(), %s)]" %(context_menu, hint_to_select))
        elif hint_to_select == '':
            self.webdriver.find_element_by_xpath("%s/b[contains(text(), %s)]" %(context_menu, hint_to_select))
        
        return self
    
    def select_checkin_day(self, day_number):
        #select = Select(self.webdriver.find_element_by_name('checkin_monthday'))
        #try:
        #    select.select_by_value("%s" %day_number)
        #except:
        #    raise ValueError("Incorrect day of the month: %s"  %day_number)
        self.select_value_from_dropdown_menu(day_number, 
                                             self.webdriver.find_element_by_name('checkin_monthday'), 
                                             'Incorrect day of the month: %s' %day_number)
        
        return self
        
    
    def select_checkin_month(self, month_number):
        #select = Select(self.webdriver.find_element_by_name('checkin_year_month'))
        #try:
        #    select.select_by_value("%s-%s" %(date.today().year, month_number))
        #except:
        #    raise ValueError("Incorrect month of the year: %s" %month_number)
        self.select_value_from_dropdown_menu("%s-%s" %(date.today().year, month_number), 
                                             self.webdriver.find_element_by_name('checkin_year_month'), 
                                             'Incorrect month of the year: %s' %month_number)
        
        return self
    
    def select_checkout_day(self, day_number):
        #select = Select(self.webdriver.find_element_by_name('checkout_monthday'))
        #try:
        #    select.select_by_value("%s" %day_number)
        #except:
        #    raise ValueError("Incorrect day of the month: %s" %day_number)
        self.select_value_from_dropdown_menu(day_number, 
                                             self.webdriver.find_element_by_name('checkout_monthday'), 
                                             'Incorrect day of the month: %s' %day_number)
        
        return self
    
    def select_checkout_month(self, month_number):
        #select = Select(self.webdriver.find_element_by_name('checkout_year_month'))
        #try:
        #    select.select_by_value("%s-%s" %(date.today().year, month_number))
        #except:
        #    raise ValueError("Incorrect month of the year: %s" %month_number)
        self.select_value_from_dropdown_menu("%s-%s" %(date.today().year, month_number), 
                                             self.webdriver.find_element_by_name('checkout_year_month'), 
                                             'Incorrect month of the year: %s' %month_number)
        
        return self
    
    def return_search_button(self):
        return self.webdriver.find_element_by_xpath("//*[@id='frm']//button[@type='submit']")
    
    def search_appartments(self):
        #self.return_search_button().click()
        #element = WebDriverWait(self.webdriver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='breadcrumb']/div[2]")))
        self.click(self.return_search_button())
        
        return ApartSearchResultPage(self.webdriver)
        