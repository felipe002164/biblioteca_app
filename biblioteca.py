import json
from modelos import Libro

class Biblioteca:
    def __init__(self, archivo="datos.json"):
        self.archivo = archivo
        self.libros = []
        self.cargar()

    def cargar(self):
        """Carga lso libros guardados en el archivo JSON, si existe."""
        try:
            with open (self.archivo, "r") as f:
                datos = json.load(f)
                self.libros = [Libro.from_dict(d) for d in datos]
        except FileNotFoundError:
            self.libros = [] # primera vex que se corre el programa, no hay archivos aun

    def guardar(self):
        """Guarda el estad actual de los libros en el archivo JSON."""
        with open(self.archivo, "w") as f:
            json.dump([libro.to_dict() for libro in self.libros], f, indent=2)

    def agregar_libro(self, titulo, autor, isbn):
        if self.buscar_por_isbn(isbn) is not None:
            raise ValueError(f"Ya existe un libro con ISBN {isbn}")
        nuevo = Libro(titulo, autor, isbn)
        self.libros.append(nuevo)
        self.guardar()
        return nuevo

    def buscar_por_isbn(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None 
    def buscar_por_titulo(self, texto):
        return [l for l in self.libros if texto.lower() in l.titulo.lower()]

    def prestar_libro(self, isbn):
        libro = self.buscar_por_isbn(isbn)
        if libro is None:
            raise ValueError("Libro no encontrado")
        if not libro.disponible:
            raise ValueError("El libro ya esta prestado")
        libro.disponible = False
        self.guardar()

    def devolver_libro(self, isbn):
        libro = self.buscar_por_isbn(isbn)
        if libro is None:
            raise ValueError("Libro no encontrado")
        libro.disponible = True
        self.guardar()


    def listar_todos(self):
        return self.libros
    
