from tkinter import *
from tkinter import filedialog
from tkinter import ttk

def Buscar_archivo():  # FUNCION QUE REALIZAR LA SELLECION DEL ARCHIVO A CARGAR 
  
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title="Seleccionar un archivo",
        initialdir="./",
        filetypes=(
            ("Archivos xml", "*.xml"),
        )
    )
    if archivo is None:
        print('No se seleccionó ningun archivo\n')
        return None
    else:
        texto = archivo.read()
        archivo.close()
        print('Lectura exitosa\n')
        return texto

def crearLista():
    ventanaLista = Tk()
    ventanaLista.title("IPCmusic CREAR LISTA DE REPRODUCCION")

    ventanaLista.geometry('650x400+300+100')
    ventanaLista.mainloop()



if __name__ == '__main__':

    ventana = Tk()
    ventana.title("IPCmusic")
    
    btnCargar = Button(ventana, text="Cargar canciones", width=18,height=1, command=Buscar_archivo)
    btnCargar.place(x= 5, y=10)

    btnLista = Button(ventana, text="Crear lista de reprodccion", width=20, height=1, command= crearLista)
    btnLista.place(x= 150, y=10)

    btnReportes = Button(ventana, text="Reportes", width=8, height=1)
    btnReportes.place(x= 580, y=10)

    label1 = Label(ventana,text="Cancion: Pompeii")
    label1.place(x = 330,y = 160)

    label2 = Label(ventana,text="Artista: Bastille")
    label2.place(x = 330,y = 190)

    label4 = Label(ventana,text="Album: Bastille")
    label4.place(x = 330,y = 220)
   

    ventana.geometry('650x400+200+100')
    ventana.mainloop()