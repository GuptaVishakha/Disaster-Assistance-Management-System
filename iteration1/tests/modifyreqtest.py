from iteration1 import createrequest
from selenium import webdriver
import mysql.connector
from flask import g
from selenium.webdriver.support.ui import Select
import unittest

class Iter1Search(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_modifysuccess(self):
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

        quant1 = driver.find_element_by_id("Waterquantity")
        quant2 = driver.find_element_by_id("Foodquantity")
        quant3 = driver.find_element_by_id("Clothingquantity")

        desc = driver.find_element_by_id("description")

        event.select_by_index(0)
        box1.click()
        box3.click()
        desc.send_keys("THIS IS A DESCRIPTION FOR THE REQUEST CURRENTLY BEING MADE")

        quant1.send_keys("11")
        quant3.send_keys("5")
        submit = driver.find_element_by_name("submit")
        submit.click()

        driver.get("http://127.0.0.1:5000/home/modify")
        changeitems = driver.find_element_by_link_text("Change Items")
        changeitems.click()

        box1 = driver.find_element_by_id("Water")
        box2 = driver.find_element_by_id("Food")
        box3 = driver.find_element_by_id("Clothing")

        box1.click()
        box2.click()
        box3.click()

        quant1 = driver.find_element_by_id("Waterquantity")
        quant2 = driver.find_element_by_id("Foodquantity")
        quant3 = driver.find_element_by_id("Clothingquantity")

        quant1.clear()
        quant2.send_keys("22")
        quant3.clear()

        submit = driver.find_element_by_name("submit")
        submit.click()
        mydb = mysql.connector.connect(host="localhost", user="root", password="team06", database="sys")
        cursor = mydb.cursor(buffered=True)
        cursor.execute("DELETE FROM requests WHERE description='THIS IS A DESCRIPTION FOR THE REQUEST CURRENTLY BEING MADE'")
        mydb.commit()
        self.assertIn("Request Updated Succesfully",driver.page_source)

    def test_noitems(self):
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
        box1.click()
        box3.click()
        desc.send_keys("THIS IS A DESCRIPTION FOR THE REQUEST CURRENTLY BEING MADE")

        quant1 = driver.find_element_by_id("Waterquantity")
        quant2 = driver.find_element_by_id("Foodquantity")
        quant3 = driver.find_element_by_id("Clothingquantity")
        quant1.send_keys("11")
        quant3.send_keys("5")

        submit = driver.find_element_by_name("submit")
        submit.click()

        driver.get("http://127.0.0.1:5000/home/modify")
        changeitems = driver.find_element_by_link_text("Change Items")
        changeitems.click()

        box1 = driver.find_element_by_id("Water")
        box2 = driver.find_element_by_id("Food")
        box3 = driver.find_element_by_id("Clothing")

        box1.click()
        box3.click()

        quant1 = driver.find_element_by_id("Waterquantity")
        quant2 = driver.find_element_by_id("Foodquantity")
        quant3 = driver.find_element_by_id("Clothingquantity")
        quant1.clear()
        quant3.clear()

        submit = driver.find_element_by_name("submit")
        submit.click()

        mydb = mysql.connector.connect(host="localhost", user="root", password="team06", database="sys")
        cursor = mydb.cursor(buffered=True)
        cursor.execute(
            "DELETE FROM requests WHERE description='THIS IS A DESCRIPTION FOR THE REQUEST CURRENTLY BEING MADE'")
        mydb.commit()

        self.assertIn("No Items Selected", driver.page_source)

    def test_nodelete(self):
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
        box1.click()
        box3.click()
        desc.send_keys("THIS IS A DESCRIPTION FOR THE REQUEST CURRENTLY BEING MADE")

        quant1 = driver.find_element_by_id("Waterquantity")
        quant2 = driver.find_element_by_id("Foodquantity")
        quant3 = driver.find_element_by_id("Clothingquantity")
        quant1.send_keys("11")
        quant3.send_keys("5")

        submit = driver.find_element_by_name("submit")
        submit.click()

        driver.get("http://127.0.0.1:5000/home/modify")
        changeitems = driver.find_element_by_link_text("Delete Request")
        changeitems.click()

        no = driver.find_element_by_id("no")

        no.click()
        mydb = mysql.connector.connect(host="localhost", user="root", password="team06", database="sys")
        cursor = mydb.cursor(buffered=True)
        cursor.execute(
            "DELETE FROM requests WHERE description='THIS IS A DESCRIPTION FOR THE REQUEST CURRENTLY BEING MADE'")
        mydb.commit()
        self.assertIn("Home", driver.title)

    def test_successfuldelete(self):
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
        box1.click()
        box3.click()
        desc.send_keys("THIS IS A DESCRIPTION FOR THE REQUEST CURRENTLY BEING MADE")

        quant1 = driver.find_element_by_id("Waterquantity")
        quant2 = driver.find_element_by_id("Foodquantity")
        quant3 = driver.find_element_by_id("Clothingquantity")
        quant1.send_keys("11")
        quant3.send_keys("5")

        submit = driver.find_element_by_name("submit")
        submit.click()

        driver.get("http://127.0.0.1:5000/home/modify")
        changeitems = driver.find_element_by_link_text("Delete Request")
        changeitems.click()

        no = driver.find_element_by_id("yes")

        no.click()
        mydb = mysql.connector.connect(host="localhost", user="root", password="team06", database="sys")
        cursor = mydb.cursor(buffered=True)
        cursor.execute(
            "DELETE FROM requests WHERE description='THIS IS A DESCRIPTION FOR THE REQUEST CURRENTLY BEING MADE'")
        mydb.commit()
        self.assertIn("Request Deleted Successfully", driver.page_source)


    def tearDown(self):

        self.driver.close()


if __name__ == "__main__":
    unittest.main()