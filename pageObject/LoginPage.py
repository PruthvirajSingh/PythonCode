import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    button_logIn_xpath="//a[text()='Log in']"
    text_logIn_xapth="//h1[@class='wds-type--page-title wds-m-b-2 style-scope wds-title']"
    testbox_userName_xpath="(//input[@id='username'])[2]"
    button_next_xpath="(//div[@class='button-content-inner style-scope sm-button'])[1]"
    textbox_password_xapth="(//input[@id='password'])[2]"
    button_loginafterpassword_xpath="//div[@class='button-content-inner style-scope sm-button']"
    button_dashBord_xpath="//a[text()='Dashboard']"
    button_nameLogo_xpath=".mm-menu__nav-button"
    button_signOut_xpath="(//span[text()='Sign Out'])[2]"
    def __init__(self,driver):
        self.driver=driver

    def logInButton(self):
        self.driver.find_element(By.XPATH,self.button_logIn_xpath).click()
    def clearValues(self):

        self.driver.find_element(By.XPATH, self.testbox_userName_xpath).clear()

    def textLogin(self,driver):

     WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.XPATH, self.text_logIn_xapth)))


    def userName(self,username,driver):

        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH, self.testbox_userName_xpath)))
        element.send_keys(username)
    def nextButton(self):
        self.driver.find_element(By.XPATH,self.button_next_xpath).click()

    def passWord(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_xapth).send_keys(password)

    def logInButtonAfterPassword(self):
        self.driver.find_element(By.XPATH,self.button_loginafterpassword_xpath).click()

    def dashbordButton(self):
        self.driver.find_element(By.XPATH,self.button_dashBord_xpath).click()

    def buttonForUser(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_nameLogo_xpath).click()

    def buttonForLogOut(self):
        self.driver.find_element(By.XPATH,self.button_signOut_xpath).click()

