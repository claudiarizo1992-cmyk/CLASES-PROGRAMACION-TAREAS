# Funcion para registrar los datos de una mascota desde el teclado
def registrar_mascota(numero_mascota):
    print(f"Ingrese los datos de la mascota {numero_mascota}:")
    nombre = input("Nombre: ")
    especie = input("Especie: ")
    edad = input("Edad: ")
    print("-" * 35)
    return nombre, especie, edad

# Funcion para mostrar la informacion de forma ordenada
def mostrar_informacion(nombre, especie, edad):
    print("---Datos de la Mascota---")
    print(f"Nombre: {nombre}")
    print(f"Especie: {especie}")
    print(f"Edad: {edad}")
    print("-")

# Funcion principal que controla el flujo del programa
def iniciar_programa():
    print("=== REGISTRO DE MASCOTAS (Prog. Tradicional) ===\n")
    nom1, esp1, ed1 = registrar_mascota(1)
    nom2, esp2, ed2 = registrar_mascota(2)
    print("\n=== MOSTRANDO INFORMACION REGISTRADA ===\n")
    mostrar_informacion(nom1, esp1, ed1)
    print()
    mostrar_informacion(nom2, esp2, ed2)

if __name__ == "__main__":
    iniciar_programa()

          
          
                                        