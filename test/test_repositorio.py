import pytest
import os
from src.repositorio import RepositorioProcesos
from src.proceso import Proceso

def test_guardar_cargar_json():
    repositorio = RepositorioProcesos()
    repositorio.agregar_proceso(Proceso("P1", 10, 2))
    repositorio.guardar_json("tests/procesos_test.json")
    
    nuevo_repo = RepositorioProcesos()
    nuevo_repo.cargar_json("tests/procesos_test.json")
    
    assert "P1" in nuevo_repo.procesos
    os.remove("tests/procesos_test.json")  # Limpieza

def test_guardar_cargar_csv():
    repositorio = RepositorioProcesos()
    repositorio.agregar_proceso(Proceso("P1", 10, 2))
    repositorio.guardar_csv("tests/procesos_test.csv")
    
    nuevo_repo = RepositorioProcesos()
    nuevo_repo.cargar_csv("tests/procesos_test.csv")
    
    assert "P1" in nuevo_repo.procesos
    os.remove("tests/procesos_test.csv")  # Limpieza
