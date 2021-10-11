import os
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
from time import sleep
class Pinkbike:

    def __init__(self,driver,name,password,bikeorpart,biketype,year,adtitle,images,condition,material,frameSize,wheelSize,forkTravel,rearTravel,partsData,phoneNumber,askingPrice,priceOffer,trades,shipping,description):
        self.driver = driver
        self.name = name
        self.password = password
        self.bikeorpart = bikeorpart
        self.biketype = biketype
        self.year = year
        self.adtitle = adtitle
        self.images = images
        self.condition = condition
        self.material = material
        self.frameSize = frameSize
        self.wheelSize = wheelSize
        self.forkTravel = forkTravel
        self.rearTravel = rearTravel
        self.partsData = partsData
        self.phoneNumber = phoneNumber
        self.askingPrice = askingPrice
        self.priceOffer = priceOffer
        self.trades = trades
        self.shipping = shipping
        self.description = description

        driver.get('https://pinkbike.com/user/login')
        print('hi')

    def loginUser(self):
        self.driver.find_element_by_name('username-login-loginlen').send_keys(self.name)
        self.driver.find_element_by_name("password-password-lt200").send_keys(self.password)
        self.driver.find_element_by_name("submitbutton['Login']").send_keys(Keys.RETURN)


    def postbike(self):
        time.sleep(2)
        self.driver.find_element_by_link_text("BuySell").click()#buysell button

        time.sleep(1)
        self.driver.find_element_by_xpath('//a[@href="'+'https://www.pinkbike.com/buysell/selectcategory/'+'"]').click()#postadd btn
        time.sleep(1)
        self.driver.find_element_by_link_text(self.biketype).click()
        bikeelems = {'year':self.year,'itemcondition':self.condition,'currency':'CAD $','offer':self.priceOffer,'trade':self.trades,'shipping':self.shipping}
        susElems = {'fronttravel':self.forkTravel,'reartravel':self.rearTravel}
        materialElem = {'material':self.material}
        #VintageFucks = {'framesize':self.frameSize, 'wheelsize':self.wheelSize}

        time.sleep(1)

        if (self.biketype == 'All Mountain/Enduro Bikes') or (self.biketype == 'DH Bikes') or (self.biketype == 'XC Bikes'):
            for i in susElems:
                self.selectOption(i,susElems[i])

        if (self.biketype != 'Kids Bikes') and (self.biketype != 'Vintage Bikes'):
            self.selectOption('material', materialElem['material'])

        if (self.biketype == 'Vintage Bikes'):
            for y in bikeelems:
                self.selectOption(y, bikeelems[y])
        else:
            self.selectOption('framesize',self.frameSize)#for the vintage fuckers
            self.selectOption('wheelsize',self.wheelSize)
            for y in bikeelems:
                self.selectOption(y, bikeelems[y])




        self.driver.find_element_by_name('title-gt1-textbb-lt55').send_keys(self.adtitle)
        self.driver.find_element_by_name('phone-textbb-lt20').clear()
        self.driver.find_element_by_name('phone-textbb-lt20').send_keys(self.phoneNumber)
        self.driver.find_element_by_name('price-gt0-lt8-float').send_keys(self.askingPrice)
        self.driver.find_element_by_name('description-gt3-textbb').send_keys(self.description + '\n' + ' Come by Ontop Bike Shop 10am-6pm, Tuesday to Sunday! \n*OntopAutoAdd v.1.0*')
        self.driver.find_element_by_name("submitbutton['Upload New Photos']").click()

        for image in self.images:
            droparea = self.driver.find_element_by_xpath('//*[@id="uppy-select-files"]/div/div[2]/div/div[1]/ul/li[1]/input')
            droparea.send_keys(image)
        self.driver.find_element_by_id('idup').click()
        try:

            element = WebDriverWait(self.driver, 1000).until(
                EC.presence_of_element_located((By.NAME, "submitbutton['Save']"))
            )
            element.click()

        finally:
            pass



    def postPart(self):
        time.sleep(1)
        self.driver.find_element_by_link_text("BuySell").click()#buysell button
        time.sleep(1)
        self.driver.find_element_by_xpath('//a[@href="'+'https://www.pinkbike.com/buysell/selectcategory/'+'"]').click()#postadd btn
        time.sleep(1)
        self.driver.find_element_by_link_text(self.biketype).click()
        if len(self.partsData) != 0:
            for field in self.partsData:
                self.selectOption(field, self.partsData[field])

        notsopartFields = {'Year:':self.year,'Condition:':self.condition,'Currency:':'CAD $','Offer:':self.priceOffer,'Trade:':self.trades,'Shipping:':self.shipping}
        for y in notsopartFields:
            self.selectOption(y, notsopartFields[y])
        self.driver.find_element_by_name('title-gt1-textbb-lt55').send_keys(self.adtitle)
        self.driver.find_element_by_name('phone-textbb-lt20').clear()
        self.driver.find_element_by_name('phone-textbb-lt20').send_keys(self.phoneNumber)
        self.driver.find_element_by_name('price-gt0-lt8-float').send_keys(self.askingPrice)
        self.driver.find_element_by_name('description-gt3-textbb').send_keys(self.description + '\n' + ' Come by Ontop Bike Shop 10am-6pm, Tuesday to Sunday! Dont email, Please Call. Thanks! \n*OntopAutoAdd v.1.0*')
        self.driver.find_element_by_name("submitbutton['Upload New Photos']").click()



        for image in self.images:
            droparea = self.driver.find_element_by_xpath('//*[@id="uppy-select-files"]/div/div[2]/div/div[1]/ul/li[1]/input')
            droparea.send_keys(image)
        self.driver.find_element_by_id('idup').click()
        try:

            element = WebDriverWait(self.driver, 1000).until(
                EC.presence_of_element_located((By.NAME, "submitbutton['Save']"))
            )
            element.click()
        finally:
            pass
    def selectOption(self,trate, wantedTrate):
        fieldnameConv = {'Offer:':'offer','Trade:':'trade','Shipping:':'shipping','Year:':'year','Currency:':'currency','Condition:':'itemcondition','Material:':'material', 'Wheel Size:':'wheelsize', 'Fork Travel:':'fronttravel', 'Frame Size:':'framesize', 'Rear Travel:':'reartravel','Front Axle:':'frontaxle','Rear Axle:':'rearaxle','Seatpost Diameter:':'seatpostdiameter','Seatpost Travel:':'seatposttravel', 'Shock Eye to Eye:':'shockeyetoeye','Shock Stroke:':'shockstroke','Shock Spring Rate:(lbs)':'shockspringtype'}
        if self.bikeorpart == 'bike':
            tratename = self.driver.find_element_by_name(trate + '-locationselect')
        elif(self.bikeorpart == 'part'):
            tratename = self.driver.find_element_by_name(fieldnameConv[trate] + '-locationselect')

        options = tratename.find_elements_by_tag_name('option')
        tratename.click()
        for i in options:
            if i.text == wantedTrate:
                i.click()

    def runPB(self):
        self.loginUser()
        if (self.bikeorpart == 'bike'):
            self.postbike()
        elif(self.bikeorpart == 'part'):
            self.postPart()
