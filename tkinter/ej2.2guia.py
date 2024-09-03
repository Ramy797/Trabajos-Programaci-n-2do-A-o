


import tkinter as tk




ventana = tk.Tk()
ventana.geometry("400x400")
ventana.title("peliculas")

def Crear_ventana_error():
    ventana_error2 =tk.Toplevel()
    ventana_error2.geometry("275x75")
    ventana_error2.title("ERROR")
    ventana_error2.config(background="red")

    lbl5=tk.Label(ventana_error2,text="la pelicula ya fue ingresada")
    lbl5.place(x=30,y=10)
    lbl5.config(background="red")

    button_cerrar=tk.Button(ventana_error2,text="cerrar",command=ventana_error2.destroy)
    button_cerrar.place(x=120,y=35,)


def añadirPelicula():

    pelicula=entry_var.get()
    if pelicula in widgetlist.get(0,tk.END):
        Crear_ventana_error()
    else:
        widgetlist.insert(tk.END,pelicula)
    entry_var.set("")
    



lbl1=tk.Label(ventana,text="ingrese la pelicula")
lbl1.place(x=25,y=25)


lbl2=tk.Label(ventana,text="peliculas")
lbl2.place(x=200,y=25)


entry_var=tk.StringVar(ventana)
entry=tk.Entry(ventana,textvariable=entry_var)
entry.place(x=25,y=50)


widgetlist=tk.Listbox(ventana)
widgetlist.place(x=200,y=50)


button1=tk.Button(ventana,text="Añadir",command=añadirPelicula)
button1.place(x=30, y=75)








ventana.mainloop()