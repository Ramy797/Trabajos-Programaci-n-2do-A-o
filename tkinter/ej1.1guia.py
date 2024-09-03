"""Escribir una aplicación GUI (llamada ContCreciente) como la que se
ve en la figura. Cada vez que se haga clic en el botón "+", el valor del
contador se incrementa en 1.
El programa lleva 3 componentes:
1 - Una Etiqueta "Contador"
2 - Un lineEdit no editable, que muestre el valor del contador
3 - Un Botón "+"""



import tkinter as tk

ventana=tk.Tk()
ventana.geometry("300x100")
ventana.title("ContCreciente")

lbl1=tk.Label(ventana,text="CONTADOR")
lbl1.grid(row=1, column=2)


entry_var=tk.StringVar(value="0")
entry=tk.Entry(textvariable=entry_var)
entry.grid(row=2,column=2)
entry.config(state=tk.DISABLED)



def incrementar():
    valor=int (entry_var.get())
    valor +=1
    entry_var.set(valor)

button=tk.Button(text="+",command=incrementar)
button.grid(row=2,column=1)



ventana.mainloop()