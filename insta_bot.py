"""
An Instagram bot written in Python using Selenium on Google Chrome. 
It will go through posts in hashtag(s) and like and comment on them, and then it will follow the author of the post.
"""

# Generic Imports
from time import sleep
import logging
import sys
from random import randint

# Library Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Own modules
from credentials import *
from config import *

logging.basicConfig(format='%(levelname)s [%(asctime)s] %(message)s', datefmt='%m/%d/%Y %r', level=logging.INFO)
logger = logging.getLogger()

def initialize_browser():

    # Do this so we don't get DevTools and Default Adapter failure
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # Initialize chrome driver and set chrome as our browser
    browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)

    return browser


def login_to_instagram(browser):
    browser.get('https://www.instagram.com/')
        
    sleep(2)
    
    # cookie 
    cookie_button = browser.find_element_by_xpath("/html/body/div[4]/div/div/button[1]")
    cookie_button.click()

    # Get the login elements and type in your credentials
    browser.implicitly_wait(10)
    username = browser.find_element_by_name('username')
    username.send_keys(USERNAME)
    browser.implicitly_wait(10)
    password = browser.find_element_by_name('password')
    password.send_keys(PASSWORD)

    sleep(2)

    # Click the login button
    browser.implicitly_wait(10)
    browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click()

    # If login information is incorrect, program will stop running
    browser.implicitly_wait(10)
    try:
        if browser.find_element_by_xpath("//*[@id='slfErrorAlert']"):
            browser.close()
            sys.exit('Error: Login information is incorrect')
        else:
            pass
    except:
        pass

    browser.implicitly_wait(10)
    
    logger.info(f'Logged in to {USERNAME}')

    # Save your login info? Not now
    browser.implicitly_wait(20)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]')))

    # Turn on notifications? Not now
    browser.implicitly_wait(20)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

def automate_instagram(browser):
    # Keep track of how many you like and comment
    likes = 0
    comments = 0
    follows = 0

    for hashtag in hashtag_list:
        browser.implicitly_wait(30)
        browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        logger.info(f'Exploring #{hashtag}')
        sleep(randint(1,2))

        # Click first thumbnail to open
        browser.implicitly_wait(30)
        first_thumbnail = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]")
        first_thumbnail.click()

        sleep(randint(1,2))

        # Go through x number of photos per hashtag
        for post in range(1,number_of_posts):

            try:
                
                # Follow
                browser.implicitly_wait(30)
                if browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                    browser.find_element_by_xpath("/html/body/div[6]/div[2]/div/article/header/div[2]/div[1]/div[2]/button").click()            
                logger.info("Followed")
                follows += 1
                
                # Like
                browser.find_element_by_xpath('//*[@aria-label="Like"]').click()
                logger.info("Liked")
                likes += 1
                
                sleep(randint(2,4))

                # Comment
                try:
                    browser.implicitly_wait(30)
                    browser.find_element_by_class_name('Ypffh').click()
                    # Random chance of commenting
                    do_i_comment = randint(1,chance_to_comment)
                    if do_i_comment == 1:

                            browser.implicitly_wait(30)
                            comment = browser.find_element_by_class_name('Ypffh')
                            comment.click()

                            sleep(wait_to_comment)

                            rand_comment_index = randint(0,len(comments_list))
                            post = comments_list[rand_comment_index]
                            comment.send_keys(post)
                            comment.send_keys(Keys.ENTER)
                            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))).click() # TEST
                            logger.info(f"Commented '{post}'")
                            comments += 1
                            sleep(wait_between_posts)


### OTHER OPTION
#                # Comment
#                try:
#                    do_i_comment = randint(1,chance_to_comment)
#                    if do_i_comment == 1:
#                        comment = browser.find_element_by_xpath("//div/form[*[local-name()='textarea']]")
#                        comment.click()                        
#                            
#                        comment = browser.find_element_by_tag_name('textarea')
#
#                        rand_comment_index = randint(0,len(comments_list))
#                        post = comments_list[rand_comment_index]
#                        #sleep(wait_to_comment)
#                        comment.send_keys(post)
#                          
#                        browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div[3]/section[3]/div/form/button[2]').click()
#                        logger.info(f"Commented '{post}'")
#                        comments += 1
#                        sleep(wait_between_posts)
#                        
#                except Exception:
#                    #Continue to next post if comments section is limited or turned off
#                    pass


                except Exception:
                    # Continue to next post if comments section is limited or turned off
                    pass

            except Exception:
                # Already liked it, continue to next post
                logger.info('Already liked this photo previously')
                pass
            
            # Go to next post
            browser.implicitly_wait(30)
            browser.find_element_by_link_text('Next').click()
            logger.info('Getting next post')
            sleep(wait_between_posts)    

    logger.info(f'Followed {follows} accounts')
    logger.info(f'Liked {likes} posts')
    logger.info(f'Commented on {comments} posts')

    # Close browser when done
    logger.info('Closing chrome browser...')
    browser.close()

if __name__ == "__main__":
    browser = initialize_browser()
    login_to_instagram(browser)
    automate_instagram(browser)