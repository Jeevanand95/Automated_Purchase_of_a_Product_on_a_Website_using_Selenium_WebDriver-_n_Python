from selenium.webdriver.common.by import By


class CheckoutPage():

    listofnames = (By.XPATH, "//div[@class='card h-100']")
    product_name= (By.XPATH,"div/h4/a")
    addcartxpath=(By.XPATH, "//a[@class='nav-link btn btn-primary']")
    checkoutbutton = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self,driver):
        self.driver=driver

    def checkoutpage(self):
        list_names = self.driver.find_elements(*CheckoutPage.listofnames)
        return list_names
    def addcart(self):
        return self.driver.find_element(*CheckoutPage.addcartxpath)

    def checkoutclick(self):
        return self.driver.find_element(*CheckoutPage.checkoutbutton)