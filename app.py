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
        self.lista_tareas = []
        self.var = BooleanVar() 
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
        self.label_width = Label(self.frame_lista_tareas, text="", width=50)
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
        self.nombre_tarea = self.entrada.get(1.0, '1.end') #Desde la línea 1 hasta el final de la línea 1
        #Comprueba si hay algo escrito para mostrarlo
        if len(self.nombre_tarea) != 0:
            self.entrada.delete(1.0, 'end')
            self.mostrar_tarea()


    #Mostrar tareas
    def mostrar_tarea(self):
        '''Crea un nuevo widget (Checkbutton) con el texto de la entrada y lo añade a la lista'''
        self.tarea = Checkbutton(self.frame_lista_tareas,
                            text=self.nombre_tarea,
                            variable="",
                            font=('Roboto', 16),
                            highlightthickness=0)
        self.tarea.pack(anchor="w")
        #Genera el evento para marcar la tarea como completada
        self.tarea.bind("<Button-1>", self.on_click)


    #Marcar o desmarcar tarea completada
    def on_click(self, event):
        #Si el estado del widget es 'active' o 'normal'
        if event.widget.cget('state') in ['active', 'normal']:
            self.var.set(True)
            #Desabilita el checkbuton pulsado y cambia el estilo para indicar que la tarea está completada
            event.widget.config(text=event.widget.cget('text'), variable=self.var,
                                font=('Roboto', 16, 'overstrike'), state='disabled')
            
        #Si el estado del widget es otro ('disabled')
        else:
            self.var.set(False)
            event.widget.config(text=event.widget.cget('text'), variable=self.var,
                                font=('Roboto', 16),
                                state='normal')


    def limpiar_tareas(self): 
        for widget in self.frame_lista_tareas.winfo_children():
            if widget.cget('state') == 'disabled':
                widget.destroy()
    

    def borrar_tareas(self):
        for widget in self.frame_lista_tareas.winfo_children():
            widget.destroy()
        #Crear el widget Label (vacío) que mantiene el ancho del frame para la lista de tareas
        self.label_width = Label(self.frame_lista_tareas, text="", width=50)
        self.label_width.pack() 

        

app = App(Tk())
app.window.mainloop()