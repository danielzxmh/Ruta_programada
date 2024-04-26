list_programacion = []
list_rutas = []
import os 





def fnt_limpiar():
    os.system("cls")
    print("Nombre de programa: Gestion de rutas")
    print("AUTOR: Erminio barrajasada amigoniano ")
    print("Año: 2024")
    print("universidad catolica luis amigo\n")

def fnt_agregar_ruta():
    fnt_limpiar()
    print("\n aGREGAR NUEVA RUTA \n")
    cod = input("Codigo  ")
    nombre = input("Nombre  ")
    descripcion = input("descripcion")
    r = cod + " " + nombre + " " + descripcion 
    list_rutas.append(r)
    input("\nruta registrada con exito <ENTER>")
sw2 = True

def fnt_menu_rutas():
    fnt_limpiar()
    opcionStr = input("Menu rutas \n1. agregar \n2. consultar \n3. salir \n")
    global sw2
    while sw2 == True
    fnt_limpiar()
    opcion_r = input()
    
def fnt_consultar_rutas():
    fnt_limpiar()
    print("\nNo hay rutas registradas")
    
        

sw = True 
while sw == True:
    fnt_limpiar()
    opcionStr = input("Menu rutas \n1. Registrar nueva ruta \n2. envios \n3. salir \n")
    if opcionStr == "1":
        fnt_agregar_ruta()
    
    
    