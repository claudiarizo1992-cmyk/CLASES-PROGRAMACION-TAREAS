class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad}")

    def hacer_sonido(self):
        if self.especie == "Perro":
            print(f"{self.nombre} dice: Guau!")
        elif self.especie == "Gato":
            print(f"{self.nombre} dice: Miau!")
        else:
            print(f"{self.nombre} hace un sonido desconocido.")

