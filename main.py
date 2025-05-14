from src.proceso import Proceso
from src.Fcfsscheduler import FCFSScheduler
from src.roundRobinScheduler import RoundRobinScheduler
from src.scheduler import Scheduler
from typing import List
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def simular_ejecucion(scheduler: Scheduler, procesos: List[Proceso]):
    """
    Simula la ejecución de los procesos usando un scheduler y muestra el diagrama de Gantt.
    
    :param scheduler: Instancia de Scheduler (FCFS, RoundRobin, etc.).
    :param procesos: Lista de procesos a planificar.
    """
    gantt_chart = scheduler.planificar(procesos)

    print("\nDiagrama de Gantt:")
    print("PID\tInicio\tFin")
    for entry in gantt_chart:
        print(f"{entry[0]}\t{entry[1]}\t{entry[2]}")

# Ejemplo de uso con FCFS y Round Robin
if __name__ == "__main__":
    procesos = [
        Proceso("P1", 10, 3),
        Proceso("P2", 5, 1),
        Proceso("P3", 8, 2)
    ]

    scheduler_fcfs = FCFSScheduler()
    scheduler_rr = RoundRobinScheduler(quantum=3)

    print("\n**Simulación con FCFS**")
    simular_ejecucion(scheduler_fcfs, procesos)

    print("\n**Simulación con Round-Robin (Quantum=3)**")
    simular_ejecucion(scheduler_rr, procesos)
