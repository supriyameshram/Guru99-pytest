from selenium.webdriver.common.by import By


class LogoutPage:
    logout_link ="//A[@href='Logout.php'][text()='Log out']"

    def __init__(self, driver):
        self.driver = driver

    def click_logout_link(self):
        self.driver.find_element(By.XPATH, self.click_logout_link()).click()

        try:

            alert = self.driver.switch_to.alert

            assert "You Have Succesfully Logged Out!!" in alert.text

            alert.accept()

        except:

            alert = self.driver.switch_to.alert

            alert.dismiss("///////")

