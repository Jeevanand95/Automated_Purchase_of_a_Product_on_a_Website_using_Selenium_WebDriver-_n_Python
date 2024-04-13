from selenium.webdriver.common.by import By


class Homepage():

    shop_click = (By.XPATH, "//li[2]/a")
    names = (By.NAME,"name")
    emails = (By.NAME,"email")
    passwords = (By.ID,"exampleInputPassword1")
    checkboxes = (By.ID,"exampleCheck1")
    dates = (By.NAME,"bday")
    confirmclicked = (By.CSS_SELECTOR,"input[class*='btn']")

    def __init__(self,driver):
        self.driver=driver

    def gethomepage(self):
        return self.driver.find_element(*Homepage.shop_click)

    def namefield(self):
        return self.driver.find_element(*Homepage.names)

    def emailfield(self):
        return self.driver.find_element(*Homepage.emails)

    def passwordfield(self):
        return self.driver.find_element(*Homepage.passwords)

    def checkboxfield(self):
        return self.driver.find_element(*Homepage.checkboxes)

    def datefield(self):
        return self.driver.find_element(*Homepage.dates)

    def confirmclick(self):
        return self.driver.find_element(*Homepage.confirmclicked)







