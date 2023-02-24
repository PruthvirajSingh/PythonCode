from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class PageTitle:
    button_pageTitle_css=".page-title.user-generated"
    text_input_css="#pageTitle"
    button_save_xpath="(//a[@class='wds-button wds-button--sm save'])[2]"

    def __init__(self,driver):
        self.driver=driver

    def pageTitleAdd(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_pageTitle_css).click()
    def addTitle(self,value):
        self.driver.find_element(By.CSS_SELECTOR, self.text_input_css).send_keys(value)

    def saveButton(self):
        self.driver.find_element(By.XPATH,self.button_save_xpath).click()