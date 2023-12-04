import datetime
from datetime import date

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from Pages.sql import SqlServer

from time import sleep
from Locators import *
from Pages.Login import LoginPage
from Pages.Login import get_url_with_refresh

from Pages.Thirdparty import ThirdParty

import unittest

service = Service()
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)

start_time = datetime.datetime.now().replace(microsecond=0)

class TestThirdparty(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        cls.tests_texts = []



    def test01_thirdparty(self):
        get_url_with_refresh(self, url_test, login_link_logo)
        login = LoginPage(driver = self.driver)
        thirdparty = ThirdParty(driver=self.driver)
        login.enter_login_phone_number(phone_number1)
        login.enter_login_check_phone_number()
        login.enter_login_password(code1)
        login.enter_login_password_submit()
        thirdparty.click_on_element('xpath', third_party_ins_icon)
        self.tests_texts.append("test")

    def test02_thirdpaty(self):
        thirdparty = ThirdParty(driver=self.driver)
        thirdparty.click_on_element('xpath', third_party_forget_car_tag)



    def test03_thirdpaty(self):
        thirdparty = ThirdParty(driver=self.driver)
        thirdparty.select_from_dropdown(third_party_vehicle_category, third_party_option_savari)
        thirdparty.select_from_dropdown(third_party_using_type, third_party_option_shakhsi)
        thirdparty.select_from_dropdown(third_party_brands, third_party_option_pejo)
        thirdparty.select_from_dropdown(third_party_production_year, third_party_option_1402)

        thirdparty.select_from_dropdown(third_party_model, third_party_option_207sandogh)
        thirdparty.click_on_element('xpath', third_party_continue_discounts_detail)




    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()


#SqlServer.run_tests_and_insert_into_sql_server(TestLogin, 'test_login')