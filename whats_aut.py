import pywhatkit
import xlrd


"""
root = tk.Tk()
myapp = App(root)
myapp.mainloop()


root = Tk()

root.mainloop()
#filed = input("introduce el nombre de el archivo exel y su extencion: ")
excelFile = xlrd.open_workbook('num.xls')

#numero de sheets
#print(excelFile.nsheets)
mensaje = input()

sheet1 = excelFile.sheet_by_index(0)
#numero de filas 
print(sheet1.nrows)

for nums in  range(3):
    numeros = sheet1.cell_value(rowx = nums, colx = 0)
    nombre = sheet1.cell_value(rowx = nums, colx = 1)
    if numeros != str(numeros):
        intnums= int(numeros)

    try:
        #definimos el numero y el mensaje esta funcion envia el mensaje de inmediato
        pywhatkit.sendwhatmsg_instantly(intnums, "mi" )
        print("Se mando")

    except:
        print("no se mando ")"""