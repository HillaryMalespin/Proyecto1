def menu():
    f=open("Agenda.txt","a")
    f.close()
    print ("Bienvenido al menú principal ¿Qué desea hacer?")
    print("")
    print("1.Opciones Administrativa")
    print("2.Opciones de usuario normal")
    print("9.Salir")
    print("")
    opcion=input("Ingrese su opción ")#Aquí tomamos lo que quiere hacer el usuario
    if opcion=="1":
        return menuAdministrativo()
    elif opcion=="2":
        return "Ha digitado 2"
    elif opcion=="9":
        return print("Que pase un buen día")
    else:
        print("Debe digitar un número de la lista")
        menu()

def menuAdministrativo():
    print("")
    print ("Bienvenido al menú administrativo ¿Qué desea hacer?")
    print("")
    print("1.Gestión de empresas")
    print("2.Gestión de transporte por empresa")
    print("3.Gestión de viaje")
    print("4.Consultar historial de reservaciones")
    print("5.Estadística de viaje")
    print("6.Menú principal")
    print("")
    opcion=input("Ingrese su opción ")
    print("")
    if opcion=="1":
        return gestionDeEmpresas()
    elif opcion=="2":
        return "Hola2"
    elif opcion=="3":
        return "Hola3"
    elif opcion=="4":
        return "Hola4"
    elif opcion=="5":
        return "Hola5"
    
    elif opcion=="6":
        return menu()

def gestionDeEmpresas():
    print("")
    print("Bienvenido a gestión de empresas ¿Qué desea hacer?")
    print("")
    print("1.Incluir empresa")
    print("2.Modificar empresa")
    print("3.Eliminar Empresa")
    print("4. Mostrar todas las empresas")
    print("5.Volver a menú pincipal")
    print("6.Volver a menú administrativo")
    print("")
    opcion=input("Ingrese su opción ")
    print("")
    if opcion=="1":
        return incluirEmpresas()
    elif opcion=="2":
        return "Ha elegido  Modificar empresa"
    elif opcion=="3":
        return "Ha elegido eliminar empresa"
    elif opcion=="4":
        return "Ha elegido mostrar todas las empresas"
    elif opcion=="5":
        return menu()
    elif opcion=="6":
        return menuAdministrativo()

def incluirEmpresas():

    cedula_empresa=input("Ingrese su numero de cédula")
    if cedula_empresa.isdigit()==True:
        if (len(cedula_empresa))==9:
                f = open("Agenda.txt","r")
                nombre_empresa= input("Ingrese su nombre")
                
    
    
    
    
    
    
