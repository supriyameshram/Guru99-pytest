from DatabaseConnector.database_connection import Database
from PageObjects.delete_page import DeletePage
Query = "SELECT user_id from customer_id"
Query1 = "DELETE FROM customer_id WHERE user_id = %d"
Query2 = "DELETE FROM add_newaccount WHERE cust_id = %d"
actual_id = "50883"


def test_delete(Setup):
        dp = DeletePage(Setup)
        db = Database()
        result = db.execute_query(Query)
        dp.click_delete_link()

        dp.set_id(result[0])
        expected = dp.get_id()
        assert expected == actual_id

        db.execute_query12(Query1 % (result[0]))
        db.execute_query12(Query2 % (result[0]))
        dp.set_submit_button()
        dp.click_logout_link()
        # assert "Do you really want to delete this customer?" in dp.driver.title
        # print("Customer Deleted Successfully!!")






