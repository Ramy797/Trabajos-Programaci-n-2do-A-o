"""Escribir una aplicación GUI (llamada Contador) como la que se ve en
la figura. Con 3 botones (Count Up - Para incrementar, Count Down -
Para restar y Reset - Para comenzar de cero).
La aplicación lleva:
1 - Una etiqueta "Contador"
2 - Un lineEdit no editable, que muestre el contador y que inicie en 0
3 - 3 Botones"""
import tkinter as tk
ventana = tk.Tk()
ventana.geometry("500x100")
ventana.title("Factorial")


def incrementar():
    n = int(entry_var.get())
    n+=1
    entry_var.set(n)


def disminuir():
    n = int(entry_var.get())
    n-=1
    entry_var.set(n)

def reset():
    n = int(entry_var.get())
    n=0
    entry_var.set(n)




lbl1=tk.Label(ventana,text="contador",pady=25,padx=25)
lbl1.grid(row=1,column=1)


entry_var=tk.StringVar(value="0")
entryNum=tk.Entry(ventana,textvariable=entry_var)
entryNum.config(state="disabled")
entryNum.grid(row=1,column=2,columnspan=3,padx=10)

buttonCountUp = tk.Button(text="Count Up",command=incrementar)
buttonCountUp.grid(row=1,column=5,padx=10)


buttonCountDown= tk.Button(text="Count Down",command=disminuir)
buttonCountDown.grid(row=1,column=6,padx=10)

buttonReset= tk.Button(text="Reset",command=reset)
buttonReset.grid(row=1,column=7,padx=10)








ventana.mainloop()