from pygame import mixer

from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image
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

def procesarCanciones(ruta): #Almacenando ,recorriendo e identificandio la informarcion
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
          img = imagen.text.replace('"',"")
      for ruta in cancion.iter("ruta"):
          #print("Ruta:", ruta.text.replace('"',""))
          ru = ruta.text.replace('"',"")
          listaSu.append(Biblioteca(artist,albu,song,img,ru))
    canciones()
      

def canciones():
    for i in range(listaSu.len()):
        table1.insert("", END, text=str(listaSu[i].cancion),values=(str(listaSu[i].album).replace('"',""), str(listaSu[i].artista).replace('"',"")))
        

def canciones2():
    for i in range(listaSu.len()):    
        table3.insert("", END, text=str(listaSu[i].cancion),values=(str(listaSu[i].album).replace('"',""), str(listaSu[i].artista).replace('"',"")))

def Play(ruta):
    global mixer
    mixer.init()
    mixer.music.load(ruta)
    mixer.music.set_volume(0.2)
    mixer.music.play()

def Pause():
    mixer.music.pause()

def Reanudar():
    mixer.music.unpause()

def get_data():
    cancion = table1.item(table1.selection())["text"]
    album = table1.item(table1.selection())["values"][0]
    artista = table1.item(table1.selection())["values"][1]
    label1['text'] = "Cancion: "+cancion
    label2['text'] = "Artista: "+artista
    label4['text'] = "Album: "+album
    ruta = get_ruta(cancion)
    imagen = get_img(cancion)
    Play(ruta)
    MostrarImagen(imagen)

def get_img(nombre):
    for i in range(listaSu.len()):
        if nombre == listaSu[i].cancion:
            return listaSu[i].imagen
        

def get_ruta(cancion):
    for i in range(listaSu.len()):
        if cancion == listaSu[i].cancion:
            return listaSu[i].ruta

def MostrarImagen(ruta):
  img = Image.open(ruta)
  new_img = img.resize((320,320))
  render = ImageTk.PhotoImage(new_img)
  img1 = Label(ventana, image=render)
  img1.image = render
  img1.place(x=30, y = 65)


def addSong():
    cancion = table3.item(table3.selection())["text"]
    album = table3.item(table3.selection())["values"][0]
    artista = table3.item(table3.selection())["values"][1]
    table4.insert("", END, text=cancion,values=(album,artista ))



def crearLista():
   
    ventanaLista = Tk()
    ventanaLista.title("IPCmusic CREAR LISTA DE REPRODUCCION")

    label3 = Label(ventanaLista,text="LISTA", width=15,height=1)
    label3.config(fg="blue",bg="yellow", font=("Veranda",13))
    label3.place(x = 60,y = 10)    

    label12 = Label(ventanaLista,text="Nombre :")
    label12.place(x = 15,y = 60)
        
    btnagregar = Button(ventanaLista, text="Agregar cancion", width=20,height=2, command=addSong)
    btnagregar.place(x= 50, y=120)
     
    btnMostrar = Button(ventanaLista, text="Mostrar Biblioteca", width=20,height=1,command=canciones2)
    btnMostrar.place(x= 400, y=10)
    global table3
    table3 = ttk.Treeview(ventanaLista, columns=("Album","Artista") ,height=10)
    table3.column("#0", width=115)
    table3.column("Album", width=115, anchor=CENTER)
    table3.column("Artista", width=115, anchor= CENTER)
    table3.heading("#0",text="CANCION", anchor=CENTER)
    table3.heading("Album",text="ALBUM", anchor=CENTER)
    table3.heading("Artista",text="ARTISTA", anchor=CENTER)  
    table3.place(x=300,y=40)

    label14 = Label(ventanaLista,text="Canciones Agregadas a la Lista", width=30,height=1)
    label14.config(fg="blue",bg="yellow", font=("Veranda",13))
    label14.place(x = 330,y = 290)
    global table4
    table4 = ttk.Treeview(ventanaLista, columns=("Album","Artista") ,height=10)
    table4.column("#0", width=115)
    table4.column("Album", width=115, anchor=CENTER)
    table4.column("Artista", width=115, anchor= CENTER)
    table4.heading("#0",text="CANCION", anchor=CENTER)
    table4.heading("Album",text="ALBUM", anchor=CENTER)
    table4.heading("Artista",text="ARTISTA", anchor=CENTER)  
    table4.place(x=300,y=320)
   
    btnsavelista = Button(ventanaLista, text="Guardar Lista", width=20,height=2)
    btnsavelista.place(x= 50, y=420)

    ventanaLista.geometry('700x580+300+50')
    ventanaLista.mainloop()


if __name__ == '__main__':
    global listaSu, listSong
    listaSu = Lista()
    listSong = Lista()

    ventana = Tk()
    ventana.title("IPCmusic HOME")

    btnCargar = Button(ventana, text="Cargar canciones", width=18,height=2, command=cargarcanciones)
    btnCargar.place(x= 10, y=10)

    btnLista = Button(ventana, text="Crear lista de reprodccion", width=20, height=2, command=  lambda: [crearLista()])
    btnLista.place(x= 820, y=5)

    btnReportes = Button(ventana, text="Reportes", width=8, height=2)
    btnReportes.place(x= 160, y=10)

    play = Button(ventana, text="PLAY", width=8, height=2, command=get_data)
    play.place(x= 20, y=400)

    pause = Button(ventana, text="PAUSE", width=8, height=2, command=Pause)
    pause.place(x= 90, y=400)

    reanudar = Button(ventana, text="REANUDAR", width=9, height=2, command=Reanudar)
    reanudar.place(x= 160, y=400)


    label1 = Label(ventana,text="Cancion:")
    label1.place(x = 100,y = 460)

    label2 = Label(ventana,text="Artista:")
    label2.place(x = 100,y = 490)

    label4 = Label(ventana,text="Album:")
    label4.place(x = 100,y = 520)
#-----------------------------------------------------------------------------------
    label3 = Label(ventana,text="BIBLIOTECA", width=13,height=1)
    label3.config(fg="blue",bg="yellow", font=("Veranda",33))
    label3.place(x = 380,y = 13)

    table1 = ttk.Treeview(ventana, columns=("Album","Artista") ,height=26)
    table1.column("#0", width=115)
    table1.column("Album", width=115, anchor=CENTER)
    table1.column("Artista", width=115, anchor= CENTER)
    table1.heading("#0",text="CANCION", anchor=CENTER)
    table1.heading("Album",text="ALBUM", anchor=CENTER)
    table1.heading("Artista",text="ARTISTA", anchor=CENTER)
         
    
    table1.place(x=380,y=65)
    #-------------------------------------------------------------------------------------
    label8 = Label(ventana,text="LISTAS DE REPRODUCCION", width=25,height=1)
    label8.config(fg="blue",bg="yellow", font=("Veranda",12))
    label8.place(x = 780,y = 50)

    table2 = ttk.Treeview(ventana, columns=("Canciones") ,height=13)
    table2.column("#0", width=115)
    table2.column("Canciones", width=115, anchor=CENTER)
    table2.heading("#0",text="NOMBRE", anchor=CENTER)
    table2.heading("Canciones",text="No. CANCIONES", anchor=CENTER)
    table2.place(x=780,y=70)

    label11 = Label(ventana,text="Modo:")
    label11.place(x = 820,y = 495)
    comboModo = ttk.Combobox(ventana, height=1, width=15, values=['---','Normal','Aleatorio'], state="readonly")
    comboModo.current(0)
    comboModo.place(x = 820,y =520)

    ventana.geometry('1050x660+200+40')
    ventana.mainloop()