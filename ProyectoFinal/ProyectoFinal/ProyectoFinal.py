from operator import concat
import tkinter as tk
from tkinter import CENTER, END, ttk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from webbrowser import get

class Editor:
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.geometry("800x600")
        self.agregar_menu()
        self.ventana.title("Editor de texto")
        #ventana1
        self.TextWin1=st.ScrolledText(self.ventana, width=45, height=30)
        self.TextWin1.grid(column=0,row=0, padx=5, pady=5) 
        #ventana2
        self.TextWin2=st.ScrolledText(self.ventana, width=45, height=30)
        self.TextWin2.grid(column=1,row=0, padx=5, pady=5)
               
        self.ventana.mainloop()

    def agregar_menu(self):
        menuOptions = tk.Menu(self.ventana)
        self.ventana.config(menu=menuOptions)
        opciones = tk.Menu(menuOptions, tearoff=0)
        opciones.add_command(label="Abrir archivo...", command=self.leer)
        opciones.add_command(label="Compilar", command=self.compilar)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.salir)
        menuOptions.add_cascade(label="Opciones", menu=opciones)

    def salir(self):
        sys.exit()

    def leer(self):
        selectArch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
        if selectArch!='':
            arch=open(selectArch, "r", encoding="utf-8")
            contenido=arch.read()
            arch.close()
            self.TextWin1.delete("1.0", tk.END) 
            self.TextWin1.insert("1.0", contenido)

    def compilar(self): 
        llaves = self.TextWin1.get("1.0","end") 
        self.TextWin2.insert("1.0", llaves.replace(' ',', '))



editorTxt=Editor()
