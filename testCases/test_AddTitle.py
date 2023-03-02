import time
import unittest

import pytest

from testCases.BaseClass import BaseClass
from pageObject.NewCreateSurvey import CreateNewSurvey
import random
import string
from pageObject.PageTitle import PageTitle
class Test_004(BaseClass):

    @pytest.mark.lambdatest2_1
    def test_addTitle(self,setUp1):
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
        self.pt=PageTitle(self.driver)
        self.pt.pageTitleAdd()
        self.pt.addTitle(random_generator())
        self.pt.saveButton()

        time.sleep(1)
        super().tearDown(self, setUp1)

    @pytest.mark.lambdatest2_2
    def test_TitleMoreThan100(self,setUp1):
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
        self.pt = PageTitle(self.driver)
        self.pt.pageTitleAdd()
        self.pt.addTitle(random_generator1())
        self.pt.saveButton()

        time.sleep(1)
        super().tearDown(self, setUp1)

def random_generator(size=9, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def random_generator1(size=120, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))