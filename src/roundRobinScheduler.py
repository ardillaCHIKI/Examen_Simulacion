from abc import ABC, abstractmethod
from typing import List, Tuple
from proceso import Proceso
from scheduler import Scheduler
from metrics import GanttEntry

class RoundRobinScheduler(Scheduler):
    """ Implementación del planificador Round-Robin con quantum fijo. """

    def __init__(self, quantum: int):
        if quantum <= 0:
            raise ValueError("El quantum debe ser un entero positivo.")
        self.quantum = quantum

    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        """
        Planifica los procesos utilizando el algoritmo Round-Robin.
        
        :param procesos: Lista de objetos Proceso a planificar.
        :return: Lista de entradas para el diagrama de Gantt.
        """
        tiempo_actual = 0
        gantt = []
        cola = procesos[:]  # Copia de la lista de procesos para manipulación

        while cola:
            proceso = cola.pop(0)  # Tomar el primer proceso de la cola
            
            if proceso.tiempo_inicio is None:
                proceso.iniciar(tiempo_actual)

            tiempo_ejecucion = min(self.quantum, proceso.tiempo_restante)
            proceso.ejecutar(tiempo_ejecucion)
            tiempo_fin = tiempo_actual + tiempo_ejecucion

            gantt.append((proceso.pid, tiempo_actual, tiempo_fin))
            tiempo_actual = tiempo_fin  # Avanza el tiempo global
            
            if proceso.tiempo_restante > 0:
                cola.append(proceso)  # Si el proceso no ha finalizado, vuelve a la cola
            else:
                proceso.finalizar(tiempo_actual)  # Marca el proceso como finalizado

        return gantt


