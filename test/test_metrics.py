import pytest
from src.scheduler import FCFSScheduler
from src.proceso import Proceso

def test_calculo_metricas():
    scheduler = FCFSScheduler()
    procesos = [Proceso("P1", 10, 2), Proceso("P2", 5, 1), Proceso("P3", 8, 3)]
    scheduler.planificar(procesos)
    
    resultados, prom_respuesta, prom_retorno, prom_espera = scheduler.calcular_metricas(procesos)
    
    assert isinstance(prom_respuesta, float)
    assert isinstance(prom_retorno, float)
    assert isinstance(prom_espera, float)
    assert resultados[0][1] == 0  # Primer proceso debe tener tiempo de respuesta 0
