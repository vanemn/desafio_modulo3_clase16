def opciones_masa():  
    print("Tipos de masa disponibles:")  
    print("1. Masa Tradicional")  
    print("2. Masa Delgada")  
    print("3. Masa con Bordes de Queso")  

def opciones_salsa():  
    print("Tipos de salsa disponibles:")  
    print("1. Salsa de Tomate")  
    print("2. Salsa Alfredo")  
    print("3. Salsa Barbecue")  
    print("4. Salsa Pesto")  

def opciones_ingredientes():  
    print("Ingredientes disponibles:")  
    print("1. Queso")  
    print("2. Jamón")  
    print("3. Pepperoni")  
    print("4. Champiñones")  
    print("5. Pimiento")  
    print("6. Cebolla")  
    print("7. Aceitunas")  
    print("8. Piña")  
  
def agregar_ingrediente(ingredientes):  
    opciones_ingredientes()  # Mostrar opciones de ingredientes  
    try:  
        eleccion = int(input("Seleccione el número del ingrediente que desea agregar: "))  
        ingredientes_disponibles = ['Queso', 'Jamón', 'Pepperoni', 'Champiñones', 'Pimiento',   
                                     'Cebolla', 'Aceitunas', 'Piña']  # Lista de ingredientes  

        if 1 <= eleccion <= len(ingredientes_disponibles):  
            nuevo_ingrediente = ingredientes_disponibles[eleccion - 1]  
            ingredientes.append(nuevo_ingrediente)  
            print(f"{nuevo_ingrediente} ha sido agregado a su pizza.")  
        else:  
            print("Opción inválida.")  
    except ValueError:  
        print("Por favor ingrese un número válido.")  

def eliminar_ingrediente(ingredientes):  
    if not ingredientes:  
        print("No hay ingredientes para eliminar.")  
        return  
    print("Ingredientes actualmente en la pizza:")  
    for i, ingrediente in enumerate(ingredientes, 1):  
        print(f"{i}. {ingrediente}")  
    
    try:  
        eleccion = int(input("Ingrese el número del ingrediente que desea eliminar: "))  
        if 1 <= eleccion <= len(ingredientes):  
            eliminado = ingredientes.pop(eleccion - 1)  
            print(f"{eliminado} ha sido eliminado de su pizza.")  
        else:  
            print("Opción inválida.")  
    except ValueError:  
        print("Por favor ingrese un número válido.")  

def cambiar_masa():  
    opciones_masa()  
    try:  
        eleccion_masa = int(input("Seleccione el número del nuevo tipo de masa: "))  
        if eleccion_masa == 1:  
            return "Masa Tradicional"  
        elif eleccion_masa == 2:  
            return "Masa Delgada"  
        elif eleccion_masa == 3:  
            return "Masa con Bordes de Queso"  
        else:  
            print("Opción inválida.")  
            return None  
    except ValueError:  
        print("Por favor ingrese un número válido.")  
        return None  

def cambiar_salsa():  
    opciones_salsa()  
    try:  
        eleccion_salsa = int(input("Seleccione el número de la nueva salsa: "))  
        if eleccion_salsa == 1:  
            return "Salsa de Tomate"  
        elif eleccion_salsa == 2:  
            return "Salsa Alfredo"  
        elif eleccion_salsa == 3:  
            return "Salsa Barbecue"  
        elif eleccion_salsa == 4:  
            return "Salsa Pesto"  
        else:  
            print("Opción inválida.")  
            return None  
    except ValueError:  
        print("Por favor ingrese un número válido.")  
        return None  

def calcular_tiempo(ingredientes):  
    return 20 + 2 * len(ingredientes)  

print("¡Bienvenido a Pizza JAT!")  

masa = ""  
salsa = ""  
ingredientes = []  

# Selección de masa  
masa = cambiar_masa()  

# Selección de salsa  
salsa = cambiar_salsa()  

# Menú de operaciones  
while True:  
    print("\nMenu:")  
    print("1. Agregar ingrediente")  
    print("2. Eliminar ingrediente")  
    print("3. Mostrar ingredientes")  
    print("4. Cambiar masa")  
    print("5. Cambiar salsa")  
    print("6. Confirmar pedido")  
    print("7. Salir")  

    opcion = int(input("Seleccione una opción: "))  

    if opcion == 1:  
        agregar_ingrediente(ingredientes)  

    elif opcion == 2:  
        eliminar_ingrediente(ingredientes)  

    elif opcion == 3:  
        print("Ingredientes actualmente en la pizza:")  
        if not ingredientes:  
            print("No hay ingredientes.")  
        else:  
            for ingrediente in ingredientes:  
                print(f"- {ingrediente}")  

    elif opcion == 4:  
        nueva_masa = cambiar_masa()  
        if nueva_masa:  
            masa = nueva_masa  
            print(f"La masa ha sido cambiada a: {masa}")  

    elif opcion == 5:  
        nueva_salsa = cambiar_salsa()  
        if nueva_salsa:  
            salsa = nueva_salsa  
            print(f"La salsa ha sido cambiada a: {salsa}")  

    elif opcion == 6:  
        if not masa or not salsa:  
            print("Por favor, asegúrese de seleccionar masa y salsa antes de confirmar el pedido.")  
            continue  
            
        tiempo_estimado = calcular_tiempo(ingredientes)  
        print(f"\nSu pizza con {masa}, {salsa} y los siguientes ingredientes {ingredientes} estará lista en aproximadamente {tiempo_estimado} minutos.")  
        confirmar = input("¿Desea confirmar su pedido? (s/n): ").lower()  
        if confirmar == 's':  
            print("¡Su pedido ha sido confirmado! Gracias por elegir Pizza JAT.")  
            break  
        else:  
            print("Pedido cancelado.")  

    elif opcion == 7:  
        print("¡Gracias por visitar Pizza JAT!")  
        break  

    else:  
        print("Opción inválida.")
