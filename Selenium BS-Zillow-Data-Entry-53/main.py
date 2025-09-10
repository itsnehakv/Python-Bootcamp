import requests
import time
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
load_dotenv()

header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.3",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}

zillow_web=requests.get("https://appbrewery.github.io/Zillow-Clone/",headers=header)
zillow_web_text=zillow_web.text

soup=BeautifulSoup(zillow_web_text,"html.parser")

link_div=soup.find_all("div", class_="StyledPropertyCardDataWrapper")

property_links=[div.find(name="a").get("href") for div in link_div]
print(property_links)

property_addresses=[address.text.strip("\n ").replace("|","") for address in soup.select("li div div article div div a address")]
print(property_addresses)

property_prices=[price.text.strip("+/mobd 1") for price in soup.find_all(name="span",class_="PropertyCardWrapper__StyledPriceLine")]
print(property_prices)

chromeoption=webdriver.ChromeOptions()
chromeoption.add_experimental_option("detach",True)
driver=webdriver.Chrome(chromeoption)

wait = WebDriverWait(driver, 5)  # Waits up to 10 seconds


def FormFilling():
    for listing in range(0,len(property_links)):
        driver.get(os.environ["GOOGLE_FORM_LINK"])

        time.sleep(2)

        address_entry=wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")))
        address_entry.send_keys(property_addresses[listing])

        price_entry=driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        price_entry.send_keys(property_prices[listing])

        link_entry=driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
        link_entry.send_keys(property_links[listing])

        submit_button=driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div")
        submit_button.click()
        time.sleep(1)


FormFilling()
