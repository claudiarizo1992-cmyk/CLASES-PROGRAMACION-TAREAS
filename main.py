
from mascota import Mascota

def main():
    print("___GESTION DE MASCOTAS (Enfoque POO) ---\n")
    # Instanciacion : Creacion del primer objeto de la clase Mascota
    mascota1 = Mascota("Max" , "Perro" , 3) # type: ignore
    # Instancion : Creacion del segundo objeto de la clase Mascota
    mascota2 = Mascota("Luna" , "Gato" , 2) # type: ignore
    # Ejecucion de metodos para el objeto 1
    print("Datos del Objeto 1 ")
    mascota1.mostrar_informacion()
    mascota1.hacer_sonido()
    print("\n" + "="*40 + "\n")
     
     # Ejecucion de metodos para el objeto 2
    print("Datos del Objeto 2")
    mascota2.mostrar_informacion()
    mascota2.hacer_sonido()
    
if __name__ == "__main__":
    main()
    