# Snake Game

Este es un juego clásico de la serpiente desarrollado en Python utilizando la biblioteca Pygame. El objetivo del juego es comer la mayor cantidad de manzanas posible sin chocar con los obstáculos ni contigo mismo.

## Funcionalidades

- Control de la serpiente con las teclas de dirección (⬆, ⬇, ⬅, ➡).
- Generación aleatoria de obstáculos.
- Pantalla de Game Over con opción para reiniciar o salir.
- Menú principal con opciones para jugar, ver instrucciones y salir.
- Pantalla de instrucciones con las reglas del juego.

## Requisitos

- Python 3.x
- Pygame

## Instalación

1. Clona el repositorio en tu máquina local:
    ```bash
    git clone https://github.com/daceron96/snake_game.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd snake_game
    ```
3. Crea un entorno virtual:
    ```bash
    python -m venv venv
    ```
4. Activa el entorno virtual:
    - En Windows:
        ```bash
        venv\Scripts\activate
        ```
    - En macOS y Linux:
        ```bash
        source venv/bin/activate
        ```
5. Instala las dependencias desde el archivo [requirements.txt](http://_vscodecontentref_/1):
    ```bash
    pip install -r requirements.txt
    ```

## Ejecución

1. Asegúrate de que el entorno virtual esté activado.
2. Ejecuta el archivo [`main.py`](main.py ) para iniciar el juego:
    ```bash
    python main.py
    ```

## Controles

- ⬆ Arriba: Mover hacia arriba
- ⬇ Abajo: Mover hacia abajo
- ⬅ Izquierda: Mover hacia la izquierda
- ➡ Derecha: Mover hacia la derecha

## Reglas

- No choques contigo mismo.
- No choques con los obstáculos.
- Si sales por un borde, apareces en el otro lado.

## Pantalla de Game Over

- Presiona `R` para reiniciar el juego y volver al menú.
- Presiona `Q` para salir del juego.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que desees realizar.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.