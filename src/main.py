#imports
import tkinter

#functions
def getUnit(number):
    return number%10

def getTen(number):
    return (number%100-number%10)//10

def getHundred(number):
    return (number%1000-number%100)//100

def setResult():
    labelUnit.config(text=str(getUnit(int(entry.get()))))
    labelTen.config(text=str(getTen(int(entry.get()))))
    labelHundred.config(text=str(getHundred(int(entry.get()))))

#form
form = tkinter.Tk()
form.geometry("400x200")

#entry value for number
entryLabel = tkinter.Label(form, text="Ingrese un número")
entryLabel.grid(row=0, column=0)
entry = tkinter.Entry(form)
entry.grid(row=0, column=1)

#button for execute "setResult" function
btnExecute = tkinter.Button(form, text="Ejecutar", command=setResult)
btnExecute.grid(row=1, columnspan=2)

#labels for result
labelUnitInfo = tkinter.Label(form, text="Unidades:")
labelUnitInfo.grid(row=2, column=0)
labelUnit = tkinter.Label(form, text="0")
labelUnit.grid(row=2, column=1)

labelTenInfo = tkinter.Label(form, text="Decenas:")
labelTenInfo.grid(row=3, column=0)
labelTen = tkinter.Label(form, text="0")
labelTen.grid(row=3, column=1)

labelHundredInfo = tkinter.Label(form, text="Centenas:")
labelHundredInfo.grid(row=4, column=0)
labelHundred = tkinter.Label(form, text="0")
labelHundred.grid(row=4, column=1)

form.mainloop()


