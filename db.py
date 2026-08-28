from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos_db import Base

DATEBASE_URL = "postgresql://postgres:clave123@localhost:5432/biblioteca"

engine = create_engine(DATEBASE_URL)
SessionLocal = sessionmaker(brind=engine)

def crear_tablas():
    Base.metadata.create_all(engine)