import pygame
import random

BLOCK_SIZE = 20  # Tamaño base de un bloque

class Obstacle:
    def __init__(self, screen_width, screen_height, count=5):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.obstacles = self.generate_obstacles(count)

    def generate_obstacles(self, count):
        """Genera líneas rectas como obstáculos en direcciones horizontales o verticales."""
        obstacles = []
        for _ in range(count):
            length = random.randint(2, 5)  # Largo de la línea (3 a 7 bloques)
            direction = random.choice(["H", "V"])  # Horizontal o Vertical
            
            if direction == "H":
                # Generar una línea horizontal
                x = random.randint(0, (self.screen_width // BLOCK_SIZE) - length) * BLOCK_SIZE
                y = random.randint(0, (self.screen_height // BLOCK_SIZE) - 1) * BLOCK_SIZE
                obstacle = [(x + i * BLOCK_SIZE, y) for i in range(length)]
            else:
                # Generar una línea vertical
                x = random.randint(0, (self.screen_width // BLOCK_SIZE) - 1) * BLOCK_SIZE
                y = random.randint(0, (self.screen_height // BLOCK_SIZE) - length) * BLOCK_SIZE
                obstacle = [(x, y + i * BLOCK_SIZE) for i in range(length)]

            obstacles.append(obstacle)

        return obstacles

    def draw(self, screen, color=(139, 69, 19)):  # Color marrón
        """Dibuja los obstáculos en la pantalla."""
        for obstacle in self.obstacles:
            for block in obstacle:
                pygame.draw.rect(screen, color, (*block, BLOCK_SIZE, BLOCK_SIZE))
