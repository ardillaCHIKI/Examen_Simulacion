from typing import List, Tuple
from src.proceso import Proceso

GanttEntry = Tuple[str, int, int]

def generar_diagrama_gantt(planificacion: List[GanttEntry]):
    """Muestra el orden de ejecución y los tiempos de inicio y fin."""
    print("\n📊 Diagrama de Gantt 📊")
    print("PID\tInicio\tFin")
    for pid, inicio, fin in planificacion:
        print(f"{pid}\t{inicio}\t{fin}")

def calcular_metricas(procesos: List[Proceso]):
    """Calcula métricas de respuesta, retorno y espera, y muestra promedios."""
    resultados = []
    suma_respuesta = suma_retorno = suma_espera = 0
    total_procesos = len(procesos)

    for proceso in procesos:
        tiempo_respuesta = proceso.tiempo_inicio - proceso.tiempo_llegada
        tiempo_retorno = proceso.tiempo_fin - proceso.tiempo_llegada
        tiempo_espera = tiempo_retorno - proceso.duracion

        resultados.append((proceso.pid, tiempo_respuesta, tiempo_retorno, tiempo_espera))

        suma_respuesta += tiempo_respuesta
        suma_retorno += tiempo_retorno
        suma_espera += tiempo_espera

    # Calculamos los valores promedio
    promedio_respuesta = suma_respuesta / total_procesos
    promedio_retorno = suma_retorno / total_procesos
    promedio_espera = suma_espera / total_procesos

    print("\n📊 Métricas de rendimiento 📊")
    print("PID\tResp\tRet\tEsp")
    for pid, resp, ret, esp in resultados:
        print(f"{pid}\t{resp}\t{ret}\t{esp}")

    print(f"\n🔹 Promedio tiempo de respuesta: {promedio_respuesta:.2f}")
    print(f"🔹 Promedio tiempo de retorno: {promedio_retorno:.2f}")
    print(f"🔹 Promedio tiempo de espera: {promedio_espera:.2f}")

    return resultados, promedio_respuesta, promedio_retorno, promedio_espera
