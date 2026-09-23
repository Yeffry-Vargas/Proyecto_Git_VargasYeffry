inventario = []


def mostrar_menu():
    print("=" * 42)
    print("BIBLIOSTOCK CLI - BIBLIOTECA HORIZONTE")
    print("=" * 42)
    print("1. Registrar ítem")
    print("2. Listar ítems")
    print("3. Buscar ítem")
    print("4. Registrar préstamo")
    print("5. Registrar devolución")
    print("6. Salir")
    print("=" * 42)


def registrar_item():
    codigo = input("Ingrese el código del ítem: ")
    titulo = input("Ingrese el título: ")
    autor = input("Ingrese el autor: ")
    categoria = input("Ingrese la categoría: ")
    cantidad = int(input("Ingrese la cantidad total: "))
    ubicacion = input("Ingrese la ubicación: ")

    item = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "cantidad_total": cantidad,
        "cantidad_disponible": cantidad,
        "ubicacion": ubicacion,
    }

    inventario.append(item)
    print(f'item "{titulo}" registrado exitosamente. Disponibles: {cantidad}')

def listar_items():
    if not inventario:
        print("No hay item registrados tadavia.")
        return

    print("=== LISTADO DE ITEMS===")
    for item in inventario:
        print(f"[{item['codigo']}] {item['titulo']} - {item['autor']} "
              f"| Disponibles: {item['cantidad_disponible']}/{item['cantidad_total']} "
              f"| Ubicación: {item['ubicacion']}")
    print ("======================")

def buscar_item():
    termino = input("Ingrese titulo o codigo a buscar: ").lower()
    encontrados = [
        item for item in inventario
        if termino in item["titulo"].lower() or termino in item["codigo"].lower()
    ]

    if not encontrados:
        print("No se encontraron items von este critero.")
        return

    print("==== RESULTADOS DE BUSQUEDA ====")
    for item in encontrados:
        print(f"[{item['codigo']}] {item['titulo']} - {item['autor']} "
              f"| Disponibles: {item['cantidad_disponible']}/{item['cantidad_total']}")

    print("=================================")

prestamos = []


def registrar_prestamo():
    codigo = input("Ingrese el codigo del item a prestar: ")
    item = next((i for i in inventario if i["codigo"] == codigo), None)

    if item is None:
        print("Item no encontrado. ")
        return

    if item["cantidad_disponible"] <= 0:
        print(f'No hay unidades disponibles de "{item["titulo"]}" ')
        return

    usuario = input("Ingrese el nombre del usuario: ")
    fecha = input("Ingrese la fecha del prestamo (YYYY-MM-DD): ")

    item["cantidad_disponible"] -= 1
    prestamos.append({
        "codigo": codigo,
        "titulo": item["titulo"],
        "usuario": usuario,
        "fecha_prestamo": fecha,
        "devuelto": False,
    })

    print(f'Prestamo registrado: "{item["titulo"]}" a {usuario} ')


def registrar_devolucion():
    codigo = input("Ingrese el código del ítem a devolver: ")
    usuario = input("Ingrese el nombre del usuario: ")

    prestamo = next(
        (p for p in prestamos
         if p["codigo"] == codigo and p["usuario"] == usuario and not p["devuelto"]),
        None
    )

    if prestamo is None:
        print("No se encontró un préstamo activo con esos datos. ")
        return

    prestamo["devuelto"] = True
    item = next((i for i in inventario if i["codigo"] == codigo), None)
    if item:
        item["cantidad_disponible"] += 1

    print(f'Devolución registrada: "{prestamo["titulo"]}" de {usuario} ')


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_item()
        elif opcion == "2":
            listar_items()
        elif opcion == "3":
            buscar_item()
        elif opcion == "4":
            registrar_prestamo()
        elif opcion == "5":
            registrar_devolucion()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción aún no implementada.")


if __name__ == "__main__":
    main()