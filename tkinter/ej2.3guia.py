import tkinter as tk
import random

def GenerarNumero():

    num1=int(spinBox1.get())
    num2=int(spinBox2.get())
    
    generado =int(random.randint(num1,num2))
    entry_var.set(generado)


ventana=tk.Tk()
ventana.geometry("400x400")
ventana.title("Generador de numeros")

lbl1=tk.Label(ventana,text="Número 1")
lbl1.place(x=100,y=60)


lbl2=tk.Label(ventana,text="Número 2")
lbl2.place(x=100,y=120)


lbl3=tk.Label(ventana,text="Número generado")
lbl3.place(x=100,y=200)


spinBox1=tk.Spinbox(ventana,from_=1,to=100)
spinBox1.place(x=200,y=60)



spinBox2=tk.Spinbox(ventana,from_=1,to=100)
spinBox2.place(x=200,y=120)


entry_var=tk.StringVar(ventana)
entry1=tk.Entry(ventana,textvariable=entry_var)
entry1.place(x=230,y=200)


button1=tk.Button(ventana,text="Generar",command=GenerarNumero)
button1.place(x=200, y=250)


ventana.mainloop()