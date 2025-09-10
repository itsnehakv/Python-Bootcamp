'''
**Click on the big cookie
**When items in the store get unlocked, pick the most expensive aka more profitable one
**The id of each store item is "product0"..."product1"...so on
**Program runs for 5 mins
**At each 5 sec interval in runtime, check the items that are enabled [give by product unlock enabled]
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep, time

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)  #w/o this, the amazon window shuts almost immediately, it is like getch()

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")
driver.maximize_window()

sleep(3) #for page to load

wait_time=5
check_time=time()+wait_time # 5 secs
run_time=time()+60*5 # 5 mins

big_cookie=driver.find_element(By.ID,value="bigCookie")

while True:
    big_cookie.click()
    if time()>check_time:
        try:
            upgrades = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")
            most_expensive_upgrades_index = len(upgrades) - 1
            most_expensive_upgrade = driver.find_element(By.ID, value=f"product{most_expensive_upgrades_index}")
            most_expensive_upgrade.click()

        except (ValueError):
            print("Couldn't find cookie count or items")

        check_time = time() + wait_time  #reset timer 5 secs

        if time() > run_time:
                try:
                    no_of_cookies = driver.find_element(by=By.ID, value="cookies")
                    print(f"Final result: { no_of_cookies.text}")
                except ValueError:
                    print("Couldn't get final cookie count")
                break

'''
------Angela SOLUTION-----

 try:
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            cookie_text = cookies_element.text
            cookie_count = int(cookie_text.split()[0].replace(",", ""))    #-->get cookie number value

            # Find all available products in the store
            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")

            # Find the most expensive item we can afford
            best_item = None
            for product in reversed(products):  # Start from most expensive (bottom of list)
                # Check if item is available and affordable (enabled class)
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            # Buy the best item if found
            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
            print("Couldn't find cookie count or items")'''