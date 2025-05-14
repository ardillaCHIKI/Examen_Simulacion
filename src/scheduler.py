from abc import ABC, abstractmethod
from typing import List, Tuple
from proceso import Proceso  # Asegúrate de importar la clase Proceso correctamente

GanttEntry = Tuple[str, int, int]
class Scheduler(ABC):
    @abstractmethod
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        """Método abstracto para planificar los procesos en el CPU."""
        pass

class FCFSScheduler(Scheduler):
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        """Planifica los procesos según el orden de llegada (FCFS)."""
        gantt = []
        tiempo_actual = 0
        
        for proceso in procesos:
            proceso.iniciar(tiempo_actual)
            tiempo_fin = tiempo_actual + proceso.duracion
            proceso.finalizar(tiempo_fin)
            gantt.append((proceso.pid, proceso.tiempo_inicio, proceso.tiempo_fin))
            tiempo_actual = tiempo_fin  # Avanzamos el tiempo
        
        return gantt

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
