import xlrd
import PageObjects.Register as tests


actual_name , actual_gender,  actual_dob,  actual_address, actual_city, actual_state, actual_pin, actual_telephone, actual_email , actual_password = "rukhu","f", "2016-12-20", "IT park parodi",'nagpur', 'maharashtra',  '765432',  '9790876754','samp@gmail.com',  'asdfg'
loc = "C:\\Users\\supriya_meshram\\PycharmProjects\\Guru99-pytest\\registration_excel.xlsx"
workbook = xlrd.open_workbook(loc)
sheet = workbook.sheet_by_name("Sheet1")
rowcount = sheet.nrows
colcount = sheet.ncols
print(rowcount)
print(colcount)


def test_open_link(driver):
    tests.open_link(driver)


def test_add_credentials(driver):
    for i in range(1, rowcount):
        row = sheet.row_slice(i)
        print(row[14].value)
        print(row[16].value)
        tests.add_credentials(driver, row[0].value, row[2].value, row[4].value, row[6].value, row[8].value, int(row[10].value), int(row[12].value), row[14].value, row[17].value)


def test_submit_form(driver):
    tests.submit_form(driver)


def test_click_continue_link(driver):
    tests.click_continue_link(driver)


def test_click_logout_link(driver):
    tests.click_logout_link(driver)






