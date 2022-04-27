from iteration1 import createrequest
from selenium import webdriver
import mysql.connector
from selenium.webdriver.support.ui import Select
import unittest

class Iter1Search(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_successfulmatch(self):
        driver = self.driver

        mydb = mysql.connector.connect(host="localhost", user="root", password="team06", database="sys")
        cursor = mydb.cursor(buffered=True)

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
        desc.send_keys("THIS IS A DESCRIPTION FOR THE REQUEST CURRENTLY BEING MADE")

        submit = driver.find_element_by_name("submit")
        submit.click()

        driver.get("http://127.0.0.1:5000/auth/login")
        userbox = driver.find_element_by_id("user")
        passbox = driver.find_element_by_id("password")
        userbox.send_keys("mchr3")
        passbox.send_keys("Team06!66")
        submit = driver.find_element_by_id("submit")
        submit.click()

        driver.get("http://127.0.0.1:5000/home/response")
        name = driver.find_element_by_id("Name")
        event = Select(driver.find_element_by_id("event"))
        box1 = driver.find_element_by_id("Water")
        box2 = driver.find_element_by_id("Food")
        box3 = driver.find_element_by_id("Clothing")
        box4 = driver.find_element_by_id("Money")
        desc = driver.find_element_by_id("description")
        quant1 = driver.find_element_by_id("Waterquantity")
        quant2 = driver.find_element_by_id("Foodquantity")
        quant3 = driver.find_element_by_id("Clothingquantity")
        quant4 = driver.find_element_by_id("Moneyquantity")
        event.select_by_index(0)
        box1.click()
        box2.click()
        box3.click()
        box4.click()
        quant1.send_keys("11")
        quant2.send_keys("22")
        quant3.send_keys("5")
        quant4.send_keys("3")
        desc.send_keys("THIS IS A DESCRIPTION FOR THE REQUEST CURRENTLY BEING MADE")
        name.send_keys("JOHN SMITH")

        submit = driver.find_element_by_name("submit")
        submit.click()

        driver.get("http://127.0.0.1:5000/auth/login")
        userbox = driver.find_element_by_id("user")
        passbox = driver.find_element_by_id("password")
        userbox.send_keys("damsadmin")
        passbox.send_keys("Team06##")
        submit = driver.find_element_by_id("submit")
        submit.click()

        driver.get("http://127.0.0.1:5000/home/match")


        reqbutton = driver.find_element_by_id("testrecreq")
        reqbutton.click()

        resbutton = driver.find_element_by_id("mchr3res")
        resbutton.click()

        submit = driver.find_element_by_id("yes")
        submit.click()


        cursor.execute("DELETE FROM requests WHERE username = 'testrec'")
        mydb.commit()
        self.assertIn("Match made successfully",driver.page_source)


    def test_noresponse(self):
        driver = self.driver

        mydb = mysql.connector.connect(host="localhost", user="root", password="team06", database="sys")
        cursor = mydb.cursor(buffered=True)

        driver.get("http://127.0.0.1:5000/auth/login")
        userbox = driver.find_element_by_id("user")
        passbox = driver.find_element_by_id("password")
        userbox.send_keys("testrec2")
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

        driver.get("http://127.0.0.1:5000/auth/login")
        userbox = driver.find_element_by_id("user")
        passbox = driver.find_element_by_id("password")
        userbox.send_keys("mchr3")
        passbox.send_keys("Team06!66")
        submit = driver.find_element_by_id("submit")
        submit.click()

        driver.get("http://127.0.0.1:5000/home/response")
        name = driver.find_element_by_id("Name")
        event = Select(driver.find_element_by_id("event"))
        box1 = driver.find_element_by_id("Water")
        box2 = driver.find_element_by_id("Food")
        box3 = driver.find_element_by_id("Clothing")
        box4 = driver.find_element_by_id("Money")
        desc = driver.find_element_by_id("description")
        quant1 = driver.find_element_by_id("Waterquantity")
        quant2 = driver.find_element_by_id("Foodquantity")
        quant3 = driver.find_element_by_id("Clothingquantity")
        quant4 = driver.find_element_by_id("Moneyquantity")
        event.select_by_index(0)
        box1.click()
        box2.click()
        box3.click()
        box4.click()
        quant1.send_keys("11")
        quant2.send_keys("22")
        quant3.send_keys("5")
        quant4.send_keys("3")
        desc.send_keys("THIS IS A DESCRIPTION FOR THE REQUEST CURRENTLY BEING MADE")
        name.send_keys("JOHN SMITH")

        submit = driver.find_element_by_name("submit")
        submit.click()

        driver.get("http://127.0.0.1:5000/auth/login")
        userbox = driver.find_element_by_id("user")
        passbox = driver.find_element_by_id("password")
        userbox.send_keys("damsadmin")
        passbox.send_keys("Team06##")
        submit = driver.find_element_by_id("submit")
        submit.click()

        driver.get("http://127.0.0.1:5000/home/match")

        reqbutton = driver.find_element_by_id("testrec2req")

        resbutton = driver.find_element_by_id("mchr3res")
        resbutton.click()

        submit = driver.find_element_by_id("yes")
        submit.click()

        cursor.execute("DELETE FROM requests WHERE username = 'testrec2'")
        mydb.commit()
        cursor.execute("DELETE FROM response WHERE username = 'mchr3'")
        mydb.commit()

        self.assertIn("Manual Match", driver.page_source)


    def test_norequest(self):
        driver = self.driver

        mydb = mysql.connector.connect(host="localhost", user="root", password="team06", database="sys")
        cursor = mydb.cursor(buffered=True)

        driver.get("http://127.0.0.1:5000/auth/login")
        userbox = driver.find_element_by_id("user")
        passbox = driver.find_element_by_id("password")
        userbox.send_keys("testrec3")
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

        driver.get("http://127.0.0.1:5000/auth/login")
        userbox = driver.find_element_by_id("user")
        passbox = driver.find_element_by_id("password")
        userbox.send_keys("mchr3")
        passbox.send_keys("Team06!66")
        submit = driver.find_element_by_id("submit")
        submit.click()

        driver.get("http://127.0.0.1:5000/home/response")
        name = driver.find_element_by_id("Name")
        event = Select(driver.find_element_by_id("event"))
        box1 = driver.find_element_by_id("Water")
        box2 = driver.find_element_by_id("Food")
        box3 = driver.find_element_by_id("Clothing")
        box4 = driver.find_element_by_id("Money")
        desc = driver.find_element_by_id("description")
        quant1 = driver.find_element_by_id("Waterquantity")
        quant2 = driver.find_element_by_id("Foodquantity")
        quant3 = driver.find_element_by_id("Clothingquantity")
        quant4 = driver.find_element_by_id("Moneyquantity")
        event.select_by_index(0)
        box1.click()
        box2.click()
        box3.click()
        box4.click()
        quant1.send_keys("11")
        quant2.send_keys("22")
        quant3.send_keys("5")
        quant4.send_keys("3")
        desc.send_keys("THIS IS A DESCRIPTION FOR THE REQUEST CURRENTLY BEING MADE")
        name.send_keys("JOHN SMITH")

        submit = driver.find_element_by_name("submit")
        submit.click()

        driver.get("http://127.0.0.1:5000/auth/login")
        userbox = driver.find_element_by_id("user")
        passbox = driver.find_element_by_id("password")
        userbox.send_keys("damsadmin")
        passbox.send_keys("Team06##")
        submit = driver.find_element_by_id("submit")
        submit.click()

        driver.get("http://127.0.0.1:5000/home/match")

        reqbutton = driver.find_element_by_id("testrec3req")
        reqbutton.click()
        resbutton = driver.find_element_by_id("mchr3res")


        submit = driver.find_element_by_id("yes")
        submit.click()

        cursor.execute("DELETE FROM requests WHERE username = 'testrec3'")
        mydb.commit()
        cursor.execute("DELETE FROM response WHERE username = 'mchr3'")
        mydb.commit()
        self.assertIn("Manual Match", driver.page_source)

    def test_cancelmatch(self):
        driver = self.driver

        mydb = mysql.connector.connect(host="localhost", user="root", password="team06", database="sys")
        cursor = mydb.cursor(buffered=True)

        driver.get("http://127.0.0.1:5000/auth/login")
        userbox = driver.find_element_by_id("user")
        passbox = driver.find_element_by_id("password")
        userbox.send_keys("damsadmin")
        passbox.send_keys("Team06##")
        submit = driver.find_element_by_id("submit")
        submit.click()

        driver.get("http://127.0.0.1:5000/home/match")

        backbutton = driver.find_element_by_id("home")
        backbutton.click()

        self.assertIn("Home", driver.title)

def tearDown(self):

        self.driver.close()


if __name__ == "__main__":
    unittest.main()