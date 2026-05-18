class Reserva:
    def __init__(self, nombre_cliente, numero_habitacion):
        #atributos privados
        self.__nombre_cliente = nombre_cliente
        self.__numero_habitacion = numero_habitacion
        self.__fechas_reserva = []
    #Métodos GET
    def get_nombre_cliente(self):
        return self.__nombre_cliente
    def get_numero_habitacion(self):
        return self.__numero_habitacion
    def get_fechas_reserva(self):
        return self.__fechas_reserva
    #Métodos SET
    def set_nombre_cliente(self, nuevo_nombre):
        self.__nombre_cliente = nuevo_nombre
    def set_numero_habitacion(self, nuevo_numero):
        if nuevo_numero > 0:
            self.__numero_habitacion = nuevo_numero
        else:
            print("Número de habitación inválido")
    #Manejo de fechas
    def agregar_fecha(self, fecha):
        if fecha not in self.__fechas_reserva:
            self.__fechas_reserva.append(fecha)
        else:
            print("La fecha ya está reservada")
    def eliminar_fecha(self, fecha):
        if fecha in self.__fechas_reserva:
            self.__fechas_reserva.remove(fecha)
        else:
            print("La fecha no existe en la reserva")
reserva1 = Reserva("Ana", 101)
print(reserva1.get_nombre_cliente())
print(reserva1.get_numero_habitacion())
reserva1.agregar_fecha("2026-05-10")
reserva1.agregar_fecha("2026-05-11")
print("Fechas:", reserva1.get_fechas_reserva())
reserva1.eliminar_fecha("2026-05-10")
print("Fechas actualizadas:", reserva1.get_fechas_reserva())
reserva1.set_numero_habitacion(202)
print("Nueva habitación:", reserva1.get_numero_habitacion())