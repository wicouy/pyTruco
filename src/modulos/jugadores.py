from modulos.cartas import Carta

class Jugador:
    MAX_CARTAS = 3  # Máximo de cartas permitido en la mano

    def __init__(self, nombre):
        self.nombre = nombre  # Identificador del jugador
        self._mano = []  # Lista privada de cartas en la mano del jugador
        self.puntos = 0  # Puntos acumulados por el jugador

    def __repr__(self):
        return f"Jugador {self.nombre} con {self.puntos} puntos y {len(self._mano)} cartas."

    @property
    def mano(self):
        """Propiedad de solo lectura para acceder a las cartas del jugador."""
        return self._mano.copy()

    def recibir_cartas(self, cartas):
        """
        Recibe una lista de cartas para añadir a la mano del jugador.
        Solo se agregarán las cartas que no excedan el límite de 3.
        
        Args:
            cartas (list de Carta): Lista de cartas a recibir.

        Returns:
            list de Carta: Lista de cartas que no pudieron ser agregadas.
        """
        cartas_agregadas = []
        cartas_no_agregadas = []

        for carta in cartas:
            if len(self._mano) < self.MAX_CARTAS:
                self._mano.append(carta)
                cartas_agregadas.append(carta)
            else:
                cartas_no_agregadas.append(carta)

        if cartas_no_agregadas:
            print(f"Advertencia: {self.nombre} no puede recibir más de {self.MAX_CARTAS} cartas.")
        
        return cartas_no_agregadas

    def jugar_carta(self, indice):
        """
        Juega una carta desde la mano y la elimina de la lista.

        Args:
            indice (int): Índice de la carta a jugar.

        Returns:
            Carta: La carta jugada.

        Raises:
            ValueError: Si el índice no es válido.
        """
        if 0 <= indice < len(self._mano):
            carta_jugada = self._mano.pop(indice)
            print(f"{self.nombre} juega: {carta_jugada}")
            return carta_jugada
        raise ValueError("Índice de carta no válido.")

    def mostrar_mano(self):
        """
        Devuelve una representación de la mano del jugador.

        Returns:
            list de str: Representación de las cartas en la mano.
        """
        return [str(carta) for carta in self._mano]

    def sumar_puntos(self, puntos):
        """
        Suma puntos al total del jugador.

        Args:
            puntos (int): Puntos a sumar.
        """
        self.puntos += puntos
        print(f"{self.nombre} suma {puntos} puntos. Total: {self.puntos} puntos.")

    def reiniciar_mano(self):
        """
        Vacia la mano del jugador para una nueva ronda.
        """
        self._mano = []
        print(f"{self.nombre} ha reiniciado su mano.")

    def tiene_cartas(self):
        """
        Devuelve True si el jugador aún tiene cartas en la mano.

        Returns:
            bool: True si tiene cartas, False de lo contrario.
        """
        return bool(self._mano)
