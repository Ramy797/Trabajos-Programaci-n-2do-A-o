import tkinter as tk


ventana=tk.Tk()
ventana.geometry("400x300")
ventana.title("Clculadora2")

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

def ejecutar():
    if validar_entry(entry_var1)or validar_entry(entry_var2):
        Crear_ventana_error_nro()
    else:
        calcular()


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

def calcular():
    opcion = opcion_var.get()
    n1=float(entry_var1.get())
    n2=float(entry_var2.get())
    if opcion==1:
        n1=float(entry_var1.get())
        n2=float(entry_var2.get())
        resultado=n1+n2
        entry_var3.set(resultado)

    if opcion==2:
        n1=float(entry_var1.get())
        n2=float(entry_var2.get())
        resultado=n1-n2
        entry_var3.set(resultado)

    if opcion==3:
        n1=float(entry_var1.get())
        n2=float(entry_var2.get())
        resultado=n1*n2
        entry_var3.set(resultado)
    
    if opcion==4:
        if n2==0:
            Crear_ventana_error_calculo()
        else:    
            n1=float(entry_var1.get())
            n2=float(entry_var2.get())
            resultado=n1/n2
            entry_var3.set(resultado)
    
       
    



lbl1=tk.Label(ventana,text="valor 1")
lbl1.place(x=50,y=60)


lbl2=tk.Label(ventana,text="valor 2")
lbl2.place(x=50,y=90)


lbl3=tk.Label(ventana,text="resultado")
lbl3.place(x=40,y=120)

entry_var1=tk.StringVar(ventana)
entry1=tk.Entry(ventana,textvariable=entry_var1)
entry1.place(x=100,y=60)


entry_var2=tk.StringVar(ventana)
entry2=tk.Entry(ventana,textvariable=entry_var2)
entry2.place(x=100,y=90)


entry_var3=tk.StringVar(ventana)
entry3=tk.Entry(ventana,textvariable=entry_var3)
entry3.place(x=100,y=120)
entry3.config(state="disabled")


opcion_var=tk.IntVar()

rbutton1=tk.Radiobutton(ventana,text="Sumar",variable=opcion_var,value=1)
rbutton1.place(x=300,y=60)


rbutton2=tk.Radiobutton(ventana,text="restar",variable=opcion_var,value=2)
rbutton2.place(x=300,y=80)


rbutton3=tk.Radiobutton(ventana,text="multiplicar",variable=opcion_var,value=3)
rbutton3.place(x=300,y=100)


rbutton4=tk.Radiobutton(ventana,text="Dividir",variable=opcion_var,value=4)
rbutton4.place(x=300,y=120)



button1=tk.Button(ventana,text="Clcular",command=ejecutar)
button1.place(x=120,y=160)



ventana.mainloop()