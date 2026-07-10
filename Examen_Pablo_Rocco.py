def leer_opcion():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por género ")
    print("2. Búsqueda de películas por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")
    print("=====================================")
    
    

peliculas = {}

cartelera = {}

def mostrar_peliculas():
    for titulo in peliculas:
        print(titulo)

def buscar_pelicula(codigo):
    buscar=input("Buscar codigo: ")
    for codigo in peliculas:
        if buscar==codigo:
            return True
        else:
            return False

def eliminar_pelicula(codigo):
    if buscar_pelicula(codigo)==True:
        del cartelera[codigo]

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
    if duracion<0:
        return False
    return True

def validar_clasificacion(clasificacion):
    if clasificacion=="A":
        return True
    elif clasificacion=="B":
        return True
    elif clasificacion=="C":
        return True
    else:
        return False
    

def validar_idioma(idioma):
    if idioma.strip()=="":
        return False
    return True
def validar_es3d(es_3d):
    if es_3d=="n":
        return False
    elif es_3d=="y":
        return True

def agregar_cartelera(codigo,precio,cupos):
    cartelera[codigo]=[precio,cupos]

def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d,precio,cupos):               
    peliculas[codigo]=[titulo,genero,duracion,clasificacion,idioma,es_3d]
    cartelera[codigo]=[precio,cupos]
    return

def validar_precio(precio):
    if precio<0:
        return False
    return True

def validar_cupos(cupos):
    if cupos>=0:
        return True
    return False

    

    


opcion=0

while opcion!=6:
    try:
        
        leer_opcion()
        
        opcion=int(input(": "))
        if opcion==1:
            pass
        elif opcion==2:
            mostrar_peliculas(titulo)
        elif opcion==3:
            pass
        elif opcion==4:
            
            codigo=input("Codigo: ")
            validar_codigo(codigo)
            if validar_codigo(codigo)==False:
                print("Error al ingresar el codigo")


            titulo=input("Titulo: ")
            validar_titulo(titulo)
            if validar_titulo(titulo)==False:
                print("Error al ingresar el titulo")
                
            genero=input("Genero: ")
            validar_genero(genero)
            if validar_genero(genero)==False:
                print("Error al ingresar genero")    
            try:                
                duracion=int(input("Duracion: "))
                validar_duracion(duracion)
                if validar_duracion(duracion)==False:
                    print("Error al ingresar la duracion")
            except ValueError:
                print("Error al ingresar la duracion")
            
            clasificacion=input("Clasificacion: ")
            validar_clasificacion(clasificacion)
            if validar_clasificacion(clasificacion)==False:
                print("Clasificacion invalida")
            
            idioma=input("Idioma: ")
            validar_idioma(idioma)
            if validar_idioma(idioma)==False:
                print("Idioma invalido")
            
            es_3d=input("Es 3D: ")
            validar_es3d(es_3d)
            if validar_es3d(es_3d)==False:
                print("Error al ingresar 3D")
                
            precio=int(input("Ingrese precio: "))
            if validar_precio(precio)==False:
                print("Precio invalido")
                
            cupos=int(input("Ingrese cupos: "))
            if validar_cupos(cupos)==False:
                print("Digito de cupos invalido")
            try:     
                if (validar_codigo(codigo) and validar_titulo(titulo) and validar_genero(genero) and validar_clasificacion(clasificacion) and validar_idioma(idioma) and validar_es3d(es_3d))==True:
                    agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d,precio,cupos)
                    print(peliculas)
                    print(cartelera)
            except NameError:
                print("Error al registrar debido a que no todas las opciones son validas")
                agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d,precio,cupos)

        elif opcion==5:
            eliminar_pelicula(codigo)
            print(cartelera)
        elif opcion==6:
            print("Programa Finalizado")
            
    
    except ValueError:
        print("No hay opcion disponible")
        


