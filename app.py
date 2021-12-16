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
        table1.insert("", END, text=str(listaSu[i].cancion),values=(str(listaSu[i].album).replace('"',""), str(listaSu[i].artista).replace('"',"")))
        

def canciones2():
    for i in range(listaSu.len()):    
        table3.insert("", END, text=str(listaSu[i].cancion),values=(str(listaSu[i].album).replace('"',""), str(listaSu[i].artista).replace('"',"")))

def changeArtista(): #CAMBIOS DE ARTISTAS
   listaOp =  []
   for i in range(listaSu.len()):
       listaOp.append(listaSu[i].artista.replace('"',""))

   comboArtista['values'] = listaOp 
   comboArtista1['values'] = listaOp 

def changeAlbum(): #CAMBIOS DE ALBUNES SEGUN ARTISTA
   listaOp =  []
   for i in range(listaSu.len()):
       listaOp.append(listaSu[i].album.replace('"',""))

   comboAlbum['values'] = listaOp
   comboAlbum1['values'] = listaOp

def changeSong(): #CAMBIONS DE CANCINES SEGUN ALBUM 
   listaOp =  []
   for i in range(listaSu.len()):
       listaOp.append(listaSu[i].cancion.replace('"',""))

   comboSong['values'] = listaOp
   comboSong1['values'] = listaOp

def agregarsong():
    artista = comboArtista1.get()
    album = comboAlbum1.get()
    cancion = comboSong1.get()
    table4.insert("", END, text=cancion,values=(album,artista))

def datos():
    artista = comboArtista.get()
    album = comboAlbum.get()
    cancion = comboSong.get()
    print(artista,album,cancion)



def crearLista():
   
    ventanaLista = Tk()
    ventanaLista.title("IPCmusic CREAR LISTA DE REPRODUCCION")

    label3 = Label(ventanaLista,text="LISTA", width=15,height=1)
    label3.config(fg="blue",bg="yellow", font=("Veranda",13))
    label3.place(x = 60,y = 10)    

    label12 = Label(ventanaLista,text="Nombre :")
    label12.place(x = 15,y = 60)

    label8 = Label(ventanaLista,text="Cancion Agregar", width=25,height=1)
    label8.config(fg="blue",bg="yellow", font=("Veranda",12))
    label8.place(x = 20,y = 110)
        
    label5 = Label(ventanaLista,text="Artista:")
    label5.place(x = 50,y = 150)
    global comboArtista1
    comboArtista1 = ttk.Combobox(ventanaLista, height=1, width=18, values=['Aun no hay Artista'],postcommand=changeArtista ,state="readonly")
    comboArtista1.current(0)
    comboArtista1.place(x = 50,y =180)

    label6 = Label(ventanaLista,text="Album:")
    label6.place(x = 50,y = 220)
    global comboAlbum1
    comboAlbum1 = ttk.Combobox(ventanaLista, height=1, width=18, values=['Aun no hay Albunes'],postcommand=changeAlbum, state="readonly")
    comboAlbum1.current(0)
    comboAlbum1.place(x = 50,y =250)
    
    label7 = Label(ventanaLista,text="Canciones:")
    label7.place(x = 50,y = 290)
    global comboSong1
    comboSong1 = ttk.Combobox(ventanaLista, height=1, width=20, values=['Aun no hay Canciones'],postcommand= changeSong, state="readonly")
    comboSong1.current(0)
    comboSong1.place(x = 50,y =320)

    btnagregar = Button(ventanaLista, text="Agregar cancion", width=20,height=2, command=agregarsong)
    btnagregar.place(x= 50, y=380)
     
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
    btnsavelista.place(x= 400, y=570)

    ventanaLista.geometry('700x650+300+50')
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
    btnLista.place(x= 780, y=70)

    btnReportes = Button(ventana, text="Reportes", width=8, height=2, command=datos)
    btnReportes.place(x= 1100, y=10)

    label1 = Label(ventana,text="Cancion: Pompeii")
    label1.place(x = 100,y = 460)

    label2 = Label(ventana,text="Artista: Bastille")
    label2.place(x = 100,y = 490)

    label4 = Label(ventana,text="Album: Bastille")
    label4.place(x = 100,y = 520)
#-----------------------------------------------------------------------------------
    label3 = Label(ventana,text="BIBLIOTECA", width=13,height=1)
    label3.config(fg="blue",bg="yellow", font=("Veranda",33))
    label3.place(x = 380,y = 13)

    table1 = ttk.Treeview(ventana, columns=("Album","Artista") ,height=17)
    table1.column("#0", width=115)
    table1.column("Album", width=115, anchor=CENTER)
    table1.column("Artista", width=115, anchor= CENTER)
    table1.heading("#0",text="CANCION", anchor=CENTER)
    table1.heading("Album",text="ALBUM", anchor=CENTER)
    table1.heading("Artista",text="ARTISTA", anchor=CENTER)
    
    label3 = Label(ventana,text="CANCION A REPRODUCIR", width=25,height=1)
    label3.config(fg="blue",bg="yellow", font=("Veranda",15))
    label3.place(x = 420,y = 450)
        
    label5 = Label(ventana,text="Artista:")
    label5.place(x = 350,y = 495)
    comboArtista = ttk.Combobox(ventana, height=1, width=18, values=['Aun no hay Artista'],postcommand=changeArtista ,state="readonly")
    comboArtista.current(0)
    comboArtista.place(x = 350,y =520)

    label6 = Label(ventana,text="Album:")
    label6.place(x = 490,y = 495)
    comboAlbum = ttk.Combobox(ventana, height=1, width=18, values=['Aun no hay Albunes'],postcommand=changeAlbum, state="readonly")
    comboAlbum.current(0)
    comboAlbum.place(x = 490,y =520)
    
    label7 = Label(ventana,text="Canciones:")
    label7.place(x = 630,y = 495)
    comboSong = ttk.Combobox(ventana, height=1, width=20, values=['Aun no hay Canciones'],postcommand= changeSong, state="readonly")
    comboSong.current(0)
    comboSong.place(x = 630,y =520)
    
    table1.place(x=380,y=65)
    #-------------------------------------------------------------------------------------
    label8 = Label(ventana,text="LISTAS DE REPRODUCCION", width=25,height=1)
    label8.config(fg="blue",bg="yellow", font=("Veranda",12))
    label8.place(x = 930,y = 50)

    table2 = ttk.Treeview(ventana, columns=("Canciones") ,height=13)
    table2.column("#0", width=115)
    table2.column("Canciones", width=115, anchor=CENTER)
    table2.heading("#0",text="NOMBRE", anchor=CENTER)
    table2.heading("Canciones",text="No. CANCIONES", anchor=CENTER)
    table2.place(x=930,y=70)

    label9 = Label(ventana,text="LISTA A REPRODUCIR", width=25,height=1)
    label9.config(fg="blue",bg="yellow", font=("Veranda",15))
    label9.place(x = 930,y = 450)
        
    label10 = Label(ventana,text="Nombre Lista:")
    label10.place(x = 940,y = 495)
    comboName = ttk.Combobox(ventana, height=1, width=18, values=['Aun no hay Lista'],state="readonly")
    comboName.current(0)
    comboName.place(x = 940,y =520)

    label11 = Label(ventana,text="Modo:")
    label11.place(x = 1090,y = 495)
    comboModo = ttk.Combobox(ventana, height=1, width=15, values=['---','Normal','Aleatorio'], state="readonly")
    comboModo.current(0)
    comboModo.place(x = 1090,y =520)

    ventana.geometry('1250x660+150+40')
    ventana.mainloop()