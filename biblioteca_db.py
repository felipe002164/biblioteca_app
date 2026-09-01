from modelos_db import Autor, Libro, Usuario, Prestamo 
from datetime import datetime

class BibliotecaDB:
    def __init__(self , session):
        self.session = session


    def agregar_libro(self, titulo, isbn, nombre_autor):
        autor = self.session.query(Autor).filter_by(nombre=nombre_autor).first()
        if autor is None:
            autor = Autor(nombre=nombre_autor)
            self.session.add(autor)
            self.session.flush() #asigna el id sin cerrar la transaccion sin cerrar el id todavia

        existente = self.session.query(Libro).filter_by(isbn=isbn).first()
        if existente is not None:
            raise ValueError(f"Ya existe un libro con ISBN {isbn}")

        libro = libro(titulo=titulo, isbn=isbn, autor_id=autor.id)
        self.session.add(libro)
        self.session.commit()
        return libro

    def prestar_libro(self, isbn, usuario_id):
        libro = self.session.query(Libro).filter_by(isbn=isbn).first()
        if libro is None:
            raise ValueError("Libro no encontrado")
        if not libro.disponible:
            raise ValueError("El libro ya esta prestado")

        libro.disponible = False
        prestamo =  Prestamo(libro_id=libro.id, usuario_id=usuario_id)
        self.session.add(prestamo)
        self.session.commit()

    def devolver_libro(self, isbn):
        libro = self.session.query(Libro).filter_by(isbn=isbn).first()
        prestamo = (
            self.session.query(Prestamo)
            .filter_by(libro_id=libro.id, fecha_devolucion=None)
            .first()
        )
        if prestamo is None:
            raise ValueError("No hay un prestamo activo para este libro")

        prestamo.fecha_devolucion = datetime.utcnow()
        libro.disponible = True 
        self.session.commit()

    def prestamos_activos_con_detalle(self):
        """Consulta con JOIN: prestamos activos + nombre de usuario + titulo de libro"""
        return (
            self.session.query(Prestamo)
            .join(Libro, Prestamo.libro_id == Libro.id)
            .join(Usuario, Prestamo.usuario_id == Usuario.id)
            .filter(Prestamo.fecha_devolucion.is_(None))
            .all()
        )
