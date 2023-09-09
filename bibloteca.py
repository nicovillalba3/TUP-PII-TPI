import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():

    libros_prestados = False 
    
    for libro in libros:
        if libro["cant_ej_pr"] > 0:
            print(f"Código: {libro['cod']}, Título: {libro['titulo']}, Ejemplares Prestados: {libro['cant_ej_pr']}")
            libros_prestados = True  
    
    if not libros_prestados:
        print("Ningún libro tiene ejemplares prestados.")
    # completar
    return None

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    libros.append(nuevo_libro)
    
    return None

def eliminar_ejemplar_libro():
    cod = input("Ingrese el código del libro: ")
    
    # Primero buscamos el libro por su código en la lista de libros
    encontrado = None
    for libro in libros:
        if libro["cod"] == cod:
            encontrado = libro
            break

    # Después el usuario confirma o no si avanza
    confirmacion = input("¿Desea confirmar la eliminación del ejemplar? (si/no): ")
    if encontrado:
        
        if confirmacion == "si":
            encontrado["cant_ej_ad"] > 0
            encontrado["cant_ej_ad"] -= 1
            print("Ejemplar eliminado con éxito.")
        else:
            print("Error: No hay ejemplares adquiridos de este libro.")
    else:
        print("Error: El código del libro no existe.")
    #completar
    return None

def prestar_ejemplar_libro():
    cod = input("Ingrese el código del libro: ")

    # Primero buscamos el libro por su código en la lista de libros
    encontrado = None
    for libro in libros:
        if libro["cod"] == cod:
            encontrado = libro
            break

    # Después el usuario confirma o no si avanza
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
    
    # Primero buscamos el libro por su código en la lista de libros
    encontrado = None
    for libro in libros:
        if libro["cod"] == cod:
            encontrado = libro
            break

    # Después el usuario confirma o no si avanza
    if encontrado:
        confirmacion = input("¿Desea confirmar el préstamo? (si/no): ")
        if confirmacion == "si":
            encontrado["cant_ej_pr"] > 0
            encontrado["cant_ej_pr"] -= 1
            print("Devolución confirmada.")
        else:
            print("No se ha realizado la devolución.")
        
    else:
        print("Error: El código del libro no existe.")
    return None

