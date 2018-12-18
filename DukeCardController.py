import urls
import currency
from selenium import webdriver
from seleniumrequests import Firefox
import requests
import time
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options

class DukeCardController:
    def __init__(self):
        options = Options()
        options.set_headless(True)
        self.driver = Firefox(options=options)

    def login(self, user, pw):
        # navigate to login
        self.driver.get(urls.LOGIN)

        # fields
        username = self.driver.find_element_by_id("j_username")
        password = self.driver.find_element_by_id("j_password")

        username.send_keys(user)
        password.send_keys(pw)

        # submit login credentials - assume MFA is done, or won't work
        submitButton = self.driver.find_element_by_id("Submit") 
        submitButton.click()

    def add_balance(self, currency_type, amount):
        self.driver.get(urls.ADD_BALANCE_GET)
        self.driver.implicitly_wait(20)
        # wait for whole page to load
        time.sleep(3)
        
        # grab page html
        html = self.driver.execute_script("return document.body.innerHTML")
        soup = BeautifulSoup(html, 'html.parser')

        # parse required tokens
        ev = soup.find(id="__EVENTVALIDATION").get('value')
        vsg = soup.find(id="__VIEWSTATEGENERATOR").get('value')
        vs = soup.find(id="__VIEWSTATE").get('value')

        str_amt = str(amount)
        tender = "FLEX" if currency_type == currency.Currency.FLEX else "FOOD"

        return self.driver.request('POST', urls.ADD_BALANCE_POST, data={
            "__VIEWSTATE": vs,
            "__VIEWSTATEGENERATOR": vsg,
            "__EVENTVALIDATION": ev,
            "tender": tender,
            "amounts": str_amt,
            "amount": str_amt + ".00",
            "request_type": "T"
            })
