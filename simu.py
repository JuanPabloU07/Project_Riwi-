inventary = []


sales_hitory = []

def main_menu():
    while True:
        print("\n------- Menu principal -------")
        print("1. Gestionar Inventario")
        print("2. Registrar Venta")
        print("3. Ver Historial de Ventas")
        print("4. Reportes")
        print("5. Salir")
        option = input("Elige una opción: ")

        if option == "1":
            menu_inventary()
        elif option == "2":
            register_vent()
        elif option == "3":
            view_sales_history()
        elif option == "4":
            menu_reports()
        elif option == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")


def menu_inventary():
    while True:
        print("\n--- Menu de inventario ---")
        print("1. Registrar libro")
        print("2. Ver listado de libros")
        print("3. Actualizar libro")
        print("4. Eliminar libro")
        print("5. Volver")
        option = input("Elige una opción: ")

        if option == "1":
            register_book()
        elif option == "2":
            view_inventary()
        elif option == "3":
            update_book()
        elif option == "4":
            delete_book()
        elif option == "5":
            break
        else:
            print("Opción no válida.")


def menu_reports():
    while True:
        print("\n--- Menu de reportes ---")
        print("1. Top 3 libros mas vendidos")
        print("2. Ventas por autor")
        print("3. Reporte de Ingresos")
        print("4. Rendimiento del Inventario")
        print("5. Volver")

        option = input("Elige una opción: ")

        if option == "1":
            top_books_report()
        elif option == "2":
            sales_report_author()
        elif option == "3":
            income_reports()
        elif option == "4":
            inventory_performance_report()
        elif option == "5":
            break
        else:
            print("Opción no válida.")


def int_input(msg):
    while True:
        try:
            valor = int_input(msg)
            return valor
        except ValueError:
            print("Entrada no válida. Ingresa un número entero.")

def input_float(msg):
    while True:
        try:
            valor = float(input(msg))
            return valor
        except ValueError:
            print("Entrada no válida. Ingresa un número válido.")

def search_book(name):
    return next((p for p in inventary if p["nombre"].lower() == name.lower()), None)


def register_book():
    print("\n--- Registrar nuevo libro ---")

    name = input("Nombre del libro: ").strip()
    if search_book(name):
        print("El libro ya existe.")
        return

    author = input("Autor: ").strip()
    category = input("Categoría: ").strip()
    price = input_float("Precio unitario: ")
    if price <= 0:
        print("El precio debe ser positivo.")
        return

    stock = int(input("Cantidad en stock: "))
    if stock < 0:
        print("El stock no puede ser negativo.")
        return

    garanty = int(input("Garantía (en meses): "))

    book = {
        "Title": name,
        "Author": author,
        "Category": category,
        "Price": price,
        "Stock": stock,
        "Quantity": garanty,
        "Vendidos": 0
    }

    inventary.append(book)
    print(" Libro registrado exitosamente!")


def view_inventary():
    print("\n--- Listado de libros ---")
    if not inventary:
        print("El inventario está vacío.")
        return
    for b in inventary:
        print(f"{b['title']} | Autor: {b['author']} | Categoría: {b['category']} | " f"Precio: ${b['price']:.2f} | Stock: {b['stock']} | Garantía: {b['quantity']} meses | Vendidos: {b['vendidos']}")

def update_book():
    print("\n--- Actualizar libro ---")
    name = input("Ingresa el nombre del libro: ")
    book = search_book(name)

    if not book:
        print("libro no encontrado.")
        return

    print("Deja el campo en blanco para mantener el valor actual.")

    new_price = input("Nuevo precio: ")
    if new_price.strip():
        book["precio"] = float(new_price)

    new_stock = input("Nuevo stock: ")
    if new_stock.strip():
        book["stock"] = int(new_stock)

    new_garanty = input("Nueva garantía (en meses): ")
    if new_garanty.strip():
        book["garantia"] = int(new_garanty)

    print(" Libro actualizado!")


def delete_book():
    print("\n--- Eliminar libro ---")
    name = input("Nombre del libro: ")
    book = search_book(name)

    if not book:
        print("Libro no encontrado.")
        return

    inventary.remove(book)
    print(" Libro eliminado.")


def register_vent():
    print("\n--- Registrar venta ---")
    customer = input("Nombre del cliente: ")

    name_book = input("Libro vendido: ")
    book = search_book(name_book)

    if not book:
        print("Libro no encontrado.")
        return

    quantity = int(input("Cantidad vendida: "))

    if quantity > book["stock"]:
        print(f"No hay suficiente stock. Disponible: {book['stock']}")
        return

    discount = input_float("Descuento aplicado (%): ")

    book["stock"] -= quantity
    book["vendidos"] += quantity

    total_price = quantity * book["precio"]
    final_price = total_price - (total_price * discount / 100)

    sales = {
        "cliente": customer,
        "libro": book["nombre"],
        "cantidad": quantity,
        "descuento": discount,
        "bruto": total_price,
        "neto": final_price
    }

    sales_hitory.append(sales)
    print(" Venta registrada exitosamente!")


def view_sales_history():
    print("\n--- Historial de ventas ---")
    if not sales_hitory:
        print("No se han registrado ventas.")
        return

    for i in sales_hitory:
        print(f"{i['cliente']} | {i['producto']} | Cantidad: {i['cantidad']} | " f"Bruto: ${i['bruto']:.2f} | Neto: ${i['neto']:.2f}")



def top_books_report():
    print("\n--- Top 3 libros mas vendidos ---")
    productos_ordenados = sorted(inventary, key=lambda p: p["vendidos"], reverse=True)
    for p in productos_ordenados[:3]:
        print(f"{p['nombre']} - Vendidos: {p['vendidos']}")


def sales_report_author():
    print("\n--- Ventas por autor ---")

    author_totals = {}
    for sale in sales_hitory:
        product = search_book(sale["producto"])
        author = product["autor"]
        author_totals[author] = author_totals.get(author, 0) + sale["neto"]

    for author, total in author_totals.items():
        print(f"{author}: ${total:.2f}")


def income_reports():
    print("\n--- Reporte de ingresos ---")
    bruto = sum(i["bruto"] for i in sales_hitory)
    neto = sum(i["neto"] for i in sales_hitory)
    print(f"Ingreso bruto: ${bruto:.2f}")
    print(f"Ingreso neto: ${neto:.2f}")


def inventory_performance_report():
    print("\n--- Rendimiento de inventario ---")
    for i in inventary:
        percentage_sold = (i["vendidos"] / (i["vendidos"] + i["stock"]) if i["vendidos"] + i["stock"] > 0 else 0)
        print(f"{i['nombre']}: {percentage_sold * 100:.2f}% vendidos")





main_menu()