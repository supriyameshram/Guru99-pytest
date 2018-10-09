import pytest
from selenium import webdriver


def pytest_addoption(parser):

   parser.addoption("--driver", action="store", default="chrome", help="Type in browser type")
   parser.addoption("--url", action="store", default="http://demo.guru99.com/v4/", help="url")
   parser.addoption("--username", action="store", default="mgr123", help="username")
   parser.addoption("--password", action="store", default="mgr!23", help="password")


@pytest.fixture(scope="module", autouse=True)
def driver(request):
   browser = request.config.getoption("--driver")
   if browser == 'chrome':
       browser = webdriver.Chrome("C:\\Users\supriya_meshram\PycharmProjects\Guru99-pytest\chromedriver.exe")
       browser.get("about:blank")
       browser.implicitly_wait(10)
       browser.maximize_window()
       return browser
   else:
       print('only chrome is supported at the moment')


@pytest.fixture(scope="module")
def username(request):
   return request.config.getoption("--username")


@pytest.fixture(scope="module")
def password(request):
   return request.config.getoption("--password")


@pytest.fixture(scope="module")
def url(request):
   return request.config.getoption("--url")

"""import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
baseURL = "http://demo.guru99.com/v4/"

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome("C:\\Users\supriya_meshram\PycharmProjects\Guru99-pytest\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseURL)

    emailField = driver.find_element(By.NAME, "uid")
    emailField.send_keys("mgr123")

    passwordField = driver.find_element(By.NAME, "password")
    passwordField.send_keys("mgr!23")

    loginButton = driver.find_element(By.NAME, "btnLogin")
    loginButton.click()

    assert "Guru99 Bank Manager HomePage" in driver.title
    print("Login Successful")

    yield driver
    driver.close()"""




