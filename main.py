from tkinter import Tk,Button,Entry,Label,Toplevel,messagebox
from bbdd import Connector

#acciones
def accion_registrar(txt_identificacion,txt_nombre,txt_centro):
    #print(f"{txt_identificacion.get()} {txt_nombre.get()} {txt_centro.get()}")
    identificacion = txt_identificacion.get()
    nombre = txt_nombre.get()
    centro = txt_centro.get()

    obj_connector = Connector()
    resultado = obj_connector.registrar(identificacion,nombre,centro)
    obj_connector.close_connection()

    messagebox.showinfo(title="OUTPUT",message=resultado)

    txt_identificacion.delete(0,'end')
    txt_nombre.delete(0,'end')
    txt_centro.delete(0,'end')

def accion_buscar(txt_identificacion):
    identificacion = txt_identificacion.get()

    obj_connector = Connector()
    resultado = obj_connector.buscar(identificacion,)
    obj_connector.close_connection()

    if len(resultado) == 0:
        messagebox.showinfo(title="OUTPUT",message="No hay resultados")
    else:
        messagebox.showinfo(title="OUTPTU",message=resultado)
    txt_identificacion.delete(0,'end')

def accion_eliminar(txt_identificacion):
    identificacion = txt_identificacion.get()

    obj_connector = Connector()
    resultado = obj_connector.eliminar(identificacion,)
    obj_connector.close_connection()

    messagebox.showinfo(title="OUTPUT",message=resultado)

    txt_identificacion.delete(0,'end')

def accion_editar(txt_identificacion,txt_centro):
    identificacion = txt_identificacion.get()
    centro = txt_centro.get()

    obj_connector = Connector()
    resultado = obj_connector.editar(centro,identificacion)
    obj_connector.close_connection()

    messagebox.showinfo(title="OUTPUT",message=resultado)
    txt_identificacion.delete(0,'end')
    txt_centro.delete(0,'end')

#acciones

#interfaces graficas de los botones de la ventana principal****************
def ventana_registrar():
    ventana_registrar = Toplevel()
    ventana_registrar.title("REGISTRAR")
    ventana_registrar.geometry("400x200")
    
    lbl_identificacion = Label(ventana_registrar,text="Identificacion:",font=("Arial",13))
    lbl_nombre = Label(ventana_registrar,text="Nombre y Apellidos:",font=("Arial",13))
    lbl_centro = Label(ventana_registrar,text="Centro de Estudio:",font=("Arial",13))

    txt_identificacion = Entry(ventana_registrar,font=("Arial",13))
    txt_nombre = Entry(ventana_registrar,font=("Arial",13))
    txt_centro = Entry(ventana_registrar,font=("Arial",13))
    
    bttn_registrar = Button(ventana_registrar,text="Registrar",font=("Arial",13),command=lambda:accion_registrar(txt_identificacion,txt_nombre,txt_centro))

    lbl_identificacion.grid(row=0,column=0)
    txt_identificacion.grid(row=0,column=1)

    lbl_nombre.grid(row=1,column=0)
    txt_nombre.grid(row=1,column=1)

    lbl_centro.grid(row=2,column=0)
    txt_centro.grid(row=2,column=1)

    bttn_registrar.grid(row=3,column=0,columnspan=2)

    ventana_registrar.columnconfigure(0,weight=1)
    ventana_registrar.columnconfigure(1,weight=1)

    ventana_registrar.rowconfigure(0,weight=1)
    ventana_registrar.rowconfigure(1,weight=1)
    ventana_registrar.rowconfigure(2,weight=1)
    ventana_registrar.rowconfigure(3,weight=1)

    ventana_registrar.mainloop()

def ventana_buscar():
    ventana_buscar = Toplevel()
    ventana_buscar.title("BUSCAR")
    ventana_buscar.geometry("400x100")

    lbl_identificacion = Label(ventana_buscar,text="Identificacion:",font=("Arial",13))
    txt_identificacion = Entry(ventana_buscar,font=("Arial",13))

    bttn_buscar = Button(ventana_buscar,text="Buscar",font=("Arial",13),command=lambda:accion_buscar(txt_identificacion))

    lbl_identificacion.grid(row=0,column=0)
    txt_identificacion.grid(row=0,column=1)
    bttn_buscar.grid(row=1,column=0,columnspan=2)

    ventana_buscar.columnconfigure(0,weight=1)

    ventana_buscar.rowconfigure(0,weight=1)
    ventana_buscar.rowconfigure(1,weight=1)

    ventana_buscar.mainloop()

def ventana_editar():
    ventana_editar = Toplevel()
    ventana_editar.title("EDITAR")

    lbl_identificacion = Label(ventana_editar,text="Identificacion:",font=("Arial",13))
    txt_identificacion = Entry(ventana_editar,font=("Arial",13))

    lbl_centro = Label(ventana_editar,text="Centro de Estudio:",font=("Arial",13))

    txt_centro = Entry(ventana_editar,font=("Arial",13))

    bttn_editar = Button(ventana_editar,text="Editar",font=("Arial",13),command = lambda : accion_editar(txt_identificacion,txt_centro))

    lbl_identificacion.grid(row=0,column=0)
    txt_identificacion.grid(row=0,column=1)

    lbl_centro.grid(row=1,column=0)
    txt_centro.grid(row=1,column=1)

    bttn_editar.grid(row=2,column=0,columnspan=2)

    ventana_editar.columnconfigure(0,weight=1)
    ventana_editar.columnconfigure(1,weight=1)

    ventana_editar.rowconfigure(0,weight=1)
    ventana_editar.rowconfigure(1,weight=1)
    ventana_editar.rowconfigure(2,weight=1)

    ventana_editar.mainloop()

def ventana_eliminar():
    ventana_eliminar = Toplevel()
    ventana_eliminar.title("ELIMINAR")

    ventana_eliminar.geometry("400x100")

    lbl_identificacion = Label(ventana_eliminar,text="Identificacion:",font=("Arial",13))
    txt_identificacion = Entry(ventana_eliminar,font=("Arial",13))

    bttn_eliminar = Button(ventana_eliminar,text="Eliminar",font=("Arial",13),command=lambda:accion_eliminar(txt_identificacion))

    lbl_identificacion.grid(row=0,column=0)
    txt_identificacion.grid(row=0,column=1)
    bttn_eliminar.grid(row=1,column=0,columnspan=2)

    ventana_eliminar.columnconfigure(0,weight=1)

    ventana_eliminar.rowconfigure(0,weight=1)
    ventana_eliminar.rowconfigure(1,weight=1)

    ventana_eliminar.mainloop()


#interfaces graficas de los botones de la ventana principal****************

if __name__ == "__main__":#cuando estamso testeando modulos
    #crear la interfaz principal

    ventana = Tk()
    ventana.title("CRUD")
    ventana.geometry('400x200')

    bttn_registrar = Button(ventana,text="Registrar Usuario",font=("Arial",13),command=ventana_registrar)#creando el boton
    bttn_buscar = Button(ventana,text="Buscar Usuario",font=("Arial",13),command=ventana_buscar)#creando el boton
    bttn_editar = Button(ventana,text="Editar Usuario",font=("Arial",13),command=ventana_editar)#creando el boton
    bttn_eliminar = Button(ventana,text = "Eliminar Usuario",font=("Arial",13),command=ventana_eliminar)#creando el boton

    bttn_registrar.grid(row=0,column=0,sticky="nsew")
    bttn_buscar.grid(row=1,column=0,sticky="nsew")
    bttn_editar.grid(row=2,column=0,sticky="nsew")
    bttn_eliminar.grid(row=3,column=0,sticky="nsew")

    ventana.columnconfigure(0,weight=1)

    ventana.rowconfigure(0,weight=1)
    ventana.rowconfigure(1,weight=1)
    ventana.rowconfigure(2,weight=1)
    ventana.rowconfigure(3,weight=1)

    ventana.mainloop()

    #crear la interfaz principal