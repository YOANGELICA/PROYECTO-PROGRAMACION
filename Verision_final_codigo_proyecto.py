import os
import random
from time import sleep
from selenium import webdriver

count=1
if(not os.path.isdir("Informacion apartamentos")):
    os.mkdir("Informacion apartamentos")

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe') 
#C:\Program Files\Webdrivers\chromedriver_win32\chromedriver.exe
#C:\Program Files (x86)\chromedriver.exe

driver.get('https://www.fincaraiz.com.co/apartamentos/arriendos?ubicacion=Bochalema&pagina=4') 
for i in range (3):  
    apts= driver.find_elements_by_xpath('//div[@class="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-6 MuiGrid-grid-lg-4 MuiGrid-grid-xl-4"]')

    for apt in apts:

        price = apt.find_element_by_xpath('.//section[@class="MuiGrid-root MuiGrid-container"]/div[@class="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12"]/span/b').text 
        print(price)

        room = apt.find_element_by_xpath('.//section[@class="MuiGrid-root MuiGrid-container"]/div[2]/span[3]').text 
        link = apt.find_element_by_xpath('.//article/a[@href]')
        print(link.get_attribute("href"))

        mtrs = apt.find_element_by_xpath('.//section/div[2]/span[1]').text
       

        arooms= room.split('h')[0]
        aprices = price.split('$')[-1]
        aaprices = aprices.replace('.', "")
        aaaprices= int(aaprices)/ int(arooms)
        mmtrs = mtrs.replace("²","^2")
        print (mmtrs)

        oprices= round(aaaprices)

        with open(f'Informacion_apartamentos.csv', 'a', encoding='utf-8') as f:
            f.write(link.get_attribute("href")+","+ str(aaprices)+ ","+ str(arooms)+ ","+ str(oprices)+","+ str(mmtrs))
            f.write('\n')
            count = count +1

    try:
        boton = driver.find_element_by_xpath('//button[@class="MuiButtonBase-root MuiPaginationItem-root MuiPaginationItem-page MuiPaginationItem-outlined MuiPaginationItem-rounded"]')
        boton.click()
        sleep(random.uniform(10.0, 15.0))
    except:
        break