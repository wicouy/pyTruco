from modulos.jugadores import Jugador
from modulos.partida import Partida

class JuegoTruco:
    def __init__(self, jugador1, jugador2, frases):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.frases = frases
        self.partida = Partida()  # Instancia de la clase Partida básica

    def finalizada(self):
        """
        Verifica si la partida ha terminado.
        Aquí puedes definir el puntaje necesario para ganar el juego.
        """
        return self.jugador1.puntos >= 30 or self.jugador2.puntos >= 30

    def jugar_ronda(self):
        """
        Lógica para jugar una ronda.
        Incluye turnos y el uso de frases de cantos según la jugada.
        """
        print("Comienza una nueva ronda...")
        # Aquí añadirías la lógica de una ronda específica del truco.
        # Ejemplo: seleccionar cartas, cantar truco, etc.

        # Ejemplo de uso de una frase al azar de envido
        print(self.frases.get("envido", [""])[0])  # Puedes añadir lógica para seleccionar una frase aleatoria.

    def mostrar_ganador(self):
        """
        Muestra el jugador con el puntaje más alto como ganador.
        """
        if self.jugador1.puntos > self.jugador2.puntos:
            print(f"¡{self.jugador1.nombre} es el ganador con {self.jugador1.puntos} puntos!")
        elif self.jugador2.puntos > self.jugador1.puntos:
            print(f"¡{self.jugador2.nombre} es el ganador con {self.jugador2.puntos} puntos!")
        else:
            print("La partida terminó en empate.")
