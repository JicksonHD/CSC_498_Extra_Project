import os
import sys
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

username = sys.argv[1]
password = sys.argv[2]

print(username)
print(password)

LOGIN_URL = "https://myportal.lau.edu.lb/"
TARGET_URL = "https://banweb.lau.edu.lb/prod/bwckschd.p_get_crse_unsec"

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get(LOGIN_URL)

username_input = driver.find_element(By.NAME, "username")
username_input.send_keys(username)

password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(password)

login_button = driver.find_element(By.XPATH, "//input[@type='submit']")
login_button.click()

my_courses = driver.find_element(By.XPATH, '//*[@id="zz4_TopNavigationMenuV4"]/div/ul/li/ul/li[3]/a')
my_courses.click()

course_offerings = driver.find_element(By.XPATH, '//*[@id="cbqwpctl00_m_g_df4e4cc9_291f_48af_90eb_524811091537"]/div/div[2]/a[4]')
course_offerings.click()

driver.get("https://banweb.lau.edu.lb/prod/bwckschd.p_disp_dyn_sched")

select_element = driver.find_element(By.XPATH, '//*[@id="term_input_id"]')
select = Select(select_element)
select.select_by_value("202410")

submit_button = driver.find_element(By.XPATH, "/html/body/div[3]/form/input[2]")
submit_button.click()

subject_element = driver.find_element(By.XPATH, '//*[@id="subj_id"]')
select = Select(subject_element)
select.select_by_value("CSC")

campus_element = driver.find_element(By.XPATH, '//*[@id="camp_id"]')
select = Select(campus_element)
select.select_by_value("2")

course_offerings = driver.find_element(By.XPATH, '/html/body/div[3]/form/input[12]')
course_offerings.click()

elements = driver.find_elements(By.CSS_SELECTOR, ".ddtitle > a")
names = [element.text for element in elements]

elements = driver.find_elements(By.CSS_SELECTOR, "tr > .dddefault:nth-child(7)")
instructors = [element.text for element in elements]

elements = driver.find_elements(By.CSS_SELECTOR, "tr > .dddefault:nth-child(2)")
times = [element.text for element in elements]

elements = driver.find_elements(By.CSS_SELECTOR, "tr > .dddefault:nth-child(3)")
days = [element.text for element in elements]

elements = driver.find_elements(By.CSS_SELECTOR, "tr > .dddefault:nth-child(4)")
locations = [element.text for element in elements]

data = list(zip(names, instructors, locations, times, days))

# Set the file path for the CSV file
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'course_data.csv')

# Create a new CSV file and write the data to it
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Instructor", "Location", "Time", "Day"])
    writer.writerows(data)

print(f"CSV file saved at {file_path}")

driver.quit()