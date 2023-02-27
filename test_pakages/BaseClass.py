import time

from Utilities.ReadProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageObject.LoginPage import Login
from Utilities import XLUtils
from pageObject.NewCreateSurvey import CreateNewSurvey
import random
import string
class BaseClass:
    baseURL = ReadConfig.readBaseUrl()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @staticmethod
    def setUp(self, setUp1):
        self.driver = setUp1
        self.logger.info("************* Test Case No 001 _login test**********************")
        self.driver.get(self.baseURL)
        self.logger.info("Enter Base Url")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.logger.info("Maximized windows")
        self.lp = Login(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print('Number of rows...', self.rows)
        self.user = XLUtils.readData(self.path, 'Sheet1', 2, 1)
        self.password = XLUtils.readData(self.path, 'Sheet1', 2, 2)
        self.exp = XLUtils.readData(self.path, 'Sheet1', 2, 3)
        self.lp.logInButton()
        time.sleep(1)
        self.lp.textLogin(setUp1)
        self.lp.userName(self.user,setUp1)
        self.logger.info("Enter the username")
        self.lp.nextButton()
        self.logger.info("Click on next button")
        self.lp.passWord(self.password)
        self.logger.info("Enter Passwrod")
        self.lp.logInButtonAfterPassword()
        self.logger.info("Login button after the password")
    @staticmethod
    def tearDown(self,setUp1):
        self.driver = setUp1
        createSurvey = CreateNewSurvey(self.driver)
        self.logger.info("click on the my Survey")
        createSurvey.mySurvy(setUp1)
        self.logger.info("Click three dots")
        createSurvey.threeDot()
        self.logger.info("Delete survey")
        createSurvey.deleteSurvey()
        createSurvey.finalDelete()
        self.lp = Login(self.driver)
        self.lp.buttonForUser()
        self.lp.buttonForLogOut()
        self.driver.close()