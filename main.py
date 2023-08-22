class asiento:
    def __init__(self, precio, registro, color):
        self.precio = precio
        self.registro = registro
        self.color = color
    
    def cambiarColor(self, color):
        colores_permitidos = ["negro", "amarillo", "verde", "rojo", "blanco"]
        if color.lower() in colores_permitidos:
            self.color = color
        else:
            return "Ese color no está disponible"

class motor: 
    def __init__ (self, numeroCilindros, tipo, registro): 
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
        
    def cambiarRegistro(self, nuRegistro):
        self.registro = nuRegistro

    def asignarTipo(self, nuTipo):
        tiposper = ["electrico","gasolina"]
        if nuTipo.lower() in tiposper: 
            self.tipo = nuTipo 

class auto: 
    cantidadCreados = 0 
    def __init__(self, modelo, precio, asientos, marca, motor, registro): 
        self.modelo = modelo 
        self.precio = precio 
        self.asientos = list(asientos)  
        self.marca = marca
        self.motor = motor
        self.registro = registro
        auto.cantidadCreados += 1  # Incrementar la cantidad de autos creados

    def cantidadAsientos(self):
        return len(self.asientos)
    
    def verificarIntegridad(self): 
        if self.motor.registro == self.registro:
            for asiento_obj in self.asientos:
                if isinstance(asiento_obj, asiento) and asiento_obj.registro != self.registro:
                    return "Las Piezas no son originales"
            return "Auto original"
        else:
            return "Las Piezas no son originales"

