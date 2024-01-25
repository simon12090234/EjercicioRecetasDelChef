from recetasdelchef.model.chef import Chef, UnidadMedida


class Consola:

    def __init__(self, chef: Chef):
        self.chef: Chef = chef

    @staticmethod
    def mostrar_bienvenida():
        print("============================")
        print("BIENVENID@ A RECETAS DEL CHEF")
        print("============================")

    @staticmethod
    def mostrar_menu():
        print("\nOPCIONES:")
        print("1. Registrar receta")
        print("2. Buscar receta")
        print("3. Recetas vegetarianas")
        print("4. Recetas veganas")
        print("5. Contador de recetas por etiqueta")
        print("6. Salir")
        opcion = int(input("Ingrese una opción: "))
        while opcion not in range(1, 7):
            print(">>> ERROR: Opción inválida. Intente nuevamente")
            opcion = int(input("Ingrese una opción: "))
        return opcion

    def ciclo_app(self):
        Consola.mostrar_bienvenida()
        fin_app: bool = False
        while not fin_app:
            opcion: int = Consola.mostrar_menu()
            fin_app = self.procesar_opcion_usuario(opcion)

    def procesar_opcion_usuario(self, opcion: int) -> bool:
        if opcion == 1:
            self.registrar_receta()
        elif opcion == 2:
            self.buscar_receta()
        elif opcion == 3:
            self.recetas_vegetarianas()
        elif opcion == 4:
            self.recetas_veganas()
        elif opcion == 5:
            self.contador_recetas_por_etiqueta()
        elif opcion == 6:
            self.salir_app()
            return True

        return False

    def registrar_receta(self):
        print(f"\n{'REGISTRAR RECETA':=^30}")
        nombre = input("Ingrese el nombre de la receta: ")
        ingredientes = []
        print("A continuación, ingrese cada uno de los ingredientes de la receta. Cuando haya terminado, "
              "presione ENTER sin ingresar nada.")
        print("\n>> Ingrediente 1")
        ingrediente = input("Ingrese el nombre del ingrediente: ")
        while ingrediente != "":
            unidad = input(f"Ingrese la unidad de medida del ingrediente ({','.join(UnidadMedida.list())}): ")
            cantidad = float(input("Ingrese la cantidad del ingrediente: "))
            ingredientes.append((ingrediente, cantidad, UnidadMedida(unidad)))
            print("\n>> Ingrediente", len(ingredientes) + 1)
            ingrediente = input("Ingrese el nombre del ingrediente: ")
        etiquetas = input("\nIngrese las etiquetas de la receta separadas por coma: ").split(",")
        descripcion = input("\nIngrese la descripción de la receta: ")
        self.chef.registrar_receta(nombre, ingredientes, descripcion, etiquetas)
        print(f"La receta '{nombre}' ha sido registrada exitosamente.")

    def buscar_receta(self):
        print(f"\n{'BUSCAR RECETA':=^30}")
        nombre = input("Ingrese el nombre de la receta: ")
        receta = self.chef.buscar_receta(nombre)
        if receta is not None:
            print(receta)
        else:
            print(f"No se encontró ninguna receta con el nombre '{nombre}'.")

    def recetas_vegetarianas(self):
        print(f"\n{'RECETAS VEGETARIANAS':=^30}")
        vegetarianas = self.chef.recetas_vegetarianas()
        if len(vegetarianas) > 0:
            for receta in vegetarianas:
                print(receta)
        else:
            print("No hay recetas vegetarianas registradas.")

    def recetas_veganas(self):
        print(f"\n{'RECETAS VEGANAS':=^30}")
        veganas = self.chef.recetas_veganas()
        if len(veganas) > 0:
            for receta in veganas:
                print(receta)
        else:
            print("No hay recetas veganas registradas.")

    def contador_recetas_por_etiqueta(self):
        print(f"\n{'CONTADOR DE RECETAS POR ETIQUETA':=^30}")
        contador = self.chef.contador_recetas_por_etiqueta()
        for etiqueta, cantidad in contador.items():
            print(f"- {etiqueta}: {cantidad}")

    @staticmethod
    def salir_app():
        print("======================")
        print("=== FIN DE PROGRAMA ===")
        print("======================")
