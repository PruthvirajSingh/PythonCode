import time

from pageObject.NewCreateSurvey import CreateNewSurvey
import random
import string

from testCases.BaseClass import BaseClass


class Test_002(BaseClass):
    def test_createSurvey(self,setUp1):
        super().setUp(self,setUp1)
        self.driver = setUp1
        self.logger.info("************* Test Case No 002 _Create survey Start from scratch**********************")
        createSurvey = CreateNewSurvey(self.driver)
        self.logger.info("create new survey")
        createSurvey.createSurvey()
        self.logger.info("Select start from scartch")

        createSurvey.startFromScrach("Start from scratch")

        self.logger.info("Name of survey")
        popUpText=createSurvey.popUpNameOfTheSurvey()
        assert popUpText==True
        createSurvey.addName(random_generator())
        self.logger.info("Click on the create survey")
        createSurvey.buttonForCreateSurvey(setUp1)
        value=createSurvey.textSurvey()
        assert value==True
        time.sleep(1)
        super().tearDown(self,setUp1)
# class Test_003(BaseClass):
#     def test_negativeTestCases(self,setUp1):
#         super().setUp(self, setUp1)
#         self.driver = setUp1
#         self.logger.info("************* Test Case No 002 _Create survey Start from scratch**********************")
#         createSurvey = CreateNewSurvey(self.driver)
#         self.logger.info("create new survey")
#         createSurvey.createSurvey()
#         self.logger.info("Select start from scartch")
#
#         createSurvey.startFromScrach("Copy a past survey")
#
#         self.logger.info("Name of survey")
#         copyOfSurvey=createSurvey.copySurvyText()
#         assert copyOfSurvey == True
#         # popUpText = createSurvey.popUpNameOfTheSurvey()
#         # assert popUpText == False
#         # createSurvey.addName(random_generator())
#         # self.logger.info("Click on the create survey")
#         # createSurvey.buttonForCreateSurvey(setUp1)
#         # value = createSurvey.textSurvey()
#         # assert value == True
#         time.sleep(1)
#         super().tearDown(self, setUp1)



def random_generator(size=9, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
