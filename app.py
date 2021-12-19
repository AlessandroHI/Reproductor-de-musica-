import os
from tkinter import font
from pygame import mixer
from Artista import Artista
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image
from Biblioteca import Biblioteca
from Nodo import Nodo
from Reproducciones import Reproducciones
from Lista import Lista
from Album import Album
from ListaSong import ListaSong
from xml.etree import ElementTree
from tkinter import messagebox
from ListaCircularDoble import LIstacircular
from ListadeReproduccion import Reproducciones
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
    global listaSu , listSong,listaArtista,listaAr,lista, listal, listaAlbum,listaAl, LISTA
    listaAl = Lista()
    listaAlbum = Lista()
    listaAr = Lista()
    archivoXML = ElementTree.parse(ruta)
    root = archivoXML.getroot()
    
    for cancion in root:
      print("Nombre cancion:",cancion.attrib["nombre"])
      song = cancion.attrib["nombre"]
      song.replace(' ',"_")
      for artista in cancion.iter("artista"):
          print("Artista:",artista.text.replace('"',""))
          artist = artista.text.replace('"',"")
          artist.replace(' ',"_")          
      for album in cancion.iter("album"):
          print("Album:",album.text.replace('"',""))
          albu = album.text.replace('"',"")
          albu.replace(' ',"_")
      for imagen in cancion.iter("imagen"):
          print("Imagen:",imagen.text.replace('"',""))
          img = imagen.text.replace('"',"")
      for ruta in cancion.iter("ruta"):
          print("Ruta:", ruta.text.replace('"',""))
          ru = ruta.text.replace('"',"")
          listaSu.append(Biblioteca(artist,albu,song,img,ru))
          listSong.append(Reproducciones(song,albu,artist,0))
          listaArtista.append(Artista(artist))
          listaAlbum.append(Album(albu))

    for i in range(listaArtista.len()): 
        aux = listaArtista[i].nombre 
        if aux in lista:
            pass 
        else:
            lista.append(aux)
    for i in lista:
        listaAr.append(Artista(i))
    for i in range(listaAlbum.len()): 
        aux = listaAlbum[i].nombre 
        if aux in listal:
            pass 
        else:
            listal.append(aux)
    for i in listal:
        listaAl.append(Album(i))

    for i in range(listaAl.len()):
        albumAux = listaAl[i].nombre
        for i in range(listaSu.len()):
            auxalbum = listaSu[i].album
            if albumAux == auxalbum:
                artista  = listaSu[i].artista
                LISTA.append(ListaSong(artista,albumAux))
                break
            else:
                pass
    canciones()
    

def addList():
    global nombreLista ,listaR
    nombreLista = entry.get()
    if listaR.vacia():
     messagebox.showinfo(message=nombreLista+" Guardado con exito", title="Mensaje")
    else:
        pass
      
def addSongs():
    global cancion,listaR1
    listaR1 = LIstacircular()
    cancion = table3.item(table3.selection())["text"]
    listaR1.agregar(cancion)
    
def addPlayLista():
    listaR.append(Reproducciones(nombreLista,listaR1))

def showList():
    for i in range(listaR.len()):
        table1.insert("", END, text=str(listaR[i].nombre),values=(str(listaR[i].cancion.len())))


def crearArchivo(ruta, contenido):
    archivo = open(ruta, 'w')
    archivo.write(contenido)
    archivo.close      

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
    mixer.music.set_volume(0.3)
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
    contSong(cancion)
    Play(ruta)
    MostrarImagen(imagen)

def contSong(cancion):
    
    for i in range(listSong.len()):
        if cancion == listSong[i].cancion:
            listSong[i].cont += 1
            break

def recorrer():
    for i in range(listSong.len()):
        print("Cancion:",listSong[i].cancion)
        print("NO. Reproducciones:",listSong[i].cont)


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


def Reportar():
    archivo = comboReporte.get()
    if archivo == "HTML":
        Reporte_HTML()
    elif archivo == "Graphviz":
        Reporte_Gra()


def Reporte_Gra():
    archivo = open("ReporteGraphviz.dot", 'w')
    inicio= '''digraph G {
        node[shape = box fillcolor="#FFEDBB" style = filled]
        bgcolor = "#273248"
        edge[dir = both  color = "#81FFE5"]
        rankdir = "LR"
        Biblioteca[label = "BIBLIOTECA" shape = tab, fillcolor ="#E581FF"];

    '''
    for i in range(listaAr.len()):
        inicio +=str(listaAr[i].nombre)+'''[label = "Atista: '''+str(listaAr[i].nombre)+'''" shape = box3d, fillcolor ="#B5E358"];
        '''
    for i in range(listaAl.len()):
        inicio +=str(listaAl[i].nombre)+'''[label = "Album: '''+ str(listaAl[i].nombre)+'''" shape = folder, fillcolor ="#FFEBD2"];
        '''
    for i in range(listaSu.len()):
        inicio +=str(listaSu[i].cancion)+'''[label = "Cancion: '''+ str(listaSu[i].cancion)+'''" shape = ellipse, fillcolor ="#F8AB54"];
        '''
    
    inicio += '''
        '''
    for i in range(listaAr.len()):
        inicio += '''Biblioteca -> '''+str(listaAr[i].nombre)+''';
        '''

    cont = 1
    for i in range(listaAr.len()):
        if cont < listaAr.len():
            inicio += str(listaAr[i].nombre)+''' -> '''+str(listaAr[cont].nombre)+'''
            '''
            cont +=1  
    

    for i in range(LISTA.len()):
        aux = LISTA[i].album
        aux1 = LISTA[i].artista
        for j in range(listaAr.len()):
            aux2 = listaAr[j].nombre
            if aux1 == aux2:
                inicio +='''
                '''
                inicio += str(aux2)+''' ->'''+str(aux)
                inicio +='''
                '''
            else:
                pass  
            

    for i in range(listaSu.len()):
        aux = listaSu[i].cancion
        aux1 = listaSu[i].album
        for j in range(listaAl.len()):
            aux2 = listaAl[j].nombre
            if aux1 == aux2:
                inicio += str(aux2)+''' ->'''+str(aux)
                inicio +='''
                '''
            else:
                pass

                            
    inicio +='''
     }
    }
    '''
    archivo.write(inicio)
    archivo.close 
    os.system('dot.exe -Tpng ReporteGraphviz.dot -o Reporte.png')

def Reporte_HTML():
    inicio = """ 
        <!doctype html>
        <html lang="en">
        <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
        <title>Reportes</title>
    </head>
    <body style="background-color:#FFEBDB;">
        <center>
            <h1 style="border: ridge #d3d3eb 5px; background-color:#25425C; color:#FFEBDB ;">REPORTES</h1>
            <p>
            <span style="border-image: initial; border: 2px solid #FB770D;background-color:#FFA45B;color:#FFFF;font-size: 25px;">No. Reproducciones</span>
            </p>
    <table class="table" style="width: 600px;">
                <thead class="table-dark">
                    <tr>
                        <th style="width: 30px;"></th>
                        <th scope="col" style="width:50px">Cancion </th>
                        <th scope="col" with="30px">Album</th>
                        <th scope="col" with="30px">Artista</th>
                        <th scope="col" with="30px">No. Reproducciones </th>
                    </tr>
                </thead>
                """

    for i in range(listSong.len()):
        inicio += """
         <tbody>  <tr>
                       <td style="width: 30px;"></td>
                       <td style="width:50px;">"""+str(listSong[i].cancion)+"""</td>
                       <td style="width:50px;">"""+str(listSong[i].album)+"""</td>
                       <td style="width:50px;">"""+str(listSong[i].artista)+"""</td>
                       <td style="width:50px; color: blue;">"""+str(listSong[i].cont)+"""</td>
                     </tr> 
                     
            </tbody>
          """

    fin = """</table> 
            <h4 style="border: ridge #d3d3eb 3px; background-color:#25425C; color:#FFEBDB ;">
                <p>
                  NOMBRE: IVAN ALESSANDRO HILARIO CHACON
                  CARNET: 201902888
                </p>
            </h4>
          </center>
        </body>
     </html>"""      
    inicio += fin  
    crearArchivo("ReportesReproducciones.html",inicio)


def crearLista():
    #--------------------GUI--------------------------------
    ventanaLista = Tk()
    ventanaLista.title("IPCmusic CREAR LISTA DE REPRODUCCION")
    ventanaLista.iconbitmap("Iconos\icono Musica.ico")

    label3 = Label(ventanaLista,text="LISTA", width=15,height=1)
    label3.config(fg="#FFEBD2",bg="#273248", font=("Bahnschrift SemiBold",15))
    label3.place(x = 60,y = 10)    

    label12 = Label(ventanaLista,text="Nombre :")
    label12.config(fg="#FFEBD2",bg="#273248", font=("Bahnschrift SemiBold",15))
    label12.place(x = 15,y = 60)
    global entry
    entry = Entry(ventanaLista, width=25) 
    entry.place(x = 110,y = 68)
    
    
        
    btnagregar = Button(ventanaLista, text="Agregar cancion", width=20,height=2, command=  lambda: [addSong(), addSongs()])
    btnagregar.config(fg="Black",bg="#FC7643",font=("Bahnschrift SemiBold",10))
    btnagregar.place(x= 50, y=180)

    guardarnombre = Button(ventanaLista, text="Guardar Nombre", width=20,height=2, command=addList)
    guardarnombre.config(fg="Black",bg="#FC7643",font=("Bahnschrift SemiBold",10))
    guardarnombre.place(x= 50, y=120)

    btnMostrar = Button(ventanaLista, text="Mostrar Biblioteca", width=20,height=2,command=canciones2)
    btnMostrar.config(fg="Black",bg="#FC7643",font=("Bahnschrift SemiBold",10))
    btnMostrar.place(x= 400, y=10)
    global table3
    table3 = ttk.Treeview(ventanaLista, columns=("Album","Artista") ,height=10)
    table3.column("#0", width=115)  
    table3.column("Album", width=115, anchor=CENTER)
    table3.column("Artista", width=115, anchor= CENTER)
    table3.heading("#0",text="CANCION", anchor=CENTER)
    table3.heading("Album",text="ALBUM", anchor=CENTER)
    table3.heading("Artista",text="ARTISTA", anchor=CENTER)  
    table3.place(x=300,y=60)

    label14 = Label(ventanaLista,text="Canciones Agregadas a la Lista", width=30,height=1)
    label14.config(fg="#FFEBD2",bg="#273248", font=("Bahnschrift SemiBold",15))
    label14.place(x = 315,y = 290)
    global table4
    table4 = ttk.Treeview(ventanaLista, columns=("Album","Artista") ,height=10)
    table4.column("#0", width=115)
    table4.column("Album", width=115, anchor=CENTER)
    table4.column("Artista", width=115, anchor= CENTER)
    table4.heading("#0",text="CANCION", anchor=CENTER)
    table4.heading("Album",text="ALBUM", anchor=CENTER)
    table4.heading("Artista",text="ARTISTA", anchor=CENTER)  
    table4.place(x=300,y=320)
   
    btnsavelista = Button(ventanaLista, text="Guardar Lista", width=20,height=2, command=addPlayLista)
    btnsavelista.config(fg="Black",bg="#FC7643",font=("Bahnschrift SemiBold",10))
    btnsavelista.place(x= 50, y=420)
    ventanaLista.config( bg="#273248" )
    ventanaLista.geometry('700x580+300+50')
    ventanaLista.mainloop()


if __name__ == '__main__':
    global listaSu, listSong, listaArtista, listaAr, listaAl, LISTA, listaR
    listaSu = Lista()
    listSong = Lista()
    listaArtista = Lista()
    listaAr = Lista()
    listalAl = Lista()
    LISTA = Lista()
    listaR = Lista()

    ventana = Tk()
    ventana.title("IPCmusic HOME")
    ventana.iconbitmap("Iconos\icono Musica.ico")

    btnCargar = Button(ventana, text="CARCGAR CANCIONES", width=18,height=2, command=cargarcanciones)
    btnCargar.config(fg="Black",bg="#FC7643",font=("Bahnschrift SemiBold",10))
    btnCargar.place(x= 10, y=10)
    btnLista = Button(ventana, text="Crear lista de reprodccion", width=23, height=1, command=  lambda: [crearLista()])
    btnLista.config(fg="Black",bg="#FC7643",font=("Bahnschrift SemiBold",11))
    btnLista.place(x= 800, y=8)
    btnReportes = Button(ventana, text="Reportar", width=8, height=2, command=Reportar)
    btnReportes.config(fg="Black",bg="#FC7643",font=("Bahnschrift SemiBold",10))
    btnReportes.place(x= 160, y=10)
    global listal
    listal = []#Elementos para combox
    comboReporte = ttk.Combobox(ventana, height=1, width=15, values=['---','HTML','Graphviz'], state="readonly")
    comboReporte.current(0)
    comboReporte.place(x = 225,y =10)
    img = PhotoImage(file="Iconos\Play.png")
    play = Button(ventana, text="PLAY", image=img,width=50, height=45, command=get_data)
    play.config(fg="Black",bg="#FC7643",font=("Bahnschrift SemiBold",10))
    play.place(x= 90, y=400)
    img2 = PhotoImage(file="Iconos\Pause.png") 
    pause = Button(ventana, text="PAUSE",image=img2, width=50, height=45, command=Pause)
    pause.config(fg="Black",bg="#FC7643",font=("Bahnschrift SemiBold",10))
    pause.place(x= 160, y=400)
    img3 = PhotoImage(file="Iconos\Reanudar.png") 
    reanudar = Button(ventana, text="REANUDAR",image=img3, width=50, height=45, command=Reanudar)
    reanudar.config(fg="Black",bg="#FC7643",font=("Bahnschrift SemiBold",10))
    reanudar.place(x= 230, y=400)
    global lista
    lista = []#Elementos para combox
    img4 = PhotoImage(file="Iconos\Back1.png")
    next = Button(ventana, text="REANUDAR",image=img4, width=50, height=45)
    next.config(fg="Black",bg="#FC7643",font=("Bahnschrift SemiBold",10))
    next.place(x= 130, y=460)
    
    img5 = PhotoImage(file="Iconos\Back.png")
    back = Button(ventana, text="REANUDAR",image=img5, width=50, height=45, command=Reanudar)
    back.config(fg="Black",bg="#FC7643",font=("Bahnschrift SemiBold",10))
    back.place(x= 200, y=460)


    label1 = Label(ventana,text="Cancion:")
    label1.config(fg="#FFEBD2",bg="#273248",font=("Bahnschrift SemiBold",14))
    label1.place(x = 110,y = 530)

    label2 = Label(ventana,text="Artista:")
    label2.config(fg="#FFEBD2",bg="#273248",font=("Bahnschrift SemiBold",14))
    label2.place(x = 110,y = 560)

    label4 = Label(ventana,text="Album:")
    label4.config(fg="#FFEBD2",bg="#273248",font=("Bahnschrift SemiBold",14))
    label4.place(x = 110,y = 590)
#-----------------------------------------------------------------------------------
    label3 = Label(ventana,text="BIBLIOTECA", width=13,height=1)
    label3.config(fg="#FFEBD2",bg="#273248", font=("Bahnschrift SemiBold",33))
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
    label8.config(fg="#FFEBD2",bg="#273248", font=("Bahnschrift SemiBold",12))
    label8.place(x = 780,y = 45)

    table2 = ttk.Treeview(ventana, columns=("Canciones") ,height=13)
    table2.column("#0", width=115)
    table2.column("Canciones", width=115, anchor=CENTER)
    table2.heading("#0",text="NOMBRE", anchor=CENTER)
    table2.heading("Canciones",text="No. CANCIONES", anchor=CENTER)
    table2.place(x=780,y=70)

    label11 = Label(ventana,text="Modo:")
    label11.config(fg="#FFEBD2",bg="#273248",font=("Bahnschrift SemiBold",13))
    label11.place(x = 820,y = 495)
    comboModo = ttk.Combobox(ventana, height=1, width=15, values=['---','Normal','Aleatorio'], state="readonly")
    comboModo.current(0)
    comboModo.place(x = 820,y =520)
    ventana.config( bg="#273248" )
    ventana.geometry('1050x660+200+40')
    ventana.mainloop()