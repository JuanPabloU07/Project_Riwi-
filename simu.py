inventary = []

sales_history = []

def main_menu():
    while True:
        print("\n----- Menu principal -----")
        print("1. Gestionar inventario")
        print("2. Registrar Venta")
        print("3. Ver Historial de Ventas")
        print("4. Reportes")
        print("5. Salir")
        option = input("Elige una opción: ")

        if option == "1":
            inventory_menu()
        elif option == "2":
            register_sale()
        elif option == "3":
            view_sales_history()
        elif option == "4":
            reports_menu()
        elif option == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")


def inventory_menu():
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


def reports_menu():
    while True:
        print("\n--- Menu de reportes ---")
        print("1. Top 3 libros mas vendidos")
        print("2. Ventas por autor")
        print("3. Reporte de Ingresos")
        print("4. Volver")

        option = input("Elige una opción: ")

        if option == "1":
            report_top_books()
        elif option == "2":
            report_sales_author()
        elif option == "3":
            report_income()
        elif option == "4":
            break
        else:
            print("Opción no válida.")


def input_int(num_int):
    while True:
        try:
            value = int(input(num_int))
            return value
        except ValueError:
            print("Entrada no válida. Ingresa un número entero.")

def input_float(num_float):
    while True:
        try:
            value = float(input(num_float))
            return value
        except ValueError:
            print("Entrada no válida. Ingresa un número válido.")

def search_book(title):
    return next((p for p in inventary if p["title"].lower() == title.lower()), None)


def register_book():
    print("\n--- Registrar nuevo libro ---")

    title = input("titulo del libro: ").strip()
    if search_book(title):
        print("El libro ya existe.")
        return

    author = input("Autor: ").strip()
    category = input("Categoría: ").strip()
    price = input_float("precio unitario: ")
    if price <= 0:
        print("El precio debe ser positivo.")
        return

    stock = input_int("Cantidad en stock: ")
    if stock < 0:
        print("El stock no puede ser negativo.")
        return

    garanty = input_int("Garantía (en meses): ")

    book = {
        "title": title,
        "author": author,
        "category": category,
        "price": price,
        "stock": stock,
        "garanty": garanty,
        "sales": 0
    }

    inventary.append(book)
    print(" Libro registrado exitosamente")


def view_inventary():
    print("\n--- Listado de inventario ---")
    if not inventary:
        print("El inventario está vacío.")
        return

    for i in inventary:
        print(f"{i['title']} | Autor: {i['author']} | Categoría: {i['category']} | "
              f"precio: ${i['price']} | Stock: {i['stock']} | Garantía: {i['garanty']} meses")


def update_book():
    print("\n--- Actualizar libro ---")
    title = input("Ingresa el titulo del libro: ")
    book = search_book(title)

    if not book:
        print("Libro no encontrado.")
        return

    print("Deja el campo en blanco para mantener el valor actual.")

    new_price = input("Nuevo precio: ")
    if new_price.strip():
        book["price"] = float(new_price)

    new_stock = input("Nuevo stock: ")
    if new_stock.strip():
        book["stock"] = int(new_stock)

    new_garanty = input("Nueva garantía (en meses): ")
    if new_garanty.strip():
        book["garanty"] = int(new_garanty)

    print(" Libro actualizado!")


def delete_book():
    print("\n--- Eliminar Libro ---")
    title = input("Titulo del Libro: ")
    book = search_book(title)

    if not book:
        print("Libro no encontrado.")
        return

    inventary.remove(book)
    print(" Libro eliminado.")


def register_sale():
    print("\n--- Registrar venta ---")
    customer = input("Nombre del cliente: ")

    title_book = input("Libro vendido: ")
    book = search_book(title_book)

    if not book:
        print("Libro no encontrado.")
        return

    quantity = input_int("Cantidad vendida: ")

    if quantity > book["stock"]:
        print(f"No hay suficiente stock. Disponible: {book['stock']}")
        return

    discount = input_float("Descuento aplicado (%): ")

    book["stock"] -= quantity
    book["sales"] += quantity

    price_total = quantity * book["price"]
    price_final = price_total - (price_total * discount / 100)

    sale = {
        "customer": customer,
        "book": book["title"],
        "quantity": quantity,
        "discount": discount,
        "bruto": price_total,
        "neto": price_final
    }

    sales_history.append(sale)
    print(" Venta registrada exitosamente!")


def view_sales_history():
    print("\n--- Historial de ventas ---")
    if not sales_history:
        print("No se han registrado ventas.")
        return

    for s in sales_history:
        print(f"{s['customer']} | {s['book']} | quantity: {s['quantity']} | "
              f"Bruto: ${s['bruto']:.2f} | Neto: ${s['neto']:.2f}")



def report_top_books():
    print("\n--- TOP 3 libros mas vendidos ---")
    books_sorted = sorted(inventary, key=lambda p: p["sales"], reverse=True)
    for v in books_sorted[:3]:
        print(f"{v['title']} - sales: {v['sales']}")


def report_sales_author():
    print("\n--- Ventas por autor ---")

    total_authors = {}
    for sale in sales_history:
        book = search_book(sale["book"])
        author = book["author"]
        total_authors[author] = total_authors.get(author, 0) + sale["neto"]

    for author, total in total_authors.items():
        print(f"{author}: ${total:.2f}")


def report_income():
    print("\n--- Reporte de ingresos ---")
    bruto = sum(s["bruto"] for s in sales_history)
    neto = sum(s["neto"] for s in sales_history)
    print(f"Ingreso bruto: ${bruto:.2f}")
    print(f"Ingreso neto: ${neto:.2f}")


main_menu()