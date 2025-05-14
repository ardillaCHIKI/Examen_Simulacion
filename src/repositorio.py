from proceso import Proceso
from typing import List
import json
import csv

class RepositorioProcesos:
    """ Clase para gestionar el conjunto de procesos activos con persistencia en JSON y CSV. """
    
    def __init__(self):
        self.procesos = {}

    def agregar_proceso(self, proceso: Proceso):
        """ Agrega un proceso al repositorio, verificando que el PID sea único. """
        if proceso.pid in self.procesos:
            raise ValueError(f"El proceso con PID '{proceso.pid}' ya existe.")
        self.procesos[proceso.pid] = proceso

    def listar_procesos(self) -> List[Proceso]:
        """ Devuelve una lista de todos los procesos registrados. """
        return list(self.procesos.values())

    def eliminar_proceso(self, pid: str):
        """ Elimina un proceso dado su PID, si existe. """
        if pid not in self.procesos:
            raise ValueError(f"No se encontró un proceso con PID '{pid}'.")
        del self.procesos[pid]

    def obtener_proceso(self, pid: str) -> Proceso:
        """ Obtiene un proceso específico por su PID. """
        if pid not in self.procesos:
            raise ValueError(f"No se encontró un proceso con PID '{pid}'.")
        return self.procesos[pid]

    def guardar_json(self, archivo: str):
        """ Guarda los procesos en un archivo JSON. """
        with open(archivo, "w") as f:
            json.dump([{ "pid": p.pid, "duracion": p.duracion, "prioridad": p.prioridad } for p in self.procesos.values()], f, indent=4)

    def cargar_json(self, archivo: str):
        """ Carga los procesos desde un archivo JSON, reemplazando los existentes. """
        with open(archivo, "r") as f:
            datos = json.load(f)
        self.procesos = {p["pid"]: Proceso(p["pid"], p["duracion"], p["prioridad"]) for p in datos}

    def guardar_csv(self, archivo: str):
        """ Guarda los procesos en un archivo CSV con separador ';'. """
        with open(archivo, "w", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["PID", "Duración", "Prioridad"])  # Encabezados
            for p in self.procesos.values():
                writer.writerow([p.pid, p.duracion, p.prioridad])

    def cargar_csv(self, archivo: str):
        """ Carga los procesos desde un archivo CSV, reemplazando los existentes. """
        with open(archivo, "r") as f:
            reader = csv.reader(f, delimiter=";")
            next(reader)  # Saltar encabezado
            self.procesos = {row[0]: Proceso(row[0], int(row[1]), int(row[2])) for row in reader}


