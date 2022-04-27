from iteration1 import createrequest
from selenium import webdriver
import mysql.connector
from selenium.webdriver.support.ui import Select
import unittest

class Iter1Search(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_successfulrequest(self):
        driver = self.driver

        mydb = mysql.connector.connect(host="localhost", user="root", password="team06", database="sys")
        cursor = mydb.cursor(buffered=True)

        driver.get("http://127.0.0.1:5000/auth/login")
        userbox = driver.find_element_by_id("user")
        passbox = driver.find_element_by_id("password")
        userbox.send_keys("testrec1")
        passbox.send_keys("Testpass123#")
        submit = driver.find_element_by_id("submit")
        submit.click()

        driver.get("http://127.0.0.1:5000/home/request")
        event = Select(driver.find_element_by_id("event"))
        box1 = driver.find_element_by_id("Water")
        box2 = driver.find_element_by_id("Food")
        box3 = driver.find_element_by_id("Clothing")
        desc = driver.find_element_by_id("description")

        quant1 = driver.find_element_by_id("Waterquantity")
        quant2 = driver.find_element_by_id("Foodquantity")
        quant3 = driver.find_element_by_id("Clothingquantity")
        event.select_by_index(0)
        box1.click()
        box2.click()
        box3.click()
        quant1.send_keys("11")
        quant2.send_keys("22")
        quant3.send_keys("5")
        desc.send_keys("THIS IS A DESCRIPTION FOR THE REQUEST CURRENTLY BEING MADE")

        submit = driver.find_element_by_name("submit")
        submit.click()
        cursor.execute("DELETE FROM requests WHERE username = 'testrec'")
        mydb.commit()
        self.assertIn("Request Created Successfully",driver.page_source)

    def test_missingdesc(self):
        driver = self.driver

        driver.get("http://127.0.0.1:5000/auth/login")
        userbox = driver.find_element_by_id("user")
        passbox = driver.find_element_by_id("password")
        userbox.send_keys("testrec")
        passbox.send_keys("Testpass123#")
        submit = driver.find_element_by_id("submit")
        submit.click()

        driver.get("http://127.0.0.1:5000/home/request")
        event = Select(driver.find_element_by_id("event"))
        box1 = driver.find_element_by_id("Water")
        box2 = driver.find_element_by_id("Food")
        box3 = driver.find_element_by_id("Clothing")
        desc = driver.find_element_by_id("description")

        quant1 = driver.find_element_by_id("Waterquantity")
        quant2 = driver.find_element_by_id("Foodquantity")
        quant3 = driver.find_element_by_id("Clothingquantity")

        event.select_by_index(0)
        box1.click()
        box2.click()
        box3.click()

        quant1.send_keys("11")
        quant2.send_keys("22")
        quant3.send_keys("5")

        submit = driver.find_element_by_name("submit")
        submit.click()

        self.assertIn("Create Request", driver.title)

    def test_nobox(self):
        driver = self.driver

        driver.get("http://127.0.0.1:5000/auth/login")
        userbox = driver.find_element_by_id("user")
        passbox = driver.find_element_by_id("password")
        userbox.send_keys("testrec")
        passbox.send_keys("Testpass123#")
        submit = driver.find_element_by_id("submit")
        submit.click()

        driver.get("http://127.0.0.1:5000/home/request")

        event = Select(driver.find_element_by_id("event"))
        box1 = driver.find_element_by_id("Water")
        box2 = driver.find_element_by_id("Food")
        box3 = driver.find_element_by_id("Clothing")
        desc = driver.find_element_by_id("description")

        event.select_by_index(0)
        desc.send_keys("THIS IS A DESCRIPTION FOR THE REQUEST CURRENTLY BEING MADE")

        submit = driver.find_element_by_name("submit")
        submit.click()

        self.assertIn("No Items Selected", driver.page_source)

    def test_alreadyrequested(self):
        driver = self.driver

        driver.get("http://127.0.0.1:5000/auth/login")
        userbox = driver.find_element_by_id("user")
        passbox = driver.find_element_by_id("password")
        userbox.send_keys("testrec")
        passbox.send_keys("Testpass123#")
        submit = driver.find_element_by_id("submit")
        submit.click()

        driver.get("http://127.0.0.1:5000/home/request")
        event = Select(driver.find_element_by_id("event"))
        box1 = driver.find_element_by_id("Water")
        box2 = driver.find_element_by_id("Food")
        box3 = driver.find_element_by_id("Clothing")
        desc = driver.find_element_by_id("description")

        quant1 = driver.find_element_by_id("Waterquantity")
        quant2 = driver.find_element_by_id("Foodquantity")
        quant3 = driver.find_element_by_id("Clothingquantity")

        event.select_by_index(0)
        box1.click()
        box2.click()
        box3.click()
        desc.send_keys("THIS IS NOT A DESCRIPTION FOR THE REQUEST CURRENTLY BEING MADE (ALREADY REQUESTED)")

        submit = driver.find_element_by_name("submit")
        submit.click()

        driver.get("http://127.0.0.1:5000/home/request")
        event = Select(driver.find_element_by_id("event"))
        box1 = driver.find_element_by_id("Water")
        box2 = driver.find_element_by_id("Food")
        box3 = driver.find_element_by_id("Clothing")
        desc = driver.find_element_by_id("description")
        quant1 = driver.find_element_by_id("Waterquantity")
        quant2 = driver.find_element_by_id("Foodquantity")
        quant3 = driver.find_element_by_id("Clothingquantity")

        event.select_by_index(0)
        box1.click()
        box2.click()
        box3.click()

        quant1.send_keys("11")
        quant2.send_keys("22")
        quant3.send_keys("5")

        desc.send_keys("THIS IS NOT A DESCRIPTION FOR THE REQUEST CURRENTLY BEING MADE (ALREADY REQUESTED)")

        submit = driver.find_element_by_name("submit")
        submit.click()

        mydb = mysql.connector.connect(host="localhost", user="root", password="team06", database="sys")
        cursor = mydb.cursor(buffered=True)
        cursor.execute("DELETE FROM requests WHERE username = 'testrec'")
        mydb.commit()
        self.assertIn("User has already made a request", driver.page_source)


    def tearDown(self):

        self.driver.close()


if __name__ == "__main__":
    unittest.main()