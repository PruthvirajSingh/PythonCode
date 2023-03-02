from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class CreateNewSurvey:
    button_createSurvey_css = ".mm-header__action-create"
    button_startFromScrach_css = ".wds-button"
    text_popUpNameOfSurvey_css=".wds-modal__text"
    text_SurveyName_css = "input#surveyTitle"
    button_newCreateSurvey_xpath = "//button[@id='newSurvey']"
    button_mySurvey_xpath = "//nav[@class='mm-navigation mm-header__navigation']//a[text()='My Surveys']"
    button_threeDot_xpath = "(//a[@class='survey-actions'])[1]"
    button_delete_xpath = "(//span[text()='Delete'])[2]"
    button_finalDelete_xpath = "(//a[text()='DELETE'])[3]"
    text_titleOfSurvey_css = ".global-navigation-header-title"
    text_copySurvey_xpath="//div[@class='wds-type--section-title']'"

    def __init__(self, driver):
        self.driver = driver

    def createSurvey(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_createSurvey_css).click()

    def startFromScrach(self, value):
        elemets = []
        elemets = self.driver.find_elements(By.CSS_SELECTOR, self.button_startFromScrach_css)
        for newElement in elemets:
            print(newElement.text)
            if newElement.text == value:
                newElement.click()
    def textOfTheButton(self,value):
        elemets = []
        elemets = self.driver.find_elements(By.CSS_SELECTOR, self.button_startFromScrach_css)
        for newElement in elemets:
            print(newElement.text)
            if newElement.text == value:
                return newElement
    def popUpNameOfTheSurvey(self):
        values=self.driver.find_element(By.CSS_SELECTOR,self.text_popUpNameOfSurvey_css).is_displayed()
        return values


    def addName(self, surveyName):
        self.driver.find_element(By.CSS_SELECTOR, self.text_SurveyName_css).send_keys(surveyName)

    def buttonForCreateSurvey(self, driver):

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.button_newCreateSurvey_xpath)))
        element.click()

    def mySurvy(self, driver):

        element = WebDriverWait(driver, 10).until(

            EC.presence_of_element_located((By.XPATH, self.button_mySurvey_xpath)))
        element.click()

    def threeDot(self):
        self.driver.find_element(By.XPATH, self.button_threeDot_xpath).click()

    def deleteSurvey(self):
        self.driver.find_element(By.XPATH, self.button_delete_xpath).click()

    def finalDelete(self):
        self.driver.find_element(By.XPATH, self.button_finalDelete_xpath).click()

    def textSurvey(self):
        value = self.driver.find_element(By.CSS_SELECTOR, self.text_titleOfSurvey_css).is_displayed()
        return value
    def copySurvyText(self):
        value=self.driver.find_element(By.CSS_SELECTOR,self.text_copySurvey_xpath).is_displayed()
        return value