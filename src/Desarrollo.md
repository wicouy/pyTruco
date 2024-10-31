# Documento de Requisitos para el Desarrollo del Juego de Truco Uruguayo en Python

## Introducción

Este documento proporciona un conjunto detallado de tareas y requisitos para que un desarrollador Junior implemente mejoras y funcionalidades en el juego de Truco Uruguayo en Python. Las tareas están diseñadas para ser simples, educativas y motivadoras, permitiendo al desarrollador ver resultados tangibles a medida que avanza.

## Objetivo del Proyecto

Mejorar la experiencia del juego de Truco Uruguayo mediante la implementación de un sistema de puntos y otras características que enriquecerán la jugabilidad y el seguimiento del progreso.

---

## 1. Clase `Carta`

### Objetivo

Representar una carta del juego, incluyendo su valor, palo y jerarquía.

### Métodos y Tareas

#### 1.1. `__init__(self, valor, palo)`

- **Tarea**:
  - Asegúrate de que el constructor valide que el valor y el palo sean válidos, y maneje errores en caso de que no lo sean.
- **Consejo**: Utiliza `if palo not in self.PALOS or valor not in self.VALORES:` para validar.
- **Propósito**: Garantizar que solo se creen cartas válidas.

#### 1.2. `obtener_jerarquia(self)`

- **Tarea**:
  - Asegúrate de que la jerarquía de la carta se calcule correctamente, considerando el palo de muestra.
- **Consejo**: Revisa el uso de `self.palo_muestra` para determinar si una carta debe tener una jerarquía superior.
- **Propósito**: Mantener la lógica del juego consistente y precisa.

#### 1.3. `definir_muestra(cls, carta_muestra)`

- **Tarea**:
  - Verifica que este método funcione correctamente al cambiar el palo de la muestra en medio de la partida.
- **Consejo**: Comprueba que cada vez que se define una nueva muestra, se actualice correctamente.
- **Propósito**: Permitir la dinámica del juego al cambiar el palo de muestra según las reglas.

---

## 2. Clase `Jugador`

### Objetivo

Gestionar la información y las acciones de cada jugador.

### Métodos y Tareas

#### 2.1. `__init__(self, nombre)`

- **Tarea**:
  - Inicializa el nombre del jugador y establece una mano vacía y puntos en 0.
- **Consejo**: Usa una lista para `self.mano` para almacenar las cartas del jugador.
- **Propósito**: Configurar el estado inicial del jugador.

#### 2.2. `recibir_cartas(self, cartas)`

- **Tarea**:
  - Implementa la lógica para recibir cartas, limitando a un máximo de 3.
- **Consejo**: Comprueba cuántas cartas ya tiene el jugador y evita que supere el límite.
- **Propósito**: Mantener las reglas del juego en cuanto a la cantidad de cartas.

#### 2.3. `jugar_carta(self, indice)`

- **Tarea**:
  - Permitir que el jugador juegue una carta de su mano, eliminándola de la lista.
- **Consejo**: Verifica que el índice proporcionado sea válido.
- **Propósito**: Facilitar la jugada de cartas durante el juego.

#### 2.4. `sumar_puntos(self, puntos)`

- **Tarea**:
  - Implementa la suma de puntos al total del jugador.
- **Consejo**: Asegúrate de que se manejen correctamente los puntos acumulados.
- **Propósito**: Actualizar el puntaje del jugador en cada ronda.

#### 2.5. `mostrar_mano(self)`

- **Tarea**:
  - Devuelve una representación visual de las cartas en la mano del jugador.
- **Consejo**: Usa un formato claro para que sea fácil de leer.
- **Propósito**: Permitir que el jugador vea qué cartas tiene.

---

## 3. Clase `Partida`

### Objetivo

Administrar el flujo de la partida, incluidos los puntos y las rondas.

### Métodos y Tareas

#### 3.1. `__init__(self, jugador1, jugador2)`

- **Tarea**:
  - Inicializa los jugadores y establece un sistema de puntos en 0 para ambos.
- **Consejo**: Define `self.puntos_jugador1` y `self.puntos_jugador2`.
- **Propósito**: Configurar el estado inicial de la partida.

#### 3.2. `asignar_puntos(self, jugada, ganador)`

- **Tarea**:
  - Implementa un método para asignar puntos según el tipo de jugada realizada.
- **Consejo**: Usa condicionales para determinar la cantidad de puntos a asignar.
- **Propósito**: Permitir que cada jugada influya en el puntaje acumulado.

#### 3.3. `verificar_ganador(self)`

- **Tarea**:
  - Define un método para verificar si un jugador ha alcanzado el puntaje para ganar la partida.
- **Consejo**: Compara los puntos actuales con `self.puntos_para_ganar`.
- **Propósito**: Finalizar la partida de forma justa cuando un jugador alcance el puntaje.

#### 3.4. `mostrar_ganador(self)`

- **Tarea**:
  - Muestra un mensaje claro que indique quién ha ganado la partida.
- **Consejo**: Usa una frase emocionante para celebrar la victoria.
- **Propósito**: Hacer que la experiencia de ganar sea satisfactoria.

---

## 4. Clase `JuegoTruco`

### Objetivo

Integrar la lógica del juego y gestionar el flujo de rondas.

### Métodos y Tareas

#### 4.1. `jugar_ronda(self)`

- **Tarea**:
  - Implementa la lógica para jugar una ronda, incluyendo las acciones de los jugadores.
- **Consejo**: Asegúrate de que se mantenga un flujo claro entre las jugadas de los jugadores.
- **Propósito**: Facilitar el desarrollo del juego en cada ronda.

#### 4.2. Mostrar Puntos Actuales Después de Cada Ronda

- **Tarea**:
  - Al final de cada ronda, imprime los puntos actuales de cada jugador.
- **Consejo**: Usa un formato claro, como: `print(f"{self.jugador1.nombre} tiene {self.jugador1.puntos} puntos.")`.
- **Propósito**: Mantener a los jugadores informados sobre su progreso durante el juego.

---

## Tareas Extras

### 1. Implementar un Registro de Jugadas

- **Descripción**: Mantener un registro de todas las jugadas realizadas durante la partida.
- **Tareas**:
  - Crea una lista `historial_jugadas` en `JuegoTruco` que almacene cada jugada y su resultado.
  - Muestra el historial al final de la partida.
- **Incentivo**: Esto permitirá a los jugadores reflexionar sobre sus decisiones durante el juego.

### 2. Agregar Mensajes Motivacionales al Inicio de Cada Ronda

- **Descripción**: Introducir frases motivacionales al comenzar cada nueva ronda.
- **Tareas**:
  - Selecciona aleatoriamente una frase de `frases.json` al inicio de `jugar_ronda`.
- **Ideas Creativas**: Usa frases que incentiven la competitividad y el disfrute del juego.

### 3. Mejorar la Estética del Juego en Consola

- **Descripción**: Hacer que el juego sea más atractivo visualmente.
- **Tareas**:
  - Implementa colores y formatos en los mensajes mostrados en la consola para distinguir entre diferentes tipos de información.
- **Incentivo**: Un diseño atractivo mantendrá a los jugadores más interesados y entusiasmados.

### 4. Incluir Opciones en el Menú

- **Descripción**: Agregar opciones para ver instrucciones y reiniciar la partida.
- **Tareas**:
  - Agrega una opción en `menu_principal` para mostrar las instrucciones del juego.
  - Permite reiniciar la partida sin cerrar el programa.
- **Propósito**: Mejorar la experiencia del usuario y la accesibilidad del juego.

---

## Conclusión

Este documento de requisitos detalla un conjunto claro de tareas que un desarrollador Junior puede seguir para implementar mejoras en el juego de Truco Uruguayo. Cada tarea está diseñada para ser accesible y educativa, brindando oportunidades para aprender y aplicar nuevas habilidades en Python. Se alienta al desarrollador a explorar cada tarea, usar su creatividad y avanzar en la implementación del juego, disfrutando del proceso de desarrollo.

---
