'''
Created on 10 січ. 2016

@author: chmel
'''
import unittest
from datetime import date
from engine.TestSetupTeardown import TestSetupTeardown

class TestLogin(TestSetupTeardown):
    user_firstname = ''
    user_surname = ''
    user_workspace = None
    item = None
    hotel = None


    @TestSetupTeardown.setup_env
    def setUp(self):
        self.user_firstname = 'Pavlo'
        self.user_surname = 'Mryhlockyi'
        self.item = 'Montenegro'
        self.hotel = 'Hotel Montenegro'
        self.user_workspace = self.booking_base_page.login().login_as_user(self.booking_user, self.booking_password)


    @TestSetupTeardown.teardown_env
    def tearDown(self):
        pass


    @TestSetupTeardown.ui_test
    def testTask1(self):
        first_name = self.user_workspace.get_user_firstname().text
        sur_name = self.user_workspace.get_user_surname().text
        self.assertEqual(first_name, self.user_firstname, "Site shows incorrect user first name: %s. Expected: %s" %(first_name, self.user_firstname))
        self.assertEqual(sur_name, self.user_surname, "Site shows incorrect user last name: %s. Expected: %s" %(sur_name, self.user_surname))
    
    @TestSetupTeardown.ui_test
    def testTask2(self):
        self.assertTrue(
                        self.user_workspace.\
                        go_to_search_apartaments().\
                        enter_country_city_name(self.item).\
                        select_checkin_day(22).\
                        select_checkin_month(9).\
                        select_checkout_day(30).\
                        select_checkout_month(9).\
                        search_appartments().get_hotels_block().\
                        verify_item(self.hotel), 
                        "Hotel %s is not found in the hotels top" %self.hotel)
    
    @TestSetupTeardown.ui_test
    def testTask3(self):
        selected_hotel = self.user_workspace.\
        go_to_search_apartaments().\
        enter_country_city_name(self.item).\
        select_checkin_day(22).\
        select_checkin_month(9).\
        select_checkout_day(30).\
        select_checkout_month(9).\
        search_appartments().\
        get_hotels_block()
        #.\
        #go_to_hotel(self.hotel).\
        #get_apartment_details()
        
        #print(selected_hotel["apartment type"])
    
    @TestSetupTeardown.ui_test
    def testTask4(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    