import re
import os
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

class Collector:

    def __init__(self,driver,name,password):
        self.driver = driver
        self.name = name
        self.password = password
        driver.get('https://www.pinkbike.com/user/login/')

    def waitTry(self,selector, select):
        self.selector = selector
        self.select = select
        import traceback

        try:
            #element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.selector, select)))
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.__dict__[selector], select)))
            #time.sleep(2)
            element.send_keys(Keys.RETURN)

        finally:
            pass


    def gettodata(self):
        self.driver.find_element_by_name('username-login-loginlen').send_keys(self.name)
        self.driver.find_element_by_name("password-password-lt200").send_keys(self.password)
        self.driver.find_element_by_name("submitbutton['Login']").send_keys(Keys.RETURN)
        #self.driver.find_element_by_link_text("BuySell").click()#buysell button
        time.sleep(2)
        try:

            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "BuySell"))
                )
            element.send_keys(Keys.RETURN)
                #driver.find_elements_by_name("submitbutton['Save']").click()
        finally:
            pass

        #self.waitTry('LINK_TEXT','BuySell')
        #self.waitTry('XPATH','/html/body/div[4]/div/div[1]/div/div/div[1]/ul/li[6]/a')
        self.driver.get('https://www.pinkbike.com/buysell/selectcategory/')
        #self.driver.find_element_by_link_text("Post New Ad").send_keys(Keys.RETURN)#buysell button

    def getsomedata(self):

        partsList = ('DH Frames', 'All Mountain/Enduro Frames', 'DJ/Street/Park Frames', 'XC Frames', 'Vintage Frames', 'Fork Parts / Springs', 'Single Crown Forks', 'Dual Crown Forks', 'Rear Shocks ( Air )', 'Rear Shocks ( Coil )', 'Rear Shock Parts', 'Rear Shock Springs', 'Brakes', 'Grips', 'Handle Bars ( 31.8 mm )', 'Handle Bars ( 35 mm )', 'Headsets', 'Pedals ( Clipless)', 'Pedals ( Flat )', 'Saddles', 'Seatposts ( Dropper )', 'Seatposts ( Fixed )', 'Seatpost Parts', 'Stems', 'Bottom Brackets', 'Cassettes', 'Chains', 'Chain Guides', 'Chain Rings', 'Cranks', 'Drivetrain Groupset', 'Hubs', 'Shifters/Derailleurs', 'Spokes', 'Tires', 'Wheels ( with Hubs )', 'Wheels ( Rims only )', 'E-Bikes MTB', 'E-Bikes Urban/Commuter', 'E-Bikes Road/Gravel', 'E-Bike Parts', 'Fat Bikes', 'Fat Bike Frames', 'Fat Bike Parts', 'BMX Bikes', 'BMX Frames', 'BMX Forks/Headsets/Pegs', 'BMX Wheels/Rims/Tires', 'BMX Seat/Post/Clamps', 'BMX Bars/Grips/Stems', 'BMX Cranks/BBs/Chains', 'BMX Brakes', 'BMX Hubs', 'BMX Pedals', 'BMX Parts', 'Gravel/CX Bikes', 'Gravel/CX Frames', 'Gravel/CX Parts', 'Road Bikes', 'Road Frames', 'Road Parts', 'Trials Bikes', 'Trials Frames', 'Trials Parts', 'Trucks/Cars', 'Ski', 'Snowboard', 'Skateboard', 'MX Bikes/Quads', 'Armour/Pads', 'Backpacks', 'Bike Bags', 'Bike Racks', 'Clothes', 'Goggles/Shades', 'GPS/Speedometers', 'Helmets', 'Computers/Tech gear', 'Video/Photo gear', 'IPODs/Music Players', 'Music/Guitar/Amps', 'Paintball', 'Other', 'Wanted Ads', 'Trades', 'Stolen Bikes/Parts', 'Lights', 'Shoes', 'Tools/Bike Stands', 'Computers/Tech gear', 'Video/Photo gear', 'IPODs/Music Players', 'Music/Guitar/Amps', 'Paintball', 'Other', 'Wanted Ads', 'Trades', 'Stolen Bikes/Parts', 'Trainers / Rollers', 'Computers/Tech gear', 'Video/Photo gear', 'IPODs/Music Players', 'Music/Guitar/Amps', 'Paintball', 'Other', 'Wanted Ads', 'Trades', 'Stolen Bikes/Parts')

        fieldsList = ['Wheel Size:','Frame Size:','Material:','Rear Travel:','Front Travel:','Front Axle:','Rear Axle:','Seatpost Diameter:','Seatpost Travel','Shock Eye to Eye:','Shock Stroke:','Shock Spring Rate:(lbs)']

        data = {'All Mountain/Enduro Frames': [], 'DJ/Street/Park Frames': [], 'XC Frames': [], 'Vintage Frames': [], 'Fork Parts / Springs': [], 'Single Crown Forks': [], 'Dual Crown Forks': [], 'Rear Shocks ( Air )': [], 'Rear Shocks ( Coil )': [], 'Rear Shock Parts': [], 'Rear Shock Springs': [], 'Brakes': [], 'Grips': [], 'Handle Bars ( 31.8 mm )': [], 'Handle Bars ( 35 mm )': [], 'Headsets': [], 'Pedals ( Clipless)': [], 'Pedals ( Flat )': [], 'Saddles': [], 'Seatposts ( Dropper )': [], 'Seatposts ( Fixed )': [], 'Seatpost Parts': [], 'Stems': [], 'Bottom Brackets': [], 'Cassettes': [], 'Chains': [], 'Chain Guides': [], 'Chain Rings': [], 'Cranks': [], 'Drivetrain Groupset': [], 'Hubs': [], 'Shifters/Derailleurs': [], 'Spokes': [], 'Tires': [], 'Wheels ( with Hubs )': [], 'Wheels ( Rims only )': [], 'E-Bikes MTB': [], 'E-Bikes Urban/Commuter': [], 'E-Bikes Road/Gravel': [], 'E-Bike Parts': [], 'Fat Bikes': [], 'Fat Bike Frames': [], 'Fat Bike Parts': [], 'BMX Bikes': [], 'BMX Frames': [], 'BMX Forks/Headsets/Pegs': [], 'BMX Wheels/Rims/Tires': [], 'BMX Seat/Post/Clamps': [], 'BMX Bars/Grips/Stems': [], 'BMX Cranks/BBs/Chains': [], 'BMX Brakes': [], 'BMX Hubs': [], 'BMX Pedals': [], 'BMX Parts': [], 'Gravel/CX Bikes': [], 'Gravel/CX Frames': [], 'Gravel/CX Parts': [], 'Road Bikes': [], 'Road Frames': [], 'Road Parts': [], 'Trials Bikes': [], 'Trials Frames': [], 'Trials Parts': [], 'Trucks/Cars': [], 'Ski': [], 'Snowboard': [], 'Skateboard': [], 'MX Bikes/Quads': [], 'Armour/Pads': [], 'Backpacks': [], 'Bike Bags': [], 'Bike Racks': [], 'Clothes': [], 'Goggles/Shades': [], 'GPS/Speedometers': [], 'Helmets': [], 'Computers/Tech gear': [], 'Video/Photo gear': [], 'IPODs/Music Players': [], 'Music/Guitar/Amps': [], 'Paintball': [], 'Other': [], 'Wanted Ads': [], 'Trades': [], 'Stolen Bikes/Parts': [], 'Lights': [], 'Shoes': [], 'Tools/Bike Stands': [], 'Trainers / Rollers': [], 'DH Frames': []}



        validFields = []
        for part in partsList:
            validFields.clear()
            self.driver.find_element_by_link_text(part).send_keys(Keys.RETURN)
            time.sleep(2)
            allFields = self.driver.find_elements_by_class_name('bsfieldname')
            for field in allFields:
                if hasattr(field,'text'):
                    if field.text == '':
                        pass
                    else:
                        validFields.append(field.text)
            print(validFields)        #do something
            for x in fieldsList:
                for y in validFields:
                    if (x == y):
                        print(part + '' + y)
                        data[part].append(y)
            self.driver.back()
            print(data)
