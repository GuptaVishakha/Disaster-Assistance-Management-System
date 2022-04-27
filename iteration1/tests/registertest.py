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

        driver.get("http://127.0.0.1:5000/auth/register")
        user = driver.find_element_by_id("user")
        password = driver.find_element_by_id("password")
        confirmpassword = driver.find_element_by_id("confirmpass")
        birthdate = driver.find_element_by_id("birthdate")
        address = driver.find_element_by_id("address")
        city = driver.find_element_by_id("city")
        state = driver.find_element_by_id("state")
        zip = driver.find_element_by_id("zip")
        usertype = Select(driver.find_element_by_id("type"))

        user.send_keys("test3")
        password.send_keys("&Test123")
        confirmpassword.send_keys("&Test123")
        birthdate.send_keys("11/11/1111")
        address.send_keys("123 Test St.")
        city.send_keys("Iowa City")
        state.send_keys("IA")
        zip.send_keys("52241")
        usertype.select_by_index(0)

        submit = driver.find_element_by_name("submit")
        submit.click()
        mydb = mysql.connector.connect(host="localhost", user="root", password="team06", database="sys")
        cursor = mydb.cursor(buffered=True)
        cursor.execute("DELETE FROM acinfo WHERE userID='test3'")
        mydb.commit()
        self.assertIn("Login",driver.title)

    def test_useralreadyregistered(self):
        driver = self.driver

        driver.get("http://127.0.0.1:5000/auth/register")
        user = driver.find_element_by_id("user")
        password = driver.find_element_by_id("password")
        confirmpassword = driver.find_element_by_id("confirmpass")
        birthdate = driver.find_element_by_id("birthdate")
        address = driver.find_element_by_id("address")
        city = driver.find_element_by_id("city")
        state = driver.find_element_by_id("state")
        zip = driver.find_element_by_id("zip")
        usertype = Select(driver.find_element_by_id("type"))

        user.send_keys("sliebermann")
        password.send_keys("&Test123")
        confirmpassword.send_keys("&Test123")
        birthdate.send_keys("11/11/1111")
        address.send_keys("123 Test St.")
        city.send_keys("Iowa City")
        state.send_keys("IA")
        zip.send_keys("52241")
        usertype.select_by_index(0)

        submit = driver.find_element_by_name("submit")
        submit.click()

        self.assertIn("User is already registered.",driver.page_source)

    def test_nopasswordmatch(self):
        driver = self.driver

        driver.get("http://127.0.0.1:5000/auth/register")
        user = driver.find_element_by_id("user")
        password = driver.find_element_by_id("password")
        confirmpassword = driver.find_element_by_id("confirmpass")
        birthdate = driver.find_element_by_id("birthdate")
        address = driver.find_element_by_id("address")
        city = driver.find_element_by_id("city")
        state = driver.find_element_by_id("state")
        zip = driver.find_element_by_id("zip")
        usertype = Select(driver.find_element_by_id("type"))

        user.send_keys("test")
        password.send_keys("&Test123")
        confirmpassword.send_keys("#Team06776")
        birthdate.send_keys("11/11/1111")
        address.send_keys("123 Test St.")
        city.send_keys("Iowa City")
        state.send_keys("IA")
        zip.send_keys("52241")
        usertype.select_by_index(0)

        submit = driver.find_element_by_name("submit")
        submit.click()

        self.assertIn("Passwords do not match",driver.page_source)

    def test_missinginfo(self):
        driver = self.driver

        driver.get("http://127.0.0.1:5000/auth/register")
        user = driver.find_element_by_id("user")

        user.send_keys("test4")
        submit = driver.find_element_by_name("submit")
        submit.click()
        self.assertIn("Create an Account",driver.title)

    def test_backtologin(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/auth/register")

        login = driver.find_element_by_link_text("Return to Login")
        login.click()
        self.assertIn("Login",driver.title)

    def tearDown(self):

        self.driver.close()


if __name__ == "__main__":
    unittest.main()