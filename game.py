import pygame
import sys
import time

from config import WINDOW_HEIGHT, WINDOW_WIDTH, BACKGROUND_COLOR
from snake import Snake
from food import Food
from obstacle import Obstacle
from menu import Menu

BLOCK_SIZE = 20  

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.menu_active = True
        self.state = "menu" 

        self.menu = Menu(self.screen)
        self.snake = Snake(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.food = Food(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.obstacles = Obstacle(WINDOW_WIDTH, WINDOW_HEIGHT, count=5)
        self.font = pygame.font.Font(None, 80)

    def handle_events(self):
        """Maneja los eventos del teclado."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event.key)
    
    def check_food_collision(self):
        """Verifica si la serpiente ha comido la comida."""
        if self.snake.body[0] == self.food.position and self.food.visible:
            self.snake.grow()
            self.food.visible = False
            self.food.last_eaten_time = pygame.time.get_ticks()

    def handle_keydown(self, key):
        """Cambia la dirección de la serpiente según la tecla presionada."""
        directions = {
            pygame.K_UP: "UP",
            pygame.K_DOWN: "DOWN",
            pygame.K_LEFT: "LEFT",
            pygame.K_RIGHT: "RIGHT"
        }
        if key in directions:
            self.snake.change_direction(directions[key])


    def update(self):
        """Actualiza la lógica del juego."""
        self.snake.move()
        self.check_food_collision()

        for obstacle in self.obstacles.obstacles:
            if self.snake.body[0] in obstacle:
                print("¡Game Over! La serpiente chocó con un obstáculo.")
                self.show_game_over()

        self.food.update()

        self.screen.fill(BACKGROUND_COLOR)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.obstacles.draw(self.screen) 
        pygame.display.flip()
    
    def show_game_over(self):
        """Muestra la pantalla de Game Over y espera una acción del jugador."""
        font = pygame.font.Font(None, 50)
        
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        restart_text = font.render("Presiona R para reiniciar o Q para salir", True, (255, 255, 255))

        # Obtener dimensiones del texto para centrarlo
        game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
        restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20))

        self.screen.fill((0, 0, 0))  # Fondo negro
        self.screen.blit(game_over_text, game_over_rect.topleft)
        self.screen.blit(restart_text, restart_rect.topleft)

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Reiniciar
                        self.__init__()  # Reinicia el juego
                        self.start()
                        waiting = False
                    elif event.key == pygame.K_q:  # Salir
                        pygame.quit()
                    sys.exit()

    def start(self):
        """Maneja el menú antes de iniciar el juego."""
        while self.state == "menu":
            self.handle_menu()

        if self.state == "game":
            self.run_game()
        
        if self.state == "instructions":
            self.show_instructions()


    def handle_menu(self):
        """Dibuja el menú y maneja los eventos del usuario."""
        self.menu.draw()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                option = self.menu.handle_events(event)
                if option == "Jugar":
                    # self.menu_active = False  # Oculta el menú y empieza el juego
                    self.state = "game"
                if option == "Instrucciones":
                    # self.menu_active = False
                    self.state = "instructions"
                elif option == "Salir":
                    pygame.quit()
                    sys.exit()

    def run_game(self):
        """Bucle principal del juego."""
        self.countdown()

        while self.running:
            self.handle_events()
            self.update()
            self.clock.tick(8)  # Controla la velocidad del juego

        pygame.quit()
        sys.exit()

    def show_instructions(self):
        """Muestra la pantalla de instrucciones."""
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        instructions = [
            "Objetivo: Come la mayor cantidad de manzanas.",
            "Controles:",
            "⬆ Arriba - ⬇ Abajo - ⬅ Izquierda - ➡ Derecha",
            "Reglas:",
            "- No choques con los obstáculos.",
            "- Si sales por un borde, apareces en el otro lado.",
            "Presiona cualquier tecla para volver al menú.",
        ]

        y_offset = 100
        for line in instructions:
            text = font.render(line, True, (255, 255, 255))
            self.screen.blit(text, (50, y_offset))
            y_offset += 40

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False
                    self.state = "menu"
                    self.start()

    def countdown(self):
        """Muestra la cuenta regresiva antes de iniciar el juego."""
        for num in ["3", "2", "1", "Start!"]:
            self.screen.fill(BACKGROUND_COLOR)
            text = self.font.render(num, True, (255, 255, 255))
            text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            self.screen.blit(text, text_rect)
            pygame.display.flip()
            time.sleep(1)

