from selenium.webdriver.common.by import By


class ConfirmCheck():

    Countrylist= (By.ID, "country")

    def __init__(self,driver):
        self.driver = driver

    def checkconfirm(self,text):
        return self.driver.find_element(*ConfirmCheck.Countrylist).send_keys(text)

    def checkbox(self):
        return self.driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()

    def finalconfirm(self):
        return self.driver.find_element(By.CSS_SELECTOR,"input[class*='btn-lg']").click()

    def newmessage(self):
        message = self.driver.find_element(By.CSS_SELECTOR,"div[class*='alert']").text
        return message

