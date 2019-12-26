from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from bs4 import BeautifulSoup
import urllib.request
import requests


class ventana_wb():

    def __init__(self,root):
        self.root = root
        self.root.title('WEB-SCRAPING v2')
        self.root.configure(bg='black')
        self.root.geometry('800x500+180+10')
        self.root.configure(cursor='pirate')
#============================FRAMEES============================================================================================
        self.titulo_lbl = Label(self.root,font=('arial',20,'bold'),text='WEB-SCRAPING',bg='black',fg='white')
        self.titulo_lbl.pack(side=TOP)

        self.index_frame = Frame(self.root,bg='gray')#frame de entrys caja texto
        self.index_frame.pack(side=TOP,pady=5)

        self.btn_frame = Frame(self.root,bg='black')#frame botones
        self.btn_frame.pack(side=BOTTOM,pady=5)

#=======================ENTRY'S Y CAJA DE TEXTO==========================================================================
        self.var_00 = StringVar()


        self.caja_texto = Text(self.index_frame,font=('arial',8,'bold'))
        self.caja_texto.config(cursor='pirate')
        self.caja_texto.pack(padx=5,pady=5)

        self.caja_lbl = Label(self.index_frame,font=('arial',12,'bold'),bg='gray',text='INGRESE UN LINK')
        self.caja_lbl.pack(side=TOP,padx=5,pady=2)

        self.caja_entry = Entry(self.index_frame,font=('arial',10,'bold'),width=60,textvariable=self.var_00)
        self.caja_entry.pack(side=TOP,pady=5)
#=====================================BOTONES====================================================================================
        self.web_sp = Button(self.btn_frame,font=('arial',15,'bold'),width=10,bg='black',fg='white',bd=5,relief='groove',text='web-scraping',command=self.wb_sp)
        self.web_sp.pack(side=LEFT,padx=2)

        self.limpi_btn = Button(self.btn_frame,font=('arial',15,'bold'),width=10,bg='black',fg='white',bd=5,relief='groove',text='limpiar',command=self.limpiar)
        self.limpi_btn.pack(side=LEFT,padx=2)

        self.guardar = Button(self.btn_frame,font=('arial',15,'bold'),width=10,bg='black',fg='white',bd=5,relief='groove',text='Guardar',command=self.guardar)
        self.guardar.pack(side=LEFT,padx=2)
        
        self.salir = Button(self.btn_frame,font=('arial',15,'bold'),width=10,bg='black',fg='white',bd=5,relief='groove',text='salir',command=lambda root=self.root:quit(root))
        self.salir.pack(side=LEFT,padx=2)        
#==============================FUNCIONES==========================================================================================
    def wb_sp(self):
        import requests
        messagebox.showinfo(title='????',message='LISTO')
        try:
            #respuesta
            url = self.var_00.get()
            page = requests.get(url)
            
            self.caja_texto.insert(END,'Respuesta :')
            self.caja_texto.insert(END,'\n')
            self.caja_texto.insert(END,page)
            self.caja_texto.insert(END,'\n\n')
            
            #web-scraping
            entrada = self.var_00.get()
            self.data = urllib.request.urlopen(entrada).read().decode()
            self.caja_texto.insert(END,self.data)
            
        except urllib.error.HTTPError:
            self.caja_texto.insert(END,'HTTP ERROR 403')
            self.caja_texto.insert(END,'\n')
        except ValueError:
            messagebox.showinfo(title='Error',message='Error utilize el protocolo de la pagina a extraer')
            self.caja_texto.insert(END,'\n')
            self.caja_texto.insert(END,'utilize la siguiente plantilla https://www.ejemplo.com')
            self.caja_texto.insert(END,'\n')
        except requests.exceptions.ConnectionError:
            self.caja_texto.insert(END,'ERROR DE CONEXION Ó (LA PAGINA NO EXISTE)')
            self.caja_texto.insert(END,'\n')
        finally:
            pass

    def guardar(self):
        guardar =open('web-scraping.txt','w',encoding="utf-8")

        guardar =open('web-scraping.txt','a',encoding="utf-8")
        entrada = self.var_00.get()
        self.data = urllib.request.urlopen(entrada).read().decode()
        texto = guardar.write(self.data)
        guardar.close()

    def limpiar(self):
        messagebox.showinfo(title='????',message='limpio')
        self.var_00.set(" ")
        self.caja_texto.delete("1.0",END)

            
def main():
    root = Tk()
    app = ventana_wb(root)

if __name__ == '__main__':
    main()
