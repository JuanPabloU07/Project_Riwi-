def mostrar_menu():
    print("\n--- Menú de Inventario ---")
    print("1. Ver inventario")
    print("2. Agregar producto")
    print("3. Eliminar producto")
    print("4. Salir")
    return input("Selecciona una opción: ")
inventario = {}

while True:
    opcion = mostrar_menu()

    if opcion == '1':
        # Función para ver el inventario
        if not inventario:
            print("El inventario está vacío.")
        else:
            print("\n--- Inventario Actual ---")
            for producto, cantidad in inventario.items():
                print(f"- {producto}: {cantidad}")

    elif opcion == '2':
        # Función para agregar producto
        nombre = input("Nombre del producto: ")
        while True:
            try:
                cantidad = int(input("Cantidad: "))
                if cantidad < 0:
                    print("La cantidad no puede ser negativa.")
                else:
                    break
            except ValueError:
                print("Entrada inválida. Por favor, introduce un número.")

        if nombre in inventario:
            inventario[nombre] += cantidad
        else:
            inventario[nombre] = cantidad
        print(f"Se han agregado {cantidad} unidades de {nombre}.")

    elif opcion == '3':
        # Función para eliminar producto
        nombre = input("Nombre del producto a eliminar: ")
        if nombre in inventario:
            del inventario[nombre]
            print(f"Producto '{nombre}' eliminado.")
        else:
            print(f"Producto '{nombre}' no encontrado.")

    elif opcion == '4':
        print("Gracias por usar el programa.")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")