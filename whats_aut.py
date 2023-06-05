import xlrd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Edge()
start_url = ('https://web.whatsapp.com')

driver.get(start_url)

time.sleep(20)

#de aqui sacamos los numeros
excelFile = xlrd.open_workbook("num.xls")
sheet1 = excelFile.sheet_by_index(0)

for i in range(1, sheet1.nrows):
    
    #elementos de el campo de busqueda
    numeros = int(sheet1.cell_value(rowx = i, colx = 0))
    file_s= driver.find_element(By.CLASS_NAME, 'selectable-text.copyable-text')
    
    try:
        file_s.send_keys(numeros)
        time.sleep(1)
        file_s.send_keys(Keys.ENTER)

    # Esperar unos segundos para asegurarse de que se haya abierto la conversación
        time.sleep(2)

    # Enviar el mensaje utilizando pywhatkit
        chat_box = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        
        # Esperar unos segundos para que el mensaje se envíe antes de pasar al siguiente número
        time.sleep(1)
        chat_box.send_keys("Mensaje")
        chat_box.send_keys(Keys.ENTER)
    
    except Exception as e:
        print('no se envio')
        de = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/span/button/span')
        de.click()
        continue
    continue

#Cerrar el navegador
driver.quit() 
