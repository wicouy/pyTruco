class Carta:
    # Palos y valores específicos de la baraja española para el truco uruguayo
    PALOS = ['Espada', 'Basto', 'Oro', 'Copa']
    VALORES = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]  # Excluye 8 y 9

    # Jerarquía base para el truco 
    JERARQUIA_BASE = {
        (1, 'Espada'): 14,  # Espadilla
        (1, 'Basto'): 13,   # Bastillo
        (7, 'Espada'): 12,
        (7, 'Oro'): 11,
        (3, 'Espada'): 10,
        (3, 'Basto'): 10,
        (3, 'Oro'): 10,
        (3, 'Copa'): 10,
        (2, 'Espada'): 9,
        (2, 'Basto'): 9,
        (2, 'Oro'): 9,
        (2, 'Copa'): 9,
        (1, 'Oro'): 8,
        (1, 'Copa'): 8,
        (12, 'Espada'): 7,
        (12, 'Basto'): 7,
        (12, 'Oro'): 7,
        (12, 'Copa'): 7,
        (11, 'Espada'): 6,
        (11, 'Basto'): 6,
        (11, 'Oro'): 6,
        (11, 'Copa'): 6,
        (10, 'Espada'): 5,
        (10, 'Basto'): 5,
        (10, 'Oro'): 5,
        (10, 'Copa'): 5,
        (7, 'Basto'): 4,
        (7, 'Copa'): 4,
        (6, 'Espada'): 3,
        (6, 'Basto'): 3,
        (6, 'Oro'): 3,
        (6, 'Copa'): 3,
        (5, 'Espada'): 2,
        (5, 'Basto'): 2,
        (5, 'Oro'): 2,
        (5, 'Copa'): 2,
        (4, 'Espada'): 1,
        (4, 'Basto'): 1,
        (4, 'Oro'): 1,
        (4, 'Copa'): 1,
    }

    # Palo de la muestra para la ronda actual
    palo_muestra = None

    @classmethod
    def definir_muestra(cls, carta_muestra):
        """Define el palo de la muestra para la ronda actual."""
        cls.palo_muestra = carta_muestra.palo

    def __init__(self, valor, palo):
        if palo not in self.PALOS or valor not in self.VALORES:
            raise ValueError("La carta no es válida.")
        self.valor = valor
        self.palo = palo
        # Propiedad booleana que indica si la carta es del palo de la muestra
        self.is_muestra = self.palo == self.palo_muestra

    def __repr__(self):
        return f"{self.valor} de {self.palo}"

    def actualizar_muestra(self):
        """Actualiza la propiedad `is_muestra` si el palo de la muestra cambia."""
        self.is_muestra = self.palo == self.palo_muestra

    def obtener_jerarquia(self):
        """Devuelve la jerarquía de la carta, considerando la muestra."""
        # Verificar si la carta es del palo de la muestra y asignarle una mayor jerarquía si es el caso
        if self.is_muestra and (self.valor, self.palo) not in self.JERARQUIA_BASE:
            return 15  # Asignar una jerarquía alta por ser del palo de la muestra
        # Si no es del palo de la muestra, devolver la jerarquía base
        return self.JERARQUIA_BASE.get((self.valor, self.palo), 0)

    def es_mayor_que(self, otra_carta):
        """Compara la carta actual con otra carta en base a la jerarquía del truco uruguayo."""
        return self.obtener_jerarquia() > otra_carta.obtener_jerarquia()
