import allure
import pytest
from allure_commons.types import AttachmentType

from pageObject.LoginPage import Login
import time

from Utilities.ReadProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils


@allure.severity(allure.severity_level.NORMAL)
class Test_001:
    baseURL = ReadConfig.readBaseUrl()
    path = "C:/Users/Pruthvirajsing/PycharmProjects/pythonProject2/TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @allure.severity(allure.severity_level.MINOR)

    def test_loginpage(self, setUp1):
        self.driver = setUp1
        self.logger.info("************* Test Case No 001 _login test**********************")
        self.driver.get(self.baseURL)
        self.logger.info("Enter Base Url")
        self.driver.implicitly_wait(30)
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
        for r in range(3, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.logInButton()
            self.lp.clearValues()
            self.lp.userName(self.user,setUp1)
            self.logger.info("Enter the username")
            self.lp.nextButton()
            self.driver.back()

            time.sleep(2)

            act_title = self.driver.current_url
            exp_title = "https://www.surveymonkey.com/dashboard/?ut_source=header"

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** passed ****")

                    lst_status.append("Pass")

                elif self.exp == 'Fail':
                    self.logger.info("**** failed ****")

                    lst_status.append("Fail")


            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")

                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")

            print(lst_status)
            self.logger.info("******* End of Login Test **********")
            self.logger.info("**************** Completed  TC_Login_001 ************* ")
            time.sleep(1)
