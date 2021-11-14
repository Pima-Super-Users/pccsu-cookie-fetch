from selenium import webdriver
import csv
import time
import re
import config

def exportAsCSV(cookies):
    data_header = ['name', 'value']
    with open('data.csv', 'w') as file_writer:
        dict_writer = csv.DictWriter(file_writer, data_header)
        dict_writer.writeheader()
        for data in cookies:
            dict_writer.writerow(data)


def newMain():
    print(config.cookiesNeeded[3])

def main():
    browser = webdriver.Chrome('chromedriver.exe') #Download this seperately
    url = "https://pima.campuslabs.com/engage/" #URL
    browser.get(url)
    print("Going to URL...")
    time.sleep(5)
    print("Going to sign-in page")
    newurl= "https://pima.campuslabs.com/engage/account/login?returnUrl=%%2Fengage%%2F"
    browser.get(newurl)
    time.sleep(5)
    username = browser.find_element_by_name("j_username") #Username form name
    password = browser.find_element_by_name("j_password") #Password form name
    username.send_keys(config.USERNAME) #Username
    password.send_keys(config.PASSWORD) #Checks every password
    button = browser.find_element_by_name("_eventId_proceed") #Change to name of submit button
    button.click()
    print("Logging in... {0}".format(config.USERNAME))
    time.sleep(5)
    cookies = []
    if browser.current_url == 'https://pima.campuslabs.com/engage/': ##Change to redirect URL when a successful login attempt is made, or make it NOT the current
        for x in range(len(config.cookiesNeeded)):
            cookie = browser.get_cookie(config.cookiesNeeded[x])
            tempCookies = {'name' : config.cookiesNeeded[x], 'value' :  cookie.get('value')}
            cookies.append(tempCookies)
    print(cookies)
    exportAsCSV(cookies)


if __name__ == "__main__":
    main()