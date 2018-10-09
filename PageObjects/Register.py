from selenium.webdriver.common.by import By

user_name1 = '//INPUT[@name="uid"]'
password1 = '//INPUT[@name="password"]'
Button = '//INPUT[@name="btnLogin"]'
register_link = '//A[@href="addcustomerpage.php"][text()="New Customer"]'
user_name = '(//INPUT[@type="text"])[1]'
gender_xpath = '(//INPUT[@type="radio"])[2]'
dob_xpath = '(//INPUT[@id="dob"])'
addr_name = '(//TEXTAREA[@rows="5"])'
city_name = '(//INPUT[@type="text"])[2]'
state_name = '(//INPUT[@type="text"])[3]'
pin_name = '(//INPUT[@type="text"])[4]'
telephone_name = '(//INPUT[@type="text"])[5]'
email_name = '(//INPUT[@type="text"])[6]'
pass_name = '//INPUT[@type="password"]'
submit = '//INPUT[@type="submit"]'
id_xpath = './/*[@id="customer"]/tbody/tr[4]/td[2]'
continue_link = "//A[@href='Managerhomepage.php'][text()='Continue']"
logout_link = "//A[@href='Logout.php'][text()='Log out']"

def open_url(driver, url):
   driver.get(url)


def add_field1(driver, value, field):
   username_field = driver.find_element(By.XPATH, field)
   username_field.clear()
   username_field.send_keys(value)


def add_credentials1(driver, username, password):
   add_field1(driver, username, user_name1)
   add_field1(driver, password, password1)


def submit_form1(driver):
   driver.find_element(By.XPATH, Button).click()


def open_link(driver):
   driver.find_element(By.XPATH, register_link).click()


def add_field(driver, value, field):
   username_field = driver.find_element(By.XPATH, field)
   username_field.send_keys(value)


def add_credentials(driver, username, dob, addr, city, state, pin, telephone, email, password):
   add_field(driver, username, user_name)
   driver.find_element(By.XPATH, gender_xpath).click()
   add_field(driver, dob, dob_xpath)
   add_field(driver, addr, addr_name)
   add_field(driver, city, city_name)
   add_field(driver, state, state_name)
   add_field(driver, pin, pin_name)
   add_field(driver, telephone, telephone_name)
   add_field(driver, email, email_name)
   add_field(driver,password, pass_name)


def submit_form(driver):
   driver.find_element(By.XPATH, submit).click()


def get_id(driver):
    id1 = driver.find_element(By.XPATH, id_xpath).text
    return id1


def click_continue_link(driver):
    driver.find_element(By.XPATH, continue_link).click()


def click_logout_link(driver):
    driver.find_element(By.XPATH, logout_link).click()

    try:
        alert = driver.switch_to.alert

        assert "You Have Succesfully Logged Out!!" in alert.text

        alert.accept()

    except:

        alert = driver.switch_to.alert

        alert.dismiss("///////")


# def verify_url(driver, url):
#    assert (url + expected_url) == driver.current_url
