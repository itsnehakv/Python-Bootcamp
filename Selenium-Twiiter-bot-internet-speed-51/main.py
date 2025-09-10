from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v137.fetch import continue_request
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time
import os
from dotenv import load_dotenv
load_dotenv()

email=os.environ["TWITTER_EMAIL"]
password=os.environ["TWITTER_PASSWORD"]
PROMISED_DOWNLOAD=150
PROMISED_UPLOAD=10
#150Mbps download, 10Mbps upload.

chromeoption=webdriver.ChromeOptions()
chromeoption.add_experimental_option("detach", True)

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver=webdriver.Chrome(chromeoption)
        self.wait = WebDriverWait(self.driver, 2)  # wait for 2 secs for page load
        self.down=0
        self.up=0

    # def driver(self):
    #     chromeoption = webdriver.ChromeOptions()
    #     chromeoption.add_experimental_option("detach",True)
    #     user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
    #     chromeoption.add_argument(f"--user-data-dir={user_data_dir}")
    #     driver = webdriver.Chrome(options=chromeoption)
    #     return driver

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        continue_button=self.driver.find_element(By.XPATH,"//*[@id='onetrust-accept-btn-handler']")
        continue_button.click()
        go_button=self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()
        time.sleep(45)
        self.up=self.driver.find_element(By.XPATH, "//*[@id='container']/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        self.down=self.driver.find_element(By.XPATH, "//*[@id='container']/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(3)
        email_entry= self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div/div[4]/label/div/div[2]/div/input")
        email_entry.click()
        email_entry.send_keys(email)
        next_button=self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div/button[2]")
        next_button.click()
        password_entry=self.wait.until(ec.presence_of_element_located((By.XPATH,"//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input")))
        password_entry.send_keys(password)
        login_button=self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/button")
        login_button.click()


        tweet_compose=self.wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div")))
        tweet=f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWNLOAD}down/{PROMISED_UPLOAD}up?"
        tweet_compose.send_keys(tweet)

        post_button=self.driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button")
        post_button.click()
        time.sleep(3)
        # self.driver.quit()


bot=InternetSpeedTwitterBot()
# bot.get_internet_speed()
bot.tweet_at_provider()