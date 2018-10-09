from selenium.webdriver.common.by import By


class EditPage():

    def __init__(self, driver):
        self.driver = driver

    def edit(self,cus):
        editLink = self.driver.find_element(By.LINK_TEXT, "Edit Account")
        editLink.click()

        acc_no = self.driver.find_element(By.NAME,"accountno")
        acc_no.send_keys(cus)

        submitButton = self.driver.find_element(By.NAME, "AccSubmit")
        submitButton.click()

        assert "Guru99 Bank Customer Registration Page" in self.driver.title

        print("Customer information updated successfully!!!")

        self.driver.find_element(By.XPATH, ".//*[@id='customer']/tbody/tr[14]/td/a").click()




