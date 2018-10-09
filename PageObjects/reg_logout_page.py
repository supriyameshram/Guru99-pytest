from selenium.webdriver.common.by import By


class LogoutPage():


    def __init__(self, driver):
        self.driver = driver

    def click_continue_link(self,):

        link1 = self.driver.find_element(By.XPATH, self.continue_link)
        link1.click()

    def click_logout_link(self):

        link2 = self.driver.find_element(By.XPATH, self.logout_link)
        link2.click()

        try:

            alert = self.driver.switch_to.alert

            assert "You Have Succesfully Logged Out!!" in alert.text

            alert.accept()
        except:

            alert = self.driver.switch_to.alert

            alert.dismiss("///////")

