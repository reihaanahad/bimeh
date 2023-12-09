import datetime
from datetime import date
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from Pages.sql import SqlServer
from time import sleep
from Locators import *
from Pages.Thirdparty import ThirdParty, get_url_with_refresh
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
        thirdparty = ThirdParty(driver=self.driver)
        thirdparty.enter_login_phone_number(phone_number1)
        thirdparty.enter_login_check_phone_number()
        thirdparty.enter_login_password(code1)
        thirdparty.enter_login_password_submit()
        thirdparty.click_on_element('xpath', third_party_ins_icon)
        self.tests_texts.append("test")

    def test02_thirdpaty(self):
        thirdparty = ThirdParty(driver=self.driver)
        thirdparty.click_on_element('xpath', third_party_forget_car_tag)

    def test03_thirdpaty(self):
        thirdparty = ThirdParty(driver=self.driver)
        thirdparty.select_from_dropdown(third_party_vehicle_category, third_party_vehicle_category_option1)
        thirdparty.select_from_dropdown(third_party_using_type, third_party_using_type_option1)
        thirdparty.select_from_dropdown(third_party_brands, third_party_brands_option1)
        thirdparty.select_from_dropdown(third_party_production_year, third_party_production_year_1402)
        thirdparty.select_from_dropdown(third_party_model, third_party_model_option1)
        thirdparty.click_on_element('xpath', third_party_continue_discounts_detail)

    def test05_thirdparty(self):
        thirdparty = ThirdParty(driver=self.driver)
        thirdparty.select_from_dropdown(third_party_previous_ins_status, third_party_previous_ins_status_yes)
        thirdparty.click_on_element('xpath', third_party_owner_change_no)
        thirdparty.select_from_dropdown(third_party_previous_company, third_party_previous_company_arman)
        thirdparty.select_from_dropdown(third_party_previous_duration, third_party_previous_duration_one_year)
        thirdparty.click_on_element('xpath', third_party_continue_ins_detail)

    def test06_thirdparty(self):
        thirdparty = ThirdParty(driver=self.driver)
        thirdparty.select_from_dropdown(third_party_discount, third_party_discount_zero)
        thirdparty.select_from_dropdown(third_party_driver_discount, third_party_driver_discount_zero)
        thirdparty.click_on_element('xpath', third_party_damage_no)
        thirdparty.click_on_element('xpath', third_party_confirm_insurance_detail)

    def test07_thirdparty(self):
        thirdparty = ThirdParty(driver=self.driver)
        thirdparty.click_on_element('xpath', third_party_close_pop_up)
        thirdparty.click_on_element('xpath', third_party_purchase_saman)
        thirdparty.click_on_element('xpath', third_party_purchase_cash)
        thirdparty.click_on_element('xpath', third_party_continue_purchase)

    def test08_thirdparty(self):
        thirdparty = ThirdParty(driver=self.driver)
        thirdparty.enter_first_name(first_name)
        thirdparty.enter_last_name(last_name)
        thirdparty.select_from_dropdown_scroll(third_party_birth_year)
        thirdparty.select_from_dropdown(third_party_birth_day, third_party_birth_day_option1)
        thirdparty.select_from_dropdown(third_party_birth_month, third_party_birth_month_option1)
        thirdparty.enter_national_code(national_code)
        thirdparty.enter_mobile_phone(phone_number1)
        thirdparty.enter_phone(tel_phone)
        thirdparty.click_on_element('xpath', third_party_address)
        thirdparty.upload(1)
        thirdparty.upload(2)
        thirdparty.upload(3)

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()


#SqlServer.run_tests_and_insert_into_sql_server(TestLogin, 'test_login')
