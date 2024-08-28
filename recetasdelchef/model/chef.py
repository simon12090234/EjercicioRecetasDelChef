from enum import Enum


class UnidadMedida(Enum):
    GRAMOS = "gramos"
    LITROS = "litros"
    TAZAS = "tazas"
    Cucharadas = "cucharadas"
    Piezas = "piezas"


class Ingrediente:
    def __init__(self, alimento: str, cantidad: float, unidad: UnidadMedida):
        self.alimento: str = alimento
        self.cantidad: float = cantidad
        self.unidad: UnidadMedida = unidad

    def __str__(self) -> str:
        return f"{self.cantidad} {self.unidad.value} de {self.alimento}"


class Receta:

    def __init__(self, nombre: str, descripcion: str, etiquetas: None):
        if etiquetas is None:
            etiquetas = []
        self.nombre: str = nombre
        self.ingredientes = []
        self.descripcion: str = descripcion
        self.etiquetas: [str] = etiquetas

    def agregar_ingrediente(self, alimento: str, cantidad: float, unidad: UnidadMedida):
        ingrediente = Ingrediente(alimento, cantidad, unidad)
        self.ingredientes.append(ingrediente)

    def __str__(self) -> str:
        ingredientes_str = "\n".join(str(ingrediente) for ingrediente in self.ingredientes)
        return f"Receta: {self.nombre} \n\n Ingredientes: {ingredientes_str} \n\n Descripcion: {self.descripcion}"


class Chef:
    def __init__(self):
        self.recetas: list[Receta] = []

    def registrar_receta(self, nombre: str, ingredientes: [tuple[str, float, UnidadMedida]], descripcion: str,
                         etiquetas: None):
        receta = Receta(nombre, descripcion, etiquetas)
        for ingrediente in ingredientes:
            receta.agregar_ingrediente(ingrediente[0], ingrediente[1], ingrediente[0])
        self.recetas.append(receta)

    def buscar_receta (self, nombre:str) -> Receta|None:
        for receta in self.recetas:
            if nombre.lower() in receta.nombre.lower():
                return receta
            else:
                return None

    def recetas_vegetarianas (self) -> list[Receta]:
        vegetarianas: list[Receta] = []
        for receta in self.recetas:
            if "vegetariano" in receta.etiquetas:
                vegetarianas.append(receta)
        return vegetarianas

    def recetas_veganas (self) -> list[Receta]:
        veganas: list[Receta] = []
        for receta in self.recetas:
            if "veganoo" in receta.etiquetas:
                veganas.append(receta)
        return veganas

    def contador_recetas_por_etiqueta (self) -> dict[str:int]:
        contador: dict[str,int] = {}
        for receta in self.recetas:
            for etiqueta in receta.etiquetas:
                if etiqueta not in contador.keys():
                    contador[etiqueta] = 1
                else:
                    contador[etiqueta] += 1
        return contador





