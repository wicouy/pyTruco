import json
from modulos.jugadores import Jugador
from modulos.core import JuegoTruco

# Cargar frases de cantos desde el archivo JSON
def cargar_frases():
    try:
        with open("extras/frases.json", "r", encoding="utf-8") as file:
            frases = json.load(file)
        print("Frases de cantos cargadas con éxito.")
        return frases
    except FileNotFoundError:
        print("Error: No se encontró el archivo de frases.")
        return {}
    except json.JSONDecodeError:
        print("Error al leer el archivo de frases.")
        return {}
    
# Menú principal
def menu_principal():
    while True:
        print("\n=== Menú Principal ===")
        print("i - Iniciar Partida")
        print("s - Salir")
        
        opcion = input("Seleccione una opción: ").strip().lower()
        
        if opcion == 'i':
            iniciar_juego()
        elif opcion == 's':
            print("Gracias por jugar al Truco Uruguayo. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Inicializar el juego
def iniciar_juego():
    print("\n=== Iniciando Partida de Truco Uruguayo ===")
    
    # Cargar frases de cantos
    frases = cargar_frases()
    
    # Crear jugadores
    jugador1 = Jugador("Juan")
    jugador2 = Jugador("Pedro")
    
    # Crear juego de truco
    juego = JuegoTruco(jugador1, jugador2, frases)
    
    # Iniciar la partida
    while not juego.finalizada():
        juego.jugar_ronda()
        
        # Opción para salir de la partida
        if input("Escriba 'salir' para terminar la partida o presione Enter para continuar: ").strip().lower() == 'salir':
            print("Partida finalizada antes de tiempo.")
            return

    # Mostrar el ganador
    juego.mostrar_ganador()

# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()
