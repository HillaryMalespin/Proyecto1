"""
Nombre: menu
funcion que despliega un menu con las opciones principales.
Cuenta con opción de salida.
"""
def menu():
    f=open("Empresas.txt","a")#Abre el archivo y luego lo cierra
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
        return opcionesGenerales()
    elif opcion=="3":
        return salir()
#Se le devuelve el menú que desea depende de la opción que seleccione
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
    opcion=input("Ingrese su opción ")# Se toma la opción que el usuario desee
    print("")
#Depende de la opción que seleccione se le retorna la función que desee
    if opcion=="1":
        return gestionDeEmpresas()
    elif opcion=="2":
        return gestionDeTransportePorEmpresas()
    elif opcion=="3":
        return gestionDeViajeMenu()
    elif opcion=="4":
        return menuFiltro()
    elif opcion=="5":
        return estadisticaDeViaje()
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
    opcion=input("Ingrese su opción ")# Se toma la opción que el usuario desee
    print("")
#Depende de la opción que seleccione se le retorna la función que desee
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
    cedula_empresa=input("Agregue el número de cédula de la persona sin espacios y con ceros ""\n")#Se le solicita el numero de cedula
    if cedula_empresa.isdigit()==True:#Verifico que la cédula sean números
        if (len(cedula_empresa))==9:#Verifico que la cédula sean nueve dígitos
            f = open("Empresas.txt","r")#Se abre el archivo para verificar si la cedula ya existe
            cedula = f.readlines()
            if cedula_empresa in "".join(cedula):
                print("Ese número de cédula ya existe")#Se verifica si ya existe ese número de cédula
                incluirEmpresas()
                f.close()#Se cierra el archivo una vez verificado
            else:
                nombre_empresa=input("Agregue el nombre de la empresa""\n")#Se le solicita el nombre de la empresa
                if (len(nombre_empresa))>0:#Se verifica que no este vacío
                    if len(nombre_empresa)> 0 and nombre_empresa.isdigit()==False:
                        Ubicación_Empresa=input("Agregue la ubicación de la empresa""\n")#Se le solicita la ubicación de la empresa
                        if len(Ubicación_Empresa)> 0 and Ubicación_Empresa.isdigit()==False:
                            flag=True
                            datos_empresa=cedula_empresa+","+nombre_empresa+","+Ubicación_Empresa+"\n"#Se procede a guardar toda la información en una variante.
                            print("")
                            print("Empresa guardada")#Mensaje de confirmación que la empresa se guardó correctamente
                            return anexarContenidoArchivo("Empresas.txt",datos_empresa)+ gestionDeEmpresas()#Procede a guardar los datos en el archvio
#En caso de que alguno de los datos sean incorrectos se le envía un mensaje de error dependiendo del error de entrada.
                        else:
                            print("La ubicación no puede estar vacía ni se numeros")+incluirEmpresas()
                    else:
                        return print("El nombre no puede ser vacio y no puede contener números")+ incluirEmpresas()
                else:
                    return print("El nombre no puede ser vacio y no puede contener números")+incluirEmpresas()
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
    num_cedula=input("Digite el número de cédula")#Se le solicita el numero de cedula
    f = open("archivo.txt","r")#Se abre el archivo
    if num_cedula != '':
        for line in f:
            if num_cedula in line:
                nuevos_datos=line.split(",")
                nuevo_nombre=input("Ingrese el nuevo nombre""\n")#Se le solicita el nuevo nombre con el que desea guardar la empresa
                nueva_ubicacion=input("Ingrese la nueva ubicación")#Se le solicita la nueva ubicación con la que desea guardar la empresa
                nuevos_datos[2]=nuevo_nombre
                nuevos_datos[3]=nueva_ubicacion
                datos_editados=",".join(nuevos_datos)#Los nuevos datos se añaden a una variable
                guardar += datos_editados
            else: guardar+=line
        f.close()
        return escribirArchivo("Empresas.txt",guardar)#Se guardan los datos nuevos en el archivo
#Si la cedula está en blanco se le manda un mensaje de error
    else:
        print("No puede dejar valores en blanco")
        ModificarContacto()

"""
nombre: Ver todas las empresas
función que devuelve todas las empresas.
"""
def verTodasLasEmpresas():#función hecha para ver todos los empresas
    file = open("Empresas.txt","r")#Se abre el archivo con la funcion de leer lineas
    print ("Sus empresas son:")
    print("\n")
    for line in file:
        print(line)#Se imprimen las lineas que contienen una empresa
    file.close()
    menu()
"""
Esta función hace lo mismo pero la utilice en otra función
"""
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
    num_cedula=input("Digite el número de cédula")#Se le solicita el numero de cedula al usuario
    file = open("Empresas.txt","r")#Se abre el archivo con la funcion de leer lineas
    for line in file:
        if num_cedula in line:#Si se encuentra la cedula la linea se borra
            guardar += ''
        else: guardar+=line#Si no, solo se guardan los datos que ya existen
    file.close()
    return escribirArchivo("Empresas.txt",guardar)#Se guardan las modificaciones en el archiivo

"""
nombre:Gestión de transporte de empresas.
función:
"""
def gestionDeTransportePorEmpresas():
    f=open("Transporte.txt","a")
    f.close()
    cedula_empresa=input("Agregue el número de cédula de la persona sin espacios y con ceros ""\n")
    placa=input("Agregue el número de placa de la persona sin espacios""\n")
    if placa.isdigit()==True:#Verifico que la placa sean números
#Abro el archivo y verifico si la cedula ya existe.
            f = open("Transporte.txt","r")
            cedula = f.readlines()
            if cedula_empresa in "".join(cedula):
                print("Ese número de cédula ya existe")
                gestionDeTransportePorEmpresas()
                f.close()
            else:#Si no existe la cedula aún se ejecuta el resto de la función
                nombre_marca=input("Agregue el nombre de la marca""\n")
                if len(nombre_marca)> 0 and nombre_marca.isdigit()==False: #Se verifica que el nombre no vaya vacío
                    modelo=input("Agreque el modelo del transporte""\n")
                    if len(modelo)> 0:#Se verifica que el espacio no vaya vacío
                        año=input("Dígite el año del transporte")
                        if año.isdigit()==True:#Se verifica que el año sean numeros
                            VIP=input("Agregue el numero de campos VIP que contiene el transporte")
                            if VIP.isdigit(): #Se verifica que el espacio no este vacío y que sean solo numeros
                                Clase_Normal=input("Agregue el numero de campos de clase normal que contiene el transporte")
                                if Clase_Normal.isdigit():#  Se verifica que el espacio no este vacío y que sean solo numeros
                                    Clase_economica=input("Agregue el numero de campos de clase economica que contiene el transporte")
                                    if Clase_economica.isdigit():#  Se verifica que el espacio no este vacío y que sean solo numeros
                                            datos_empresa=cedula_empresa+","+nombre_marca+","+modelo+","+año+","+VIP+","+Clase_Normal+","+Clase_economica#Aquí se guardan todos los datos
                                            print("Se han guardados todos los datos correctamente.")+ menu()
                                            return anexarContenidoArchivo("Viajes.txt",datos_empresa)#Aquí se guardan los datos finalmente en el archivo
#En caso de que haya algún error con algún dato, se le manda un mensaje de error dependiendo de la entrada.
                                    else:
                                        print("La cantidad de asientos deben ser números y no debe ir vacío")+ gestionDeTransportePorEmpresas()
                                else:
                                    print("La cantidad de asientos deben ser números y no debe ir vacío")+ gestionDeTransportePorEmpresas()
                            else:
                                print("La cantidad de asientos deben ser números y no debe ir vacío")+ gestionDeTransportePorEmpresas()
                        else:
                            print("El año no puede ir vacío")+ gestionDeTransportePorEmpresas()
                    else:
                        print("El año debe ser un numero entero")+ gestionDeTransportePorEmpresas()
                else:
                    print("El modelo no debe ir vacío")+ gestionDeTransportePorEmpresas()
    else:
        return print("la placa deben ser números")+ gestionDeTransportePorEmpresas()
"""
Nombre: gestion de viaje menu
Menu que despliega las opciones acerca de gestion de viajes
"""
def gestionDeViajeMenu():
    print("")
    print("Bienvenido a gestión de viajes ¿Qué desea hacer?")
    print("")
    print("1.Guardar viaje")
    print("2.Modificar viaje")
    print("3.Eliminar viaje")
    print("4.Mostrar todas los viajes")
    print("5.Volver a menú principal")
    print("6.Volver a menú administrativo")
    print("")
    opcion=input("Ingrese su opción ")#Se le solicita la opción al usuarrio
    print("")
#Depende de la opción que digite se le devuelve la función que desea
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

#Uso de la librería random para solicitar un numero al azar para que sea el numero de viaje.
from random import randint
n=randint(1,500)
n2=randint(1,500)
Numero_de_viaje=n+n2#El numero obtenido
def gestionDeViaje():
    f=open("Viajes.txt","a")#Se abre el archivo
    f.close
    ciudad_salida=input("Digite el lugar de donde saldrá ""\n")#Se le solicita la informacion del lugar de salida al usuario
    if len (ciudad_salida)>0:#Se verifica que el espacio no este en blanco
        Fecha_salida=input("Digite la fecha en la que sale""\n")#Se le solicita la informacion de la fecha de salida al usuario
        hora_salida=input("Digite la hora en la que sale""\n")#Se le solicita la informacion de la hora de salida al usuario
        if len(Fecha_salida)> 0 and len (hora_salida)>0:#Se verifica que el espacio no este en blanco
            Ciudad_de_llegada=input("Agregue el destino al que desea llegar""\n")
            if len(Ciudad_de_llegada)>0:#Se verifica que el espacio no este en blanco
                Fecha_llegada=input("Digite la fecha en la que llega""\n")#Se le solicita la informacion de la fecha de llegada al usuario
                hora_llegada=input("Digite la hora en la que llega""\n")#Se le solicita la informacion de la hora de llegada al usuario
                if len(Fecha_llegada)> 0 and len (hora_llegada)>0:#Se verifica que el espacio no este en blanco
                        file = open("Empresas.txt","r")
                        print("\n")
                        for line in file:
                            print(line) #Se abre el archivo de empresas para que el usuario elija la empresa que desee
                        file.close()
                        print("Estas son las empresas con las que contamos")
                        empresaYtransporte=input("digite la empresa y transporte que desee")#El usuario digita la empresa que desea
                        Clase_economica=10
                        Clase_Normal=100
                        VIP= 1000
                        monto= print("Clase economica="+" "+str(Clase_economica)+" "+"Clase Normal="+str(Clase_Normal)+" "+"VIP="+str(VIP))
                        monto_pagar=input("Digite cual clase desea pagar")
                        if len(monto_pagar)>0:
                            #Se guarda todos los datos en una misma variable
                            datos_viaje=str(Numero_de_viaje)+","+ciudad_salida+","+Fecha_salida+","+hora_salida+","+Ciudad_de_llegada+","+Fecha_llegada+","+hora_llegada+","+empresaYtransporte+","+str(monto_pagar)
                            print("Se ha guardado su viaje exitosamente")#Mensaje de confirmación para que el usuario sepa que el viaje se ha guardado correctamente
                            print("Su numero de viaje es:")
                            print(Numero_de_viaje)
                            return anexarContenidoArchivo("Viajes.txt",datos_viaje)+menu()#Se guarda o se anexa la información en el archivo
                        
                        #Si no se cumple correctamente con alguno de los datos se le manda un mensaje de error al usuario.
                        
                        else:
                            return print("El monto no puede ir en blanco")+gestionDeViaje()
                else:
                    return print("La fecha y hora no pueden ir vacías. Digite su fecha y hora de salida") + gestionDeViaje()
            else:
                return print("La ciudad de llegada no puede ir en blanco. Digite su lugar de llegada") + gestionDeViaje()
        else:
            return print("La fecha y hora no pueden ir vacías. Digite su fecha y hora de llegada") + gestionDeViaje()
    else:
        return print("La ciudad de salida no puede ir en blanco. Digite su lugar de llegada") + gestionDeViaje()
    

"""
nombre: modificar empresa
función que hace que el usuario pueda modificar los datos de una empresa.
"""
def modificarViaje():
    global guardar
    guardar=''
    num_cedula=input("Digite el número de cédula")#Se le solicita el numero de cédula al usuario
    f = open("Viajes.txt","r")
    if num_cedula != '':#Se verifica que la cedula no sea vacía
        for line in f:
            if num_cedula in line:
                nuevos_datos=line.split(",")
                nuevo_nombre=input("Ingrese el nuevo nombre""\n")#Se le solicita los nuevos datos
                nueva_ubicacion=input("Ingrese la nueva ubicación")#Se le solicita los nuevos datos
                nuevos_datos[2]=nuevo_nombre#Se guardan los nuevos datos en una nueva variable
                nuevos_datos[3]=nueva_ubicacion#Se guardan los nuevos datos en una nueva variable
                datos_editados=",".join(nuevos_datos)#Se guardan todos los datos nuevos en una nueva variable
                guardar += datos_editados#Se guardan todos los datos nuevos en una nueva variable
            else: guardar+=line#Se guardan todos los datos que ya habían en una nueva variable
        f.close()
        return escribirArchivo("Empresas.txt",guardar)#Se guarda la información modificada en el archivo.
    #Mensaje de error si no se encuentra la cedula o el valor es vacío.
    else:
        print("No puede dejar valores en blanco")
        ModificarContacto()

"""
nombre: Ver todas los viajes
función que devuelve todos los viajes.
"""
def verTodosLosViajes():#función hecha para ver todos los empresas
    file = open("Viajes.txt","r")#Se abre el archivo y se lee por lineas 
    print ("Sus viajes son:")
    print("\n")
    for line in file:
        print(line)#Se imprimen todos los viajes linea por linea
    file.close()
    menu()

"""
nombre: Eliminar viaje
función que elimina un viaje
"""
def EliminarViaje():
    global guardar
    guardar=''
    num_cedula=input("Digite el número de cédula")#Se le solicita la cedula al usuario para verificar que existe
    file = open("Viajes.txt","r")
    for line in file:
        if num_cedula in line:#Se busca la cedula línea por línea
            guardar += ''
        else: guardar+=line#Se guarda toda la información excepto la que queremos eliminar
    file.close()
    return escribirArchivo("Viajes.txt",guardar)#Se guarda en el archivo con el viaje eliminado
"""
nombre: reservación de viaje
función que dunciona como filtro para los identificadores de reservación de viaje.
"""
def ReservaciónDeViaje():
    f=open("Reservaciones.txt","a")
    f.close()
    print("Bienvenido/a a reservación de viaje")
    print("")
    #Se le brinda las opciones de identificadores
    print("Identificadores")
    print ("1.Numero de viaje")
    print ("2.Empresas")
    print ("3.Fecha salida")
    print ("4.Fecha llegada")
    print("")
    identificador = input("Seleccione uno de los identificadores")#Se le solicita al usuario que escoja un identificador
    if identificador == 1:
        return anexarContenidoArchivo("Reservaciones.txt", Numero_viaje)
        f = open (archivo,'a')#Se abre el archivo con la función de append
        f.write(mensaje)
        f.close()
        return ReservaciónDeViaje_Aux()# y se le retorna la función auxiliar
    elif identificador == 2:
        return anexarContenidoArchivo("Reservaciones.txt", verTodasLasEmpresas)
        f = open (archivo,'a')#Se abre el archivo con la función de append
        f.write(mensaje)
        f.close()
        return ReservaciónDeViaje_Aux()# y se le retorna la función auxiliar
    elif identificador == 3:
        return anexarContenidoArchivo("Reservaciones.txt", Fecha_salida)
        f = open (archivo,'a')#Se abre el archivo con la función de append
        f.write(mensaje)
        f.close()
        return ReservaciónDeViaje_Aux()# y se le retorna la función auxiliar
    elif identificador == 4:
        return anexarContenidoArchivo("Reservaciones.txt", Fecha_llegada)
        f = open (archivo,'a')#Se abre el archivo con la función de append
        f.write(mensaje)
        f.close()
        return ReservaciónDeViaje_Aux()# y se le retorna la función auxiliar
   
    #Si no digita alguna opción se le manda un mensaje de error
    else:
        print("El identificador debe ser algunos de los brindados anteriormente")
        return ReservaciónDeViaje()

#Función auxiliar de reservación de viajes
def ReservaciónDeViaje_Aux():
    f=open("Reservaciones.txt","a")#Se abre el archivo con la función de append
    f.close()
    nombre= input("Ingrese su nombre completo")#Se le solicita el nombre al usuario
    if isinstance (nombre,str):
        Asientos=input(int("Digite la cantidad de asientos que desea"))#Se le solicita la cantidad de asientos que desea al usuario
        f=open("Reservaciones.txt","a")
        f.close()
        return gestionDeViaje()
        #Se guardan todos los datos del usuario y se le imprimen
        print (Numero_de_viaje+","+ciudad_salida+","+Fecha_salida+","+hora_salida+","+Ciudad_de_llegada+","+Fecha_llegada+","+hora_llegada+","+empresaYtransporte+","+monto_pagar)
        

"""
Nombre: Consultar el historial de reservaciones.
Función que atiende consultas sobre el historial de reservaciones.
Despliega un filtro en el que el usuario puede seleccionar para buscar su reservación
"""
def menuFiltro():
    print("Bienvenido/a al historial de reservación")
    print("")
    print("¿Por cuál filtro desea buscar la información?")
    print("")
    print("1.Rango de fecha de salida")
    print("2.Rango de fecha de entrada")
    print("3.Rango de fecha de reservación")
    print("4.Lugar de salida y entrada")
    opcion=input("Ingrese su opción ")#Aquí tomamos lo que quiere hacer el usuario
    print("")
    if opcion=="1":
        return historialDeReserva1()
    elif opcion=="2":
        return historialDeReserva2()
    elif opcion=="3":
        return historialDeReserva3()
    elif opcion=="3":
        return historialDeReserva4()
    else:
        print("Debe digitar un número de la lista")
        print("")
        menuFiltro()
"""
Funciones de historial de reserva.
Estas se les devuekve al usuario dependiendo del filtro que eligieron
cada una imprime la impormación de reserva solicitada por el usuario.
"""
def historialDeReserva1():
    fechaDeSalida=input("Digite la fecha de salida")
    f = open("Reservaciones.txt","r")
    if fechaDeSalida != '':
        for line in f:
            if fechaDeSalida[2] in line:
                print(line)

def historialDeReserva2():
    fechaDeEntrada=input("Digite la fecha de enntrada")
    f = open("Reservaciones.txt","r")
    if fechaDeEntrada != '':
        for line in f:
            if fechaDeSalida[5] in line:
                print(line)

def historialDeReserva3():
    fechaDeReservación=input("Digite la fecha de reservación")
    f = open("Reservaciones.txt","r")
    if fechaDeEntrada != '':
        for line in f:
            if fechaDeSalida[2] in line:
                print(line)

def historialDeReserva4():
    LugardeSalida=input("Digite el lugar de salida")
    f = open("Reservaciones.txt","r")
    if fechaDeEntrada != '':
        for line in f:
            if fechaDeSalida[1] in line:
                print(line)


    
"""
"""
#Falta
def estadisticaDeViaje():
    return verTodosLosViajes()

"""
Nombre: opciones generales
función que despliega un menú de opciones generales
"""
def opcionesGenerales():
    #Se le brinda las opciones al usuario
    print ("Bienvenido al menú de opciones generales ¿Qué desea hacer?")
    print("")
    print("1.Consulta de viajes")
    print("2.Reservación de viajes")
    print("3.Cancelación de reservación")
    print("4.Salir")
    print("")
    opcion=input("Ingrese su opción ")#Aquí tomamos lo que quiere hacer el usuario
    if opcion=="1":
        return consultaDeViajes()
    elif opcion=="2":
        return ReservaciónDeViaje()
    elif opcion=="3":
        return cancelacionDeReserva()
    elif opcion=="3":
        return print("Que pase un buen día")
    else:
        return salir()

"""
Nombre:Consulta de viaje
Función que retorna todos los viajes
"""
def consultaDeViajes():
    return verTodosLosViajes()

def cancelacionDeReserva():
    global guardar
    guardar=''
    num_cedula=input("Digite el número de cédula")#Se le solicita la cedula al usuario para verificar que existe
    file = open("Reservaciones.txt","r")
    for line in file:
        if num_cedula in line:#Se busca la cedula línea por línea
            guardar += ''
        else: guardar+=line#Se guarda toda la información excepto la que queremos cancelar y se elimina
    file.close()
    return escribirArchivo("Reservaciones.txt",guardar)#Se guarda en el archivo con la reservacion cancelada

"""
Nombre: Salir
funcion de salida que retorna un mensaje de buen día
"""
def salir():
    print("Que tenga un buen día")
####################################################################################################################

"""
Funciones complementarias dadas previamente para el manejo de archivos
"""
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
    
    
    
    
    
    
