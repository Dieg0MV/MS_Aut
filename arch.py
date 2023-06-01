import xlrd
import pywhatkit
from selenium import webdriver
#imprime la primera columna y la primer fila
#print(sheet1.cell_value(rowx = 0, colx = 0))
#print(sheet1.nrows)
driver = webdriver.Chrome('//home/mrhead/Descargas/geckodriver')
driver.get('https://web.whatsapp.com')

time.sleep(10)

#de aqui sacamos los numeros
excelFile = xlrd.open_workbook("name.xls")
sheet1 = excelFile.sheet_by_index(0)

for i in range(0, sheet1.nrows):
    #elementos de el campo de busqueda
    file_s = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')


    numeros = sheet1.cell_value(rowx = i, colx = 0)

    file_s.send_keys(numeros)

    file_s.send_keys(u'\ue007')

    # Esperar unos segundos para asegurarse de que se haya abierto la conversación
    time.sleep(5)

    # Enviar el mensaje utilizando pywhatkit
    pywhatkit.sendwhatmsg_instantly(numeros, "hola mundo")

    # Esperar unos segundos para que el mensaje se envíe antes de pasar al siguiente número
    time.sleep(10)

# Cerrar el navegador
driver.quit()

    #inter = "+" + str(numeros)
    #mi = str(numeros)
