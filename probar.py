from db import SessionLocal, crear_tablas
from biblioteca_db import BibliotecaDB
from modelos_db import Usuario

crear_tablas()
session = SessionLocal()
biblioteca = BibliotecaDB(session)

usuario = Usuario(nombre="Felipe")
session.add(usuario)
session.commit()

libro = biblioteca.agregar_libro("Cien años de soledad", "999-1", "Gabriel Garcia Marquez")
biblioteca.prestar_libro("999-1", usuario.id)

for prestamo in biblioteca.prestamos_activos_con_detalle():
    print(f"{prestamo.usuario.nombre} tiene prestado: {prestamo.libro.titulo}")