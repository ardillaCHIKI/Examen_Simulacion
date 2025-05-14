import pytest
from src.scheduler import FCFSScheduler, RoundRobinScheduler
from src.proceso import Proceso

def test_fcfs_planificacion():
    scheduler = FCFSScheduler()
    procesos = [Proceso("P1", 10, 2), Proceso("P2", 5, 1), Proceso("P3", 8, 3)]
    gantt = scheduler.planificar(procesos)
    assert gantt == [("P1", 0, 10), ("P2", 10, 15), ("P3", 15, 23)]

def test_round_robin_planificacion():
    scheduler = RoundRobinScheduler(quantum=3)
    procesos = [Proceso("P1", 10, 2), Proceso("P2", 5, 1), Proceso("P3", 8, 3)]
    gantt = scheduler.planificar(procesos)
    assert len(gantt) > len(procesos)  # Round-Robin ejecuta en ciclos
