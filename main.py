from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import argparse
import time
import random
from loguru import logger

def add_zeros_to_left(number, desired_length):
    zeros_to_add = max(0, desired_length - len(str(number)))
    return f"{'0' * zeros_to_add}{str(number)}"

def find_xpath_send(xpath, input_data):
    el = driver.find_element("xpath", xpath)
    el.send_keys(input_data)

def init_var():
    parser = argparse.ArgumentParser()
    parser.add_argument("--account", help="Please input your account")
    parser.add_argument("--password", help="Please input your password")
    parser.add_argument("--second_password", help="Please input your second_password")
    parser.add_argument("--mail", help="Please input your mail")
    parser.add_argument("--amount", help="Please input your amount", type=int)
    parser.add_argument("--start", help="Please input your start", type=int)
    return parser.parse_args()

def open_window():
    service = Service(executable_path=r'./chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--disable-notifications")
    options.add_argument("--window-size=500,1080")
    global driver
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://secretms.com/register")
    
def register(account):
    find_xpath_send('//*[@id="inputUsername"]', account)
    find_xpath_send('//*[@id="inputPassword"]', params.password)
    find_xpath_send('//*[@id="inputCPassword"]', params.password)
    find_xpath_send('//*[@id="inputPin"]', params.second_password)
    find_xpath_send('//*[@id="inputCPin"]', params.second_password)
    find_xpath_send('//*[@id="inputEmail"]', params.mail)
    driver.find_element('id', 'form-register').submit()

if __name__ == "__main__":
    params = init_var()
    for i in range(params.start, params.start+params.amount):
        account = f"{params.account}{add_zeros_to_left(i,3)}"
        logger.info(f"Create Account: {account} / Password: {params.password}")
        open_window()
        register(account)
        driver.quit()

# python .\main.py --account icsd --password cid28787 --second_password 123456 --mail testmail@gmail.com --amount 5 --start 1