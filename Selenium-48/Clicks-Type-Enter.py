from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)  #w/o this, the amazon window shuts almost immediately, it is like getch()

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

'''
The HTML file changes when it is windowed, the name 'search' 
is hidden and the search bar is just a magnifying glass 🔎.
'''
driver.maximize_window()

# abc=driver.find_element(By.CLASS_NAME, value="extiw")
# abc.click()

# click_link=driver.find_element(By.CLASS_NAME, value="vector-icon mw-ui-icon-search mw-ui-icon-wikimedia-search")
# click_link.click()

search_bar=driver.find_element(By.NAME, value="search")
search_bar.send_keys("Python", Keys.ENTER)




