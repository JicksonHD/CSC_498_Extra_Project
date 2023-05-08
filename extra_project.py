import sys
import requests
from bs4 import BeautifulSoup
import csv
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


username = sys.argv[1]
password = sys.argv[2]

LOGIN_URL = "https://myportal.lau.edu.lb/Pages/studentPortal.aspx"
COURSE_URL = "https://myportal.lau.edu.lb/path/to/course/offering/page"

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get(LOGIN_URL)

username_input = driver.find_element_by_name("username")
username_input.send_keys(username)

password_input = driver.find_element_by_name("password")
password_input.send_keys(password)

password_input.send_keys(Keys.RETURN)

driver.get(COURSE_URL)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")