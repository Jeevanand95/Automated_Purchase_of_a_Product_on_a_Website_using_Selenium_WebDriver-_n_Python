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
        log = self.loggingname()
        Home = Homepage(self.driver)
        Home.gethomepage().click()
        log.info("clicked")
        Checkout = CheckoutPage(self.driver)
        for names in Checkout.checkoutpage():
            product_name = names.find_element(*Checkout.product_name).text
            if product_name=="Blackberry":
                names.find_element(By.XPATH,"div/button").click()
        Checkout.addcart().click()
        Checkout.checkoutclick().click()
        confirmcheck = ConfirmCheck(self.driver)
        confirmcheck.checkconfirm("ind")
        self.webwait().click()
        confirmcheck.checkbox()
        confirmcheck.finalconfirm()
        confirmcheck.newmessage()
        assert 'Success!' in confirmcheck.newmessage()



