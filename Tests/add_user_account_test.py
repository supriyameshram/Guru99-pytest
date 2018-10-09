from DatabaseConnector.database_connection import Database
from PageObjects.addaccount_page import AddAccountPage
Query = "SELECT cust_id, initial_deposit from add_newaccount"
Query1 = "INSERT INTO add_account(accn_id, cust_id) VALUES(%d,%d)"
actual_id, actual_deposit = "2216","10000"


def test_addaccount(Setup):
        ad = AddAccountPage(Setup)
        db = Database()
        ad.click_account_link()
        row = db.execute_query(Query)

        ad.set_id(row[0])
        result = ad.get_id()
        assert result == actual_id

        ad.set_account()

        ad.set_deposit(row[1])
        result = ad.get_deposit()
        assert result == actual_deposit

        ad.click_submit_button()

        acc_id = ad.get_id1()

        db.execute_query12(Query1 % (int(acc_id), row[0]))

        assert "Gtpl Bank Customer Registration Page" in ad.driver.title
        print("Account Generated Successfully!!!")






