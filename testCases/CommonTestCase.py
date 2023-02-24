import time

import allure
import pytest
from allure_commons.types import AttachmentType

from Utilities import XLUtils
from Utilities.ReadProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageObject.LoginPage import Login

class CommanTestCases:
    baseURL = ReadConfig.readBaseUrl()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()
    @pytest.fixture(autouse=True)
    def loginpage(self, setUp):
            self.driver = setUp
            self.logger.info("************* Test Case No 001 _login test**********************")
            self.driver.get(self.baseURL)
            self.logger.info("Enter Base Url")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.logger.info("Maximized windows")
            self.lp = Login(self.driver)
            lst_status = []
            self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
            print('Number of rows...', self.rows)

            self.user = XLUtils.readData(self.path, 'Sheet1', 2, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', 2, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', 2, 3)
            self.lp.logInButton()
            self.lp.userName(self.user)
            self.logger.info("Enter the username")
            self.lp.nextButton()
            self.logger.info("Click on next button")
            self.lp.passWord(self.password)
            self.logger.info("Enter Passwrod")
            self.lp.logInButtonAfterPassword()
            self.logger.info("Login button after the password")
            self.lp.dashbordButton()
            time.sleep(2)
            act_title = self.driver.current_url
            exp_title = "https://www.surveymonkey.com/dashboard/?ut_source=header"

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** passed ****")
                    self.lp.buttonForUser()
                    self.lp.buttonForLogOut()
                    lst_status.append("Pass")

                elif self.exp == 'Fail':
                    allure.attach(self.driver.get_screenshot_as_png(), name="testLogin", attachment_type=AttachmentType.PNG)
                    self.logger.info("**** failed ****")
                    self.lp.buttonForUser()
                    self.lp.buttonForLogOut()
                    lst_status.append("Fail")

                print(lst_status)
