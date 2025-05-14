import json
import csv
from proceso import Proceso

class RepositorioProcesos:
    def __init__(self):
        """Inicializa el repositorio con un diccionario para almacenar procesos por su pid."""
        self.procesos = {}

    def agregar_proceso(self, proceso: Proceso):
        """Agrega un proceso al repositorio, verificando que el pid sea único."""
        if proceso.pid in self.procesos:
            raise ValueError(f"El PID '{proceso.pid}' ya existe en el repositorio.")
        self.procesos[proceso.pid] = proceso

    def listar_procesos(self):
        """Devuelve una lista con todos los procesos registrados."""
        return list(self.procesos.values())

    def eliminar_proceso(self, pid: str):
        """Elimina un proceso del repositorio dado su pid."""
        if pid not in self.procesos:
            raise ValueError(f"No se encontró un proceso con PID '{pid}'.")
        del self.procesos[pid]

    def obtener_proceso(self, pid: str):
        """Obtiene un proceso dado su pid."""
        if pid not in self.procesos:
            raise ValueError(f"No se encontró un proceso con PID '{pid}'.")
        return self.procesos[pid]

    def guardar_json(self, archivo: str):
        """Guarda los procesos en un archivo JSON."""
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump([vars(proceso) for proceso in self.procesos.values()], f, indent=4)

    def cargar_json(self, archivo: str):
        """Carga procesos desde un archivo JSON, reemplazando los existentes."""
        with open(archivo, "r", encoding="utf-8") as f:
            procesos_cargados = json.load(f)
        self.procesos = {p["pid"]: Proceso(**p) for p in procesos_cargados}

    def guardar_csv(self, archivo: str):
        """Guarda los procesos en un archivo CSV con separador ';'."""
        with open(archivo, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["pid", "duracion", "prioridad", "tiempo_restante", "tiempo_llegada", "tiempo_inicio", "tiempo_fin"])
            for proceso in self.procesos.values():
                writer.writerow([proceso.pid, proceso.duracion, proceso.prioridad, proceso.tiempo_restante, proceso.tiempo_llegada, proceso.tiempo_inicio, proceso.tiempo_fin])

    def cargar_csv(self, archivo: str):
        """Carga procesos desde un archivo CSV, reemplazando los existentes."""
        with open(archivo, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            self.procesos = {row["pid"]: Proceso(row["pid"], int(row["duracion"]), int(row["prioridad"])) for row in reader}

