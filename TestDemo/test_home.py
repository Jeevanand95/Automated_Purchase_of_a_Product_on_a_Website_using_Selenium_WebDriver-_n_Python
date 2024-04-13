import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilies.Baseclass import BaseClass
from pageobjectmodel.Checkoutconfirm import ConfirmCheck
from pageobjectmodel.Checkoutpage import CheckoutPage
from pageobjectmodel.homepage import Homepage


class TestEnd(BaseClass):

    def test_frst(self):
        log= self.loggingname()
        Home = Homepage(self.driver)
        Home.namefield().send_keys("Jeeva")
        log.info("new name is enterted")
        Home.emailfield().send_keys("jeeva@gmail.com")
        Home.passwordfield().send_keys("lollipop")
        log.info("new name is enterted")
        Home.checkboxfield().click()
        self.selectoptions()
        Home.datefield().send_keys("26-03-1995")
        Home.confirmclick().click()






