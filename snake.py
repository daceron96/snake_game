import pygame

# Tamaño de la serpiente y velocidad
BLOCK_SIZE = 20  

class Snake:
    def __init__(self, x, y, screen_width, screen_height):
        self.body = [(x, y)]  
        self.direction = "RIGHT"  
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.growing = False

    def move(self):
        if len(self.body) == 0:
            return  

        head_x, head_y = self.body[0]

        if self.direction == "UP":
            head_y -= BLOCK_SIZE
        elif self.direction == "DOWN":
            head_y += BLOCK_SIZE
        elif self.direction == "LEFT":
            head_x -= BLOCK_SIZE
        elif self.direction == "RIGHT":
            head_x += BLOCK_SIZE

        head_x %= self.screen_width
        head_y %= self.screen_height

        self.body.insert(0, (head_x, head_y))

        if not self.growing:
            self.body.pop()
        else:
            self.growing = False  

    def change_direction(self, new_direction):
        """Evita que la serpiente se mueva en la dirección opuesta directamente."""
        opposite_directions = {
            "UP": "DOWN",
            "DOWN": "UP",
            "LEFT": "RIGHT",
            "RIGHT": "LEFT"
        }

        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction

    def draw(self, screen, color=(0, 255, 0)):
        """Dibujar la serpiente en la pantalla."""
        for segment in self.body:
            pygame.draw.rect(screen, color, (*segment, BLOCK_SIZE, BLOCK_SIZE))

    def grow(self):
        """Activa el crecimiento para el próximo movimiento."""
        self.growing = True