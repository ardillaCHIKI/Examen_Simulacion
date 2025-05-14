import pytest
from src.proceso import Proceso

def test_creacion_proceso_valido():
    proceso = Proceso("P1", 10, 2)
    assert proceso.pid == "P1"
    assert proceso.duracion == 10
    assert proceso.prioridad == 2

def test_pid_no_vacio():
    with pytest.raises(ValueError):
        Proceso("", 10, 2)

def test_pid_duplicado():
    Proceso.procesos_existentes.clear()  # Resetear el conjunto de PIDs existentes
    Proceso("P1", 10, 2)
    with pytest.raises(ValueError):
        Proceso("P1", 5, 1)

def test_duracion_positiva():
    with pytest.raises(ValueError):
        Proceso("P2", -5, 1)

