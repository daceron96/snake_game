import pygame
import random

BLOCK_SIZE = 20  # Tamaño de la comida
RESPAWN_TIME = 2000  # Tiempo en milisegundos (1 segundo)

class Food:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.position = self.generate_position()
        self.visible = True  # Indica si la comida es visible
        self.last_eaten_time = None

    def generate_position(self):
        """Genera una posición aleatoria alineada a la cuadrícula de la serpiente."""
        x = random.randint(0, (self.screen_width // BLOCK_SIZE) - 1) * BLOCK_SIZE
        y = random.randint(0, (self.screen_height // BLOCK_SIZE) - 1) * BLOCK_SIZE
        return (x, y)

    def update(self):
        """Verifica si ha pasado suficiente tiempo para reaparecer."""
        if not self.visible and pygame.time.get_ticks() - self.last_eaten_time >= RESPAWN_TIME:
            self.position = self.generate_position()
            self.visible = True

    def draw(self, screen, color=(255, 0, 0)):
        """Dibuja la comida si es visible."""
        if self.visible:
            pygame.draw.rect(screen, color, (*self.position, BLOCK_SIZE, BLOCK_SIZE))
