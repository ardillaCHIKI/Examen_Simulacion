from abc import ABC, abstractmethod
from typing import List, Tuple
from proceso import Proceso

GanttEntry = Tuple[str, int, int]  # Definición de la tupla para el diagrama de Gantt

class Scheduler(ABC):
    """ Clase abstracta que define la interfaz para los planificadores de CPU. """

    @abstractmethod
    def planificar(self, procesos: List['Proceso']) -> List[GanttEntry]:
        """
        Método abstracto para planificar la ejecución de procesos.
        Debe ser implementado por las clases derivadas.
        
        :param procesos: Lista de objetos Proceso a planificar.
        :return: Lista de entradas para el diagrama de Gantt.
        """
        pass

