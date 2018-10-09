from selenium.webdriver.common.by import By


class EditPage:
    edit_link = "//A[@href='EditCustomer.php'][text()='Edit Customer']"
    name = "//INPUT[@name='cusid']"
    submit = "//INPUT[@name='AccSubmit']"
    addr1 = "//TEXTAREA[@name='addr']"
    city1 = "//INPUT[@name='city']"
    state1 = "//INPUT[@name='state']"
    pin1 = "//INPUT[@name='pinno']"
    no = "//INPUT[@name='telephoneno']"
    email = "//INPUT[@name='emailid']"
    submit1 = "//INPUT[@name='sub']"
    continue_link = "//A[@href='Managerhomepage.php'][text()='Continue']"
    logout_link = "//A[@href='Logout.php'][text()='Log out']"

    def __init__(self, driver):
        self.driver = driver

    def click_edit_link(self):
        self.driver.find_element(By.XPATH, self.edit_link).click()

    def set_id(self, value):
        name = self.driver.find_element(By.XPATH,self.name)
        name.clear()
        name.send_keys(value)

    def get_id(self):
        driver = self.driver.find_element(By.XPATH, self.name)
        element = driver.find_element(By.XPATH, self.name)
        return element.get_attribute("value")

    def click_submit(self):
         self.driver.find_element(By.XPATH, self.submit).click()

    def set_address(self):
        addr1 = self.driver.find_element(By.XPATH, self.addr1)
        addr1.clear()
        addr1.send_keys("abc xyz")

    def get_address(self):
        driver = self.driver.find_element(By.XPATH, self.addr1)
        element = driver.find_element(By.XPATH, self.addr1)
        return element.get_attribute("value")

    def set_city(self):
        city = self.driver.find_element(By.XPATH, self.city1)
        city.clear()
        city.send_keys("pune")

    def get_city(self):
        driver = self.driver.find_element(By.XPATH, self.city1)
        element = driver.find_element(By.XPATH, self.city1)
        return element.get_attribute("value")

    def set_state(self):
        state = self.driver.find_element(By.XPATH, self.state1)
        state.clear()
        state.send_keys("Tamilnadu")

    def get_state(self):
        driver = self.driver.find_element(By.XPATH, self.state1)
        element = driver.find_element(By.XPATH, self.state1)
        return element.get_attribute("value")

    def set_pin(self):
        pin_no = self.driver.find_element(By.XPATH, self.pin1)
        pin_no.clear()
        pin_no.send_keys("345672")

    def get_pin(self):
        driver = self.driver.find_element(By.XPATH, self.pin1)
        element = driver.find_element(By.XPATH, self.pin1)
        return element.get_attribute("value")

    def set_telephone(self):
        mobile_no = self.driver.find_element(By.XPATH, self.no)
        mobile_no.clear()
        mobile_no.send_keys("7456209069")

    def get_telephone(self):
        driver = self.driver.find_element(By.XPATH, self.no)
        element = driver.find_element(By.XPATH, self.no)
        return element.get_attribute("value")

    def set_email(self):
        email1 = self.driver.find_element(By.XPATH, self.email)
        email1.clear()
        email1.send_keys("mnbvcfghkl@gmail.com")

    def get_email(self):
        driver = self.driver.find_element(By.XPATH, self.email)
        element = driver.find_element(By.XPATH, self.email)
        return element.get_attribute("value")

    def click_submit_button(self):
        self.driver.find_element(By.XPATH, self.submit1).click()

        assert "Guru99 Bank Customer Registration Page" in self.driver.title

        print("Customer information updated successfully!!!")

    def click_continue_link(self):

        self.driver.find_element(By.XPATH, self.continue_link).click()

    def click_logout_link(self):
        self.driver.find_element(By.XPATH, self.logout_link).click()




