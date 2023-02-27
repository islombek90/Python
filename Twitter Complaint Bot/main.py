from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


import math
import threading
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException

my_username = "" # your username
my_password = "" # your password

PROMISED_DOWN = 150
PRMOISED_UP = 10

chrome_driver_path = "your local path to/chromedriver.exe"


caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  # Don't wait for page to fully load



class InternetSpeedTwitterBot():
    def __init__(self):
        self.upolad_speed = 0
        self.dowloand_speed = 0
        self.driver = webdriver.Chrome(desired_capabilities=caps,
                          executable_path=chrome_driver_path)

    def speed_test(self):
        self.speed_site = self.driver.get("https://www.speedtest.net/#")
        time.sleep(3)
        start=self.driver.find_element_by_class_name('start-button')
        print(start.text)

        start.click()
        time.sleep(60)
        download = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        print(download.text)
        self.download_speed= float(download.text)
        upload = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        print(upload.text)
        self.upload_speed = float(upload.text)


    def tweet_at_provider(self):
        #if  self.upolad_speed < PRMOISED_UP  or  self.dowloand_speed < PROMISED_DOWN:
            self.twitter =self.driver.get("https://twitter.com/?lang=tr")
            time.sleep(4)
            login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[5]/a')
            login.click()

            time.sleep(5)
            username = self.driver.find_element_by_css_selector('input')
            username.click()
            username.send_keys(my_username)
            time.sleep(2)
            next = self.driver.find_element_by_class_name('r-1pz39u2')
            next.click()

            time.sleep(3)
            password = self.driver.find_element_by_css_selector('input')
            password.click()
            password.send_keys(my_password)
            sign_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[3]/div/div')
            sign_in.click()

            time.sleep(3)
            post_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
            post_input.send_keys("Hello i am bot and this a test")
            post_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div')
            post_button.click()








complain = InternetSpeedTwitterBot()
#complain.speed_test()
complain.tweet_at_provider()

