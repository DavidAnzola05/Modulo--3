class GuerreroDAAC:
    def __init__(self, raza, arma, elemento, vida, ataque, defensa):
        self.raza = raza
        self.arma = arma
        self.elemento = elemento
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def __str__(self):
        return f"GuerreroDAAC(raza={self.raza}, arma={self.arma}, elemento={self.elemento}, vida={self.vida}, ataque={self.ataque}, defensa={self.defensa})"


class CreadorGuerrerosDAAC:
    categorias = {
        "raza": {
            "Humano": {"vida": 10, "ataque": 5, "defensa": 5},
            "Elfo": {"vida": 7, "ataque": 8, "defensa": 4},
            "Orco": {"vida": 14, "ataque": 7, "defensa": 3}
        },
        "arma": {
            "Espada": {"ataque": 5},
            "Arco": {"ataque": 3},
            "Hacha": {"ataque": 7}
        },
        "elemento": {
            "Fuego": {"ataque": 4},
            "Hielo": {"defensa": 4},
            "Trueno": {"ataque": 2, "defensa": 1}
        }
    }

    def elegir_opcion(self, categoria):
        print(f"\nElige {categoria}:")
        opciones = list(self.categorias[categoria].keys())
        for i, v in enumerate(opciones, 1):
            print(f"{i}. {v}")
        eleccion = int(input("Opción: ")) - 1
        return opciones[eleccion]

    def crear_guerrero(self):
        raza = self.elegir_opcion("raza")
        arma = self.elegir_opcion("arma")
        elemento = self.elegir_opcion("elemento")

        stats = {"vida": 0, "ataque": 0, "defensa": 0}

        for k, v in self.categorias["raza"][raza].items():
            stats[k] += v
        for k, v in self.categorias["arma"][arma].items():
            stats[k] += v
        for k, v in self.categorias["elemento"][elemento].items():
            stats[k] += v

        return GuerreroDAAC(raza, arma, elemento, stats["vida"], stats["ataque"], stats["defensa"])


def menuDAAC():
    creador = CreadorGuerrerosDAAC()
    while True:
        print("\n=== CREA TU GUERRERO DAAC ===")
        print("1. Crear guerrero")
        print("2. Salir")
        op = input("Opción: ")

        if op == "1":
            g = creador.crear_guerrero()
            print("\n=== GUERRERO CREADO ===")
            print(g)
        elif op == "2":
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menuDAAC()
