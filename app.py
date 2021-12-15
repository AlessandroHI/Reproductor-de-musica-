from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from Biblioteca import Biblioteca
from Lista import Lista
from xml.etree import ElementTree

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
        return archivo

def cargarcanciones():
    archivo = Buscar_archivo()
    procesarCanciones(archivo)       

def procesarCanciones(ruta): #Almacenando recorriendo y identificandio la informarcion
    global listaSu
    archivoXML = ElementTree.parse(ruta)
    root = archivoXML.getroot()
    listaArtistas = Lista()


    for cancion in root:
      #print("Nombre cancion:",cancion.attrib["nombre"])
      song = cancion.attrib["nombre"]
      for artista in cancion.iter("artista"):
         # print("Artista:",artista.text.replace('"',""))
          artist = artista.text
      for album in cancion.iter("album"):
         # print("Album:",album.text.replace('"',""))
          albu = album.text
      for imagen in cancion.iter("imagen"):
          #print("Imagen:",imagen.text.replace('"',""))
          img = imagen.text
      for ruta in cancion.iter("ruta"):
          #print("Ruta:", ruta.text.replace('"',""))
          ru = ruta.text
          listaSu.append(Biblioteca(artist,albu,song,img,ru))
    canciones()
      

def canciones():
    for i in range(listaSu.len()):
        arbol.insert("", END, text=str(listaSu[i].cancion),values=(str(listaSu[i].album).replace('"',""), str(listaSu[i].artista).replace('"',"")))

def crearLista():
    ventanaLista = Tk()
    ventanaLista.title("IPCmusic CREAR LISTA DE REPRODUCCION")
    ventanaLista.geometry('650x400+300+100')
    ventanaLista.mainloop()


if __name__ == '__main__':
    global listaSu, listSong
    listaSu = Lista()
    listSong = Lista()

    ventana = Tk()
    ventana.title("IPCmusic")
    
    btnCargar = Button(ventana, text="Cargar canciones", width=18,height=1, command=cargarcanciones)
    btnCargar.place(x= 10, y=10)

    btnLista = Button(ventana, text="Crear lista de reprodccion", width=20, height=1, command= crearLista)
    btnLista.place(x= 900, y=10)

    btnReportes = Button(ventana, text="Reportes", width=8, height=1)
    btnReportes.place(x= 1100, y=10)

    label1 = Label(ventana,text="Cancion: Pompeii")
    label1.place(x = 100,y = 360)

    label2 = Label(ventana,text="Artista: Bastille")
    label2.place(x = 100,y = 390)

    label4 = Label(ventana,text="Album: Bastille")
    label4.place(x = 100,y = 420)

    label3 = Label(ventana,text="BIBLIOTECA", width=13,height=1)
    label3.config(fg="blue",bg="yellow", font=("Veranda",33))
    label3.place(x = 380,y = 13)

    arbol = ttk.Treeview(ventana, columns=("Album","Artista") ,height=24)
    arbol.column("#0", width=115)
    arbol.column("Album", width=115, anchor=CENTER)
    arbol.column("Artista", width=115, anchor= CENTER)
    arbol.heading("#0",text="Cancion", anchor=CENTER)
    arbol.heading("Album",text="Album", anchor=CENTER)
    arbol.heading("Artista",text="Artista", anchor=CENTER)
    arbol.place(x=380,y=65)
    ventana.geometry('1200x600+180+100')
    ventana.mainloop()