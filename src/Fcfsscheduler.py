from proceso import Proceso
from scheduler import Scheduler
from typing import List, Tuple
GanttEntry = Tuple[str, int, int]  # Definición de la tupla para el diagrama de Gantt

class FCFSScheduler(Scheduler):
    """ Implementación del planificador First-Come, First-Served (FCFS). """

    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        """
        Planifica los procesos en el orden de llegada sin interrupciones.
        
        :param procesos: Lista de objetos Proceso a planificar.
        :return: Lista de entradas para el diagrama de Gantt.
        """
        tiempo_actual = 0
        gantt = []

        for proceso in procesos:
            proceso.iniciar(tiempo_actual)
            tiempo_fin = tiempo_actual + proceso.duracion
            proceso.finalizar(tiempo_fin)
            gantt.append((proceso.pid, proceso.tiempo_inicio, proceso.tiempo_fin))
            tiempo_actual = tiempo_fin  # Avanza el tiempo global
        
        return gantt


