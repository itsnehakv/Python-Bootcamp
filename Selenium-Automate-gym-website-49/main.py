import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import os
from dotenv import load_dotenv
load_dotenv()

#----Configuring Chrome to launch with a persistent user profile (chrome_profile folder)---
chromeoption=webdriver.ChromeOptions()
chromeoption.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chromeoption.add_argument(f"--user-data-dir={user_data_dir}")

'''
#1
**os.getcwd() - returns the current working directory
**"chrome_profile - folder name
**os.path.join(...) - safely combines path components, in a way that works across different OS's
  It creates a full path to the "chrome_profile" folder inside the current working directory.'''
'''
#2
---tells Chrome to use a specific user data directory.---
** .add_argument()  - adds a command-line argument to the Chrome launch.
** --user-data-dir - Tells Chrome to use a specific folder to store its user profile data (like login sessions)
** {user_data_dir} will be replaced by the actual path (like C:/Projects/MyApp/chrome_profile).
'''

#----Launching Chrome----
driver=webdriver.Chrome(chromeoption)
driver.get(os.environ["GYM_URL"])
driver.maximize_window()
wait = WebDriverWait(driver, 2)  # wait for 2 secs for page load

#------Wrapper function to keep retrying in case of Network failure (for login page)------
def retry(func, retries=7, description=None):  # Wrapper func - takes another function as an argument, adds extra functionality
    for attempt in range(retries):
        try:
            result=func()
            print(f"\nSuccess at accessing {description} page on attempt #{attempt + 1}\n")
            return result
        except TimeoutException:
            print(f"Failure at accessing {description} page on attempt #{attempt + 1}")

        time.sleep(1)

    raise Exception(f"Accessing {description} page failed after multiple retries.")


#------Function to get through Login page------
def login():
    login_button=wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()

    ''''ensures a web element is both visible and enabled before attempting to interact with it, particularly for clicking.
    The method element_to_be_clickable() expects a single argument: a locator tuple. Therefore the "two" parenthesis
     --> func((tuple)) '''

    email_entry=wait.until(ec.presence_of_element_located((By.ID, "email-input")))
    email_entry.clear()
    email_entry.send_keys(os.environ["ACCOUNT_EMAIL"])

    password_entry=driver.find_element(By.NAME, value="password")
    password_entry.clear()
    password_entry.send_keys(os.environ["ACCOUNT_PASSWORD"])

    submit=driver.find_element(By.ID, value="submit-button")
    submit.click()

    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))  #wait for the page after login to load


retry(func=login, description="Login")


# Function to book a class process that checks if the button text changed with retry
def book_class(booking_button):
    booking_button.click()
    # Wait for button state to change - will time out if booking failed
    wait.until(lambda d: booking_button.text == "Booked")


# -----Counters for script activity-----
booking_stats={
"CLASSES_BOOKED": 0,
"WAITLISTS_JOINED": 0,
"ALREADY_BOOKED_WAITLIST" : 0,
"TOTAL_CLASSES" : 0
}


#------Function for Booking Gym Classes-------
def booking_classes():

    class_cards=driver.find_elements(By.CSS_SELECTOR, value="div[id^='class-card']"  )

    for card in class_cards:
        day_group=card.find_element(By.XPATH, value="./ancestor::div[contains(@id, 'day-group-')]")
        #used to traverse upwards from a given element to find the nearest ancestor <div> whose id contains "day-group-"
        day_title=day_group.find_element(By.TAG_NAME, value="h2")
        day_title_name=day_title.text #Mon, Sep 8    Mon, Sep 8     Tue, Sep 9    (for each class)
        if 'Tue' in day_title_name or 'Thu' in day_title_name:
            class_time=card.find_element(By.CSS_SELECTOR, value="p[id^='class-time-']").text

            if '6:00 PM' in class_time:
                class_name=card.find_element(By.CSS_SELECTOR, value="h3[id^='class-name-']").text

                book_button=card.find_element(By.CSS_SELECTOR, value="button[id^='book-button-']")
                if 'Book Class' in book_button.text:
                    retry(lambda: book_class(book_button), description="Booking")
                    print(f"Booked: {class_name} for {day_title_name}")
                    booking_stats["CLASSES_BOOKED"]+=1

                elif 'Booked' in book_button.text:
                    print(f"Already booked: {class_name} on {day_title_name}")
                    booking_stats["ALREADY_BOOKED_WAITLIST"]+=1

                elif 'Join Waitlist' in book_button.text:
                    retry(lambda: book_class(book_button), description="Booking")
                    print(f"Joined a waitlist: {class_name} on {day_title_name}")
                    booking_stats["WAITLISTS_JOINED"]+=1

                elif 'Waitlisted' in book_button.text:
                    print(f"Already waitlisted: {class_name} on {day_title_name}")
                    booking_stats["ALREADY_BOOKED_WAITLIST"]+=1

                booking_stats["TOTAL_CLASSES"]=booking_stats["CLASSES_BOOKED"]+booking_stats["ALREADY_BOOKED_WAITLIST"]+booking_stats["WAITLISTS_JOINED"]
        time.sleep(0.5)

retry(booking_classes, description="Class Bookings")


#----Summary for the booking activity-----
print(f"\n---BOOKING SUMMARY---\nClasses booked: {booking_stats["CLASSES_BOOKED"]}\nWaitlists joined: {booking_stats["WAITLISTS_JOINED"]}\n"
      f"Already booked/waitlisted: {booking_stats["ALREADY_BOOKED_WAITLIST"]}\n"
      f"Total Tuesday/Thursday 6 pm classes processed: {booking_stats["TOTAL_CLASSES"]}\n")


# print("\n\n--- DETAILED CLASS LIST ---\n")
# if CLASSES_BOOKED>0:
#     print(f"[New Booking] {class_name} on {day_title_name}")
# if WAITLISTS_JOINED>0:
#     print(f"[New Waitlist] {class_name} on {day_title_name}\n")



#------Going to "My Bookings" and verifying the bookings-----
def get_my_bookings():
    my_bookings=wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,"a[id='my-bookings-link']")))
    my_bookings.click()

    wait.until(ec.presence_of_element_located((By.ID, 'my-bookings-page')))    #***********
    time.sleep(2)


    cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")  #*= -->Select any element whose id attribute contains the substring anywhere in it.

    if not cards:
        raise TimeoutException("No bookings found - page may not have been loaded")

    return cards

all_my_bookings_cards=retry(get_my_bookings, description="My Bookings")

verified_count=0

#-----Verifying the booked and waitlisted classes------
for card in all_my_bookings_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")   #***********
        when_text = when_paragraph.text

        if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f"✓ Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        # Skip if no "When:" text found (not a booking card)
        pass

print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {booking_stats["TOTAL_CLASSES"]} bookings")
print(f"Found: {verified_count} bookings")
if booking_stats["TOTAL_CLASSES"] != verified_count:
    print(f"❌ Mismatch: Missing {booking_stats["TOTAL_CLASSES"]-verified_count}")
else:
    print("✅ SUCCESS: All bookings verified!")

#     no_of_booked_classes=len(booked_classes)
    #     waitlisted_classes=driver.find_elements(By.CSS_SELECTOR, "div[id^='waitlist-card-waitlist']")
    #     no_of_waitlisted_classes=len(waitlisted_classes)
    #
    # print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")
    # for booked in booked_classes:
    #     booked_class_name=booked.find_element(By.CSS_SELECTOR, "h3[id^='booking-class-name").text
    #     print(f"Verified: {booked_class_name}")
    # # print("\n")
    #
    # for waitlist in waitlisted_classes:
    #     waitlisted_class_name =waitlist.find_element(By.CSS_SELECTOR, "h3[id^='waitlist-class-name").text
    #     print(f"Verified: {waitlisted_class_name}")
    # print("\n")
'''
ERRORS I ENCOUNTERED
** E. bot wasn't considering the Tuesday classes. Why?
** A. Because even tho i gave "book_button.click()" i didn't give it enough 
      time to actually confirm that it did indeed get booked.
      The lambda function inside "book_class()" ensures this. 
      
NEW TOPICS I LEARNED
** use of [id*=]
** use of [id^=]
** use of .//<tag-name>[....]
** use of lambda function
** use of expected_conditions in Selenium
'''

'''
-----.//p[strong[text()='When:']]------
This is part types of XPath syntax's
** .//p[...] --> From the current element, find all <p> elements at any depth (.//) that satisfy the condition inside the brackets [...].”
** The . at the start means “relative to the current element” (not the root).
** //p means look for <p> tags anywhere beneath the current node.

-------presence_of_element_located---------

**element_to_be_clickable confirms the presence of an element, that does not guarantee:
     it's fully rendered or if it's visible and interactive. So we use time.sleep() for extra reinforcement
     
     
     
'''







