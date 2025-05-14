
import pytest
from src.metrics import calcular_metricas
from src.proceso import Proceso

def test_calculo_metricas():
    procesos = [Proceso("P1", 10, 2), Proceso("P2", 5, 1), Proceso("P3", 8, 3)]
    procesos[0].tiempo_inicio, procesos[0].tiempo_fin = 0, 10
    procesos[1].tiempo_inicio, procesos[1].tiempo_fin = 10, 15
    procesos[2].tiempo_inicio, procesos[2].tiempo_fin = 15, 23

    resultados, prom_respuesta, prom_retorno, prom_espera = calcular_metricas(procesos)

    assert isinstance(prom_respuesta, float)
    assert isinstance(prom_retorno, float)
    assert isinstance(prom_espera, float)
    assert resultados[0][1] == 0  # Primer proceso debe tener tiempo de respuesta 0

