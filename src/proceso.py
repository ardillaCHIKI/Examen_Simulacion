class Proceso(object):
    procesos_existentes = set()  # Conjunto para almacenar los PID existentes
    
    def __init__(self, pid: str, duracion: int, prioridad: int):
        if not pid:
            raise ValueError("El PID no puede estar vacío.")
        if pid in Proceso.procesos_existentes:
            raise ValueError(f"El PID '{pid}' ya está en uso.")
        if duracion <= 0:
            raise ValueError("La duración debe ser un entero positivo.")
        
        self.pid = pid
        self.duracion = duracion
        self.prioridad = prioridad
        self.tiempo_restante = duracion
        self.tiempo_llegada = 0
        self.tiempo_inicio = None
        self.tiempo_fin = None
        
        Proceso.procesos_existentes.add(pid)  # Registrar el PID en el conjunto de procesos existentes
    
    def iniciar(self, tiempo_actual: int):
        """ Marca el inicio del proceso """
        self.tiempo_inicio = tiempo_actual
    
    def finalizar(self, tiempo_actual: int):
        """ Marca la finalización del proceso """
        self.tiempo_fin = tiempo_actual
    
    def ejecutar(self, tiempo_cpu: int):
        """ Reduce el tiempo restante del proceso """
        if self.tiempo_restante > 0:
            self.tiempo_restante -= min(tiempo_cpu, self.tiempo_restante)
    
    def __str__(self):
        return f"Proceso {self.pid}: Duración={self.duracion}, Prioridad={self.prioridad}, Tiempo restante={self.tiempo_restante}"

