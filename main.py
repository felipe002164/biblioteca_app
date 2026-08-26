from biblioteca import Biblioteca 

def mostrar_menu():
    print("\n====BIBLIOTECA====")
    print("1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Buscar por titulo")
    print("5. Listar todos los libros")
    print("6. Salir")

def main():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Elija una opcion: ")

        if opcion == "1":
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            try: 
                biblioteca.agregar_libro(titulo, autor, isbn)
                print("Libro agregado con exito")
            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "2":
            isbn = input("ISBN del libro a orestar: ")
            try:
                biblioteca.prestar_libro(isbn)
                print("Prestamo realizado.")
            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "3":
            isbn = input("ISBN del libro a devolver: ")
            try:
                biblioteca.devolver_libro(isbn)
                print("Devolucion registrada.")
            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "4":
            texto = input("Escriba paret dek titulo a buscar: ")
            resultados = biblioteca.buscar_por_titulo(texto)
            if not resultados:
                print("No se encontraron coincidencias.")
            for libro in resultados:
                print(libro)

        elif opcion == "5":
            for libro in biblioteca.listar_todos():
                print(libro)

        elif opcion == "6":
            print("Hasta luego")
            break

        else:
            print("Opcion invalida.")

if __name__ == "__main__":
    main()
