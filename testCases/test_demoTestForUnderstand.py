import random
import string
import time

import allure
import pytest
from allure_commons.types import AttachmentType

from Utilities import XLUtils
from Utilities.ReadProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageObject.LoginPage import Login
from pageObject.NewCreateSurvey import CreateNewSurvey
from pageObject.PageTitle import PageTitle


class DemoClassForTheUnderstand:
    @pytest.fixture(scope='function')
    def myFixture(self):
        print("Before test")
        yield
        print("After test")

    def test_A(self):
        print("I am test A")


t1 = DemoClassForTheUnderstand()
t1.test_A()
#     baseURL = ReadConfig.readBaseUrl()
#     path = ".//TestData/LoginData.xlsx"
#     logger = LogGen.loggen()
#
#     @pytest.fixture(scope='function')
#     def setUp(self, setUp1):
#         self.driver = setUp1
#         self.logger.info("************* Test Case No 001 _login test**********************")
#         self.driver.get(self.baseURL)
#         self.logger.info("Enter Base Url")
#         self.driver.implicitly_wait(10)
#         self.driver.maximize_window()
#         self.logger.info("Maximized windows")
#         self.lp = Login(self.driver)
#         self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
#         print('Number of rows...', self.rows)
#         self.user = XLUtils.readData(self.path, 'Sheet1', 2, 1)
#         self.password = XLUtils.readData(self.path, 'Sheet1', 2, 2)
#         self.exp = XLUtils.readData(self.path, 'Sheet1', 2, 3)
#         self.lp.logInButton()
#         time.sleep(1)
#         self.lp.textLogin(setUp1)
#         self.lp.userName(self.user, setUp1)
#         self.logger.info("Enter the username")
#         self.lp.nextButton()
#         self.logger.info("Click on next button")
#         self.lp.passWord(self.password)
#         self.logger.info("Enter Passwrod")
#         self.lp.logInButtonAfterPassword()
#         self.logger.info("Login button after the password")
#         yield
#
#         createSurvey = CreateNewSurvey(self.driver)
#         allure.attach(self.driver.get_screenshot_as_png(), name="login and create survey",
#                       attachment_type=AttachmentType.PNG)
#         self.logger.info("click on the my Survey")
#         createSurvey.mySurvy(setUp1)
#         self.logger.info("Click three dots")
#         createSurvey.threeDot()
#         self.logger.info("Delete survey")
#         createSurvey.deleteSurvey()
#         createSurvey.finalDelete()
#         self.lp = Login(self.driver)
#         self.lp.buttonForUser()
#         self.lp.buttonForLogOut()
#         self.driver.close()
#
#     def test_newTestCase(self, setUp1):
#         self.driver = setUp1
#         createSurvey = CreateNewSurvey(self.driver)
#         self.logger.info("create new survey")
#         createSurvey.createSurvey()
#         self.logger.info("Select start from scartch")
#         createSurvey.startFromScrach("Start from scratch")
#         self.logger.info("Name of survey")
#         createSurvey.addName(random_generator())
#         self.logger.info("Click on the create survey")
#         createSurvey.buttonForCreateSurvey(setUp1)
#         self.pt = PageTitle(self.driver)
#         self.pt.pageTitleAdd()
#         self.pt.addTitle(random_generator1())
#         self.pt.saveButton()
#
#
# def random_generator(size=9, chars=string.ascii_lowercase + string.digits):
#     return ''.join(random.choice(chars) for x in range(size))
#
#
# def random_generator1(size=120, chars=string.ascii_lowercase + string.digits):
#     return ''.join(random.choice(chars) for x in range(size))
