from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from selenium.webdriver.firefox.options import Options 
from selenium.webdriver.common.action_chains import ActionChains

class ExampleClass:
    def __init__(self):
        self.driver = webdriver.Firefox()
    def load(self,url):
        self.driver.get(url)
    def dropdown(self,IdName,classname,index):
        time.sleep(2)

        self.driver.find_element(By.ID,IdName).click()
        time.sleep(1)
        classes=self.driver.find_elements(By.CLASS_NAME , classname)

        classes[index].click()
    def select(self,classname,attribute):
        
        classes=self.driver.find_elements(By.CSS_SELECTOR,classname)
        
        for i in classes:
            if str(i.text)==attribute:
                i.click()
                break
    def scroll(self,classname,n):
        scrolll =self.driver.find_element(By.CLASS_NAME , classname)
        for i in range(n):
            time.sleep(1)
            self.driver.execute_script("arguments[0].scrollBy(0, 120);",scrolll)
    def quit(self):
        self.driver.quit()    
    # def actionchains(self):
    #     ActionChains(self.driver).move_to_element(self.driver.find_element(By.XPATH,'//*[@id="Group_9752"]')).click().perform()
    def find_element_by_xpath(self,xpath):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, xpath).click()
    def find_element_by_class(self,ClassName):
        self.driver.find_element(By.CLASS_NAME, ClassName).click()
    def find_element_by_Id(self,IdName):
        self.driver.find_element(By.ID, IdName).click()
    def input(self,IdName,input):
        self.driver.find_element(By.ID,IdName).send_keys(input)
    def find_elements_by_classes(self,ClassName,index):
        time.sleep(1)
        radios=self.driver.find_elements(By.CLASS_NAME ,ClassName)
        time.sleep(1)

        radios[index].click()
    def find_elements_by_xpaths(self,xpath,index):
        radios=self.driver.find_elements(By.XPATH, xpath)
        radios[index].click()
    def find_txt(self,xpath):
        self.driver.implicitly_wait(20)
        txt=self.driver.find_element(By.XPATH,xpath).text
        return txt
    def upload(self,n):
        e=self.driver.find_elements(By.XPATH, "//input[@type='file']")
        file_input=e[n]
        file_input.send_keys("C:\download.jpg")
    def scroll_down(self,n):
        self.driver.execute_script(f"window.scrollTo(0,{n});")
    def scroll_element(self,xpath):
        element = self.driver.find_element(By.XPATH,xpath)
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)
    def action(self,xpath):
        element=self.driver.find_element(By.XPATH,xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
