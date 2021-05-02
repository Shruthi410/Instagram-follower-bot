from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

CHROME_DRIVER_PATH = "C:/Development/chromedriver.exe"
SIMILAR_ACCOUNT = "chefsteps"
USERNAME = "shruthi41098"
PASSWORD = "Shruthiinsta123"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(3)
        self.email = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.email.send_keys(USERNAME)
        self.password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        self.password.send_keys(PASSWORD)
        self.password.send_keys(Keys.ENTER)

    def find_followers(self):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        self.following = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        self.following.click()
        sleep(2)
        self.scroll = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(20):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.scroll)

    def follow(self):
        follow_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in follow_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()