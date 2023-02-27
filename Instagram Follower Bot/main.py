
from selenium import webdriver, common

from selenium.webdriver.common.keys import Keys
import time
import math
import threading
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

my_username = "" #enter  your email
my_password = "" # enter your password
similar_account = "fcbayern"

chrome_driver_path = "C:/chromedriver.exe"

#
# # driver.get("https://www.amazon.com.tr")
#
#
#
# class InstaFollower():
#     def __init__(self):
#         self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
#     def login(self):
#         self.driver.get("https://www.instagram.com/")
#         time.sleep(2)
#         self.username = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
#         time.sleep(2)
#         self.username.click()
#         self.username.send_keys(my_username)
#         time.sleep(2)
#         self.password = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
#         self.password.click()
#         self.password.send_keys(my_password)
#         time.sleep(1)
#         self.login_button = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div')
#         self.login_button.click()
#         time.sleep(4)
#         not_now_button = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/section/main/div/div/div/div/button')
#         not_now_button.click()
#         time.sleep(2)
#         no_notification_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
#         no_notification_button.click()
#
#
#     def find_followers(self):
#         search_site= self.driver.find_element_by_xpath('/html/body/div[1]/div/div/section/nav/div[2]/div/div/div[2]/input')
#         time.sleep(1)
#         # search_site.click()
#         search_site.send_keys(similar_account)
#         search_site.send_keys(Keys.ENTER)
#         time.sleep(2)
#
#         search_site.send_keys(Keys.ENTER)
#         time.sleep(1)
#         search_site.send_keys(Keys.ENTER)
#
#
#
#
#     def follow(self):
#         followings = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/section/main/div/header/section/ul/li[3]/a')
#         followings.click()
#         # scr1 = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[3]')
#         #
#         #
#         # self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
#         # following_list = self.driver.find_element_by_class_name('L3NKy')
#
#         for element in range(1,50):
#             time.sleep(1)
#             try:
#                 new_folllow =self.driver.find_element_by_xpath(f'/html/body/div[6]/div/div/div[3]/ul/div/li[{element}]/div/div[2]/button')
#                 print(f'{element}')
#                 time.sleep(1)
#                 new_folllow.click()
#             except common.exceptions.ElementNotInteractableException:
#                 print("Element Not Interactable Exception")
#                 self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]').click()
#             except common.exceptions.NoSuchElementException:
#                 print("No Such Element Exception")
#             finally:
#                 time.sleep(1)
#
#
#
#
#
#
#
#         # print(following_list.text)
#         # following_list.click()
#
#
#
# start = InstaFollower()
# start.login()
# time.sleep(3)
# start.find_followers()
# time.sleep(3)
# start.follow()



class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(my_username)
        password.send_keys(my_password)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{similar_account}")

        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(chrome_driver_path)
bot.login()
bot.find_followers()
bot.follow()
