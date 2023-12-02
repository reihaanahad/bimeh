import datetime
from datetime import date

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from Pages.sql import SqlServer

from time import sleep
from Locators import *
from Pages.Login import LoginPage
import unittest

service = Service()
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)

start_time = datetime.datetime.now().replace(microsecond=0)

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        cls.tests_texts = []

###Login

    def test01_login(self):
        self.driver.get(url_test)
        login = LoginPage(driver = self.driver)
        login.visibility_of_elements(login_link_logo)
        login.visibility_of_elements(login_link_terms)
        login.enter_login_phone_number(" ")
        login.enter_login_check_phone_number()
        login.assert_login_wrong_phone_number(login_wrong_phone_number, 'نام کاربری نامعتبر ')
        self.tests_texts.append("test")

    def test02_login(self):
        self.driver.get(url_test)
        login = LoginPage(driver = self.driver)
        login.visibility_of_elements(login_link_logo)
        login.visibility_of_elements(login_link_terms)
        login.enter_login_phone_number("0938909035r")
        login.enter_login_check_phone_number()
        login.assert_login_wrong_phone_number(login_wrong_phone_number, 'نام کاربری نامعتبر ')
        self.tests_texts.append("test")

    def test03_login(self):
        self.driver.get(url_test)
        login = LoginPage(driver = self.driver)
        login.visibility_of_elements(login_link_logo)
        login.visibility_of_elements(login_link_terms)
        login.enter_login_phone_number("0 9 3 8 9 0 9 0 3 5 9")
        login.enter_login_check_phone_number()
        login.assert_login_wrong_phone_number(login_wrong_phone_number, 'نام کاربری نامعتبر ')
        self.tests_texts.append("test")

    def test04_login(self):
        self.driver.get(url_test)
        login = LoginPage(driver = self.driver)
        login.visibility_of_elements(login_link_logo)
        login.visibility_of_elements(login_link_terms)
        login.enter_login_phone_number("0938909035")
        login.enter_login_check_phone_number()
        login.assert_login_wrong_phone_number(login_wrong_phone_number, 'نام کاربری نامعتبر ')
        self.tests_texts.append("test")

    def test05_login(self):
        self.driver.get(url_test)
        login = LoginPage(driver = self.driver)
        login.visibility_of_elements(login_link_logo)
        login.visibility_of_elements(login_link_terms)
        login.enter_login_phone_number("093890903599")
        login.enter_login_check_phone_number()
        login.assert_login_wrong_phone_number(login_verified_phone_number, '09389090359')
        self.tests_texts.append("test")

    def test06_login(self):
        self.driver.get(url_test)
        login = LoginPage(driver=self.driver)
        login.visibility_of_elements(login_link_logo)
        login.visibility_of_elements(login_link_phone_edit)
        login.visibility_of_elements(login_link_forget)
        login.visibility_of_elements(login_link_otp_login)
        login.visibility_of_elements(login_hidden_password)
        login.enter_login_password(" ")
        login.enter_login_password_submit()
        login.assert_login_wrong_password(login_wrong_password, 'نام کاربری یا رمز عبور اشتباه است')

    def test07_login(self):
        self.driver.get(url_test)
        login = LoginPage(driver=self.driver)
        login.visibility_of_elements(login_link_logo)
        login.visibility_of_elements(login_link_phone_edit)
        login.visibility_of_elements(login_link_forget)
        login.visibility_of_elements(login_link_otp_login)
        login.visibility_of_elements(login_hidden_password)
        login.enter_login_password_submit()
        login.assert_login_wrong_password(login_wrong_password, 'نام کاربری یا رمز عبور اشتباه است')

    def test08_login(self):
        self.driver.get(url_test)
        login = LoginPage(driver=self.driver)
        login.visibility_of_elements(login_link_logo)
        login.visibility_of_elements(login_link_phone_edit)
        login.visibility_of_elements(login_link_forget)
        login.visibility_of_elements(login_link_otp_login)
        login.visibility_of_elements(login_hidden_password)
        login.enter_login_password("rahad31*")
        login.enter_login_password_submit()
        login.assert_login_wrong_password(login_wrong_password, 'نام کاربری یا رمز عبور اشتباه است')

    def test09_login(self):
        self.driver.get(url_test)
        login = LoginPage(driver=self.driver)
        login.visibility_of_elements(login_link_logo)
        login.visibility_of_elements(login_link_phone_edit)
        login.visibility_of_elements(login_link_forget)
        login.visibility_of_elements(login_link_otp_login)
        login.visibility_of_elements(login_hidden_password)
        login.enter_login_password("rahad31*")
        login.test_pass_type("//*[@type='password']")
        login.enter_login_hidden_password()
        login.test_pass_type("//*[@type='text']")

    def test10_login(self):
        self.driver.get(url_test)
        login = LoginPage(driver=self.driver)
        login.enter_login_link_phone_edit()
        login.visibility_of_elements(login_link_logo)
        login.visibility_of_elements(login_link_terms)
        login.visibility_of_elements(login_phone_number)
        login.enter_login_check_phone_number()




    # def test02_login(self):
    #     self.driver.get(url_test)


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()


#SqlServer.run_tests_and_insert_into_sql_server(TestLogin, 'test_login')
