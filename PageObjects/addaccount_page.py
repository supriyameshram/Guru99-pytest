from selenium.webdriver.common.by import By


class AddAccountPage:

    add_account_link = "//A[@href='addAccount.php'][text()='New Account']"
    cus_id = "//INPUT[@name='cusid']"
    account = "//SELECT[@name='selaccount']/option[1]"
    deposit = "//INPUT[@name='inideposit']"
    submit_button = "//INPUT[@type='submit']"
    id = ".//*[@id='account']/tbody/tr[4]/td[2]"
    continue_link = "//A[@href='Managerhomepage.php'][text()='Continue']"

    def __init__(self, driver):
        self.driver = driver

    def click_account_link(self):
        self.driver.find_element(By.XPATH, self.add_account_link).click()

    def set_id(self, value):
        name = self.driver.find_element(By.XPATH, self.cus_id)
        name.clear()
        name.send_keys(value)

    def get_id(self):
        driver = self.driver.find_element(By.XPATH, self.cus_id)
        element = driver.find_element(By.XPATH, self.cus_id)
        return element.get_attribute("value")

    def set_account(self):
        self.driver.find_element(By.XPATH, self.account).click()

    def get_account(self):
        driver = self.driver.find_element(By.XPATH, self.account)
        element = driver.find_element(By.XPATH, self.account)
        return element.get_attribute("value")

    def set_deposit(self, value):
        deposit1 = self.driver.find_element(By.XPATH, self.deposit)
        deposit1.clear()
        deposit1.send_keys(value)

    def get_deposit(self):
        driver = self.driver.find_element(By.XPATH, self.deposit)
        element = driver.find_element(By.XPATH, self.deposit)
        return element.get_attribute("value")

    def click_submit_button(self):
        self.driver.find_element(By.XPATH, self.submit_button).click()

    def click_continue_link(self):
        self.driver.find_element(By.XPATH, self.continue_link).click()

    def get_id1(self):
        id1 = self.driver.find_element(By.XPATH, self.id)
        return id1







