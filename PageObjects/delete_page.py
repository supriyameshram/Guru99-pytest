from selenium.webdriver.common.by import By


class DeletePage():

    delete_link_text = 'Delete Customer'
    cust_id = '//INPUT[@type="text"]'
    submit_button = '//INPUT[@type="submit"]'
    logout_link = '//A[@href="Logout.php"][text()="Log out"]'

    def __init__(self, driver):
        self.driver = driver

    def click_delete_link(self):
        self.driver.find_element(By.LINK_TEXT, self.delete_link_text).click()

    def set_id(self, value):
        name = self.driver.find_element(By.XPATH, self.cust_id)
        name.clear()
        name.send_keys(value)

    def get_id(self):
        driver = self.driver.find_element(By.XPATH,self.cust_id)
        element = driver.find_element(By.XPATH,self.cust_id)
        return element.get_attribute("value")

    def set_submit_button(self):
        submit1 = self.driver.find_element(By.XPATH, self.submit_button)
        submit1.click()

        try:

            alert = self.driver.switch_to.alert

            assert "Do you really want to delete this customer?"

            print("Customer Deleted Successfully!")

            alert.accept()

        except:

            alert = self.driver.switch_to.alert

            alert.dismiss("///////")

    def click_logout_link(self):

        logout_link1 = self.driver.find_element(By.LINK_TEXT, self.logout_link)
        logout_link1.click()

        try:

            alert = self.driver.switch_to.alert

            assert "You Have Succesfully Logged Out!!" in alert.text

            alert.accept()

        except:

            alert = self.driver.switch_to.alert

            alert.dismiss("///////")










