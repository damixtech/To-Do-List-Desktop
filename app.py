from tkinter import *
from ttkbootstrap import Style


#Class
class App():
    def __init__(self, window):
        self.style = Style(theme='morph')
        self.window = window
        self.window.title('To-do')
        self.window.geometry('450x500')
        self.window.minsize(400,600)

        #PROBANDO NUEVO MÉTODO
        self.vars_control = {}
        
        #Llamar a la función que crea los widgets
        self.create_widgets()
        
    
    #Crear widgets
    def create_widgets(self):
        #Título
        self.title = Label(self.window, text='To-do list',  pady=30,
                           font=('Roboto', 16, 'bold'))
        self.title.pack()
        #Frame añadir tarea
        self.frame_añadir_tarea = Frame(self.window)
        self.frame_añadir_tarea.pack()
        ##Barra para nombrar tarea
        self.entrada = Text(self.frame_añadir_tarea,
                            height=1, font=('Roboto', 14), width=15)
        self.entrada.pack(side='left')
        ##Boton para añadir tarea
        self.boton_crear = Button(self.frame_añadir_tarea, text="Añadir tarea",
                                  command=self.añadir_tarea, font=('Roboto', 16))
        self.boton_crear.pack(side='left')
        
        #Frame para lista de tareas
        self.frame_lista_tareas = Frame(self.window, height=100)
        self.frame_lista_tareas.pack()
        ##Label vacía para dar anchura al frame de la lista de tareas
        self.label_width = Label(self.frame_lista_tareas, width=50)
        self.label_width.pack()   

        #Frame para botones inferiores
        self.frame_botones_borrar = Frame(self.window)
        self.frame_botones_borrar.pack()
        ##Botón borrar tareas completas
        self.boton_borrar_completadas = Button(self.frame_botones_borrar,
                                               text="Limpiar",
                                               command=self.limpiar_tareas,
                                               font=('Roboto', 12, 'bold'))
        self.boton_borrar_completadas.pack(side='left')
        ##Botón borrar todas las tareas
        self.boton_borrar_todas = Button(self.frame_botones_borrar,
                                         text="Vaciar", command=self.borrar_tareas,
                                         font=('Roboto', 12, 'bold'))
        self.boton_borrar_todas.pack(side='left')


    #Añadir tarea
    def añadir_tarea(self):
        #Desde la línea 1 hasta el final de la línea 1
        self.nombre_tarea = self.entrada.get(1.0, '1.end') 
        #Comprueba si hay algo escrito para mostrarlo
        if len(self.nombre_tarea) != 0:
            self.entrada.delete(1.0, 'end')
            self.mostrar_tarea()


    #Mostrar tareas
    def mostrar_tarea(self):
        '''Crea un nuevo widget (Checkbutton) con el texto de la entrada
        y lo añade a la lista'''
        self.var = BooleanVar()
        var_value = self.var.get()
        self.vars_control[self.nombre_tarea] = var_value
        self.tarea = Checkbutton(self.frame_lista_tareas,
                            text=self.nombre_tarea,
                            variable=self.var,
                            font=('Roboto', 16),
                            highlightthickness=0,
                            )
        self.tarea.pack(anchor="w")
        #Genera un evento al marcar o desmarcar un checkbutton con el botón
        #izquierdo del ratón
        self.tarea.bind("<Button-1>", self.on_click)


    #Marcar o desmarcar tarea completada
    def on_click(self, event):
        #Extrae el nombre de la tarea (Clave en el diccionario de variables)
        tarea = event.widget.cget('text')
        #Extrae el valor de la variable de control almacenada en el dict
        #vars_contorl con la clave [tarea]
        var = self.vars_control[tarea] #Valor (True o False)
        
        #Cambiar valores de las variables
        if var == False:
            self.vars_control[tarea] = True
        else:
            self.vars_control[tarea] = False
        
        #Si el valor de la variable es True
        if self.vars_control[tarea] == True:
            #Cambia el estilo para indicar que la tarea está completada
            event.widget.config(font=('Roboto',16, 'overstrike'))
        #Si el valor de la variable es False
        else:
            #Vuelve a poner la fuente como al inicio, sin 'overstrike'
            event.widget.config(font=('Roboto', 16))
            

    def limpiar_tareas(self): 
        '''Comprueba las tareas que están marcadas y las elimina'''
        for widget in self.frame_lista_tareas.winfo_children():
            tipo = widget.winfo_class()
            if tipo == 'Checkbutton':
                tarea = widget.cget('text')
                if self.vars_control[tarea] == True:
                    widget.destroy()


    def borrar_tareas(self):
        '''Elimina todas las tareas, estén o no marcadas'''
        for widget in self.frame_lista_tareas.winfo_children():
            tipo = widget.winfo_class()
            if tipo == 'Checkbutton':
                widget.destroy()
        

app = App(Tk())
app.window.mainloop()