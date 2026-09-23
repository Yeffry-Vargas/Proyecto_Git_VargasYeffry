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


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_item()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción aún no implementada.")


if __name__ == "__main__":
    main()