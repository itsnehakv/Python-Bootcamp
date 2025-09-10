from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)  #w/o this, the amazon window shuts almost immediately, it is like getch()

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

price_whole=driver.find_element(By.CLASS_NAME,"a-price-whole").text   #it is an html element w/o ".text"
print(price_whole)

'''
--ATTRIBUTES--
**price_whole.get_attribute("ATTRIBUTE NAME") -->gives specified attribute value
**price_whole.tag_name() --->gives the tag name like h3, input, p
**button.size -->give dimensions of selected button element as dict

--XPATH--
**through_x_path=driver.find_element(By.XPATH, value="//*[@id="video-title"]/yt-formatted-string") 
To get xpath. Right click on req. ele.-->Copy-->Copy XPath 
XPath is like a file path. Hierarchy. Order.

--CSS SELECTOR--
**link=driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a")
Here, .documentation-widget is class name of a div elemenet. Anchor tag "a" is 
present inside that div. We have selected the anchor tag 
'''

driver.quit()

'''----EXTRA (Related to the Tinder project Day 50)-----
Sample:
fb_login = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
This is part types of XPath syntax's
** //* — look anywhere in the document.
** [@id="modal-manager"] — select the element with ID modal-manager.

**--In Selenium, each window has a identification handle, we can get all the window handles with:
--> driver.window_handles
The above line of code returns a list of all the window handles. The first window is at position 0 

-->fb_login_window = driver.window_handles[1]
We can switch our Selenium to target the new facebook login window by:
driver.switch_to.window(fb_login_window)
You can print the driver.title to verify that it's the facebook login window that is currently target:
-->print(driver.title)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
'''