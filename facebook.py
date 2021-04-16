import os
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
class Facebook:

    def __init__(self,driver,name,password,biketype,year,adtitle,condition,material,frameSize,wheelSize,forkTravel,rearTravel,phoneNumber,askingPrice,priceOffer,trades,shipping,description):
        self.driver = driver
        self.name = name
        self.password = password
        self.biketype = biketype
        self.year = year
        self.adtitle = adtitle
        self.condition = condition
        self.material = material 
        self.frameSize = frameSize
        self.wheelSize = wheelSize
        self.forkTravel = forkTravel
        self.rearTravel = rearTravel
        self.phoneNumber = phoneNumber
        self.askingPrice = askingPrice 
        self.priceOffer = priceOffer
        self.trades = trades
        self.shipping = shipping
        self.description = description
        driver.get('https://www.facebook.com/login')

    
    def loginUser(self):
        self.driver.find_element_by_id('email').send_keys(self.name)
        self.driver.find_element_by_id("pass").send_keys(self.password)
        self.driver.find_element_by_id("loginbutton").send_keys(Keys.RETURN)

    def runFB(self):
        self.loginUser()