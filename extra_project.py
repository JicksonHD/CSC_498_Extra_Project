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

# Replace the element selector below with the actual element containing course details
course_list = soup.select("ELEMENT_SELECTOR")

with open("course_offerings.csv", mode="w", newline="") as csv_file:
    fieldnames = ["Time", "Instructor Name", "Remaining Seats"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    
    for course in course_list:
        # Replace the placeholder with the actual element containing course data
        time = course.select_one("ELEMENT_SELECTOR_FOR_TIME").text
        instructor = course.select_one("ELEMENT_SELECTOR_FOR_INSTRUCTOR").text
        remaining_seats = course.select_one("ELEMENT_SELECTOR_FOR_REMAINING_SEATS").text
        
        writer.writerow({"Time": time, "Instructor Name": instructor, "Remaining Seats": remaining_seats})

driver.quit()
