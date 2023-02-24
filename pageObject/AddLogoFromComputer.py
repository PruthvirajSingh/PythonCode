from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class AddLogoHere():
    button_addLogo_xpath="//div[@class='addLogoHere ']//span"
    linkText_addLogo_xpath="//div[@class='url-bar']//span//input"
    Place_afterLogo_xpath="//span[@class='logo-container notranslate']"

    def __init__(self,driver):
        self.driver=driver

    def addLogoButton(self,driver):
        # self.driver.find_element(By.XPATH,self.button_addLogo_xpath).click()
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.button_addLogo_xpath)))
        element.click()

    def clickOnTheLink(self,value,driver):
        # self.driver.find_element(By.XPATH,self.linkText_addLogo_xpath).send_keys(value)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,self.linkText_addLogo_xpath)))
        element.send_keys(value)
    def imageDisplayed(self):
        element=self.driver.find_element(By.XPATH,self.Place_afterLogo_xpath)
        return element.is_displayed()