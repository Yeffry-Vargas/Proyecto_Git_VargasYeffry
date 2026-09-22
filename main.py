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


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción aún no implementada.")


if __name__ == "__main__":
    main()