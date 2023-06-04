import xlrd
import pywhatkit
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

import time


driver = webdriver.Chrome('/home/mrhead/Desktop/whats_app/chromedriver')
start_url = ('https://web.whatsapp.com')

driver.get(start_url)

time.sleep(50)

file_s=driver.find_element(By.CLASS_NAME, 'selectable-text.copyable-text')

#de aqui sacamos los numeros
excelFile = xlrd.open_workbook("name.xls")
sheet1 = excelFile.sheet_by_index(0)

for i in range(0, sheet1.nrows):
    #elementos de el campo de busqueda


    numeros = sheet1.cell_value(rowx = i, colx = 0)

    file_s.send_keys(numeros)
    time.sleep(5)
    file_s.send_keys(Keys.ENTER)

    # Esperar unos segundos para asegurarse de que se haya abierto la conversación
    time.sleep(5)

    # Enviar el mensaje utilizando pywhatkit
    msg = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    # Esperar unos segundos para que el mensaje se envíe antes de pasar al siguiente número
    time.sleep(10)

# Cerrar el navegador
driver.quit()
