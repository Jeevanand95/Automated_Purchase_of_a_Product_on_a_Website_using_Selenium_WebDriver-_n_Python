import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setup')
class BaseClass():
    def webwait(self):
        wait_driver = WebDriverWait(self.driver, 10)
        new_wait = (wait_driver.until
                    (expected_conditions.presence_of_element_located((By.XPATH, "//a[text()='India']"))))
        return new_wait


    def selectoptions(self):
        selectopt = Select(self.driver.find_element(By.ID,"exampleFormControlSelect1"))
        selectopt.select_by_visible_text("Male")
        return selectopt

    def loggingname(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger
