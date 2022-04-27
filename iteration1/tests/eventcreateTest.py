from iteration1 import createaccount
from selenium import webdriver
import mysql.connector
from selenium.webdriver.support.ui import Select
import unittest

class Iter1Search(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_successfulregister(self):
        driver = self.driver

        driver.get("http://127.0.0.1:5000/auth/eventcreation")
        user = driver.find_element_by_id("user")
        description = driver.find_element_by_id("description")
        geographiclocation = driver.find_element_by_id("geographiclocation")
        state = driver.find_element_by_id("state")
        eventname = driver.find_element_by_id("eventname")
        eventduration = driver.find_element_by_id("eventduration")
        requireditem = driver.find_element_by_id("required item")
        usertype = Select(driver.find_element_by_id("type"))

        user.send_keys("test3")
        description.send_keys("flood")
        geographiclocation.send_keys("Iowacity")
        state.send_keys("IA")
        eventname.send_keys("Floods")
        eventduration.send_keys("3days")
        requireditem.send_keys("money")
        usertype.select_by_index(0)

        submit = driver.find_element_by_name("submit")
        submit.click()
        mydb = mysql.connector.connect(host="localhost", user="root", password="team06", database="sys")
        cursor = mydb.cursor(buffered=True)
        cursor.execute("DELETE FROM acinfo WHERE userID='test3'")
        mydb.commit()
        self.assertIn("homepage",driver.title)

    def test_useralreadyregistered(self):
        driver = self.driver

        driver.get("http://127.0.0.1:5000/auth/eventcreation")
        user = driver.find_element_by_id("user")
        description = driver.find_element_by_id("description")
        geographiclocation = driver.find_element_by_id("geographiclocation")
        state = driver.find_element_by_id("state")
        eventname = driver.find_element_by_id("eventname")
        eventduration = driver.find_element_by_id("eventduration")
        requireditem = driver.find_element_by_id("required item")
        usertype = Select(driver.find_element_by_id("type"))

        user.send_keys("test3")
        description.send_keys("flood")
        geographiclocation.send_keys("Iowacity")
        state.send_keys("IA")
        eventname.send_keys("")
        eventduration.send_keys("3days")
        requireditem.send_keys("money")
        usertype.select_by_index(0)

        submit = driver.find_element_by_name("submit")
        submit.click()

        self.assertIn("event name missing.",driver.page_source)

    def test_nopasswordmatch(self):
        driver = self.driver

        driver.get("http://127.0.0.1:5000/auth/eventcreation")
        user = driver.find_element_by_id("user")
        description = driver.find_element_by_id("description")
        geographiclocation = driver.find_element_by_id("geographiclocation")
        state = driver.find_element_by_id("state")
        eventname = driver.find_element_by_id("eventname")
        eventduration = driver.find_element_by_id("eventduration")
        requireditem = driver.find_element_by_id("required item")
        usertype = Select(driver.find_element_by_id("type"))

        user.send_keys("test3")
        description.send_keys("flood")
        geographiclocation.send_keys("Iowacity")
        state.send_keys("USA")
        eventname.send_keys("Floods")
        eventduration.send_keys("3days")
        requireditem.send_keys("money")
        usertype.select_by_index(0)

        submit = driver.find_element_by_name("submit")
        submit.click()

        self.assertIn("enter a valid state",driver.page_source)


    def tearDown(self):

        self.driver.close()


if __name__ == "__main__":
    unittest.main()
