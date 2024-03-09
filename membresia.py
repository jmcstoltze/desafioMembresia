
# Importa módulo abc de la clase ABC y el decorador abstractmethod
from abc import ABC, abstractmethod

# Definición de una clase abstracta llamada Membresía
class Membresia(ABC):
    # Constructor de la clase Membresía que toma el correo del suscriptor y el número de tarjeta
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta

    # Método getter que retorna el atributo correo del suscriptor
    @property
    def correo_suscriptor(self):
        return self.__correo_suscriptor

    # Método getter que retorna el atributo número de tarjeta
    @property
    def numero_tarjeta(self):
        return self.__numero_tarjeta

    # Método abstracto a implementar por las subclases para cambiar el tipo de membresía hacia una nueva membresía
    @abstractmethod
    def cambiar_suscripcion(self, nueva_membresia: int):
        pass

    # Método protegido para crear una nueva instancia de membresía según el tipo especificado
    def _crear_nueva_membresia(self, nueva_membresia: int):
        
        # Retorna instancia del tipo especificado
        if nueva_membresia == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)

# Clase membresía Gratis que hereda de Membresía
class Gratis(Membresia):

    # Atributos de clase
    costo = 0
    cantidad_dispositivos = 1

    # Método para cambiar la suscripción de la membresía (1 a 4)
    def cambiar_suscripcion(self, nueva_membresia: int):
        
        # Retorna la nueva membresía creada o self si no es válida
        if nueva_membresia < 1 or nueva_membresia > 4:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

# Clase membresía básica que hereda de Membresía
class Basica(Membresia):

    # Atributos de clase
    costo = 3000
    cantidad_dispositivos = 2

    # Método constructor de la clase con parámetros
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        
        # Llama al constructor de la clase Membresia
        super().__init__(correo_suscriptor, numero_tarjeta)

        # Verifica si la instancia es del tipo Familiar o Sin Conexión
        if isinstance(self, Familiar) or isinstance(self, SinConexion):
            
            # Retorna un valor para días de regalo
            self.__dias_regalo = 7

        # Si la instancia es del tipo Pro
        elif isinstance(self, Pro):

            # Retorna un valor para días de regalo
            self.__dias_regalo = 15 

    # Método que devuelve la clase Gratis con valores de correo y tarjeta
    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

    # Método para cambiar suscripción que recibe un parámetro int del tipo de membresía
    def cambiar_suscripcion(self, nueva_membresia: int):
        
        # Si está fuera del rango devuelve la instancia actual
        if nueva_membresia < 2 or nueva_membresia > 4:
            return self
        
        # Si es válido, devuelve una nueva instancia a través de método protegido, según el tipo solicitado
        else:
            return self._crear_nueva_membresia(nueva_membresia)

# Clase Familiar que hereda de clase Básica
class Familiar(Basica):

    # Atributos de clase
    costo = 5000
    cantidad_dispositivos = 5

    # Método para cambiar suscripción que recibe un parámetro int del tipo de membresía
    def cambiar_suscripcion(self, nueva_membresia: int):
        
        # Si el tipo no corresponde a los indicados, retorna la misma instancia sin cambios
        if nueva_membresia not in [1, 3, 4]:
            return self
        
        # De lo contrario crea la instancia de la nueva membresía con método protegido
        else:
            return self._crear_nueva_membresia(nueva_membresia)

    # Método para modificar los controles parentales
    def modificar_control_parental(self):
        
        # Por implementar
        pass

# Clase membresía SinConexión, que hereda de la membresía básica
class SinConexion(Basica):

    # Atributo de clase
    costo = 3500

    # Método para cambiar suscripción que recibe un parámetro int del tipo de membresía
    def cambiar_suscripcion(self, nueva_membresia: int):
        
        # Si el tipo no corresponde a los indicados, retorna la misma instancia sin cambios
        if nueva_membresia not in [1, 2, 4]:
            return self
        
        # De lo contrario crea la instancia de la nueva membresía con método protegido
        else:
            return self._crear_nueva_membresia(nueva_membresia)

    # Método para incrementar la cantidad máxima de contenido offline
    def incrementar_cantidad_maxima_offline(self):
        
        # Por implementar
        pass

# Clase de la membresía Pro, que hereda de la clase Familiar y la clase SinConexion
class Pro(Familiar, SinConexion):

    # Atributos de clase
    costo = 7000
    cantidad_dispositivos = 6

    # Método para cambiar suscripción que recibe un parámetro de tipo de membresía
    def cambiar_suscripcion(self, nueva_membresia: int):
        
        # Si el tipo no corresponde a los indicados, retorna la misma instancia sin cambios
        if nueva_membresia < 1 or nueva_membresia > 3:
            return self
        
        # De lo contrario crea la instancia de la nueva membresía con método protegido
        else:
            return self._crear_nueva_membresia(nueva_membresia)


# Módulo de pruebas del archivo membresia.py
if __name__ == "__main__":

    # Crea instancia de la clase Gratis
    g = Gratis("correo@prueba.cl", "123 456 789")
    # Imprime del tipo de la instancia creada
    print(type(g)) # <class '__main__.Gratis'>

    # Genera una nueva instancia invocando la función con el valor del tipo de suscripción
    b = g.cambiar_suscripcion(1)
    # Imprime el tipo de la nueva instancia
    print(type(b)) # <class '__main__.Basica'>

    # Genera una nueva instancia invocando la función con el valor del tipo de suscripción
    f = b.cambiar_suscripcion(2)
    # Imprime el tipo de la nueva instancia
    print(type(f)) # <class '__main__.Familiar'>

    # Genera una nueva instancia invocando la función con el valor del tipo de suscripción
    sc = f.cambiar_suscripcion(3)
    # Imprime el tipo de la nueva instancia
    print(type(sc)) # <class '__main__.SinConexion'>

    # Genera una nueva instancia invocando la función con el valor del tipo de suscripción
    pro = sc.cambiar_suscripcion(4)
    # Imprime el tipo de la nueva instancia
    print(type(pro)) # <class '__main__.Pro'>

    # Genera una nueva instancia invocando la función con el valor del tipo de suscripción
    g2 = pro.cancelar_suscripcion()
    # Imprime el tipo de la nueva instancia
    print(type(g2)) # <class '__main__.Gratis'>
