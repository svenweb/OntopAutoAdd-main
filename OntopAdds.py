from easygui import *
import os
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from pinkbike import Pinkbike
from craigslist import Craigslist
from facebook import Facebook
import tkinter as tk
from tkinter import filedialog
# root = tk.Tk()
# root.withdraw()
# files = filedialog.askopenfilenames(parent=root, initialdir="/home/sven", title='Please select files')




# class Pinkbike:
#     def __init__(self,biketype,year,adtitle,condition,material,frameSize,wheelSize,forkTravel,rearTravel,phoneNumber,askingPrice,priceOffer,trades,shipping,description):
#         self.biketype = biketype
#         self.year = year
#         self.adtitle = adtitle
#         self.condition = condition
#         self.material = material
#         self.frameSize = frameSize
#         self.wheelSize = wheelSize
#         self.forkTravel = forkTravel
#         self.rearTravel = rearTravel
#         self.phoneNumber = phoneNumber
#         self.askingPrice = askingPrice
#         self.priceOffer = priceOffer
#         self.trades = trades
#         self.shipping = shipping
#         self.description = description



#     driver.get('https://pinkbike.com/user/login')
#     #driver.implicitly_wait(10)
#     print(driver.title)
#     def loginUser(name,password):

#         driver.find_element_by_name('username-login-loginlen').send_keys(name)
#         driver.find_element_by_name("password-password-lt200").send_keys(password)
#         driver.find_element_by_name("submitbutton['Login']").send_keys(Keys.RETURN)






#     def postadd(self,biketype,year,adtitle,condition,material,frameSize,wheelSize,forkTravel,rearTravel,phoneNumber,askingPrice,priceOffer,trades,shipping,description):
#         driver.find_element_by_xpath("/html/body/div[1]/div[3]/ul/li[6]/a").click()#buysell button
#         driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div/div[1]/ul/li[6]/a/span").click()#postadd btn
#         bikeelems = {'year':year,'itemcondition':condition,'material':material,'framesize':frameSize,'wheelsize':wheelSize,'fronttravel':forkTravel,'reartravel':rearTravel,'currency':'CAD $','offer':priceOffer,'trade':trades,'shipping':shipping}
#         #bikeelems2 = {'fronttravel':forkTravel, 'reartravel':rearTravel}
#         driver.find_element_by_link_text(biketype).click()
#         #selectOption('fronttravel', forkTravel)
#         for y in bikeelems:
#             selectOption(y, bikeelems[y])

#         driver.find_element_by_name('title-gt1-textbb-lt55').send_keys(adtitle)
#         driver.find_element_by_name('phone-textbb-lt20').send_keys(phoneNumber)
#         driver.find_element_by_name('price-gt0-lt8-float').send_keys(askingPrice)
#         driver.find_element_by_name('description-gt3-textbb').send_keys(description)
#         driver.find_element_by_name("submitbutton['Upload NewclearPhotos']").click()

#         droparea = driver.find_element_by_xpath('//*[@id="uppy-select-files"]/div/div[2]/div/div[1]/ul/li[1]/input')
#         droparea.send_keys(os.getcwd()+"/testbike.jpg")
#         driver.find_element_by_id('idup').click()
#         try:

#             element = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.NAME, "submitbutton['Save']"))
#             )
#             element.click()
#             #driver.find_elements_by_name("submitbutton['Save']").click()
#         finally:
#             pass


#     def selectOption(trate, wantedTrate):
#         tratename = driver.find_element_by_name(trate + '-locationselect')
#         options = tratename.find_elements_by_tag_name('option')
#         tratename.click()
#         for i in options:
#             if i.text == wantedTrate:
#                 i.click()

#     def runPB():
#         loginUser('boogiej', 'testaccount')
#         postadd(biketype,year,adtitle,condition,material,frameSize,wheelSize,forkTravel,rearTravel,phoneNumber,askingPrice,priceOffer,trades,shipping,description)
#         driver.quit()



#     # def craigsMain():
#     #     driver.get('https://accounts.craigslist.org/login')


#     # pinkbikeMain()
#     # craigsMain()
version = "Ontop Auto Add v.1.0"

#bikeorpartChoice = buttonbox(msg="Yo! You posting a bike or a part?", title=version, choices=('Bike','Part'))




def bike():
    basicInfoBike = []
    basicInfoBike= multenterbox("Enter info",title=version, fields=('Add Title', 'Price','Year','Make','Model'))

    optConvBike = {
        'typeBike_PB.CR':{'All Mountain/Enduro Bikes':'mountain','DH Bikes':'mountain','XC Bikes':'mountain','Dirt Jump Bikes':'bmx','BMX Bikes':'bmx','Road Bikes':'road','Gravel/CX Bikes':'gravel','E-Bikes MTB':'other','E-Bikes Urban/Commuter':'other','E-Bikes Road/Gravel':'other','Kids Bikes':'kids','Vintage Bikes':'other'},
        'materialBike_PB.CR':{'Aluminium':'aluminum','Carbon Fiber':'carbon fiber','Chromoly':'composite','Steel':'steel','Titanium':'titanium','Unknown':'other/unknown'},
        'framesizeBike_CR.PB':{'Extra Small':'XS','Small':'S','Medium':'M','Large':'L','Extra Large':'XL'},
        'wheelSizeBike_CR.PB':{'10 in':'16" or less','12 in':'16" or less','14 in':'16" or less','16 in':'16" or less','18 in':'Unkown','20 in':'20"','24 in':'24"','26 in':'26"','27.5 in':'27.5" / 650B','29 in':'29"','650C':'650C','700C':'700C'},
        'condition_PB.CR':{'New - Dealer/Store':'new','Excellent':'excellent','Good':'good','Poor':'fair','For parts / not working':'salvage'}
    }

    forksusPB_Inp = ''
    rearsusPB_Inp = ''
    typeBike_Inp = choicebox('What is the type of the bike?', title=version, choices=('All Mountain/Enduro Bikes','DH Bikes','XC Bikes','Dirt Jump Bikes','Road Bikes','Gravel/CX Bikes','E-Bikes MTB','E-Bikes Urban/Commuter','E-Bikes Road/Gravel','Kids Bikes','Vintage Bikes'))
    materialBike_Inp = choicebox('What is the material of the frame?', title=version, choices=('Aluminium','Carbon Fiber','Chromoly','Steel','Titanium','Unknown'))
    frameSizeBike_Inp = choicebox('What is the size of the frame?', title=version, choices=('Extra Small','Small','Medium','Large','Extra Large'))
    suspensionCR_Inp = choicebox('What type of suspension?', title=version, choices=('none (rigid)','suspension fork (hardtail)','frame and fork (full suspension)'))
    if (suspensionCR_Inp == 'none (rigid)'):
        forksusPB_Inp = '0 mm'
        rearsusPB_Inp = '0 mm'
    elif(suspensionCR_Inp == 'suspension fork (hardtail)'):
        forksusPB_Inp = choicebox('How much travel does the fork have?', title=version, choices=('60 mm','80 mm','100 mm','110 mm','120 mm','140 mm','160 mm','170 mm','180 mm','190 mm','200 mm','203 mm','208 mm','Unkown'))
        rearsusPB_Inp = '0 mm'
    elif(suspensionCR_Inp == 'frame and fork (full suspension)'):
        forksusPB_Inp = choicebox('How much travel does the fork have?', title=version, choices=('60 mm','80 mm','100 mm','110 mm','120 mm','140 mm','160 mm','170 mm','180 mm','190 mm','200 mm','203 mm','208 mm','Unkown'))
        rearsusPB_Inp = choicebox('How much travel does the rear have?', title=version, choices=('60 mm','80 mm','100 mm','110 mm','120 mm','140 mm','160 mm','170 mm','180 mm','190 mm','200 mm','203 mm','208 mm','215 mm','255 mm','Unkown'))

    brakeType_Inp = choicebox('What is the braketype(craigslist)', title=version, choices=('caliper','cantilever','coaster','disc (hydraulic)','disc (mechanical)','drum','gyro/bmx','hydraulic rim brakes','none','u-brakes','v-brakes','other/unknown'))
    handlebarType_Inp = choicebox('What is the handlebar type?(craigslist?', title=version, choices=('aero','bmx','bullhorn','cruiser','downhill','drop','flat','riser','triathlon','other/unknown'))
    electricAssist_Inp = choicebox('Any electric Assist?', title=version, choices=('none','pedal assist','throttle','other'))
    wheelSizeBike_Inp = choicebox('What is the size of the wheels?', title=version, choices=('10 in','12 in','14 in','16 in','18 in','20 in','24 in','26 in','27.5 in','29 in','650C','700C'))
    conditionBike_Inp = choicebox('What is the condition of the bike?', title=version, choices=('New - Dealer/Store','Excellent','Good','Poor','For parts / not working'))
    bikeDescription_Inp = enterbox("What is the description of the bike?", title=version)
    msgbox("Press ok to select photos of bike", title=version)
    photoBike_Inp = fileopenbox("Please select the images of the bike", title=version, multiple=True)
    print(photoBike_Inp)
    PATH = '/home/sven/Desktop/OntopAutoAdd-main'
    driver = webdriver.Firefox(PATH)
    pbLoad = Pinkbike(driver,'snowygear@gmail.com','testaccountferda','bike',typeBike_Inp,basicInfoBike[2],basicInfoBike[0],photoBike_Inp,conditionBike_Inp,materialBike_Inp,optConvBike.get('framesizeBike_CR.PB')[frameSizeBike_Inp],optConvBike.get('wheelSizeBike_CR.PB')[wheelSizeBike_Inp],forksusPB_Inp,rearsusPB_Inp,'','604-990-9550',basicInfoBike[1],'Firm','No Trades','Local pickup only',bikeDescription_Inp)
    pbLoad.runPB()

    CR = Craigslist(driver,'bike','bit4104@gmail.com',"testaccountferda",basicInfoBike[0],basicInfoBike[2],bikeDescription_Inp,"nothing",photoBike_Inp,frameSizeBike_Inp,basicInfoBike[3],basicInfoBike[4],optConvBike.get('typeBike_PB.CR')[typeBike_Inp],optConvBike.get('materialBike_PB.CR')[materialBike_Inp],wheelSizeBike_Inp,suspensionCR_Inp,brakeType_Inp,handlebarType_Inp, electricAssist_Inp, conditionBike_Inp)
    CR.run()

    # from multiprocessing import Process
    # import sys
    #
    # if __name__=='__main__':
    #     p1 = Process(target = pbLoad.runPB())
    #     p1.start()
    #     p2 = Process(target = CR.run())
    #     p2.start()

#print(multphototest)

#bike()
# if bikeorpartChoice == "Bike":
#     bike()
def part():

    optConvPart = {
        'PartCondition_PB.CR':{'New - Dealer/Store':'new','Excellent':'excellent','Good':'good','Poor':'fair','For parts / not working':'salvage'},



    }

    fieldsList = {'Wheel Size:':['16" or less','20"','24"','26"','27.5" / 650B','29"','650C','700C','Unknown'],'Frame Size:':['XS','S','M','L','XL'],'Material:':['Aluminium','Carbon Fiber','Chromoly','Steel','Titanium','Unknown'],'Rear Travel:':['0 mm (Hardtail)','80 mm','100 mm','110 mm','111 mm','120 mm','130 mm','135 mm','140 mm','143 mm','145 mm','150 mm','153 mm','155 mm','160 mm','170 mm','180 mm','190 mm','200 mm','215 mm','216 mm','254 mm','255 mm','Unknown'],'Fork Travel:':['0 mm (Rigid)','40 mm','60 mm','80 mm','90 mm','95 mm','100 mm','110 mm','120 mm','130 mm','140 mm','150 mm','160 mm','170 mm','175 mm','180 mm','190 mm','200 mm','203 mm','208 mm','Unknown'],'Front Axle:':['100 Lefty','100 QR','12 x 100 TA','15 x 100 TA','15 x 110 TA Boost','15 x 150 TA','20 x 110 TA','Unknown / Not Present'],'Rear Axle:':['10 x 130 QR','10 x 135 QR','10 x 141 QR','10 x 170 QR','12 x 135 TA','12 x 142 TA','12 x 148 TA','12 x 150 TA','12 x 157 TA','12 x 177 TA','Unknown / Not Present'],'Seatpost Diameter:':['25.4','26.2','26.8','27.2','30.0','30.9','31.6','34.9','Unknown'
],'Seatpost Travel:':['35 mm','65 mm','80 mm','85 mm','100 mm','110 mm','120 mm','125 mm','130 mm','140 mm','150 mm','160 mm','170 mm','175 mm','180 mm','185 mm','200 mm','210 mm','220 mm','Unknown'
],'Shock Eye to Eye:':['6.5"','7.25"','7.5"','7.875"','8.5"','8.75"','9.5"','10.5"','165 mm','185 mm','190 mm','200 mm','205 mm','210 mm','215 mm','216 mm','222 mm','225 mm','230 mm','240 mm','250 mm','Unknown'
],'Shock Stroke:':['1.5"','1.75"','1.875"','2.0"','2.25"','2.5"','2.75"','3.0"','3.5"','45 mm','50 mm','51 mm','52.5 mm','55 mm','57 mm','57.5 mm','60 mm','62.5 mm','63 mm','65 mm','70 mm','75 mm','76 mm','Unknown'
],'Shock Spring Rate:(lbs)':['200','225','250','275','300','325','350','375','400','425','450','475','500','525','550','575','600','650','700','Unknown']

}




    pinkikeMegaData = {'All Mountain/Enduro Frames': ['Wheel Size:','Fork Travel:', 'Frame Size:', 'Material:', 'Rear Travel:'], 'DJ/Street/Park Frames': ['Wheel Size:', 'Frame Size:', 'Material:'], 'XC Frames': ['Wheel Size:', 'Frame Size:', 'Material:', 'Rear Travel:'], 'Vintage Frames': [], 'Fork Parts / Springs': [], 'Single Crown Forks': ['Wheel Size:', 'Front Axle:','Fork Travel:'], 'Dual Crown Forks': ['Wheel Size:', 'Front Axle:','Fork Travel'], 'Rear Shocks ( Air )': ['Shock Eye to Eye:', 'Shock Stroke:'], 'Rear Shocks ( Coil )': ['Shock Eye to Eye:', 'Shock Stroke:', 'Shock Spring Rate:(lbs)'], 'Rear Shock Parts': [], 'Rear Shock Springs': ['Material:', 'Shock Spring Rate:(lbs)'], 'Brakes': [], 'Grips': [], 'Handle Bars ( 31.8 mm )': ['Material:'], 'Handle Bars ( 35 mm )': ['Material:'], 'Headsets': [], 'Pedals ( Clipless)': [], 'Pedals ( Flat )': [], 'Saddles': [], 'Seatposts ( Dropper )': ['Seatpost Diameter:','Seatpost Travel:'], 'Seatposts ( Fixed )': ['Seatpost Diameter:'], 'Seatpost Parts': [], 'Stems': [], 'Bottom Brackets': [], 'Cassettes': [], 'Chains': [], 'Chain Guides': [], 'Chain Rings': [], 'Cranks': ['Material:'], 'Drivetrain Groupset': [], 'Hubs': ['Front Axle:', 'Rear Axle:'], 'Shifters/Derailleurs': [], 'Spokes': [], 'Tires': ['Wheel Size:'], 'Wheels ( with Hubs )': ['Wheel Size:', 'Material:', 'Front Axle:', 'Rear Axle:'], 'Wheels ( Rims only )': ['Wheel Size:'], 'E-Bikes MTB': ['Wheel Size:', 'Frame Size:', 'Material:'], 'E-Bikes Urban/Commuter': ['Wheel Size:', 'Frame Size:'], 'E-Bikes Road/Gravel': ['Wheel Size:', 'Frame Size:'], 'E-Bike Parts': [], 'Fat Bikes': ['Wheel Size:', 'Frame Size:'], 'Fat Bike Frames': ['Wheel Size:', 'Frame Size:'], 'Fat Bike Parts': [], 'BMX Bikes': ['Wheel Size:', 'Frame Size:'], 'BMX Frames': ['Wheel Size:', 'Frame Size:'], 'BMX Forks/Headsets/Pegs': [], 'BMX Wheels/Rims/Tires': ['Wheel Size:'], 'BMX Seat/Post/Clamps': [], 'BMX Bars/Grips/Stems': [], 'BMX Cranks/BBs/Chains': [], 'BMX Brakes': [], 'BMX Hubs': [], 'BMX Pedals': [], 'BMX Parts': [], 'Gravel/CX Bikes': ['Wheel Size:', 'Frame Size:', 'Material:'], 'Gravel/CX Frames': ['Wheel Size:', 'Frame Size:', 'Material:'], 'Gravel/CX Parts': [], 'Road Bikes': ['Wheel Size:', 'Frame Size:', 'Material:'], 'Road Frames': ['Wheel Size:', 'Frame Size:', 'Material:'], 'Road Parts': [], 'Trials Bikes': ['Wheel Size:', 'Frame Size:'], 'Trials Frames': ['Wheel Size:', 'Frame Size:'], 'Trials Parts': [], 'Trucks/Cars': [], 'Ski': [], 'Snowboard': [], 'Skateboard': [], 'MX Bikes/Quads': [], 'Armour/Pads': [], 'Backpacks': [], 'Bike Bags': [], 'Bike Racks': [], 'Clothes': [], 'Goggles/Shades': [], 'GPS/Speedometers': [], 'Helmets': [], 'Computers/Tech gear': [], 'Video/Photo gear': [], 'IPODs/Music Players': [], 'Music/Guitar/Amps': [], 'Paintball': [], 'Other': [], 'Wanted Ads': [], 'Trades': [], 'Stolen Bikes/Parts': [], 'Lights': [], 'Shoes': [], 'Tools/Bike Stands': [], 'Trainers / Rollers': [], 'DH Frames': ['Wheel Size:', 'Frame Size:', 'Material:', 'Rear Travel:']}


    basicInfoPart= multenterbox("Enter info",title=version, fields=('Add Title','Price','Make','Model'))
    yearPartCheck_Inp = choicebox("Do ya know the year?",title=version,choices=('Yup!','Nope'))
    if (yearPartCheck_Inp == 'Yup!'):
        yearPart_Inp = enterbox("Enter the year!",title=version)
    partTypePB_Inp = choicebox("What part is it?(pinkbike)", title=version, choices=('DH Frames', 'All Mountain/Enduro Frames', 'DJ/Street/Park Frames', 'XC Frames', 'Vintage Frames', 'Fork Parts / Springs', 'Single Crown Forks', 'Dual Crown Forks', 'Rear Shocks ( Air )', 'Rear Shocks ( Coil )', 'Rear Shock Parts', 'Rear Shock Springs', 'Brakes', 'Grips', 'Handle Bars ( 31.8 mm )', 'Handle Bars ( 35 mm )', 'Headsets', 'Pedals ( Clipless)', 'Pedals ( Flat )', 'Saddles', 'Seatposts ( Dropper )', 'Seatposts ( Fixed )', 'Seatpost Parts', 'Stems', 'Bottom Brackets', 'Cassettes', 'Chains', 'Chain Guides', 'Chain Rings', 'Cranks', 'Drivetrain Groupset', 'Hubs', 'Shifters/Derailleurs', 'Spokes', 'Tires', 'Wheels ( with Hubs )', 'Wheels ( Rims only )', 'Fat Bike Frames', 'Fat Bike Parts', 'BMX Frames', 'BMX Forks/Headsets/Pegs', 'BMX Wheels/Rims/Tires', 'BMX Seat/Post/Clamps', 'BMX Bars/Grips/Stems', 'BMX Cranks/BBs/Chains', 'BMX Brakes', 'BMX Hubs', 'BMX Pedals', 'BMX Parts', 'Gravel/CX Frames', 'Gravel/CX Parts', 'Road Bikes', 'Road Frames', 'Road Parts', 'Trials Frames', 'Trials Parts', 'Trucks/Cars', 'Ski', 'Snowboard', 'Skateboard', 'MX Bikes/Quads', 'Armour/Pads', 'Backpacks', 'Bike Bags', 'Bike Racks', 'Clothes', 'Goggles/Shades', 'GPS/Speedometers', 'Helmets', 'Computers/Tech gear', 'Video/Photo gear', 'IPODs/Music Players', 'Music/Guitar/Amps', 'Paintball', 'Other', 'Wanted Ads', 'Trades', 'Stolen Bikes/Parts', 'Lights', 'Shoes', 'Tools/Bike Stands', 'Computers/Tech gear', 'Video/Photo gear', 'IPODs/Music Players', 'Music/Guitar/Amps', 'Paintball', 'Other', 'Wanted Ads', 'Trades', 'Stolen Bikes/Parts', 'Trainers / Rollers', 'Computers/Tech gear', 'Video/Photo gear', 'IPODs/Music Players', 'Music/Guitar/Amps', 'Paintball', 'Other', 'Wanted Ads', 'Trades', 'Stolen Bikes/Parts'))
    metaData = {}

    if pinkikeMegaData[partTypePB_Inp] != []:
        specificFields = pinkikeMegaData[partTypePB_Inp]
        for x in specificFields:
            metaValue = choicebox(("Enter the "+x),title=version,choices=(fieldsList[x]))
            metaData[x] = metaValue
    print(metaData)
    partTypeCR_Inp = choicebox("What part is it (craigslist)",title=version,choices=('brakes','cassette, freewheel, cogs','crankset, bottom bracket, guards','derailleurs','fork only','frameset (frame and fork)','frame only','grips, bar ends, tape','handlebars','headset, stem, spacers','hubs','lights, computers, accessories','pedals','racks, fenders, bags','racks, fenders, bags','seatpost and clamp','shifters','suspension parts','tires','wheels and wheel parts','other'))
    photoBike_Inp = fileopenbox("Please select the images of the part", title=version, multiple=True)
    conditionPart_Inp = choicebox('What is the condition of the part?', title=version, choices=('New - Dealer/Store','Excellent','Good','Poor','For parts / not working'))
    descriptionPart_Inp = enterbox("Enter the description of the part",title=version)

    pbLoad = Pinkbike(driver,'snowygear@gmail.com','testaccountferda',typeBike_Inp,basicInfoBike[2],basicInfoBike[0],conditionBike_Inp,materialBike_Inp,optConvBike.get('framesizeBike_CR.PB')[frameSizeBike_Inp],optConvBike.get('wheelSizeBike_CR.PB')[wheelSizeBike_Inp],forksusPB_Inp,rearsusPB_Inp,'604-990-9550',basicInfoBike[1],'Firm','No Trades','Local pickup only',bikeDescription_Inp)
    pbLoad.runPB()

    CR = Craigslist(driver,'part','bit4104@gmail.com','testaccountferda','Test Bike','90','its a sick bike','fork only',photoBike_Inp,'Small','santacruz','nomad','mountain','alloy','10 in','frame and fork (full suspension)','drum','drop','none','new')
    CR.run()

#part()
bike()

# from pinkbikelinkCollector import Collector
# pbLinkload = Collector(driver,'svenyensen','pythonz2')
# pbLinkload.gettodata()
# pbLinkload.getsomedata()
#pbLoad = Pinkbike(driver,'johnbaconback','testaccountferda',"All Mountain/Enduro Bikes",'2019','MEGATeasdasstaasdsdBike3','Good','Steel','S','26"','180 mm','160 mm','778998877','800','Firm','No Trades','Local pickup only','its a super super megawickeasdasdasd bike eh')
#pbLoad.runPB()

#CR = Craigslist(driver,'part','bit4104@gmail.com','testaccountferda','Test Bike','90','its a sick bike','fork only','Small','santacruz','nomad','mountain','alloy','10 in','frame and fork (full suspension)','drum','drop','none','new')
#CR.run()

# fB = Facebook(driver,'bit4104@gmail.com','testaccountferda!',"All Mountain/Enduro Bikes",'2019','MEGATestaasdsdBike3','Good','Steel','S','26"','180 mm','160 mm','778998877','800','Firm','No Trades','Local pickup only','its a super super megawickeasdasdasd bike eh')
# fB.runFB()


#
#
# 'Aluminium','Carbon Fiber','Chromoly','Steel','Titanium','Unknown'
#
# ' selected="selected">Select Wheel Size</option>
# '16" or less','20"','24"','26"','27.5" / 650B','29"','650C','700C','Unknown'
#
#     'elected="selected">Select Rear Travel</option>
# '0 mm (Hardtail)','80 mm','100 mm','110 mm','111 mm','120 mm','130 mm','135 mm','140 mm','143 mm','145 mm','150 mm','153 mm','155 mm','160 mm','170 mm','180 mm','190 mm','200 mm','215 mm','216 mm','254 mm','255 mm','Unknown'
#
# <option value="-1" selected="selected">Select Fork Travel</option>
# '0 mm (Rigid)','40 mm','60 mm','80 mm','90 mm','95 mm','100 mm','110 mm','120 mm','130 mm','140 mm','150 mm','160 mm','170 mm','175 mm','180 mm','190 mm','200 mm','203 mm','208 mm','Unknown'
#
# <option value="-1" selected="selected">Select Front Axle/Hub</option>
# '100 Lefty','100 QR','12 x 100 TA','15 x 100 TA','15 x 110 TA Boost','15 x 150 TA','20 x 110 TA','Unknown / Not Present'
#
#
# <option value="-1" selected="selected">Select Rear Axle/Hub</option>
# '10 x 130 QR','10 x 135 QR','10 x 141 QR','10 x 170 QR','12 x 135 TA','12 x 142 TA','12 x 148 TA','12 x 150 TA','12 x 157 TA','12 x 177 TA','Unknown / Not Present'
#
# <option value="-1" selected="selected">Select Seatpost Diameter</option>
# '25.4','26.2','26.8','27.2','30.0','30.9','31.6','34.9','Unknown'
#
#
# <option value="-1" selected="selected">Select Seatpost Travel</option>
# '35 mm','65 mm','80 mm','85 mm','100 mm','110 mm','120 mm','125 mm','130 mm','140 mm','150 mm','160 mm','170 mm','175 mm','180 mm','185 mm','200 mm','210 mm','220 mm','Unknown'
#
# <option value="-1" selected="selected">Select Eye To Eye</option>
# '6.5"','7.25"','7.5"','7.875"','8.5"','8.75"','9.5"','10.5"','165 mm','185 mm','190 mm','200 mm','205 mm','210 mm','215 mm','216 mm','222 mm','225 mm','230 mm','240 mm','250 mm','Unknown'
#
# <option value="-1" selected="selected">Select Eye To Eye</option>
# '1.5"','1.75"','1.875"','2.0"','2.25"','2.5"','2.75"','3.0"','3.5"','45 mm','50 mm','51 mm','52.5 mm','55 mm','57 mm','57.5 mm','60 mm','62.5 mm','63 mm','65 mm','70 mm','75 mm','76 mm','Unknown'
#
#
# <option value="-1" selected="selected">Select Shock Type</option>
# '200','225','250','275','300','325','350','375','400','425','450','475','500','525','550','575','600','650','700','Unknown'
