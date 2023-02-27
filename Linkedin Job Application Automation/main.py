from selenium import webdriver
import time
import math
import threading
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException

my_username = "" #enter  you email
my_password = "" # enter your password


chrome_driver_path = "" #your path to local chrome driver

driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.get("https://www.amazon.com.tr")

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

log_in = driver.find_element_by_xpath("/html/body/div[1]/header/nav/div/a[2]")
log_in.click()

username = driver.find_element_by_id("username")
username.send_keys(my_username)
password = driver.find_element_by_id("password")
password.send_keys(my_password)
driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button').click()

time.sleep(3)
search_jobs = driver.find_elements_by_class_name("jobs-search-results__list")
print(search_jobs[0].text)
search_job = driver.find_elements_by_id("jx34fOeSUHKxdrkVDuS/wA==")

ease_apply = driver.find_element_by_class_name("jobs-apply-button--top-card")
ease_apply.click()

next_button = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button')
next_button.click()
time.sleep(1)
review_button = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button[2]')
review_button.click()

time.sleep(1)
submit_button = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div[2]/footer/div[3]/button[2]')
submit_button.click()













