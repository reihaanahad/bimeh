
import os

from selenium.webdriver import ActionChains

from Locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


# import pytesseract
# from PIL import Image


def wait_until_element_has_an_attribute(self, element_selector, element_locator):
    wait = WebDriverWait(self.driver, 20)
    element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
    sleep(0.2)
    element.click()
    sleep(0.2)

def wait_until_element_has_an_attribute_and_send_keys(self, element_selector, element_locator, text):
    wait = WebDriverWait(self.driver, 20)
    element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
    sleep(1)
    #ActionChains(self.driver).move_to_element(element).send_keys(Keys.CONTROL + "a").send_keys(Keys.BACKSPACE).send_keys(text).perform()

    element.click()
    sleep(0.2)
    element.send_keys(Keys.CONTROL + "a")
    sleep(0.2)
    element.send_keys(Keys.BACKSPACE)
    sleep(0.2)
    element.send_keys(text)
    sleep(0.2)


def get_url_with_refresh(self, url, element_id, max_retries=2, delay_seconds=0.1):
    for retry_count in range(max_retries + 1):
        self.driver.get(url)
        try:
            self.driver.find_element('xpath', element_id)
            return
        except NoSuchElementException:
            print(f"Element with id '{element_id}' not found. Retrying in {delay_seconds} seconds...")

        if retry_count < max_retries:
            sleep(delay_seconds)
        else:
            raise Exception(f"Maximum number of retries reached. Element with id '{element_id}' not found.")

class ThirdParty:
    def __init__(self, driver):
        self.driver = driver

    def enter_login_phone_number(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', login_phone_number, text)

    def enter_login_check_phone_number(self):
        wait_until_element_has_an_attribute(self, 'xpath', login_check_phone_number)

    def enter_login_password(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', login_password, text)

    def enter_login_password_submit(self):
        wait_until_element_has_an_attribute(self, 'xpath', login_password_submit)

    def click_on_element(self, element_selector, element_locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((element_selector, element_locator)))
        sleep(0.2)
        element.click()
        sleep(0.2)

    def select_from_dropdown(self, element_locator, option_locator):
        wait = WebDriverWait(self.driver, 20)
        sleep(1)
        element = self.driver.find_element('xpath', element_locator)
        sleep(0.5)
        element.click()
        sleep(1)
        option = wait.until(EC.element_to_be_clickable(('xpath', option_locator)))
        sleep(0.5)
        option.click()

    def select_from_dropdown_scroll(self, element_locator):
        wait = WebDriverWait(self.driver, 20)
        sleep(1)
        element = self.driver.find_element('xpath', element_locator)
        sleep(0.5)
        element.click()
        scrolll = self.driver.find_element(By.CLASS_NAME, 'rc-virtual-list-holder')
        for i in range(7):
            sleep(1)
            self.driver.execute_script("arguments[0].scrollBy(0, 120);", scrolll)
        classes = self.driver.find_elements(By.CLASS_NAME, 'ant-select-item-option-content')
        classes[2].click()

    def enter_first_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', third_party_first_name, text)

    def enter_last_name(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', third_party_last_name, text)

    def enter_national_code(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', third_party_national_code, text)

    def enter_mobile_phone(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', third_party_mobile_phone, text)

    def enter_phone(self, text):
        wait_until_element_has_an_attribute_and_send_keys(self, 'xpath', third_party_phone, text)

    def upload(self, n):
        e = self.driver.find_elements(By.XPATH, "//input[@type='file']")
        file_input = e[n]
        file_input.send_keys("C:\download.jpg")
