import PageObjects.Register as tests
from DatabaseConnector.database_connection import Database


Query = "SELECT user_name, dob, addr, city, state, pin, mobile_no, email, password FROM new_registration_data"
Query1 = "INSERT INTO customer_id(user_id, user_name) VALUES(%d,'%s')"
Query2 = "INSERT INTO add_newaccount(cust_id,initial_deposit) VALUES(%d,'10000')"
db = Database()
row = db.execute_query(Query)

actual_name, actual_gender,  actual_dob,  actual_address, actual_city, actual_state, actual_pin, actual_telephone, actual_email , actual_password = "rukhu","f", '2016-12-20', "IT park parodi",'nagpur', 'maharashtra',  '765432',  '9790876754','samp123@gmail.com',  'asdfg'


def test_open_url(driver, url):
   tests.open_url(driver, url)


# Test step 2 - Add credentials
def test_add_credentials1(driver, username, password):
   tests.add_credentials1(driver, username, password)


# Test step 3 - Submit form
def test_submit_form1(driver):
   tests.submit_form1(driver)


def test_open_link(driver):
    tests.open_link(driver)


def test_add_credentials(driver):
    tests.add_credentials(driver, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])


def test_submit_form(driver):
    tests.submit_form(driver)


def test_get_id(driver):
    id = tests.get_id(driver)
    db.execute_query12(Query1 % (int(id), row[0]))
    db.execute_query12(Query2 % (int(id)))


def test_click_continue_link(driver):
    tests.click_continue_link(driver)


def test_click_logout_link(driver):
    tests.click_logout_link(driver)

