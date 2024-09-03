"""scribir una aplicación GUI (llamada Calculadora) que funcione como
una simple calculadora.
La aplicación lleva:
1 - Tres etiquetas (Primer número, Segundo número y Resultado)
2 - 3 lineEdit (el lineEdit de Resultado no se puede modificar)
3 - 6 Botones (+, -, *, /, % y RESET). El botón CLEAR debe borrar los
3 lineEdit. Al presionar (+, -, *, / o %) el único campo que se modifica
es Resultado."""
import tkinter as tk
ventana = tk.Tk()


def Crear_ventana_error_calculo():
   ventana_error = tk.Toplevel()
   ventana_error.geometry("275x75")
   ventana_error.title("ERROR EN CALCULO")
   ventana_error.config(background="red")
   lbl4=tk.Label(ventana_error,text="NO ES POSIBLE REALIZAR EL CALCULO")
   lbl4.place(x=20,y=10)   
   lbl4.config(background="red")

   button_cerrar=tk.Button(ventana_error,text="cerrar",command=ventana_error.destroy)
   button_cerrar.place(x=120,y=35)


def Crear_ventana_error_nro():
    ventana_error2 =tk.Toplevel()
    ventana_error2.geometry("275x75")
    ventana_error2.title("ERROR")
    ventana_error2.config(background="red")

    lbl5=tk.Label(ventana_error2,text="INGRESE UNICAMENTE NÚMEROS")
    lbl5.place(x=30,y=10)
    lbl5.config(background="red")

    button_cerrar=tk.Button(ventana_error2,text="cerrar",command=ventana_error2.destroy)
    button_cerrar.place(x=120,y=35,)

def validar_entry(entry):
    valor= entry.get()
    if valor=="":
        return True
    if valor.isdigit():
        return False
    return True


def ejecutar_suma():
    if validar_entry(entry_var) or validar_entry(entry_var2):
        Crear_ventana_error_nro()
    else:
        sumar()

def ejecutar_resta():
    if validar_entry(entry_var) or validar_entry(entry_var2):
        Crear_ventana_error_nro()
    
    else:
        restar()
    
def ejecutar_div():
    n2= entry_var2.get()
    if validar_entry(entry_var) or validar_entry(entry_var2):
        Crear_ventana_error_nro()
    elif float(entry_var2.get())==0:
        Crear_ventana_error_calculo()
    else:
        dividir()

def ejecutar_mult():
    if validar_entry(entry_var) or validar_entry(entry_var2):
        Crear_ventana_error_nro()
    else:
        multiplicar()

def ejecutar_porc():
    if validar_entry(entry_var) or validar_entry(entry_var2):
        Crear_ventana_error_nro()
    else:
        porcentaje()
   
    

def sumar():
    n1=float(entry_var.get())
    n2=float(entry_var2.get())
    resultado = n1+n2
    entry_var3.set(resultado)


def restar():
    n1=float(entry_var.get())
    n2=float(entry_var2.get())
    resultado = n1-n2
    entry_var3.set(resultado)

def multiplicar():
    n1=float(entry_var.get())
    n2=float(entry_var2.get())
    if n2==0:
        Crear_ventana_error_calculo()
    resultado = n1*n2
    entry_var3.set(resultado)

def dividir():
    n1=float(entry_var.get())
    n2=float(entry_var2.get())
    resultado = n1/n2
    entry_var3.set(resultado)

def porcentaje():
    n1=float(entry_var.get())
    n2=float(entry_var2.get())
    resultado = n1*n2
    resultado = resultado/100
    entry_var3.set(resultado)

def clear():
    entry_var.set('')
    entry_var2.set('')
    entry_var3.set('')

ventana.geometry("250x250")
ventana.title("Calculadora")

lbl1=tk.Label(ventana,text="primer número")
lbl1.grid(row=1, column=1,columnspan=2,pady=2,padx=0)

lbl2=tk.Label(ventana,text="segundo número")
lbl2.grid(row=2, column=1,columnspan=2,pady=2,padx=5)


lbl3=tk.Label(ventana,text="resultado")
lbl3.grid(row=3, column=1,columnspan=2,pady=2,padx=5)



entry_var=tk.StringVar(value="")
entryNum=tk.Entry(ventana,textvariable=entry_var)
entryNum.grid(row=1,column=3,columnspan=4)


entry_var2=tk.StringVar(value="")
entryNum2=tk.Entry(ventana,textvariable=entry_var2)
entryNum2.grid(row=2,column=3,columnspan=4)


entry_var3=tk.StringVar(value="")
entryNum3=tk.Entry(ventana,textvariable=entry_var3)
entryNum3.grid(row=3,column=4,columnspan=5)
entryNum3.config(state="disabled")


button1=tk.Button(ventana,text="+",command=ejecutar_suma,)
button1.grid(row=4,column=1,columnspan=3,padx=5,pady=5)

button2=tk.Button(ventana,text="*",command=ejecutar_mult)
button2.grid(row=5,column=1,columnspan=3,padx=5,pady=5)

button3=tk.Button(ventana,text="%",command=ejecutar_porc)
button3.grid(row=6,column=1,columnspan=3,padx=5,pady=5)

button4=tk.Button(ventana,text="-",command=ejecutar_resta)
button4.grid(row=4,column=3,columnspan=6,padx=5,pady=5)


button5=tk.Button(ventana,text="/",command=ejecutar_div)
button5.grid(row=5,column=3,columnspan=6,padx=5,pady=5)


button6=tk.Button(ventana,text="clear",command=clear)
button6.grid(row=6,column=3,columnspan=6,padx=5,pady=5)


ventana.mainloop()