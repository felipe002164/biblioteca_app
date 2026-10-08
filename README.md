Biblioteca App

Sistema de gestión de biblioteca en Python, construido en dos etapas para mostrar la evolución de una misma idea:

Versión de consola con persistencia en JSON: clases, manejo de errores y tests con pytest.
Versión con base de datos PostgreSQL: modelos con SQLAlchemy, migraciones con Alembic y consultas con JOIN.
Características
Registro de libros con validación de ISBN duplicado.
Préstamo y devolución de libros, con control de disponibilidad.
Búsqueda de libros por título.
Persistencia en archivo JSON (versión de consola).
Persistencia en PostgreSQL con cuatro tablas relacionadas: autores, libros, usuarios y prestamos.
Consulta con JOIN para listar los préstamos activos con el nombre del usuario y el título del libro.
Migraciones versionadas con Alembic.
Tecnologías
Python 3
SQLAlchemy (ORM)
PostgreSQL
Alembic (migraciones)
Docker (para la base de datos local)
pytest
Estructura del proyecto
biblioteca_app/
├── modelos.py          # Clase Libro (versión JSON)
├── biblioteca.py       # Clase Biblioteca con persistencia en JSON
├── main.py             # Menú de consola (versión JSON)
├── modelos_db.py       # Modelos SQLAlchemy: Autor, Libro, Usuario, Prestamo
├── db.py               # Conexión a PostgreSQL y sesión
├── biblioteca_db.py    # Clase BibliotecaDB (versión PostgreSQL)
├── probar.py           # Script de prueba manual de BibliotecaDB
├── alembic/            # Migraciones
├── alembic.ini
└── tests/
    └── test_biblioteca.py
Modelo de datos
Tabla	Descripción	Relaciones
autores	Autores de los libros	Un autor tiene muchos libros
libros	Catálogo con título, ISBN y disponibilidad	Pertenece a un autor
usuarios	Personas que piden libros prestados	Un usuario tiene muchos préstamos
prestamos	Registro de cada préstamo, con fecha de préstamo y de devolución	Une un libro con un usuario

Un préstamo está activo mientras fecha_devolucion sea NULL.

Instalación

Requisitos: Python 3, Git y, para la versión con base de datos, Docker Desktop.

powershell
git clone https://github.com/felipe002164/biblioteca_app.git
cd biblioteca_app
python -m venv venv
venv\Scripts\activate
pip install sqlalchemy psycopg2-binary alembic pytest
Uso
Versión de consola (JSON)
powershell
python main.py

Los datos se guardan en datos.json, que se crea automáticamente al agregar el primer libro.

Versión con PostgreSQL
Levanta una base de datos local con Docker:
powershell
docker run --name biblioteca-db -e POSTGRES_PASSWORD=<tu_contraseña> -e POSTGRES_DB=biblioteca -p 5432:5432 --restart unless-stopped -d postgres
Configura la cadena de conexión con tu contraseña en db.py (DATABASE_URL) y en alembic.ini (sqlalchemy.url). Usa credenciales solo para desarrollo local y no las subas a un repositorio público.
Aplica las migraciones para crear las tablas:
powershell
alembic upgrade head
Ejecuta el script de prueba:
powershell
python probar.py

Debe imprimir los préstamos activos, por ejemplo: Felipe tiene prestado: Cien años de soledad.

Si el puerto 5432 ya está ocupado por otro PostgreSQL en tu equipo, cambia el mapeo (por ejemplo -p 5433:5432) y actualiza el puerto en las dos cadenas de conexión.

Tests
powershell
pytest -v

Los tests actuales cubren la versión con JSON: agregar libros, rechazar ISBN duplicado, prestar, impedir prestar un libro ya prestado y devolver. Cada test usa un archivo temporal, así que no toca tus datos reales.

Qué aprendí construyéndolo
Diseñar clases con responsabilidades separadas (modelo de datos y lógica de la biblioteca).
Serializar objetos a JSON y reconstruirlos.
Modelar relaciones entre tablas con claves foráneas y relationship de SQLAlchemy.
Versionar cambios de la base de datos con Alembic.
Resolver problemas reales de entorno: conflictos de puertos, autenticación en PostgreSQL y permisos en Windows.
Mejoras pendientes
Agregar tests para la versión con PostgreSQL.
Leer la cadena de conexión desde variables de entorno.
Crear una interfaz web que consuma esta lógica.
Autor

Felipe García · github.com/felipe002164
