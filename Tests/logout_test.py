from PageObjects.delete_page import DeletePage
from PageObjects.reg_logout_page import LogoutPage


class TestDelete:

    def test_logout(self, Setup):
        lp = LogoutPage(Setup)
        lp.logout_link()

