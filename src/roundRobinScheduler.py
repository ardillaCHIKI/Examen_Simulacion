from abc import ABC, abstractmethod
from typing import List, Tuple
from proceso import Proceso
from scheduler import Scheduler
from metrics import GanttEntry

class RoundRobinScheduler(Scheduler):
    def __init__(self, quantum: int):
        if quantum <= 0:
            raise ValueError("El quantum debe ser un entero positivo.")
        self.quantum = quantum

    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        """Planifica los procesos usando el algoritmo Round-Robin con un quantum fijo."""
        gantt = []
        tiempo_actual = 0
        cola_procesos = procesos[:]  # Copia de la lista para iterar sin modificar la original

        while cola_procesos:
            proceso = cola_procesos.pop(0)  # Tomamos el primer proceso en la cola
            
            if proceso.tiempo_inicio is None:
                proceso.iniciar(tiempo_actual)  # Asignamos el tiempo de inicio si no lo tiene

            tiempo_ejecucion = min(self.quantum, proceso.tiempo_restante)
            tiempo_actual += tiempo_ejecucion
            proceso.tiempo_restante -= tiempo_ejecucion
            
            gantt.append((proceso.pid, tiempo_actual - tiempo_ejecucion, tiempo_actual))

            if proceso.tiempo_restante > 0:
                cola_procesos.append(proceso)  # Si queda tiempo por ejecutar, lo volvemos a la cola
            else:
                proceso.finalizar(tiempo_actual)  # Si termina, registramos su tiempo de finalización

        return gantt