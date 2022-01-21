#!/usr/bin/python

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains




driver = webdriver.Chrome()

driver.get('https://www.kucoin.com/')

#click login button
driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[4]/a[1]/div').click()


#enter your email and password here 
email_add =("")
password = ("")

# enter email
email = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div[3]/form/div[1]/div[1]/input')
email.send_keys(email_add)



#enter pass 
pas = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div[3]/form/div[2]/div[1]/input')
pas.send_keys(password)

#click login
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div[3]/form/button/span[1]').click()


input("Pass captcha and 2fa, Then press Enter to continue...")
print("Proceeding....")

def createbot() : 

    driver.get('https://www.kucoin.com/trading-bot')


    time.sleep(3)
    #click best preforming spot grid bot
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/ul/li[1]/div/div[1]').click()
    time.sleep(4)
    #click create
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[3]/div/button/span[1]').click()

    time.sleep(4)

    #Move value to 100%
    slider = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[2]/div/div[2]/div[3]/form/div[2]/div[6]/div/div[2]/span');
    move = ActionChains(driver)
    move.click_and_hold(slider).move_by_offset(190, 100).release().perform()

    #Click create bot
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[2]/div/div[2]/div[3]/form/div[2]/div[9]/button/span[1]').click()
    time.sleep(4)
    #Confirm
    driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[3]/div/div[8]/button/span[1]').click()

    print("Bot created!")

    time.sleep(4)
    time.sleep(4)
    
def killbot() :

    while(True):

        element = 0

        element = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[4]/div[1]/div[2]/div/span').text    
        element = element.rstrip("%")
        element = float(element)
        # change this value if you want profit to be taken at an amount other than 1%
        if element >= +1.0:
            print('Green!')
            #shutdownbutton
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/span/span').click()
            time.sleep(1)
            #usdt
            driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[3]/div/ul/li[3]/div/div/div[1]').click()
            time.sleep(1)
            #kill it! 
            driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[3]/div/div[4]/button/span[1]').click()
            #dasitmane! 
            break
        else:
            time.sleep(3)
            print("current: ", element)
        # change this value if you want losses to be taken at an amount other than -4.5%    
        if element < -4.5:
            print('You are fucked boi time to sell')
            #shutdownbutton
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/span/span').click()
            time.sleep(1)
            #usdt
            driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[3]/div/ul/li[3]/div/div/div[1]').click()
            time.sleep(1)
            #kill it! 
            driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[3]/div/div[4]/button/span[1]').click()

            break
           
            
wins = float(0)
losses = float(0)            

while(True):
    createbot()
    killbot()














  







