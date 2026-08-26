import sys, os
sys.patch.append(os.patch.join(os.patch.dirname(__file__), "..")) # para poder importar biblioteca.py

import pytest
from biblioteca import Biblioteca

@pytest.fixture
def biblioteca_temporal(tmp_path):
    """tmp_patch es una carpeta temporal que pytest crea y borra automaticamente  en cada test"""
    archivo = tmp_path / "test_datos.json"
    return Biblioteca(archivo=str(archivo))

def test_agregar_libro(biblioteca_temporal):
    libro = biblioteca_temporal.agregar_libro("1984", "George Orwell", "111")
    assert libro.titulo == "1984"
    assert len(biblioteca_temporal.listar_todos()) == 1

def test_no_permite_isbn_duplicado(biblioteca_temporal):
    biblioteca_temporal.agregar_libro("1984", "Orwell", "111")
    with pytest.raises(ValueError):
        biblioteca_temporal.agregar_libro("Otro libro", "Otro autor", "111")

def test_prestar_libro(biblioteca_temporal):
    biblioteca_temporal.agregar_libro("1984", "Orwell", "111")
    biblioteca_temporal.prestar_libro("111")
    libro = biblioteca_temporal.buscar_por_isbn("111")
    assert libro.disponible is False

def test_no_presta_libro_ya_prestado(biblioteca_temporal):
    biblioteca_temporal.agregar_libro("1984", "Orwell", "111")
    biblioteca_temporal.prestar_libro("111")
    with pytest.raises(ValueError):
        biblioteca_temporal.prestar_libro("111")

def test_devolver_libro(biblioteca_temporal):
    biblioteca_temporal.agregar_libro("1984", "Orwell", "111")
    biblioteca_temporal.prestar_libro("111")
    biblioteca_temporal.devolver_libro("111")
    libro = biblioteca_temporal.buscar_por_isbn("111")
    assert libro.disponible is True