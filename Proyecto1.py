"""
Nombre: menu
funcion que despliega un menu con las opciones principales.
Cuenta con opción de salida.
"""
def menu():
    f=open("Empresas.txt","a")
    f.close()
    print ("Bienvenido al menú principal ¿Qué desea hacer?")
    print("")
    print("1.Opciones Administrativa")
    print("2.Opciones de usuario normal")
    print("3.Salir")
    print("")
    opcion=input("Ingrese su opción ")#Aquí tomamos lo que quiere hacer el usuario
    if opcion=="1":
        return menuAdministrativo()
    elif opcion=="2":
        return "Ha digitado 2"
    elif opcion=="3":
        return print("Que pase un buen día")
    else:
        print("Debe digitar un número de la lista")
        menu()
"""
Nombre: menú administrativo.
funcion que demuestra las funciones administrativas
"""
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
        return gestionDeTransportePorEmpresas()
    elif opcion=="3":
        return "Hola3"
    elif opcion=="4":
        return "Hola4"
    elif opcion=="5":
        return "Hola5"
    elif opcion=="6":
        return menu()
"""
nombre: gestion de empresas
despliega opciones que el usuario desee ejecutar.
El usuario puede incluir, modificar o eliminar una emprea.
Tambien hay opcion de mostrar todas las empresas y volver a los menú anteriores.
"""
def gestionDeEmpresas():
    print("")
    print("Bienvenido a gestión de empresas ¿Qué desea hacer?")
    print("")
    print("1.Incluir empresa")
    print("2.Modificar empresa")
    print("3.Eliminar Empresa")
    print("4.Mostrar todas las empresas")
    print("5.Volver a menú principal")
    print("6.Volver a menú administrativo")
    print("")
    opcion=input("Ingrese su opción ")
    print("")
    if opcion=="1":
        return incluirEmpresas()
    elif opcion=="2":
        return modificarEmpresa()
    elif opcion=="3":
        return EliminarEmpresa()
    elif opcion=="4":
        return verTodasLasEmpresas()
    elif opcion=="5":
        return menu()
    elif opcion=="6":
        return menuAdministrativo()

"""
nombre: incluir empresas
El usuario será capaz de incluir una empresa que no haya sido registrada.
"""
def incluirEmpresas():
    cedula_empresa=input("Agregue el número de cédula de la persona sin espacios y con ceros ""\n")
    if cedula_empresa.isdigit()==True:#Verifico que la cédula sean números
        if (len(cedula_empresa))==9:#Verifico que la cédula sean nueve dígitos
            f = open("Empresas.txt","r")
            cedula = f.readlines()
            if cedula_empresa in "".join(cedula):
                print("Ese número de cédula ya existe")#Se verifica si ya existe ese número de cédula
                incluirEmpresas()
                f.close()
            else:#En este bloque se verifica que ningun dato esté vacío.
                nombre_empresa=input("Agregue el nombre de la empresa""\n")
                if len(nombre_empresa)> 0 and nombre_empresa.isdigit()==False:
                    Ubicación_Empresa=input("Agregue la ubicación de la empresa""\n")
                    if len(Ubicación_Empresa)> 0 and Ubicación_Empresa.isdigit()==False:
                        return print("Se ha guardado correctamente")+ gestionDeEmpresas()
                    else:
                        print("La ubicación no puede estar vacía ni se numeros")+incluirEmpresas()
                else:
                    return print("El nombre no puede ser vacio y no puede contener números")+ incluirEmpresas()
        else:
            return print("La cédula debe de tener 9 dígitos")+incluirEmpresas()
    else:
        return print("la cédula deben ser números")+incluirEmpresas()


"""
nombre: modificar empresa
función que hace que el usuario pueda modificar los datos de una empresa.
"""
def modificarEmpresa():
    global guardar
    guardar=''
    num_cedula=input("Digite el número de cédula")
    f = open("archivo.txt","r")
    if num_cedula != '':
        for line in f:
            if num_cedula in line:
                nuevos_datos=line.split(",")
                nuevo_nombre=input("Ingrese el nuevo nombre""\n")
                nueva_ubicacion=input("Ingrese la nueva ubicación")
                nuevos_datos[2]=nuevo_nombre
                nuevos_datos[3]=nueva_ubicacion
                datos_editados=",".join(nuevos_datos)
                guardar += datos_editados
            else: guardar+=line
        file.close()
        return escribirArchivo("Empresas.txt",guardar)
    else:
        print("No puede dejar valores en blanco")
        ModificarContacto()

"""
nombre: Ver todas las empresas
función que devuelve todas las empresas.
"""
def verTodasLasEmpresas():#función hecha para ver todos los contactos
    file = open("Empresas.txt","r")
    print ("Sus empresas son:")
    print("\n")
    for line in file:
        print(line)
    file.close()
    menu()
    
"""
nombre: Eliminar Empresa
función que elimina una empresa
"""
def EliminarEmpresa():
    global guardar
    guardar=''
    num_cedula=input("Digite el número de cédula")
    file = open("Empresas.txt","r")
    for line in file:
        if num_cedula in line:
            guardar += ''
        else: guardar+=line
    file.close()
    return escribirArchivo("Empresas.txt",guardar)

"""
nombre:Gestión de transporte de empresas.
función:
"""
def gestionDeTransportePorEmpresas():
    f=open("Transporte.txt","a")
    f.close()
    placa=input("Agregue el número de placa de la persona sin espacios""\n")
    if placa.isdigit()==True:#Verifico que la cédula sean números
            f = open("Transporte.txt","r")
            placa = f.readlines()
            if cedula_empresa in "".join(cedula):
                print("Ese número de cédula ya existe")#Se verifica si ya existe ese número de cédula
                gestionDeTransportePorEmpresas()
                f.close()
                nombre_marca=input("Agregue el nombre de la marca""\n")
                if len(nombre_empresa)> 0 and nombre_empresa.isdigit()==False:
                    modelo=input("Agreque el modelo del transporte""\n")
                    if len(modelo)> 0:
                        return print("Se ha guardado correctamente")+ gestionDeTransportePorEmpresas()
                        año=input("Dígite el año del transporte")
                        if año.isdigit()==True:
                            VIP=input("Agregue el numero de campos VIP que contiene el transporte")+ gestionDeTransportePorEmpresas()
                            if VIP.isdigit() and VIP>0):
                                Clase_Normal=input("Agregue el numero de campos de clase normal que contiene el transporte")+ gestionDeTransportePorEmpresas()
                                if Clase_Normal.isdigit() and Clase_Normal>0):
                                    Clase_economica=input("Agregue el numero de campos de clase economica que contiene el transporte")+ gestionDeTransportePorEmpresas()
                                    if Clase_economica.isdigit() and Clase_economica>0):
                                        return input("Digite su empresa:")+ gestionDeTransportePorEmpresas()
                                        return verTodasLasEmpresas()
                                    f=open("Empresas.txt","r")
                                    empresa=f.readlines
                                        if empresa in "".join(empresa)
                                        print("Se han guardados todos los datos correctamente.")+ gestionDeTransportePorEmpresas()
                                        return menu()
                                    else:
                                        print("La cantidad de asientos deben ser números y no debe ir vacío")+ gestionDeTransportePorEmpresas()
                                else:
                                        print("La cantidad de asientos deben ser números y no debe ir vacío")+ gestionDeTransportePorEmpresas()
                            else:
                                        print("La cantidad de asientos deben ser números y no debe ir vacío")+ gestionDeTransportePorEmpresas()
                        else:
                            print("El año debe ser un numero entero")+ gestionDeTransportePorEmpresas()
                    else:
                        print("El modelo no debe ir vacío")+ gestionDeTransportePorEmpresas()
                else:
                    return print("La cédula no existe")+ gestionDeTransportePorEmpresas()
    else:
        return print("la placa deben ser números")+ gestionDeTransportePorEmpresas()

def gestionDeViaje()


    

def escribirArchivo(archivo, mensaje):
    f = open (archivo,'w')
    f.write(mensaje)
    f.close()
    print("Se ha guardado la nueva información")
    menu()
                
    
    
    
    
    
    
