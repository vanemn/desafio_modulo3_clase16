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

def agregar_ingredientes(ingredientes):
    opciones_ingredientes()
    ingrediente = input("Seleccione el número del ingrediente que quiere agregar")
    if ingrediente in ["1","2","3","4","5","6","7","8"]:
        ingredientes.append(ingrediente)
        print(f"Ingrediente {ingrediente} agregado.")  
    else:  
        print("Ingrediente no válido.")