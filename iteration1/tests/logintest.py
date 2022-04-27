from iteration1 import loginauth
from selenium import webdriver
import mysql.connector
from flask import g
from selenium.webdriver.support.ui import Select
import unittest

class Iter1Search(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_loginsuccess(self):
        driver = self.driver

        driver.get("http://127.0.0.1:5000/auth/login")
        userbox = driver.find_element_by_id("user")
        passbox = driver.find_element_by_id("password")
        userbox.send_keys("testrec")
        passbox.send_keys("Testpass123#")
        submit = driver.find_element_by_id("submit")
        submit.click()
        self.assertIn("Home", driver.title)
    def test_loginuserfail(self):
        driver = self.driver

        driver.get("http://127.0.0.1:5000/auth/login")
        userbox = driver.find_element_by_id("user")
        passbox = driver.find_element_by_id("password")
        userbox.send_keys("testrec222")
        passbox.send_keys("Testpass123#")
        submit = driver.find_element_by_id("submit")
        submit.click()
        self.assertIn("Incorrect username", driver.page_source)

    def test_loginpassfail(self):
        driver = self.driver

        driver.get("http://127.0.0.1:5000/auth/login")
        userbox = driver.find_element_by_id("user")
        passbox = driver.find_element_by_id("password")
        userbox.send_keys("testrec")
        passbox.send_keys("Testpass12345#")
        submit = driver.find_element_by_id("submit")
        submit.click()
        self.assertIn("Incorrect password", driver.page_source)
