from PageObjects.edit_page import EditPage
from DatabaseConnector.database_connection import Database
Query = "SELECT user_id,user_name from customer_id"
actual_id = "65176"


def test_edit(Setup):
    ep = EditPage(Setup)
    db = Database()
    ep.click_edit_link()
    result = db.execute_query(Query)

    ep.set_id(result[0])
    result = ep.get_id()
    assert result == actual_id

    ep.click_submit()

    ep.set_address()

    ep.set_city()

    ep.set_state()

    ep.set_pin()

    ep.set_telephone()

    ep.set_email()

    ep.click_submit_button()

    ep.click_continue_link()

    ep.click_logout_link()


        # ep.edit(result[0])
        # #db.execute_query12("Update new_registration_data SET addr='%s', city='%s', state='%s' pin='%s' mobile_no='%s' email='%s' WHERE user_name =='%s'" %(row[0],row[1],row[2],row[3],row[4],row[5],result[1]))
