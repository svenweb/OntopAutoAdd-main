import os
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
class Facebook:

    def __init__(self,driver,name,password):
        #,biketype,year,adtitle,condition,material,frameSize,wheelSize,forkTravel,rearTravel,phoneNumber,askingPrice,priceOffer,trades,shipping,description):
        self.driver = driver
        self.name = name
        self.password = password
        # self.biketype = biketype
        # self.year = year
        # self.adtitle = adtitle
        # self.condition = condition
        # self.material = material
        # self.frameSize = frameSize
        # self.wheelSize = wheelSize
        # self.forkTravel = forkTravel
        # self.rearTravel = rearTravel
        # self.phoneNumber = phoneNumber
        # self.askingPrice = askingPrice
        # self.priceOffer = priceOffer
        # self.trades = trades
        # self.shipping = shipping
        # self.description = description
        driver.get('https://www.facebook.com/login')

    def waitTry(self,selector, select):
        self.selector = selector
        self.select = select
        import traceback

        try:
            element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.__dict__[selector], select)))
            #element.click()

        finally:
            element.click()

    def loginUser(self):
        self.driver.find_element_by_id('email').send_keys(self.name)
        time.sleep(1)
        self.driver.find_element_by_id("pass").send_keys(self.password)
        time.sleep(1)
        self.driver.find_element_by_id("loginbutton").send_keys(Keys.RETURN)

    def post(self):
        time.sleep(1)
        self.waitTry('XPATH',"//span[.='Marketplace']")

        #marketplace_button = self.driver.find_element_by_xpath('//div[contains(text(), "Marketplace")]')
        self.waitTry('XPATH', "//span[.='Create New Listing']")
        #marketplace_button.click()
        self.waitTry('XPATH', "//span[.='Item for Sale']")
        time.sleep(1)
        self.waitTry('XPATH', "//span[.='Category']")


    def runFB(self):
        self.loginUser()
        self.post()
driver = webdriver.Firefox('/Users/sven/Desktop/geckoworks')
f = Facebook(driver,'snowygear@gmail.com','The1bestsophia!')

f.runFB()
