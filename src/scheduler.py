from abc import ABC, abstractmethod
from typing import List
from src.proceso import Proceso

GanttEntry = tuple[str, int, int]

class Scheduler(ABC):
    @abstractmethod
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        pass