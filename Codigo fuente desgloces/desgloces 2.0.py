from fpdf import FPDF
from tkinter import *
base = Tk()
#--------------------- Cabecera    ----------------------------------------------------------
base.title("Barcocinas Desgloces v2.0")
base.iconbitmap("descarga.ico")
base.resizable(False,False)
#---------------------  Frames     ----------------------------------------------------------
botonesFrame = Frame(base,width="125" ,height="225")
botonesFrame.pack(side="left",anchor="n")
#--------------------------------------------------------------------------------------------
alacenaFrame = Frame(base,width="325" ,height="225")
#--------------------------------------------------------------------------------------------
GabTarjaFrame = Frame(base,width="325" ,height="225")
#--------------------------------------------------------------------------------------------
GabPuertaFrame = Frame(base,width="325" ,height="225")
#--------------------------------------------------------------------------------------------
CajonFrame = Frame(base,width="325" ,height="225")
#--------------------------------------------------------------------------------------------
EsqFrame = Frame(base,width="325" ,height="225")
#---------------------  variables globales  -------------------------------------------------
EntradasAlacena = []
CalculosAlacena = []
EntradasGabTarja = []
CalculosGabTarja = []
EntradasGabPuerta = []
CalculosGabPuerta = []
EntradasCajon = []
CalculosCajon = []
EntradasEsq = []
CalculosEsq = []
CuadroNombre = StringVar()
CuadroCantidad = IntVar()
CuadroEspesor = IntVar()
CuadroPuerta = IntVar()
CuadroAlto = IntVar()
CuadroAncho = IntVar()
CuadroProf = IntVar()
CuadroDivisiones = IntVar()
CuadroFrente = IntVar()
CuadroLatIzq = IntVar()
CuadroLatDer = IntVar()
#-----------------------------  CONSTANTES    ------------------------------------------------
FORMAICA = 30
GRANITO = 15
REBAJE = 5
REPISA = 60
CORREDERA = 50
#-----------------------------  FUNCIONES REUTILIABLES  -------------------------------------------
def validation():
    return CuadroAlto.get() != 0 and CuadroAncho.get() != 0 and CuadroProf.get() != 0 and len(CuadroNombre.get()) != 0
def validationC():
    return CuadroFrente.get() != 0 and CuadroAncho.get() != 0 and CuadroDivisiones.get() != 0 and len(CuadroNombre.get()) != 0
def validationV():
    return len(CalculosAlacena) != 0 or len(CalculosGabTarja) != 0 or len(CalculosGabPuerta) != 0 or len(CalculosCajon) != 0 or len(CalculosEsq) != 0
#-----------------------------  ALACENAS    -------------------------------------------------------
def NuevaAlacena():
    GabTarjaFrame.pack_forget()
    GabPuertaFrame.pack_forget()
    CajonFrame.pack_forget()
    EsqFrame.pack_forget()
    alacenaFrame.pack(side="right", anchor="n")
    Label(alacenaFrame, text="Nombre: ").grid(row=1, column=6, padx=10, pady=2)
    Entry(alacenaFrame,textvariable=CuadroNombre).grid(row=1,column=7,padx=10,pady=2)
    Label(alacenaFrame, text="Cantidad: ").grid(row=2, column=6, padx=10, pady=2)
    Entry(alacenaFrame,textvariable=CuadroCantidad).grid(row=2, column=7, padx=10, pady=2)
    Label(alacenaFrame, text="Espesor: ").grid(row=3, column=6, padx=10, pady=2)
    Entry(alacenaFrame,textvariable=CuadroEspesor).grid(row=3, column=7, padx=10, pady=2)
    Label(alacenaFrame, text="Puertas: ").grid(row=4, column=6, padx=10, pady=2)
    Entry(alacenaFrame,textvariable=CuadroPuerta).grid(row=4, column=7, padx=10, pady=2)
    Label(alacenaFrame, text="Alto: ").grid(row=1, column=8, padx=10, pady=2)
    Entry(alacenaFrame,textvariable=CuadroAlto).grid(row=1, column=9, padx=10, pady=2)
    Label(alacenaFrame, text="Ancho: ").grid(row=2, column=8, padx=10, pady=2)
    Entry(alacenaFrame,textvariable=CuadroAncho).grid(row=2, column=9, padx=10, pady=2)
    Label(alacenaFrame, text="Profundidad: ").grid(row=3, column=8, padx=10, pady=2)
    Entry(alacenaFrame,textvariable=CuadroProf).grid(row=3, column=9, padx=10, pady=2)
    Button(alacenaFrame, text="ACEPTAR",command=calcularAlacena).grid(row=4, column=9, padx=10, pady=2)

def calcularAlacena():
    estado=StringVar()
    TempList = []
    TempList2 = []
    Costados = []
    tira = []
    respaldo = []
    cubierta = []
    piso = []
    repisa = []
    puerta = []
    piezas = []
    estado.set("")
    if validation():
        estado.set("                                       ")
        TempList.append(CuadroNombre.get())
        TempList.append(CuadroCantidad.get())
        TempList.append(CuadroEspesor.get())
        TempList.append(CuadroPuerta.get())
        TempList.append(CuadroAlto.get())
        TempList.append(CuadroAncho.get())
        TempList.append(CuadroProf.get())
        EntradasAlacena.append(TempList)
        aux=TempList[4] #altura
        Costados.append(aux)
        aux=TempList[6] #profundidad
        Costados.append(aux)
        aux=TempList[4]-(2*TempList[2]) #altura-2*espesor
        tira.append(aux)
        aux = 70
        tira.append(aux)
        aux=TempList[5]-(2*TempList[2]) #anchura-2*espesor
        respaldo.append(aux)
        aux = TempList[4] - (2 * TempList[2])  # altura-2*espesor
        respaldo.append(aux)
        aux=TempList[5]-(2*TempList[2]) #anchura-2*espesor
        cubierta.append(aux)
        aux = TempList[6] # profundidad
        cubierta.append(aux)
        aux = TempList[5] - (2 * TempList[2])  # anchura-2*espesor
        piso.append(aux)
        aux = TempList[6]  # profundidad
        piso.append(aux)
        aux = TempList[5] - (2 * TempList[2])  # anchura-2*espesor
        repisa.append(aux)
        aux = TempList[6]-REPISA  # profundidad-REPISA
        repisa.append(aux)
        aux = TempList[4] - REBAJE  # altura-REBAJE
        puerta.append(aux)
        aux = (TempList[5]/TempList[3]) - REBAJE  # anchura/puertas  - REBAJE
        puerta.append(aux)
        aux = 2 * TempList[1]
        piezas.append(aux)
        aux = 1 * TempList[1]
        piezas.append(aux)
        aux = TempList[3] * TempList[1]
        piezas.append(aux)
        TempList2.append(Costados)
        TempList2.append(tira)
        TempList2.append(respaldo)
        TempList2.append(cubierta)
        TempList2.append(piso)
        TempList2.append(repisa)
        TempList2.append(puerta)
        TempList2.append(piezas)
        CalculosAlacena.append(TempList2)
        Label(alacenaFrame, text="Alacena calculada",font=("bold",14)).grid(row=5, column=6, padx=10, pady=2,columnspan=4)
        CuadroNombre.set("")
        CuadroCantidad.set(0)
        CuadroEspesor.set(0)
        CuadroPuerta.set(0)
        CuadroAlto.set(0)
        CuadroAncho.set(0)
        CuadroProf.set(0)
    else:
        estado.set("DATOS INCOMPLETOS")
    Label(alacenaFrame, textvariable=estado).grid(row=5, column=9, padx=10, pady=2)
#-----------------------------  GABINETE TARJA    -------------------------------------------------
def NuevoGabineteTarja():
    alacenaFrame.pack_forget()
    GabPuertaFrame.pack_forget()
    CajonFrame.pack_forget()
    EsqFrame.pack_forget()
    GabTarjaFrame.pack(side="right", anchor="n")
    Label(GabTarjaFrame,text="Nombre: ").grid(row=1,column=6,padx=10,pady=2)
    Entry(GabTarjaFrame,textvariable=CuadroNombre).grid(row=1,column=7,padx=10,pady=2)
    Label(GabTarjaFrame, text="Cantidad: ").grid(row=2, column=6, padx=10, pady=2)
    Entry(GabTarjaFrame,textvariable=CuadroCantidad).grid(row=2, column=7, padx=10, pady=2)
    Label(GabTarjaFrame, text="Espesor: ").grid(row=3, column=6, padx=10, pady=2)
    Entry(GabTarjaFrame,textvariable=CuadroEspesor).grid(row=3, column=7, padx=10, pady=2)
    Label(GabTarjaFrame, text="Puertas: ").grid(row=4, column=6, padx=10, pady=2)
    Entry(GabTarjaFrame,textvariable=CuadroPuerta).grid(row=4, column=7, padx=10, pady=2)
    Label(GabTarjaFrame, text="Alto: ").grid(row=1, column=8, padx=10, pady=2)
    Entry(GabTarjaFrame,textvariable=CuadroAlto).grid(row=1, column=9, padx=10, pady=2)
    Label(GabTarjaFrame, text="Ancho: ").grid(row=2, column=8, padx=10, pady=2)
    Entry(GabTarjaFrame,textvariable=CuadroAncho).grid(row=2, column=9, padx=10, pady=2)
    Label(GabTarjaFrame, text="Profundidad: ").grid(row=3, column=8, padx=10, pady=2)
    Entry(GabTarjaFrame,textvariable=CuadroProf).grid(row=3, column=9, padx=10, pady=2)
    Button(GabTarjaFrame, text="ACEPTAR",command=calcularGabineteTarja).grid(row=4, column=9, padx=10, pady=2)

def calcularGabineteTarja():
    estado=StringVar()
    TempList = []
    TempList2 = []
    Costados = []
    armadores = []
    respaldo = []
    piso = []
    puertaF = []
    puertaG = []
    piezas = []
    estado.set("")
    if validation():
        estado.set("                                       ")
        TempList.append(CuadroNombre.get())
        TempList.append(CuadroCantidad.get())
        TempList.append(CuadroEspesor.get())
        TempList.append(CuadroPuerta.get())
        TempList.append(CuadroAlto.get())
        TempList.append(CuadroAncho.get())
        TempList.append(CuadroProf.get())
        EntradasGabTarja.append(TempList)
        aux=TempList[4] #altura
        Costados.append(aux)
        aux=TempList[6] #profundidad
        Costados.append(aux)
        aux=TempList[5]-(2*TempList[2]) #anchura-2*espesor
        armadores.append(aux)
        aux = 130
        armadores.append(aux)
        aux=TempList[4]-TempList[2] #altura-espesor
        respaldo.append(aux)
        aux = TempList[5] - (2 * TempList[2])  # anchura-2*espesor
        respaldo.append(aux)
        aux = TempList[5] - (2 * TempList[2])  # anchura-2*espesor
        piso.append(aux)
        aux = TempList[6]  # profundidad
        piso.append(aux)
        aux = TempList[4] - FORMAICA  # altura-FORMAICA
        puertaF.append(aux)
        aux = (TempList[5]/TempList[3]) - REBAJE  # anchura/puertas  - REBAJE
        puertaF.append(aux)
        aux = TempList[4] - GRANITO# altura-GRANITO
        puertaG.append(aux)
        aux = (TempList[5] / TempList[3]) - REBAJE  # anchura/puertas  - REBAJE
        puertaG.append(aux)
        aux = 2 * TempList[1]
        piezas.append(aux)
        aux = 1 * TempList[1]
        piezas.append(aux)
        aux = TempList[3] * TempList[1]
        piezas.append(aux)
        TempList2.append(Costados)
        TempList2.append(armadores)
        TempList2.append(respaldo)
        TempList2.append(piso)
        TempList2.append(puertaF)
        TempList2.append(puertaG)
        TempList2.append(piezas)
        CalculosGabTarja.append(TempList2)
        Label(GabTarjaFrame, text="Gabinete calculado",font=("bold",14)).grid(row=5, column=6, padx=10, pady=2,columnspan=4)
        CuadroNombre.set("")
        CuadroCantidad.set(0)
        CuadroEspesor.set(0)
        CuadroPuerta.set(0)
        CuadroAlto.set(0)
        CuadroAncho.set(0)
        CuadroProf.set(0)
    else:
        estado.set("DATOS INCOMPLETOS")
    Label(GabTarjaFrame, textvariable=estado).grid(row=5, column=9, padx=10, pady=2)
#-----------------------------  GABINETE PUERTA    -------------------------------------------------
def NuevoGabinetePuerta():
    alacenaFrame.pack_forget()
    GabTarjaFrame.pack_forget()
    CajonFrame.pack_forget()
    EsqFrame.pack_forget()
    GabPuertaFrame.pack(side="right", anchor="n")
    Label(GabPuertaFrame,text="Nombre: ").grid(row=1,column=6,padx=10,pady=2)
    Entry(GabPuertaFrame,textvariable=CuadroNombre).grid(row=1,column=7,padx=10,pady=2)
    Label(GabPuertaFrame, text="Cantidad: ").grid(row=2, column=6, padx=10, pady=2)
    Entry(GabPuertaFrame,textvariable=CuadroCantidad).grid(row=2, column=7, padx=10, pady=2)
    Label(GabPuertaFrame, text="Espesor: ").grid(row=3, column=6, padx=10, pady=2)
    Entry(GabPuertaFrame,textvariable=CuadroEspesor).grid(row=3, column=7, padx=10, pady=2)
    Label(GabPuertaFrame, text="Puertas: ").grid(row=4, column=6, padx=10, pady=2)
    Entry(GabPuertaFrame,textvariable=CuadroPuerta).grid(row=4, column=7, padx=10, pady=2)
    Label(GabPuertaFrame, text="Alto: ").grid(row=1, column=8, padx=10, pady=2)
    Entry(GabPuertaFrame,textvariable=CuadroAlto).grid(row=1, column=9, padx=10, pady=2)
    Label(GabPuertaFrame, text="Ancho: ").grid(row=2, column=8, padx=10, pady=2)
    Entry(GabPuertaFrame,textvariable=CuadroAncho).grid(row=2, column=9, padx=10, pady=2)
    Label(GabPuertaFrame, text="Profundidad: ").grid(row=3, column=8, padx=10, pady=2)
    Entry(GabPuertaFrame,textvariable=CuadroProf).grid(row=3, column=9, padx=10, pady=2)
    Button(GabPuertaFrame, text="ACEPTAR",command=calcularGabinetePuerta).grid(row=4, column=9, padx=10, pady=2)

def calcularGabinetePuerta():
    estado=StringVar()
    TempList = []
    TempList2 = []
    Costados = []
    armadores1 = []
    armadores2 = []
    respaldo = []
    piso = []
    separadores = []
    entrepanio = []
    puertaF = []
    puertaG = []
    piezas = []
    estado.set("")
    if validation():
        estado.set("                                       ")
        TempList.append(CuadroNombre.get())
        TempList.append(CuadroCantidad.get())
        TempList.append(CuadroEspesor.get())
        TempList.append(CuadroPuerta.get())
        TempList.append(CuadroAlto.get())
        TempList.append(CuadroAncho.get())
        TempList.append(CuadroProf.get())
        EntradasGabPuerta.append(TempList)
        aux=TempList[4] #altura
        Costados.append(aux)
        aux=TempList[6] #profundidad
        Costados.append(aux)
        aux=TempList[5]-(2*TempList[2]) #anchura-2*espesor
        armadores1.append(aux)
        aux = 100
        armadores1.append(aux)
        aux = TempList[5] - (2 * TempList[2])  # anchura-2*espesor
        armadores2.append(aux)
        aux = 70
        armadores2.append(aux)
        aux=TempList[4]-TempList[2] #altura-espesor
        respaldo.append(aux)
        aux = TempList[5] - (2 * TempList[2])  # anchura-2*espesor
        respaldo.append(aux)
        aux = TempList[5] - (2 * TempList[2])  # anchura-2*espesor
        piso.append(aux)
        aux = TempList[6]  # profundidad
        piso.append(aux)
        aux = TempList[4] - TempList[2]  # altura-espesor
        separadores.append(aux)
        aux = TempList[6] - TempList[2]  # profundidad-espesor
        separadores.append(aux)
        aux = 400
        entrepanio.append(aux)
        aux = TempList[5] - (2 * TempList[2])  # anchura-2*espesor
        entrepanio.append(aux)
        aux = TempList[4] - FORMAICA  # altura-FORMAICA
        puertaF.append(aux)
        aux = (TempList[5]/TempList[3]) - REBAJE  # anchura/puertas  - REBAJE
        puertaF.append(aux)
        aux = TempList[4] - GRANITO  # altura-FORMAICA
        puertaG.append(aux)
        aux = (TempList[5] / TempList[3]) - REBAJE  # anchura/puertas  - REBAJE
        puertaG.append(aux)
        aux = 2 * TempList[1]
        piezas.append(aux)
        aux = 1 * TempList[1]
        piezas.append(aux)
        aux = TempList[3] * TempList[1]
        piezas.append(aux)
        TempList2.append(Costados)
        TempList2.append(armadores1)
        TempList2.append(armadores2)
        TempList2.append(respaldo)
        TempList2.append(piso)
        TempList2.append(separadores)
        TempList2.append(entrepanio)
        TempList2.append(puertaF)
        TempList2.append(puertaG)
        TempList2.append(piezas)
        CalculosGabPuerta.append(TempList2)
        Label(GabPuertaFrame, text="Gabinete calculado",font=("bold",14)).grid(row=5, column=6, padx=10, pady=2,columnspan=4)
        CuadroNombre.set("")
        CuadroCantidad.set(0)
        CuadroEspesor.set(0)
        CuadroPuerta.set(0)
        CuadroAlto.set(0)
        CuadroAncho.set(0)
        CuadroProf.set(0)
    else:
        estado.set("DATOS INCOMPLETOS")
    Label(GabPuertaFrame, textvariable=estado).grid(row=5, column=9, padx=10, pady=2)
#-----------------------------  CAJONES    -----------------------------------------------------
def NuevoCajon():
    alacenaFrame.pack_forget()
    GabTarjaFrame.pack_forget()
    GabPuertaFrame.pack_forget()
    EsqFrame.pack_forget()
    CajonFrame.pack(side="right", anchor="n")
    Label(CajonFrame,text="Nombre: ").grid(row=1,column=6,padx=10,pady=2)
    Entry(CajonFrame,textvariable=CuadroNombre).grid(row=1,column=7,padx=10,pady=2)
    Label(CajonFrame, text="Cantidad: ").grid(row=2, column=6, padx=10, pady=2)
    Entry(CajonFrame,textvariable=CuadroCantidad).grid(row=2, column=7, padx=10, pady=2)
    Label(CajonFrame, text="Espesor: ").grid(row=3, column=6, padx=10, pady=2)
    Entry(CajonFrame,textvariable=CuadroEspesor).grid(row=3, column=7, padx=10, pady=2)
    Label(CajonFrame, text="Divisiones: ").grid(row=4, column=6, padx=10, pady=2)
    Entry(CajonFrame,textvariable=CuadroDivisiones).grid(row=4, column=7, padx=10, pady=2)
    Label(CajonFrame, text="Frente: ").grid(row=1, column=8, padx=10, pady=2)
    Entry(CajonFrame,textvariable=CuadroFrente).grid(row=1, column=9, padx=10, pady=2)
    Label(CajonFrame, text="Ancho: ").grid(row=2, column=8, padx=10, pady=2)
    Entry(CajonFrame,textvariable=CuadroAncho).grid(row=2, column=9, padx=10, pady=2)
    Button(CajonFrame, text="ACEPTAR",command=calcularCajon).grid(row=4, column=9, padx=10, pady=2)

def calcularCajon():
    estado=StringVar()
    TempList = []
    TempList2 = []
    Costados = []
    Frente = []
    TrasFrente = []
    Fondo = []
    piezas = []
    estado.set("")
    if validationC():
        estado.set("                                       ")
        TempList.append(CuadroNombre.get())
        TempList.append(CuadroCantidad.get())
        TempList.append(CuadroEspesor.get())
        TempList.append(CuadroDivisiones.get())
        TempList.append(CuadroFrente.get())
        TempList.append(CuadroAncho.get())
        EntradasCajon.append(TempList)
        aux=450
        Costados.append(aux)
        aux=TempList[4]-CORREDERA #Frente-corredera
        Costados.append(aux)
        aux=(TempList[5]/TempList[3])-90 #anchura/divisiones    - 90
        Frente.append(aux)
        aux =TempList[4]-CORREDERA
        Frente.append(aux)
        aux = (TempList[5]/TempList[3])-90 #anchura/divisiones    - 90
        TrasFrente.append(aux)
        aux = TempList[4]-CORREDERA
        TrasFrente.append(aux)
        aux = (TempList[5]/TempList[3])-90 #anchura/divisiones    - 90
        Fondo.append(aux)
        aux = 450 - (2 * TempList[2])  # 450-2*espesor
        Fondo.append(aux)
        aux = 2 * TempList[1]
        piezas.append(aux)
        aux = 1 * TempList[1]
        piezas.append(aux)
        TempList2.append(Costados)
        TempList2.append(Frente)
        TempList2.append(TrasFrente)
        TempList2.append(Fondo)
        TempList2.append(piezas)
        CalculosCajon.append(TempList2)
        Label(CajonFrame, text="Cajon calculado",font=("bold",14)).grid(row=5, column=6, padx=10, pady=2,columnspan=4)
        CuadroNombre.set("")
        CuadroCantidad.set(0)
        CuadroEspesor.set(0)
        CuadroFrente.set(0)
        CuadroDivisiones.set(0)
        CuadroAncho.set(0)
    else:
        estado.set("DATOS INCOMPLETOS")
    Label(CajonFrame, textvariable=estado).grid(row=5, column=9, padx=10, pady=2)
#-----------------------------  ESQUINEROS    ----------------------------------------------------
def NuevoEsq():
    GabTarjaFrame.pack_forget()
    GabPuertaFrame.pack_forget()
    CajonFrame.pack_forget()
    CajonFrame.pack_forget()
    EsqFrame.pack(side="right", anchor="n")
    Label(EsqFrame, text="Nombre: ").grid(row=1, column=6, padx=10, pady=2)
    Entry(EsqFrame,textvariable=CuadroNombre).grid(row=1,column=7,padx=10,pady=2)
    Label(EsqFrame, text="Cantidad: ").grid(row=2, column=6, padx=10, pady=2)
    Entry(EsqFrame,textvariable=CuadroCantidad).grid(row=2, column=7, padx=10, pady=2)
    Label(EsqFrame, text="Espesor: ").grid(row=3, column=6, padx=10, pady=2)
    Entry(EsqFrame,textvariable=CuadroEspesor).grid(row=3, column=7, padx=10, pady=2)
    Label(EsqFrame, text="Lat Der: ").grid(row=4, column=6, padx=10, pady=2)
    Entry(EsqFrame,textvariable=CuadroLatDer).grid(row=4, column=7, padx=10, pady=2)
    Label(EsqFrame, text="Lat Izq: ").grid(row=5, column=6, padx=10, pady=2)
    Entry(EsqFrame, textvariable=CuadroLatIzq).grid(row=5, column=7, padx=10, pady=2)
    Label(EsqFrame, text="Alto: ").grid(row=1, column=8, padx=10, pady=2)
    Entry(EsqFrame,textvariable=CuadroAlto).grid(row=1, column=9, padx=10, pady=2)
    Label(EsqFrame, text="Ancho: ").grid(row=2, column=8, padx=10, pady=2)
    Entry(EsqFrame,textvariable=CuadroAncho).grid(row=2, column=9, padx=10, pady=2)
    Label(EsqFrame, text="Profundidad: ").grid(row=3, column=8, padx=10, pady=2)
    Entry(EsqFrame,textvariable=CuadroProf).grid(row=3, column=9, padx=10, pady=2)
    Button(EsqFrame, text="ACEPTAR",command=calcularEsq).grid(row=4, column=9, padx=10, pady=2)

def calcularEsq():
    estado=StringVar()
    TempList = []
    TempList2 = []
    Costados1 = []
    Costados2 = []
    Respaldo1 = []
    Respaldo2 = []
    Entrepanio = []
    Suelo = []
    Puerta1G = []
    Puerta2G = []
    Puerta1F = []
    Puerta2F = []
    piezas = []
    estado.set("")
    if validation():
        estado.set("                                       ")
        TempList.append(CuadroNombre.get())
        TempList.append(CuadroCantidad.get())
        TempList.append(CuadroEspesor.get())
        TempList.append(CuadroLatDer.get())
        TempList.append(CuadroLatIzq.get())
        TempList.append(CuadroAlto.get())
        TempList.append(CuadroAncho.get())
        TempList.append(CuadroProf.get())
        EntradasEsq.append(TempList)
        aux=TempList[5]  #altura
        Costados1.append(aux)
        aux=TempList[3] #LatDer
        Costados1.append(aux)
        aux = TempList[5]  # altura
        Costados2.append(aux)
        aux = TempList[4]  # LatIzq
        Costados2.append(aux)
        aux = TempList[5] - TempList[2] # altura - espesor
        Respaldo1.append(aux)
        aux = TempList[6] - (2*TempList[2])  # ancho - 2*espesor
        Respaldo1.append(aux)
        aux = TempList[5] - TempList[2] # altura - espesor
        Respaldo2.append(aux)
        aux = TempList[7] - (3*TempList[2])  # profundidad - 3*espesor
        Respaldo2.append(aux)
        aux = TempList[7] - TempList[2]  # profundidad - espesor
        Entrepanio.append(aux)
        aux = TempList[6] - TempList[2]  # ancho - espesor
        Entrepanio.append(aux)
        aux = TempList[7] - TempList[2]  # profundidad - espesor
        Suelo.append(aux)
        aux = TempList[6] - TempList[2]  # ancho - espesor
        Suelo.append(aux)
        aux= TempList[5] - GRANITO #altura-granito
        Puerta1G.append(aux)
        aux = TempList[7] - TempList[4] - 25 # profundidad-LatIzq-25
        Puerta1G.append(aux)
        aux = TempList[5] - GRANITO #altura-granito
        Puerta2G.append(aux)
        aux = TempList[6] - TempList[3] - 25 # anchura-LatDer-25
        Puerta2G.append(aux)
        aux = TempList[5] - FORMAICA #altura-formaica
        Puerta1F.append(aux)
        aux = TempList[7] - TempList[4] - 25 # profundidad-LatIzq-25
        Puerta1F.append(aux)
        aux = TempList[5] -FORMAICA #altura-formaica
        Puerta2F.append(aux)
        aux = TempList[6] - TempList[3] - 25 # anchura-LatDer-25
        Puerta2F.append(aux)
        aux = 1 * TempList[1]
        piezas.append(aux)
        TempList2.append(Costados1)
        TempList2.append(Costados2)
        TempList2.append(Respaldo1)
        TempList2.append(Respaldo2)
        TempList2.append(Entrepanio)
        TempList2.append(Suelo)
        TempList2.append(Puerta1G)
        TempList2.append(Puerta2G)
        TempList2.append(Puerta1F)
        TempList2.append(Puerta2F)
        TempList2.append(piezas)
        CalculosEsq.append(TempList2)
        Label(EsqFrame, text="Esquinero calculado",font=("bold",14)).grid(row=6, column=6, padx=10, pady=2,columnspan=4)
        CuadroNombre.set("")
        CuadroCantidad.set(0)
        CuadroEspesor.set(0)
        CuadroLatDer.set(0)
        CuadroLatIzq.set(0)
        CuadroAlto.set(0)
        CuadroAncho.set(0)
        CuadroProf.set(0)
    else:
        estado.set("DATOS INCOMPLETOS")
    Label(EsqFrame, textvariable=estado).grid(row=5, column=9, padx=10, pady=2)
#------------------------------------   MOSTAR CORTES  -------------------------------------------------
def MostrarCortes():
    nombre = StringVar()
    valores1 = IntVar()
    valores2 = IntVar()
    valores3 = IntVar()
    valores4 = IntVar()
    ventana_cortes = Toplevel()
    ventana_cortes.config(width=600, height=600)
    ventana_cortes.iconbitmap("descarga.ico")
    ventana_cortes.title("Orden de corte")
    if validationV():
        Label(ventana_cortes, text="LISTA DE MUEBLES",font=("bold",12)).grid(row=0, column=0, padx=2, pady=2,columnspan=6)
        Label(ventana_cortes, text="---------------------------------------------------------------------------------------").grid(row=1, column=0, padx=2, pady=2, columnspan=6)
        Label(ventana_cortes, text="nombre").grid(row=2, column=0, padx=2,pady=2)
        Label(ventana_cortes, text="altura").grid(row=2, column=3,padx=2, pady=2)
        Label(ventana_cortes, text="anchura").grid(row=2, column=4,padx=2, pady=2)
        Label(ventana_cortes, text="profundidad").grid(row=2, column=5,padx=2, pady=2)
        Label(ventana_cortes, text="cantidad").grid(row=2, column=6,padx=2, pady=2)
        Label(ventana_cortes, text="---------------------------------------------------------------------------------------").grid(row=3, column=0, padx=2, pady=2, columnspan=6)
        if  len(EntradasAlacena) != 0:
            i = 0
            y = 0
            aux=4
            for x in range(0,len(EntradasAlacena),1):
                nombre.set(EntradasAlacena[x][y])
                Label(ventana_cortes, textvariable=nombre).grid(row=aux, column=i, padx=2, pady=2)
                i = i + 3
                y = y + 4
                valores1.set(EntradasAlacena[x][y])
                Label(ventana_cortes, textvariable=valores1).grid(row=aux, column=i, padx=2, pady=2)
                i = i + 1
                y = y + 1
                valores2.set(EntradasAlacena[x][y])
                Label(ventana_cortes, textvariable=valores2).grid(row=aux, column=i, padx=2, pady=2)
                i = i + 1
                y = y + 1
                valores3.set(EntradasAlacena[x][y])
                Label(ventana_cortes, textvariable=valores3).grid(row=aux, column=i, padx=2, pady=2)
                i = i + 1
                y = y - 5
                valores4.set(EntradasAlacena[x][y])
                Label(ventana_cortes, textvariable=valores4).grid(row=aux, column=i, padx=2, pady=2)
                aux = aux + 1
                y = 0
                i = 0

    else:
        Label(ventana_cortes, text="INTRUDUZCA DATOS PRIMERO").grid(row=1, column=1, padx=10, pady=10)
#----------------------------------------   ARCHIVO PDF    ---------------------------------------------
def GenerarArchivo():
    ArchivoPDF = FPDF(orientation="P",unit="mm",format="A4")
    ArchivoPDF.add_page()
# ----------------------------------------   CABECERA    -----------------------------------------------------
    ArchivoPDF.set_font("Arial","",18)
    ArchivoPDF.image("logo.png",x=10,y=10,w=60,h=15)
    ArchivoPDF.cell(w=0,h=15,txt="Orden de Corte",border=0,ln=1,align="C",fill=0)
    ArchivoPDF.set_font("Arial", "", 14)
    ArchivoPDF.ln(2)
    ArchivoPDF.cell(w=0, h=10, txt="Lista de muebles", border=0, ln=1, align="L", fill=0)
    ArchivoPDF.set_font("Arial", "", 12)
    ArchivoPDF.ln(2)
    ArchivoPDF.cell(w=60, h=5, txt="Nombre", border=1, align="L", fill=0)
    ArchivoPDF.cell(w=40, h=5, txt="Altura", border=1, align="L", fill=0)
    ArchivoPDF.cell(w=40, h=5, txt="Anchura", border=1, align="L", fill=0)
    ArchivoPDF.cell(w=40, h=5, txt="Profundidad", border=1, align="L", fill=0)
    ArchivoPDF.multi_cell(w=10, h=5, txt="#", border=1, align="L", fill=0)
#----------------------------------------   ENTRADAS    -----------------------------------------------------
    y = 0
    if len(EntradasAlacena) != 0:
        for x in range(0, len(EntradasAlacena), 1):
            ArchivoPDF.cell(w=60, h=5, txt=str(EntradasAlacena[x][y]), border=1, align="L", fill=0)
            y = y + 4
            ArchivoPDF.cell(w=40, h=5, txt=str(EntradasAlacena[x][y]), border=1, align="L", fill=0)
            y = y + 1
            ArchivoPDF.cell(w=40, h=5, txt=str(EntradasAlacena[x][y]), border=1, align="L", fill=0)
            y = y + 1
            ArchivoPDF.cell(w=40, h=5, txt=str(EntradasAlacena[x][y]), border=1, align="L", fill=0)
            y = y - 5
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(EntradasAlacena[x][y]), border=1, align="L", fill=0)
            y = 0
    if len(EntradasGabTarja) != 0:
        for x in range(0, len(EntradasGabTarja), 1):
            ArchivoPDF.cell(w=60, h=5, txt=str(EntradasGabTarja[x][y]), border=1, align="L", fill=0)
            y = y + 4
            ArchivoPDF.cell(w=40, h=5, txt=str(EntradasGabTarja[x][y]), border=1, align="L", fill=0)
            y = y + 1
            ArchivoPDF.cell(w=40, h=5, txt=str(EntradasGabTarja[x][y]), border=1, align="L", fill=0)
            y = y + 1
            ArchivoPDF.cell(w=40, h=5, txt=str(EntradasGabTarja[x][y]), border=1, align="L", fill=0)
            y = y - 5
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(EntradasGabTarja[x][y]), border=1, align="L", fill=0)
            y = 0
    if len(EntradasGabPuerta) != 0:
        for x in range(0, len(EntradasGabPuerta), 1):
            ArchivoPDF.cell(w=60, h=5, txt=str(EntradasGabPuerta[x][y]), border=1, align="L", fill=0)
            y = y + 4
            ArchivoPDF.cell(w=40, h=5, txt=str(EntradasGabPuerta[x][y]), border=1, align="L", fill=0)
            y = y + 1
            ArchivoPDF.cell(w=40, h=5, txt=str(EntradasGabPuerta[x][y]), border=1, align="L", fill=0)
            y = y + 1
            ArchivoPDF.cell(w=40, h=5, txt=str(EntradasGabPuerta[x][y]), border=1, align="L", fill=0)
            y = y - 5
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(EntradasGabPuerta[x][y]), border=1, align="L", fill=0)
            y = 0
    if len(EntradasCajon) != 0:
        for x in range(0, len(EntradasCajon), 1):
            ArchivoPDF.cell(w=60, h=5, txt=str(EntradasCajon[x][y]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=40, h=5, txt=str(450), border=1, align="L", fill=0)
            y = y + 5
            ArchivoPDF.cell(w=40, h=5, txt=str(EntradasCajon[x][y]), border=1, align="L", fill=0)
            y = y - 1
            ArchivoPDF.cell(w=40, h=5, txt=str(EntradasCajon[x][y]), border=1, align="L", fill=0)
            y = y - 3
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(EntradasCajon[x][y]), border=1, align="L", fill=0)
            y = 0
    if len(EntradasEsq) != 0:
        for x in range(0, len(EntradasEsq), 1):
            ArchivoPDF.cell(w=60, h=5, txt=str(EntradasEsq[x][y]), border=1, align="L", fill=0)
            y = y + 5
            ArchivoPDF.cell(w=40, h=5, txt=str(EntradasEsq[x][y]), border=1, align="L", fill=0)
            y = y + 1
            ArchivoPDF.cell(w=40, h=5, txt=str(EntradasEsq[x][y]), border=1, align="L", fill=0)
            y = y + 1
            ArchivoPDF.cell(w=40, h=5, txt=str(EntradasEsq[x][y]), border=1, align="L", fill=0)
            y = y - 6
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(EntradasEsq[x][y]), border=1, align="L", fill=0)
            y = 0
# ----------------------------------------   CALCULOS    -----------------------------------------------------
    ArchivoPDF.set_font("Arial", "", 14)
    ArchivoPDF.ln(2)
    ArchivoPDF.cell(w=0, h=10, txt="Despieze de muebles", border=0, ln=1, align="L", fill=0)
    ArchivoPDF.set_font("Arial", "", 11)
#----------------------------------------   ALACENAS    ---------------------------------------------------------------
    y = 0
    if len(EntradasAlacena) != 0:
        for x in range(0, len(CalculosAlacena), 1):
            ArchivoPDF.ln(2)
            #----------------------------------------   fila1   --------------------------------------------------------
            ArchivoPDF.cell(w=0, h=5, txt=str(EntradasAlacena[x][y]), border=1, ln=1, align="L", fill=0)
            # ----------------------------------------   fila2   -------------------------------------------------------
            ArchivoPDF.cell(w=10, h=5, txt="#", border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Pieza", border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Alto", border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt="Ancho", border=1, align="L", fill=0)
            # ----------------------------------------   fila3   -------------------------------------------------------
            y=7
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosAlacena[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Laterales", border = 1, align = "L", fill = 0)
            y = y - 7
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosAlacena[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosAlacena[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila4   -------------------------------------------------------
            y = 7
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosAlacena[x][y][1]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Tira", border = 1, align = "L", fill = 0)
            y = y - 6
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosAlacena[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosAlacena[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila5   -------------------------------------------------------
            y = 7
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosAlacena[x][y][1]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Trasera", border = 1, align = "L", fill = 0)
            y = y - 5
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosAlacena[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosAlacena[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila6   -------------------------------------------------------
            y = 7
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosAlacena[x][y][1]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Techo", border = 1, align = "L", fill = 0)
            y = y - 4
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosAlacena[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosAlacena[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila7   -------------------------------------------------------
            y = 7
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosAlacena[x][y][1]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Suelo", border = 1, align = "L", fill = 0)
            y = y - 3
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosAlacena[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosAlacena[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila8   -------------------------------------------------------
            y = 7
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosAlacena[x][y][1]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Repisa", border = 1, align = "L", fill = 0)
            y = y - 2
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosAlacena[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosAlacena[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila9   -------------------------------------------------------
            y = 7
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosAlacena[x][y][2]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Puerta", border = 1, align = "L", fill = 0)
            y = y - 1
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosAlacena[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosAlacena[x][y][1]), border=1, align="L", fill=0)
#--------------------------------------------   GAB TARJA ----------------------------------------------------------------
        y = 0
    if len(EntradasGabTarja) != 0:
        for x in range(0, len(CalculosGabTarja),1):
            ArchivoPDF.ln(2)
            # ----------------------------------------   fila1   -------------------------------------------------------
            ArchivoPDF.cell(w=0, h=5, txt=str(EntradasGabTarja[x][y]), border=1, ln=1, align="L", fill=0)
            # ----------------------------------------   fila2   -------------------------------------------------------
            ArchivoPDF.cell(w=10, h=5, txt="#", border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Pieza", border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Alto", border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt="Ancho", border=1, align="L", fill=0)
            # ----------------------------------------   fila3   -------------------------------------------------------
            y = 6
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosGabTarja[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Laterales", border=1, align="L", fill=0)
            y = y - 6
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosGabTarja[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosGabTarja[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila4   -------------------------------------------------------
            y = 6
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosGabTarja[x][y][1]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Armadores", border=1, align="L", fill=0)
            y = y - 5
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosGabTarja[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosGabTarja[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila5   -------------------------------------------------------
            y = 6
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosGabTarja[x][y][1]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Trasera", border=1, align="L", fill=0)
            y = y - 4
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosGabTarja[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosGabTarja[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila6   -------------------------------------------------------
            y = 6
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosGabTarja[x][y][1]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Piso", border=1, align="L", fill=0)
            y = y - 3
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosGabTarja[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosGabTarja[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila7   -------------------------------------------------------
            y = 6
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosGabTarja[x][y][1]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="PuertaF", border=1, align="L", fill=0)
            y = y - 2
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosGabTarja[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosGabTarja[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila8   -------------------------------------------------------
            y = 6
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosGabTarja[x][y][1]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="PuertaG", border=1, align="L", fill=0)
            y = y - 1
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosGabTarja[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosGabTarja[x][y][1]), border=1, align="L", fill=0)

# --------------------------------------------   GAB PUERTA ------------------------------------------------------------
        y = 0
    if len(EntradasGabPuerta) != 0:
        for x in range(0, len(CalculosGabPuerta), 1):
            ArchivoPDF.ln(2)
            # ----------------------------------------   fila1   -------------------------------------------------------
            ArchivoPDF.cell(w=0, h=5, txt=str(EntradasGabPuerta[x][y]), border=1, ln=1, align="L", fill=0)
            # ----------------------------------------   fila2   -------------------------------------------------------
            ArchivoPDF.cell(w=10, h=5, txt="#", border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Pieza", border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Alto", border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt="Ancho", border=1, align="L", fill=0)
            # ----------------------------------------   fila3   -------------------------------------------------------
            y = 9
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosGabPuerta[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Laterales", border=1, align="L", fill=0)
            y = y - 9
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosGabPuerta[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosGabPuerta[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila4   -------------------------------------------------------
            y = 9
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosGabPuerta[x][y][1]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Armadores 1", border=1, align="L", fill=0)
            y = y - 8
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosGabPuerta[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosGabPuerta[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila5   -------------------------------------------------------
            y = 9
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosGabPuerta[x][y][1]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Armadores 2", border=1, align="L", fill=0)
            y = y - 7
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosGabPuerta[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosGabPuerta[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila6   -------------------------------------------------------
            y = 9
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosGabPuerta[x][y][1]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Trasera", border=1, align="L", fill=0)
            y = y - 6
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosGabPuerta[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosGabPuerta[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila7   -------------------------------------------------------
            y = 9
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosGabPuerta[x][y][1]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Piso", border=1, align="L", fill=0)
            y = y - 5
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosGabPuerta[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosGabPuerta[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila8   -------------------------------------------------------
            y = 9
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosGabPuerta[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Separadores", border=1, align="L", fill=0)
            y = y - 4
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosGabPuerta[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosGabPuerta[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila9   -------------------------------------------------------
            y = 9
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosGabPuerta[x][y][1]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Entrepaño", border=1, align="L", fill=0)
            y = y - 3
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosGabPuerta[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosGabPuerta[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila10   -------------------------------------------------------
            y = 9
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosGabPuerta[x][y][2]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Puerta Formaica", border=1, align="L", fill=0)
            y = y - 2
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosGabPuerta[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosGabPuerta[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila11   -------------------------------------------------------
            y = 9
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosGabPuerta[x][y][2]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Puerta Granito", border=1, align="L", fill=0)
            y = y - 1
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosGabPuerta[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosGabPuerta[x][y][1]), border=1, align="L", fill=0)
# --------------------------------------------   CAJONES ---------------------------------------------------------------
        y = 0
    if len(EntradasCajon) != 0:
        for x in range(0, len(CalculosCajon), 1):
            ArchivoPDF.ln(2)
            # ----------------------------------------   fila1   -------------------------------------------------------
            ArchivoPDF.cell(w=0, h=5, txt=str(EntradasCajon[x][y]), border=1, ln=1, align="L", fill=0)
            # ----------------------------------------   fila2   -------------------------------------------------------
            ArchivoPDF.cell(w=10, h=5, txt="#", border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Pieza", border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Alto", border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt="Ancho", border=1, align="L", fill=0)
            # ----------------------------------------   fila3   -------------------------------------------------------
            y = 4
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosCajon[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Laterales", border=1, align="L", fill=0)
            y = y - 4
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosCajon[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosCajon[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila4   -------------------------------------------------------
            y = 4
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosCajon[x][y][1]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Frente", border=1, align="L", fill=0)
            y = y - 3
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosCajon[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosCajon[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila5   -------------------------------------------------------
            y = 4
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosCajon[x][y][1]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Trasfrente", border=1, align="L", fill=0)
            y = y - 2
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosCajon[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosCajon[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila6   -------------------------------------------------------
            y = 4
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosCajon[x][y][1]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Fondo", border=1, align="L", fill=0)
            y = y - 1
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosCajon[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosCajon[x][y][1]), border=1, align="L", fill=0)
# --------------------------------------------   ESQUINERO ------------------------------------------------------------
        y = 0
    if len(EntradasEsq) != 0:
        for x in range(0, len(CalculosEsq), 1):
            ArchivoPDF.ln(2)
            # ----------------------------------------   fila1   -------------------------------------------------------
            ArchivoPDF.cell(w=0, h=5, txt=str(EntradasEsq[x][y]), border=1, ln=1, align="L", fill=0)
            # ----------------------------------------   fila2   -------------------------------------------------------
            ArchivoPDF.cell(w=10, h=5, txt="#", border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Pieza", border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Alto", border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt="Ancho", border=1, align="L", fill=0)
            # ----------------------------------------   fila3   -------------------------------------------------------
            y = 10
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosEsq[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Lateral 1", border=1, align="L", fill=0)
            y = y - 10
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosEsq[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosEsq[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila4   -------------------------------------------------------
            y = 10
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosEsq[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Lateral 2", border=1, align="L", fill=0)
            y = y - 9
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosEsq[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosEsq[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila5   -------------------------------------------------------
            y = 10
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosEsq[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Respaldo 1", border=1, align="L", fill=0)
            y = y - 8
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosEsq[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosEsq[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila6   -------------------------------------------------------
            y = 10
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosEsq[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Respaldo 2", border=1, align="L", fill=0)
            y = y - 7
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosEsq[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosEsq[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila7   -------------------------------------------------------
            y = 10
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosEsq[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Entrepaño", border=1, align="L", fill=0)
            y = y - 6
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosEsq[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosEsq[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila8   -------------------------------------------------------
            y = 10
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosEsq[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Suelo", border=1, align="L", fill=0)
            y = y - 5
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosEsq[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosEsq[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila9   -------------------------------------------------------
            y = 10
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosEsq[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Puerta 1 Granito", border=1, align="L", fill=0)
            y = y - 4
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosEsq[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosEsq[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila10   -------------------------------------------------------
            y = 10
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosEsq[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Puerta 2 Granito", border=1, align="L", fill=0)
            y = y - 3
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosEsq[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosEsq[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila11   -------------------------------------------------------
            y = 10
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosEsq[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Puerta 1 Formaica", border=1, align="L", fill=0)
            y = y - 2
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosEsq[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosEsq[x][y][1]), border=1, align="L", fill=0)
            # ----------------------------------------   fila12   -------------------------------------------------------
            y = 10
            ArchivoPDF.cell(w=10, h=5, txt=str(CalculosEsq[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.cell(w=60, h=5, txt="Puerta 2 Formaica", border=1, align="L", fill=0)
            y = y - 1
            ArchivoPDF.cell(w=60, h=5, txt=str(CalculosEsq[x][y][0]), border=1, align="L", fill=0)
            ArchivoPDF.multi_cell(w=0, h=5, txt=str(CalculosEsq[x][y][1]), border=1, align="L", fill=0)



    ArchivoPDF.output("Orden de corte.pdf")
#-------------------------------------------------------------------------------------------------------

Button(botonesFrame,text="Alacenas",command=NuevaAlacena).grid(row=1,column=0,padx=2,pady=2)
Button(botonesFrame,text="Gabinete Tarja",command=NuevoGabineteTarja).grid(row=2,column=0,padx=2,pady=2)
Button(botonesFrame,text="Gabinete Puertas",command=NuevoGabinetePuerta).grid(row=3,column=0,padx=2,pady=2)
Button(botonesFrame,text="Cajon",command=NuevoCajon).grid(row=4,column=0,padx=2,pady=2)
Button(botonesFrame,text="Esquinero",command=NuevoEsq).grid(row=5,column=0,padx=2,pady=2)
#Button(botonesFrame,text="Mostrar Cortes").grid(row=6,column=0,padx=2,pady=2)
Button(botonesFrame,text="Generar Archivo",command=GenerarArchivo).grid(row=7,column=0,padx=2,pady=2)
Label(botonesFrame,text="Desgloce de cortes",font=("bold",12)).grid(row=0,column=0,padx=2,pady=2)
base.mainloop()