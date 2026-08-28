from sqlalchemy import Colum, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime


Base = declarative_base()

class Autor(Base):
    __tablename__="autores"
    id = Column(Integer, primary_Key=True)
    libros = relationship("Libro", back_populates="autor")

class Libro(Base):
    __tablename__ = "libros"
    id = Column(Integer, primary_Key=True)
    titulo = Column(String(200), nullable=True)
    isbn = Column(Integer(20), unique=True, nullable=False)
    disponible = Column(Boolean, default=True)
    autor_id = Column(Integer, ForeignKey("autores.id"))
    autor = relationship("Autor", back_populates="libros")

class Usuario(Base):
    __tablename__= "usuarios"
    id = Column(Integer, primary_Key=True)
    nombre = Column(String(100), nullable=False)

class Prestamo(Base):
    __tablename__: "prestamos"
    id = Column(Integer, primary_Key=True)
    libro_id = Column(Integer, ForeignKey("libros.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    fecha_prestamo = Column(DateTime, default=datetime.utcnow)
    fecha_devolucion = Column(DateTime, nullable=True) #null mientras no lo devuelvan 

    libro = relationship("Libro")
    usuario = relationship("Usuario")
