class objeto:
    def __init__(self, titulo,autor ,numero_paginas , genero): 
        self.titulo = titulo
        self.autor = autor
        self.paginas = numero_paginas
        self.genero = genero
        self.paginas_actual = 1

    def mostrar_informacion(self):
            print("\n---DETALLES DEL LIBRO---")
            print(f"Titulo: {self.titulo}")
            print(f"Autor: {self.autor}")
            print(f"Genero: {self.genero}")
            print(f"Total de paginas: {self.paginas}")
            print(f"Progreso: Paginas : {self.paginas_actual}")
        
    def leer_paginas(self, cantidad_paginas):
         
         if cantidad_paginas <= 0:
              print("\n error: cantidad no valida")
              return
         
         nueva_pagina = self.paginas_actual + cantidad_paginas
         if nueva_pagina >= self.paginas:
              self.paginas_actual = self.paginas
              print("\n Felicidades! Leiste el libro: {self.titulo}")
         else:
              self.paginas_actual=  nueva_pagina
              print(f"\n avanzaste a la pagina {self.paginas_actual}")
              
     
#Creacion de dos objetos distintos 
libro1 = objeto("Cien Años de Soledad", "Gabriel Garcia Marquez" , 496, "Realismo Magico")
libro2 = objeto("Don Quijote", "Miguel de Cervantes" , 864, "Aventuras")
                   #Uso de los objetos y sus metodos
libro1.mostrar_informacion()
libro1.leer_paginas(50)
libro2.mostrar_informacion()
libro2.leer_paginas(900)

                   
                   