#Esta es la version final del programa
import xlrd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import filedialog

class MSGimg:
    def __init__(self):
        message = input('escribe tu mensaje: ')
        filename= filedialog.askopenfilename()
        image_path= filedialog.askopenfilename()
        #configuraciones para manejar el browser 
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.start_url = 'https://web.whatsapp.com'
        self.driver.get(self.start_url)
        wait = WebDriverWait(self.driver, 30)
        
        # De aquí sacamos los números
        self.filename = filename
        self.excelFile = xlrd.open_workbook(self.filename)
        self.sheet1 = self.excelFile.sheet_by_index(0)

        #recorremos la lista de numeros por fila
        for i in range(1, self.sheet1.nrows):
                
                # Elementos del campo de búsqueda
                numeros = self.sheet1.cell_value(rowx=i, colx=1)
                if not numeros:
                     print("listo")
                     break
                
                file_s = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')))
                time.sleep(5)
         
                file_s.send_keys(int(numeros))
                time.sleep(1)
                file_s.send_keys(Keys.ENTER)

                # Esperar unos segundos para asegurarse de que se haya abierto la conversación
                time.sleep(2)
    
                chat_box = self.driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')

                # Esperar unos segundos para que el mensaje se envíe antes de pasar al siguiente número
                time.sleep(1)
                self.message = message
                chat_box.send_keys(self.message)
                chat_box.send_keys(Keys.ENTER)
                time.sleep(5)
                
                # Hacer clic en el botón de adjuntar archivo
                attach_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span')))        
                attach_button.click()

                # Seleccionar la opción de enviar una imagen
                image_option = self.driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input')
                image_option.send_keys(image_path)
                
    
class MSsingle:
    def __init__(self):
        message = input('ingresa tu mensaje: ')
        filename = filedialog.askopenfilename()
        #configuraciones para manejar el browser 
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.start_url = 'https://web.whatsapp.com'
        self.driver.get(self.start_url)
        wait = WebDriverWait(self.driver, 30)
        
        # De aquí sacamos los números
        self.filename = filename
        self.excelFile = xlrd.open_workbook(self.filename)
        self.sheet1 = self.excelFile.sheet_by_index(0)

        #recorremos la lista de numeros por fila
        for i in range(1, self.sheet1.nrows):
                
                # Elementos del campo de búsqueda
                numeros = self.sheet1.cell_value(rowx=i, colx=1)
                if not numeros:
                     print("listo", self.sheet1.nrows)
                     break
                
                file_s = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')))
                time.sleep(5)
         
                file_s.send_keys(int(numeros))
                time.sleep(1)
                file_s.send_keys(Keys.ENTER)

                # Esperar unos segundos para asegurarse de que se haya abierto la conversación
                time.sleep(2)

                chat_box = self.driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')

                # Esperar unos segundos para que el mensaje se envíe antes de pasar al siguiente número
                time.sleep(1)
                self.message = message
                chat_box.send_keys(self.message)
                chat_box.send_keys(Keys.ENTER)
                time.sleep(3)

while True:
    option = int(input("Seleccione 1 si quieres enviar un mensaje con imagen, 2 para un mensaje simple: "))
    if option == 1:
        if __name__ == '__main__':
            MSGimg()
        break 
    elif option == 2:
        if __name__ == '__main__':
            MSsingle()
        break
    else:
        print("Opción no válida. Por favor, seleccione 1 o 2.")
