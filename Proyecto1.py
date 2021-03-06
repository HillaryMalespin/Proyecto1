"""
Nombre: menu
funcion que despliega un menu con las opciones principales.
Cuenta con opción de salida.
"""
def menu():
    f=open("Empresas.txt","a")
    f.close()
    print ("Bienvenido/a al menú principal ¿Qué desea hacer?")
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
    print ("Bienvenido/a al menú administrativo ¿Qué desea hacer?")
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
        return gestionDeViajeMenu()
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
    print("Bienvenido/a a gestión de empresas ¿Qué desea hacer?")
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
    flag=False
    f=open("Empresas.txt","a")
    f.close()
    cedula_empresa=input("Agregue el número de cédula de la persona sin espacios y con ceros ""\n")
    if cedula_empresa.isdigit()==True:#Verifico que la cédula sean números
        if (len(cedula_empresa))==9:#Verifico que la cédula sean nueve dígitos
            f = open("Empresas.txt","r")
            cedula = f.readlines()
            if cedula_empresa in "".join(cedula):
                print("Ese número de cédula ya existe")#Se verifica si ya existe ese número de cédula
                incluirEmpresas()
                f.close()
            else:
                nombre_empresa=input("Agregue el nombre de la empresa""\n")
                if (len(nombre_empresa))>0:#En este bloque se verifica que ningun dato esté vacío.
                    if len(nombre_empresa)> 0 and nombre_empresa.isdigit()==False:
                        Ubicación_Empresa=input("Agregue la ubicación de la empresa""\n")
                        if len(Ubicación_Empresa)> 0 and Ubicación_Empresa.isdigit()==False:
                            flag=True
                            datos_empresa=cedula_empresa+","+nombre_empresa+","+Ubicación_Empresa+"\n"
                            print("")
                            print("Empresa guardada")
                            return anexarContenidoArchivo("Empresas.txt",datos_empresa)+ gestionDeEmpresas()#Procede a guardar los datos en el archvio
                        else:
                            print("La ubicación no puede estar vacía ni se numeros")+incluirEmpresas()
                    else:
                        return print("El nombre no puede ser vacio y no puede contener números")+ incluirEmpresas()
                else:
                    return print("La cédula debe de tener 9 dígitos")+incluirEmpresas()
        else:
            print("Debe contener los ceros")+incluirEmpresas()
    else:
        print("La cedula solo deben ser numeros")+incluirEmpresas()


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
        f.close()
        return escribirArchivo("Empresas.txt",guardar)
    else:
        print("No puede dejar valores en blanco")
        ModificarContacto()

"""
nombre: Ver todas las empresas
función que devuelve todas las empresas.
"""
def verTodasLasEmpresas():#función hecha para ver todos los empresas
    file = open("Empresas.txt","r")
    print ("Sus empresas son:")
    print("\n")
    for line in file:
        print(line)
    file.close()
    menu()

def verTodasLasEmpresas2():#función hecha para ver todos los empresas
    file = open("Empresas.txt","r")
    print("\n")
    for line in file:
        print(line)
    file.close()
    
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
    cedula_empresa=input("Agregue el número de cédula de la persona sin espacios y con ceros ""\n")
    placa=input("Agregue el número de placa de la persona sin espacios""\n")
    if placa.isdigit()==True:#Verifico que la cédula sean números
            f = open("Transporte.txt","r")
            cedula = f.readlines()
            if cedula_empresa in "".join(cedula):
                print("Ese número de cédula ya existe")
                gestionDeTransportePorEmpresas()
                f.close()
            else:
                nombre_marca=input("Agregue el nombre de la marca""\n")
                if len(nombre_marca)> 0 and nombre_marca.isdigit()==False:
                    modelo=input("Agreque el modelo del transporte""\n")
                    if len(modelo)> 0:
                        return print("Se ha guardado correctamente")+ gestionDeTransportePorEmpresas()
                        año=input("Dígite el año del transporte")
                        if año.isdigit()==True:
                            VIP=input("Agregue el numero de campos VIP que contiene el transporte")+ gestionDeTransportePorEmpresas()
                            if VIP.isdigit() and (VIP>0):
                                Clase_Normal=input("Agregue el numero de campos de clase normal que contiene el transporte")+ gestionDeTransportePorEmpresas()
                                if Clase_Normal.isdigit() and (Clase_Normal>0):
                                    Clase_economica=input("Agregue el numero de campos de clase economica que contiene el transporte")+ gestionDeTransportePorEmpresas()
                                    if Clase_economica.isdigit() and (Clase_economica>0):
                                        return input("Digite su empresa:")+ gestionDeTransportePorEmpresas()
                                        return verTodasLasEmpresas()
                                    f=open("Empresas.txt","r")
                                    empresa=f.readlines
                                    if empresa in "".join(empresa):
                                        datos_empresa=cedula_empresa+","+nombre_marca+","+modelo+","+año+","+VIP+","+Clase_Normal+","+Clase_economica
                                        print("Se han guardados todos los datos correctamente.")+ menu()
                                        return anexarContenidoArchivo("Viajes.txt",datos_empresa)+menu()
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
                    return print("La cédula ya existe")+ gestionDeTransportePorEmpresas()
    else:
      return print("la placa deben ser números")+ gestionDeTransportePorEmpresas()

def gestionDeViajeMenu():
    print("")
    print("Bienvenido a gestión de viajes ¿Qué desea hacer?")
    print("")
    print("1.Guardar viaje")
    print("2.Modificar vieja")
    print("3.Eliminar viaje")
    print("4.Mostrar todas los viajes")
    print("5.Volver a menú principal")
    print("6.Volver a menú administrativo")
    print("")
    opcion=input("Ingrese su opción ")
    print("")
    if opcion=="1":
        return gestionDeViaje()
    elif opcion=="2":
        return modificarViaje()
    elif opcion=="3":
        return EliminarViaje()
    elif opcion=="4":
        return verTodosLosViajes()
    elif opcion=="5":
        return menu()
    elif opcion=="6":
        return menuAdministrativo()

    
from random import randint
n=randint(1,500)
n2=randint(1,500)
Numero_de_viaje=n+n2
def gestionDeViaje():
    f=open("Viajes.txt","a")
    f.close
    ciudad_salida=input("Digite el lugar de donde saldrá ""\n")
    if len (ciudad_salida)>0:
        Fecha_salida=input("Digite la fecha en la que sale""\n")
        hora_salida=input("Digite la hora en la que sale""\n")
        if len(Fecha_salida)> 0 and len (hora_salida)>0:
            Ciudad_de_llegada=input("Agregue el destino al que desea llegar""\n")
            if len(Ciudad_de_llegada)>0:
                Fecha_llegada=input("Digite la fecha en la que sale""\n")
                hora_llegada=input("Digite la hora en la que sale""\n")
                if len(Fecha_llegada)> 0 and len (hora_llegada)>0:
                        file = open("Empresas.txt","r")
                        print("\n")
                        for line in file:
                            print(line)
                        file.close()
                        print("Estas son las empresas con las que contamos")
                        empresaYtransporte=input("digite la empresa y transporte que desee")
                        monto= print(Clase_economica, Clase_Normal, VIP)
                        monto_pagar=input("Digite cual clase desea pagar")
                        if len(monto_pagar)>0:
                            return ("Su viaje a sido guardado")
                            datos_viaje=Numero_de_viaje+","+ciudad_salida+","+Fecha_salida+","+hora_salida+","+Ciudad_de_llegada+","+Fecha_llegada+","+hora_llegada+","+empresaYtransporte+","+monto_pagar
                            return anexarContenidoArchivo("Viajes.txt",datos_viaje)
                            print("Su numero de viaje es:")
                            return Numero_de_viaje
                            return menu()
                        else:
                            return print("El monto no puede ir en blanco")+gestionDeViaje()
                else:
                    return print("La fecha y hora no pueden ir vacías. Digite su fecha y hora de salida")+gestionDeViaje()
            else:
                return print("La ciudad de llegada no puede ir en blanco. Digite su lugar de llegada")+gestionDeViaje()
        else:
            return print("La fecha y hora no pueden ir vacías. Digite su fecha y hora de llegada")+gestionDeViaje()
    else:
        return print("La ciudad de salida no puede ir en blanco. Digite su lugar de llegada")+gestionDeViaje()
    

"""
nombre: modificar empresa
función que hace que el usuario pueda modificar los datos de una empresa.
"""
def modificarViaje():
    global guardar
    guardar=''
    num_cedula=input("Digite el número de cédula")
    f = open("Viajes.txt","r")
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
nombre: Ver todas los viajes
función que devuelve todos los viajes.
"""
def verTodosLosViajes():#función hecha para ver todos los empresas
    file = open("Viajes.txt","r")
    print ("Sus viajes son:")
    print("\n")
    for line in file:
        print(line)
    file.close()
    menu()

"""
nombre: Eliminar viaje
función que elimina un viaje
"""
def EliminarViaje():
    global guardar
    guardar=''
    num_cedula=input("Digite el número de cédula")
    file = open("Viajes.txt","r")
    for line in file:
        if num_cedula in line:
            guardar += ''
        else: guardar+=line
    file.close()
    return escribirArchivo("Viajes.txt",guardar)


def ReservaciónDeViaje():
    f=open("Reservaciones.txt","a")
    f.close()
    print("Bienvenido/a a reservación de viaje")
    print("")
    return Numero_viaje
    return verTodasLasEmpresas()
    return Fecha_salida
    return Fecha_llegada
    identificador= input("Seleccione uno de los identificadores")
    if identificador==Numero_viaje:
        return anexarContenidoArchivo("Reservaciones.txt", Numero_viaje)
        f = open (archivo,'a')
        f.write(mensaje)
        f.close()
    elif identificador==verTodasLasEmpresas:
        return anexarContenidoArchivo("Reservaciones.txt", verTodasLasEmpresas)
        f = open (archivo,'a')
        f.write(mensaje)
        f.close()
    elif identificador==Fecha_salida:
        return anexarContenidoArchivo("Reservaciones.txt", Fecha_salida)
        f = open (archivo,'a')
        f.write(mensaje)
        f.close()
    elif identificador==Fecha_llegada:
        return anexarContenidoArchivo("Reservaciones.txt", Fecha_llegada)
        f = open (archivo,'a')
        f.write(mensaje)
        f.close()
        return ReservaciónDeViaje_Aux()
    else:
        print("El identificador debe ser algunos de los brindados anteriormente")


def ReservaciónDeViaje_Aux():
    f=open("Reservaciones.txt","a")
    f.close()
    nombre= input("Ingrese su nombre completo")
    if isinstance (nombre,str):
        Asientos=input(int("Digite la cantidad de asientos que desea"))
        f=open("Reservaciones.txt","a")
        f.close()
        return gestionDeViaje()
        print (Numero_de_viaje+","+ciudad_salida+","+Fecha_salida+","+hora_salida+","+Ciudad_de_llegada+","+Fecha_llegada+","+hora_llegada+","+empresaYtransporte+","+monto_pagar)
        

"""
Nombre: Consultar el historial de reservaciones.
Función que atiende consultas sobre el historial de reservaciones.
"""
def menuFiltro():
    print("Bienvenido/a al historial de reservación")
    print("")
    print("¿Por cuál filtro desea byscar la información?")
    print("")
    print("1.Rango de fecha de salida")
    print("2.Rango de fecha de entrada")
    print("3.Rango de fecha de reservación")
    print("4.Lugar de salida y entrada")
    opcion=input("Ingrese su opción ")#Aquí tomamos lo que quiere hacer el usuario
    print("")
    if opcion=="1":
        return "hola"
    elif opcion=="2":
        return "Ha digitado 2"
    elif opcion=="3":
        return print("Que pase un buen día")
    elif opcion=="3":
        return print("Que pase un buen día")
    else:
        print("Debe digitar un número de la lista")
        menu()
"""
"""
def estadisticaDeViaje():
    return verTodosLosViaje()

"""
"""
def opcionesGenerales():
    print ("Bienvenido al menú de opciones generales ¿Qué desea hacer?")
    print("")
    print("1.Consulta de viajes")
    print("2.Reservación de viajes")
    print("3.Cancelación de reservación")
    print("4.Salir")
    print("")
    opcion=input("Ingrese su opción ")#Aquí tomamos lo que quiere hacer el usuario
    if opcion=="1":
        return menuAdministrativo()
    elif opcion=="2":
        return "Ha digitado 2"
    elif opcion=="3":
        return print("Que pase un buen día")
    elif opcion=="3":
        return print("Que pase un buen día")
    else:
        print("Debe digitar un número de la lista")
        menu()

def consultaDeViajes():
    return verTodosLosViaje()

def cancelacionDeReserva():
    f=open("Reservaciones.txt","a")
    f.close()


def salir():
    print("Que tenga un buen día")
    









####################################################################################################################
def escribirArchivo(archivo, mensaje):
    f = open (archivo,'w')
    f.write(mensaje)
    f.close()
    print("Se ha guardado la nueva información")
    menu()

def anexarContenidoArchivo(archivo, mensaje):
    f = open (archivo,'a')
    f.write(mensaje)
    f.close()

def leerArchivoReadLinesFor(archivo):
    f = open (archivo,'r')
    for mensaje in f.readlines():
        print(mensaje)
    f.close()    
    
    
    
    
    
    
