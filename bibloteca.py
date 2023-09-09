import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():

    print(libros)
    # completar
    return None

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    libros.append(nuevo_libro)
    #print(libros)
    #print(nuevo_libro)
    #completar
    return None

def eliminar_ejemplar_libro():

    #completar
    return None

def prestar_ejemplar_libro():
    cod = input("Ingrese el código del libro: ")

    encontrado = None
    for libro in libros:
        if libro["cod"] == cod:
            encontrado = libro
            break
    
    if encontrado:
        if encontrado["cant_ej_pr"] < encontrado["cant_ej_ad"]:
            print(f"Autor: {encontrado['autor']}")
            print(f"Título: {encontrado['titulo']}")
            print(f"Cantidad de ejemplares disponibles: {encontrado['cant_ej_ad'] - encontrado['cant_ej_pr']}")
            confirmacion = input("¿Desea confirmar el préstamo? (si/no): ")
            if confirmacion == "si":
                encontrado["cant_ej_pr"] += 1
                print("Préstamo confirmado.")
            else:
                print("Préstamo cancelado.")
        else:
            print("No quedan ejemplares disponibles para prestar.")
    else:
        print("Error: El código del libro no existe.")
    #completar
    return None

def devolver_ejemplar_libro():
    cod = input("Ingrese el código del libro a devolver: ")
    
    # Buscar el libro por su código en la lista de libros
    encontrado = None
    for libro in libros:
        if libro["cod"] == cod:
            encontrado = libro
            break

    if encontrado:
        confirmacion = input("¿Desea confirmar el préstamo? (si/no): ")
        if confirmacion == "si":
            encontrado["cant_ej_pr"] > 0
            encontrado["cant_ej_pr"] -= 1
            print("Devolución confirmada.")
        else:
            print("No se ha realizado la devolución.")
        #if encontrado["cant_ej_pr"] > 0:
        #    encontrado["cant_ej_pr"] -= 1
        #    print("Devolución confirmada.")
        #else:
        #    print("Error: No hay ejemplares prestados de este libro.")
    else:
        print("Error: El código del libro no existe.")
    return None

#def nuevo_libro():
    #completar
#    return None