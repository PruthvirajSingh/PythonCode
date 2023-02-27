import time

from testCases.BaseClass import BaseClass
import random
import string
import os
from pageObject.NewCreateSurvey import CreateNewSurvey
from pageObject.AddLogoFromComputer import AddLogoHere
class Test_003(BaseClass):
   def test_addLogo(self,setUp1):
       super().setUp(self, setUp1)
       self.driver = setUp1
       createSurvey = CreateNewSurvey(self.driver)
       self.logger.info("create new survey")
       createSurvey.createSurvey()
       self.logger.info("Select start from scartch")
       createSurvey.startFromScrach("Start from scratch")
       self.logger.info("Name of survey")
       createSurvey.addName(random_generator())
       self.logger.info("Click on the create survey")
       createSurvey.buttonForCreateSurvey(setUp1)
       self.addLogo= AddLogoHere(self.driver)
       self.addLogo.addLogoButton(self.driver)
       self.addLogo.clickOnTheLink(os.getcwd()+"//TestData/pexels-johannes-plenio-1435075.jpg",self.driver)
       time.sleep(2)
       values=self.addLogo.imageDisplayed()
       if(values==True):
           print("test case pass")
           time.sleep(1)
           super().tearDown(self, setUp1)

def random_generator(size=9, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
