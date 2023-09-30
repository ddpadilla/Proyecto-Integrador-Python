from functools import reduce
import readchar
import os
import time

class Juego:
    def __init__(self, mapa_str, posicion_inicial, posicion_final):
        self.mapa = convertir_mapa(mapa_str)
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final

    def limpiar_pantalla(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def main_loop(self):
        px, py = self.posicion_inicial
        self.mapa[px][py] = "P"  # Inicializar la posición del jugador

        while (px, py) != self.posicion_final:
            self.limpiar_pantalla()
            self.mostrar_mapa()
            
            tecla = readchar.readkey()
            nueva_px, nueva_py = px, py

            if tecla == readchar.key.RIGHT:
                nueva_py += 1
            elif tecla == readchar.key.LEFT:
                nueva_py -= 1
            elif tecla == readchar.key.DOWN:
                nueva_px += 1
            elif tecla == readchar.key.UP:
                nueva_px -= 1

            if (
                0 <= nueva_px < len(self.mapa) and
                0 <= nueva_py < len(self.mapa[0]) and
                self.mapa[nueva_px][nueva_py] != "#"
            ):
                self.mapa[px][py] = "."
                px, py = nueva_px, nueva_py
                self.mapa[px][py] = "P"

                if (px, py) == self.posicion_final:
                    print(" \n"
                        "Felicidades, Ganaste!")
                    break

    def mostrar_mapa(self):
        for fila in self.mapa:
            print("".join(fila))

def convertir_mapa(mapa_str):
    filas = mapa_str.strip().split("\n")
    matriz = list(map(list, filas))
    return matriz

class JuegoArchivo(Juego):
    def __init__(self, mapa_archivo):
        with open("mapa.txt", "r") as archivo:
            lineas = archivo.readlines()
            mapa_str = reduce(lambda x, y: x+y, lineas)
            super().__init__(mapa_str, posicion_inicial, posicion_final)

if __name__ == "__main__":
    print("Bienvenido al juego Laberinto")
    print("--------------------------------")
    nombre = input("Ingrese su nombre: ")
    print(f"Bienvenido {nombre} al juego, cargando laberinto...")
    time.sleep(3)

    # Crear una instancia de JuegoArchivo y ejecutar el juego
    nombre_archivo_mapa = "mapa.txt"
    posicion_inicial = (0, 0)
    posicion_final = (10, 9)
    juego = JuegoArchivo(nombre_archivo_mapa)
    juego.main_loop()



