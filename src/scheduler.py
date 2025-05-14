from abc import ABC, abstractmethod
from typing import List, Tuple
from proceso import Proceso  

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
