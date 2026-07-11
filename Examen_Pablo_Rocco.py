def leer_opcion():

    opcion = 0

    while opcion != 6:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por género")
        print("2. Búsqueda de películas por rango de precio")
        print("3. Actualizar precio de película")
        print("4. Agregar película")
        print("5. Eliminar película")
        print("6. Salir")
        print("=====================================")
        try:
            opcion = int(input("Ingrese opcion: "))
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opcion valida")
        except ValueError:
            print("Debe seleccionar una opcion valida")

peliculas = {}

cartelera = {}

def buscar_codigo(codigo):
    for i in peliculas:
        if i.upper()==codigo.upper():
            return True
    return False

def validar_codigo(codigo):
    if codigo.strip()=="":
        return False
    return True

def validar_titulo(titulo):
    if titulo.strip()=="":
        return False
    return True

def validar_genero(genero):
    if genero.strip()=="":
        return False
    return True

def validar_duracion(duracion):
    if duracion<=0:
        return False
    return True

def validar_clasificacion(clasificacion):
    clasificacion = clasificacion.upper()
    if clasificacion=="A":
        return True
    elif clasificacion=="B":
        return True
    elif clasificacion=="C":
        return True
    return False


def validar_idioma(idioma):
    if idioma.strip()=="":
        return False
    return True

def validar_es3d(es_3d):
    if es_3d=="s":
        return True
    elif es_3d=="n":
        return True
    return False

def validar_precio(precio):
    if precio<=0:
        return False
    return True

def validar_cupos(cupos):
    if cupos<0:
        return False
    return True

def agregar_cartelera(codigo, precio, cupos):
    cartelera[codigo]=[precio, cupos]
    return

def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):
    if buscar_codigo(codigo):
        return False
    peliculas[codigo]=[titulo, genero, duracion, clasificacion, idioma, es_3d]
    agregar_cartelera(codigo, precio, cupos)
    return True

def cupos_genero(genero):
    total=0
    for codigo in peliculas:
        if peliculas[codigo][1].upper()==genero.upper():
            total=total+cartelera
    print("Total de cupos:", total)
    return

def busqueda_precio(precio_minimo, precio_maximo):
    lista=[]
    for codigo in cartelera:
        precio=cartelera[codigo][0]
        cupos=cartelera[codigo][1]
        if precio>=precio_minimo and precio<=precio_maximo:
            if cupos>0:
                lista.append(peliculas[codigo][0])

    if len(lista)==0:
        print("No existen películas en ese rango")
        return
    lista.sort()
    print("Películas encontradas")
    for i in lista:
        print(i)

    return

def actualizar_precio(codigo, nuevo_precio):
    if buscar_codigo(codigo)==False:
        return False
    cartelera[codigo][0]=nuevo_precio
    return True

def eliminar_pelicula(codigo):
    if buscar_codigo(codigo)==False:
        return False
    
    del peliculas[codigo]
    del cartelera[codigo]
    
    return True






opcion=0

while opcion!=6:

    opcion=leer_opcion()

    if opcion==1:
        genero = input("Ingrese genero: ")
        cupos_genero(genero)
    elif opcion==2:
        try:
            precio_minimo=int(input("Precio minimo:"))
            precio_maximo=int(input("Precio maximo:"))

            if precio_minimo>precio_maximo:
                print("El precio mínimo no puede ser mayor al máximo")
            else:
                busqueda_precio(precio_minimo, precio_maximo)
        except ValueError:
            print("Debe ingresar valores numericos")

    elif opcion==3:
        codigo=input("Ingrese cdigo: ")
        try:
            nuevo_precio=int(input("Ingrese nuevo precio:"))
            if validar_precio(nuevo_precio)==False:
                print("Precio invalido")
            else:
                if actualizar_precio(codigo, nuevo_precio)==True:
                    print("Precio actualizado")
                else:
                    print("La pelicula no existe")
        except ValueError:
            print("Debe ingresar un numero")

    elif opcion==4:
        codigo=input("Codigo: ")
        titulo=input("Titulo: ")
        genero=input("Genero: ")
        try:
            duracion=int(input("Duración: "))
        except ValueError:
            duracion=-1
        clasificacion=input("Clasificacion: ")
        idioma=input("Idioma: ")
        es_3d=input("Es 30D: ").lower()
        try:
            precio=int(input("Precio: "))
        except ValueError:
            precio=-1
        try:
            cupos=int(input("Cupos: "))
        except ValueError:
            cupos=-1

        if validar_codigo(codigo)==False:
            print("Codigo invalido")

        elif buscar_codigo(codigo)==True:
            print("El codigo ya existe")

        elif validar_titulo(titulo)==False:
            print("Error al ingresar el titulo")

        elif validar_genero(genero)==False:
            print("Error al ingresar genero")

        elif validar_duracion(duracion)==False:
            print("Error al ingresar la duracion")

        elif validar_clasificacion(clasificacion)==False:
            print("Clasificacion invalida")

        elif validar_idioma(idioma)==False:
            print("Idioma invalido")

        elif validar_es3d(es_3d)==False:
            print("Error al ingresar 3D")

        elif validar_precio(precio)==False:
            print("Precio invalido")

        elif validar_cupos(cupos)==False:
            print("Digito de cupos invalido")

        else:
            if es_3d=="s":
                es_3d=True
            else:
                es_3d=False
            agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos)
            print("Pelicula agregda correctamente")

    elif opcion == 5:
        codigo = input("Ingrese codigo: ")
        if eliminar_pelicula(codigo) == True:
            print("Pelicula eliminada correctamente")
        else:
            print("La pelicula no existe")


            
print("Programa finalizado")

        


