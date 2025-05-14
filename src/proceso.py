class Proceso:
    procesos_existentes = set()  # Conjunto para almacenar los pids existentes
    
    def __init__(self, pid: str, duracion: int, prioridad: int):
        if not pid:
            raise ValueError("El PID no puede estar vacío.")
        if pid in Proceso.procesos_existentes:
            raise ValueError(f"El PID '{pid}' ya existe.")
        if duracion <= 0:
            raise ValueError("La duración debe ser un entero positivo.")
        if prioridad < 0:
            raise ValueError("La prioridad debe ser un entero no negativo.")
        
        self.pid = pid
        self.duracion = duracion
        self.prioridad = prioridad
        self.tiempo_restante = duracion
        self.tiempo_llegada = 0  # Asumido como 0
        self.tiempo_inicio = None
        self.tiempo_fin = None
        
        Proceso.procesos_existentes.add(pid)
    
    def iniciar(self, tiempo_actual: int):
        """Registra el tiempo de inicio del proceso."""
        if self.tiempo_inicio is None:
            self.tiempo_inicio = tiempo_actual
    
    def finalizar(self, tiempo_actual: int):
        """Registra el tiempo de finalización del proceso."""
        self.tiempo_fin = tiempo_actual

    def __repr__(self):
        return (f"Proceso(pid='{self.pid}', duracion={self.duracion}, prioridad={self.prioridad}, "
                f"tiempo_restante={self.tiempo_restante}, tiempo_llegada={self.tiempo_llegada}, "
                f"tiempo_inicio={self.tiempo_inicio}, tiempo_fin={self.tiempo_fin})")

