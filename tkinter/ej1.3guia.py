"""Escribir una aplicación GUI (llamada Factorial) como la que se ve en
la figura. Cada ves que se haga clic en el botón "Siguiente", debe
calcular el factorial del primer lineEdit y mostrarlo en el segundo. Al
dar siguiente (n se incrementa en 1) n = 2 con su factorial
correspondiente."""
import tkinter as tk

def Factorial():
    num = int(entry_var.get())
    if num==1 or num ==0:
        resultado=1
    else:
        resultado = num * FacotrialRecursico(num-1)

    entryResultado_var.set(resultado)  

def FacotrialRecursico(num):
    if num==0 or num ==1:
        return 1
    else:
        return num * FacotrialRecursico(num-1)
    
 
def incrementar()    :
    n= int(entry_var.get())
    n+=1
    return entry_var.set(n)
def ejecutar():
    Factorial()
    incrementar()


ventana = tk.Tk()
ventana.geometry("500x100")
ventana.title("Factorial")

lbl1=tk.Label(ventana,text="n")
lbl1.grid(row=1,column=1)


entry_var=tk.StringVar(value="1")
entryNumero=tk.Entry(ventana,textvariable=entry_var)
entryNumero.grid(row=1,column=2)
entryNumero.config(state="disabled")


lbl2=tk.Label(ventana,text="Factorial(n)")
lbl2.grid(row=1,column=3)


entryResultado_var= tk.StringVar(value="")
entryResultado=tk.Entry(ventana,textvariable=entryResultado_var)
entryResultado.grid(row=1,column=4)
entryResultado.config(state="disabled")
buttonSig=tk.Button(ventana,text="Siguiuente",command=ejecutar)
buttonSig.grid(row=1,column=5)



    
ventana.mainloop()