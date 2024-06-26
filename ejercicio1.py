from datetime import date
import random

class Fecha:
    def __init__(self, dia=None, mes=None, año=None):
        if dia is None and mes is None and año is None:
            hoy = date.today()
            self.dia = hoy.day
            self.mes = hoy.month
            self.año = hoy.year
        else:
            self.dia = dia
            self.mes = mes
            self.año = año

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.año:04d}"

    def __eq__(self, otra_fecha):
        return self.dia == otra_fecha.dia and self.mes == otra_fecha.mes and self.año == otra_fecha.año

    def calcular_dif_fecha(self, otra_fecha):
        fecha1 = date(self.año, self.mes, self.dia)
        fecha2 = date(otra_fecha.año, otra_fecha.mes, otra_fecha.dia)
        return abs((fecha1 - fecha2).days)

class Alumno:
    def __init__(self, nombre, dni, fecha_ingreso, carrera):
        self.datos = {
            "Nombre": nombre,
            "DNI": dni,
            "FechaIngreso": fecha_ingreso,
            "Carrera": carrera
        }

    def cambiar_datos(self, **nuevos_datos):
        for clave, valor in nuevos_datos.items():
            if clave in self.datos:
                self.datos[clave] = valor

    def antiguedad(self):
        fecha_ingreso = self.datos["FechaIngreso"]
        hoy = date.today()
        fecha_ingreso_date = date(fecha_ingreso.año, fecha_ingreso.mes, fecha_ingreso.dia)
        return (hoy - fecha_ingreso_date).days

    def __str__(self):
        return (f"Nombre: {self.datos['Nombre']}, DNI: {self.datos['DNI']}, "
                f"Fecha de Ingreso: {self.datos['FechaIngreso']}, Carrera: {self.datos['Carrera']}")

    def __eq__(self, otro_alumno):
        return self.datos == otro_alumno.datos

class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class IteradorListaDoblementeEnlazada:
    def __init__(self, cabeza):
        self.actual = cabeza

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration
        else:
            dato = self.actual.dato
            self.actual = self.actual.siguiente
            return dato

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

    def __iter__(self):
        return IteradorListaDoblementeEnlazada(self.cabeza)

    @staticmethod
    def lista_ejemplo():
        lista = ListaDoblementeEnlazada()
        nombres = ["Juan", "Ana", "Pedro", "Marta", "Luis", "Sofia"]
        carreras = ["Ingeniería", "Medicina", "Derecho", "Arquitectura", "Economía"]

        for _ in range(10):
            nombre = random.choice(nombres)
            dni = random.randint(10000000, 99999999)
            fecha_ingreso = Fecha(random.randint(1, 28), random.randint(1, 12), random.randint(2010, 2023))
            carrera = random.choice(carreras)
            alumno = Alumno(nombre, dni, fecha_ingreso, carrera)
            lista.agregar(alumno)

        return lista

    def ordenar_por_dni(self):
        if self.cabeza is None:
            return

        actual = self.cabeza.siguiente
        while actual is not None:
            key = actual.dato
            mover = actual.anterior

            while mover is not None and mover.dato.datos["DNI"] > key.datos["DNI"]:
                mover.siguiente.dato = mover.dato
                mover = mover.anterior

            if mover is None:
                self.cabeza.dato = key
            else:
                mover.siguiente.dato = key

            actual = actual.siguiente

# Ejemplo de uso:

# Crear lista de ejemplo
lista_alumnos = ListaDoblementeEnlazada.lista_ejemplo()

# Mostrar los alumnos antes de ordenar
print("Lista antes de ordenar:")
for alumno in lista_alumnos:
    print(alumno)

# Ordenar la lista por DNI
lista_alumnos.ordenar_por_dni()

# Mostrar los alumnos después de ordenar
print("\nLista después de ordenar por DNI:")
for alumno in lista_alumnos:
    print(alumno)
