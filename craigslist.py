import os
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from waiting import wait
import logging
import time
class Craigslist:
    def __init__(self,driver,bikeorpart,email,password,title,price,description,partType,images,framesize,brand,model,biketype,frameMaterial,wheelSize,suspension,brakeType,handlebarType, electricAssist, condition):
        self.driver = driver
        self.email = email
        self.password = password
        self.bikeorpart = bikeorpart
        self.title = title
        self.price = price
        self.description = description
        self.partType = partType
        self.framesize = framesize
        self.brand = brand
        self.model = model
        self.biketype = biketype
        self.frameMaterial = frameMaterial
        self.wheelSize = wheelSize
        self.suspension = suspension
        self.brakeType = brakeType
        self.handlebarType = handlebarType
        self.electricAssist = electricAssist
        self.condition = condition
        self.link_textValues = [frameMaterial,wheelSize,suspension,brakeType,handlebarType,electricAssist,condition]
        self.images = images

        driver.get('https://accounts.craigslist.org/login?rp=%2Flogin%2Fhome&rt=L')

    def waitTry(self,selector, select):
        self.selector = selector
        self.select = select
        import traceback

        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.__dict__[selector], select)))
            element.click()

        finally:
            pass


    def checkImageLoad(self,num):
        imageDivContainer = self.driver.find_element_by_xpath('/html/body/article/section/div[2]')
        imglistDiv = imageDivContainer.find_elements_by_tag_name('img')
        if (len(imglistDiv) == num):
            return True


    def postImages(self,imgNum):
        imageDivContainer = self.driver.find_element_by_xpath('/html/body/article/section/div[2]/figure/div')
        imglistDiv = imageDivContainer.find_elements_by_tag_name('img')
        if wait(lambda : self.checkImageLoad(imgNum)) == True:
            self.driver.find_element_by_class_name('done.bigbutton').click()




    def login(self):
        self.driver.find_element_by_id('inputEmailHandle').send_keys(self.email)
        self.driver.find_element_by_id('inputPassword').send_keys(self.password)
        self.driver.find_element_by_id('login').click()

    def postBikeSort(self):
        self.bikesortDict = {
            'id':{'PostingTitle':self.title,'PostingBody':(self.description+ '\n' + ' Come by Ontop Bike Shop 10am-6pm, Tuesday to Sunday! Dont email, please call, Thanks! \n*OntopAutoAdd v.1.0*')},
            'name':{'price':self.price,'geographic_area':'North Vancouver','postal':'V7N 3J6','bicycle_frame_size_freeform':self.framesize,'sale_manufacturer':self.brand,'sale_model':self.model},
            'links':{'ui-id-1-button':self.biketype,'ui-id-2-button':self.frameMaterial,'ui-id-3-button':self.wheelSize,'ui-id-4-button':self.suspension,'ui-id-5-button':self.brakeType,'ui-id-6-button':self.handlebarType,'ui-id-7-button':self.electricAssist,'ui-id-8-button':self.condition}
        }
        return self.bikesortDict


    def getToPost(self):
        self.driver.find_element_by_link_text('craigslist').click()
        self.waitTry('ID','post')
        self.waitTry('XPATH','/html/body/article/section/form/ul/li[2]/label/input')
        self.waitTry('XPATH','/html/body/article/section/form/ul/li[6]/label/span[1]/input')

    def postPart(self):
        self.driver.find_element_by_xpath('//*[@id="new-edit"]/div/label/label[10]/input').click()
        bikeIDdict = self.postBikeSort().get('id')
        bikeNAMEdict = self.postBikeSort().get('name')
        partLinks = {'ui-id-1-button':self.partType,'ui-id-2-button':self.condition}
        for x in bikeIDdict:
            self.driver.find_element_by_id(x).send_keys(bikeIDdict[x])

        for i in bikeNAMEdict:
            if i == 'bicycle_frame_size_freeform':
                pass
            else:
                self.driver.find_element_by_name(i).send_keys(bikeNAMEdict[i])

        for y in partLinks:
            self.driver.find_element_by_id(y).click()
            for p in self.driver.find_elements_by_class_name('ui-menu-item'):
                print(p.text)
                if p.text == str(partLinks[y]):
                    p.click()

        self.driver.find_element_by_name('show_phone_ok').click()
        self.driver.find_element_by_name('contact_phone').send_keys('604-990-9550')
        self.driver.find_element_by_name('show_address_ok').click()
        self.driver.find_element_by_name('xstreet0').send_keys('3051 Lonsdale Avenue')
        self.driver.find_element_by_name('go').click()
        self.waitTry('XPATH', '//*[@id="leafletForm"]/button')

        for x in self.images:
            time.sleep(1)
            self.driver.find_element_by_tag_name('input').send_keys(x)
        self.postImages(len(self.images))
        self.waitTry('NAME','go')




    def postBike(self):
        self.driver.find_element_by_xpath('//*[@id="new-edit"]/div/label/label[11]/input').click()
        bikeIDdict = self.postBikeSort().get('id')
        bikeNAMEdict = self.postBikeSort().get('name')
        bikeLINKdict = self.postBikeSort().get('links')
        for x in bikeIDdict:
            self.driver.find_element_by_id(x).send_keys(bikeIDdict[x])

        for i in bikeNAMEdict:
            self.driver.find_element_by_name(i).send_keys(bikeNAMEdict[i])

        for y in bikeLINKdict:
            self.driver.find_element_by_id(y).click()
            print(bikeLINKdict[y])
            for p in self.driver.find_elements_by_class_name('ui-menu-item'):
               print(p.text)
               if p.text == bikeLINKdict[y]:
                   p.click()
        self.driver.find_element_by_name('show_phone_ok').click()
        self.driver.find_element_by_name('contact_phone').send_keys('604-990-9550')
        self.driver.find_element_by_name('show_address_ok').click()
        self.driver.find_element_by_name('xstreet0').send_keys('3051 Lonsdale Avenue')
        self.driver.find_element_by_name('go').click()

        self.waitTry('XPATH', '//*[@id="leafletForm"]/button')
        time.sleep(1)
        for x in self.images:
            self.driver.find_element_by_tag_name('input').send_keys(x)
        self.postImages(len(self.images))
        self.waitTry('NAME','go')

    def run(self):
        self.login()
        self.getToPost()
        if (self.bikeorpart == 'part'):
            self.postPart()
        elif(self.bikeorpart == 'bike'):
            self.postBike()
        self.driver.quit()
