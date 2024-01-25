from recetasdelchef.model.chef import Chef
from recetasdelchef.view.ui_consola import Consola

if __name__ == "__main__":
    chef = Chef()
    app = Consola(chef)
    app.ciclo_app()
