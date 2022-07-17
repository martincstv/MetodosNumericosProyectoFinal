from tkinter import *

from math import *                    #Libreria de funciones matematicas
import sympy as sp                    #Libreria para matematica simbolica
from sympy.plotting import plot       # Libreria para graficas

#----------------------------------------------------------------------------------------------------------------------
def form_Newton_inicio():
    inicio.iconify()
    inicio.deiconify()
    form_Newton.destroy()

def form_Newton():
    global form_Newton
    form_Newton = Toplevel(inicio)
    ancho = 325
    alto = 100
    x = form_Newton.winfo_screenwidth() // 2 - ancho // 2
    y = form_Newton.winfo_screenheight() // 2 - alto // 2
    posicion = str(ancho) + "x" + str(alto) + "+" + str(x) + "+" + str(y)
    form_Newton.geometry(posicion)
    form_Newton.title("Interpolación por Newton")
    form_Newton.resizable(0,0)
    #--------------------------------
    labe1 = Label(form_Newton, text="X")
    caja1 = Entry(form_Newton)
    labe2 = Label(form_Newton, text="Y")
    caja2 = Entry(form_Newton)
    boton1 = Button(form_Newton, text="Calcular")
    boton2 = Button(form_Newton, text="Regresar", command=form_Newton_inicio)
    labe1.grid(row=0, column=0)
    caja1.grid(row=0, column=1)
    labe2.grid(row=1, column=0)
    caja2.grid(row=1, column=1)
    boton2.grid(row=2, column=0)
    boton1.grid(row=2,column=1)
    #--------------------------------
    if(form_Newton):
        inicio.withdraw()
    #-------------------------------
    form_Newton.mainloop()
#-----------------------------------------------------------------------------------------------------------------
def form_Lagrange_inicio():
    inicio.iconify()
    inicio.deiconify()
    form_Lagrange.destroy()

def form_Lagrange():
    global form_Lagrange
    form_Lagrange = Toplevel(inicio)
    ancho = 325
    alto = 100
    x = form_Lagrange.winfo_screenwidth() // 2 - ancho // 2
    y = form_Lagrange.winfo_screenheight() // 2 - alto // 2
    posicion = str(ancho) + "x" + str(alto) + "+" + str(x) + "+" + str(y)
    form_Lagrange.geometry(posicion)
    form_Lagrange.title("Interpolación por Lagrange")
    form_Lagrange.resizable(0,0)
    #--------------------------------
    labe1 = Label(form_Lagrange, text="X")
    caja1 = Entry(form_Lagrange)
    labe2 = Label(form_Lagrange, text="Y")
    caja2 = Entry(form_Lagrange)
    boton1 = Button(form_Lagrange, text="Calcular")
    boton2 = Button(form_Lagrange, text="Regresar", command=form_Lagrange_inicio)
    labe1.grid(row=0, column=0)
    caja1.grid(row=0, column=1)
    labe2.grid(row=1, column=0)
    caja2.grid(row=1, column=1)
    boton2.grid(row=2, column=0)
    boton1.grid(row=2,column=1)
    #--------------------------------
    if(form_Lagrange):
        inicio.withdraw()
    #-------------------------------
    form_Lagrange.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------

def form_Taylor_inicio():
    inicio.iconify()
    inicio.deiconify()
    form_Taylor.destroy()

def form_Taylor():
    global form_Taylor
    form_Taylor = Toplevel(inicio)
    ancho = 300
    alto = 100
    x = form_Taylor.winfo_screenwidth() // 2 - ancho // 2
    y = form_Taylor.winfo_screenheight() // 2 - alto // 2
    posicion = str(ancho) + "x" + str(alto) + "+" + str(x) + "+" + str(y)
    form_Taylor.geometry(posicion)
    form_Taylor.title("Serie de Taylor")
    form_Taylor.resizable(0,0)
    #--------------------------------
    labe1 = Label(form_Taylor, text="Funcion")
    caja1 = Entry(form_Taylor)
    labe2 = Label(form_Taylor, text="Valor a")
    caja2 = Entry(form_Taylor)
    labe3 = Label(form_Taylor, text="# Iteraciones")
    caja3 = Entry(form_Taylor)
    #--------------------------------
    x = sp.Symbol('x')
    def Taylor(fx, a, n):
        i = 0                   #Ciclo inicia en 0
        formula_tay = 0         
        F_graf = fx             #Grafica de la funcion
        while i<=n:
            formula_tay += (fx.diff(x,i).subs(x,a))/(factorial(i))*(x-a)**i     #Formula de Taylor
            i+=1                                                                #Contador
        g = plot(formula_tay,F_graf,(x,-5,5), title='Serie de Taylor', show=False)    #Graficar la funcion y el polinomio de maclaurin
        g[0].line_color='g'            #Grafica funcion
        g[1].line_color='r'            #Grafica Taylor
        g.show()                       #Mostrar Grafica
        print(formula_tay)

    def Calcular():
        #funcion = sp.exp(-x)
        funcion = sp.exp(caja1.get())
        Taylor(funcion, 1, 10)

    #--------------------------------
    boton1 = Button(form_Taylor, text="Calcular", command=Calcular)
    boton2 = Button(form_Taylor, text="Regresar", command=form_Taylor_inicio)
    labe1.grid(row=0, column=0)
    caja1.grid(row=0, column=1)
    labe2.grid(row=1, column=0)
    caja2.grid(row=1, column=1)
    labe3.grid(row=2, column=0)
    caja3.grid(row=2, column=1)
    boton2.grid(row=3, column=0)
    boton1.grid(row=3,column=1)
    #--------------------------------
    if(form_Taylor):
        inicio.withdraw()
    #-------------------------------
    form_Taylor.mainloop()

#-------------------------------------------------------------------------------------------------------------------------------------
def form_Maclaurin_inicio():
    inicio.iconify()
    inicio.deiconify()
    form_Maclaurin.destroy()

def form_Maclaurin():
    global form_Maclaurin
    form_Maclaurin = Toplevel(inicio)
    ancho = 300
    alto = 100
    x = form_Maclaurin.winfo_screenwidth() // 2 - ancho // 2
    y = form_Maclaurin.winfo_screenheight() // 2 - alto // 2
    posicion = str(ancho) + "x" + str(alto) + "+" + str(x) + "+" + str(y)
    form_Maclaurin.geometry(posicion)
    form_Maclaurin.title("Serie de Maclaurin")
    form_Maclaurin.resizable(0,0)
    #--------------------------------
    labe1 = Label(form_Maclaurin, text="Funcion")
    caja1 = Entry(form_Maclaurin)
    labe2 = Label(form_Maclaurin, text="# Iteraciones")
    caja2 = Entry(form_Maclaurin)
    boton1 = Button(form_Maclaurin, text="Calcular")
    boton2 = Button(form_Maclaurin, text="Regresar", command=form_Maclaurin_inicio)
    #--------------------------------
    labe1.grid(row=0, column=0)
    caja1.grid(row=0, column=1)
    labe2.grid(row=1, column=0)
    caja2.grid(row=1, column=1)
    boton2.grid(row=2, column=0)
    boton1.grid(row=2,column=1)
    #--------------------------------
    if(form_Maclaurin):
        inicio.withdraw()
    #-------------------------------
    form_Maclaurin.mainloop()
#-------------------------------------------------------------------------------------------------
def inicio():
    global inicio
    inicio = Tk()
    ancho = 720
    alto = 720
    x = inicio.winfo_screenwidth() // 2 - ancho // 2
    y = inicio.winfo_screenheight() // 2 - alto // 2
    posicion = str(ancho) + "x" + str(alto) + "+" + str(x) + "+" + str(y)
    inicio.geometry(posicion)
    inicio.title("Métodos Numéricos")
    inicio.resizable(0,0)
    #--------------------------------
    encabezado1 = Label(inicio,text="UNIVERSIDAD TÉCNICA DE AMBATO")
    encabezado1.pack(side=TOP)
    img = PhotoImage(file="logo-uta.png")
    _img = Label(inicio, image=img)
    _img.pack()
    encabezado2 = Label(inicio, text="FACULTAD DE INGENIERÍA EN SISTEMAS, ELECTRÓNICA E INDUSTRIAL")
    encabezado2.pack(side=TOP)
    encabezado3 = Label(inicio, text="PROYECTO FINAL “INTERPOLACIÓN POLINOMIAL”")
    encabezado3.pack(side=TOP)
    encabezado4 = Label(inicio, text="INGENIERÍA EN TECNOLOGÍAS DE LA INinicioACIÓN")
    encabezado4.pack(side=TOP)
    encabezado5 = Label(inicio, text="CUARTO “A”")
    encabezado5.pack(side=TOP)
    encabezado6 = Label(inicio, text="MÉTODOS NUMÉRICOS ING. MARLON SANTAMARIA VILLACIS, MG.")
    encabezado6.pack(side=TOP)
    Label(inicio, text="\n").pack()
    #--------------------------------
    boton1 = Button(inicio, text="Interpolación por Newton", width=40, height=2, command=form_Newton)
    boton1.pack()
    Label(inicio, text="").pack()
    boton2 = Button(inicio, text="Interpolación por Lagrange", width=40, height=2, command=form_Lagrange)
    boton2.pack()
    Label(inicio, text="").pack()
    boton3 = Button(inicio, text="Serie de Taylor", width=40, height=2, command=form_Taylor)
    boton3.pack()
    Label(inicio, text="").pack()
    boton4 = Button(inicio, text="Serie de Maclaurin", width=40, height=2, command=form_Maclaurin)
    boton4.pack()
    Label(inicio, text="\n").pack()
    #--------------------------------
    pie = Label(inicio, text="INTEGRANTES: Juan Alejandro, Xavier Bastidas, Martin Castillo")
    pie.pack()
    #--------------------------------
    inicio.mainloop()

inicio()

