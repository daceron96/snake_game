import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 40)  
        self.button_width = 200
        self.button_height = 50
        self.button_spacing = 20  
        self.button_color = (50, 150, 250)
        self.hover_color = (30, 120, 220)
        self.text_color = (255, 255, 255)
        
        screen_width, screen_height = screen.get_size()
        center_x = (screen_width - self.button_width) // 2
        start_y = (screen_height - (4 * self.button_height + 3 * self.button_spacing)) // 2

        self.buttons = [
            {"text": "Jugar", "rect": pygame.Rect(center_x, start_y, self.button_width, self.button_height), "hover": False},
            {"text": "Instrucciones", "rect": pygame.Rect(center_x, start_y + (self.button_height + self.button_spacing), self.button_width, self.button_height), "hover": False},
            {"text": "Salir", "rect": pygame.Rect(center_x, start_y + 2 * (self.button_height + self.button_spacing), self.button_width, self.button_height), "hover": False},
        ]

    def draw(self):
        """Dibuja el menú con hover funcional"""
        self.screen.fill((30, 30, 30))  

        mouse_pos = pygame.mouse.get_pos()
        cursor_on_button = False  

        for button in self.buttons:
            if button["rect"].collidepoint(mouse_pos):  
                button["hover"] = True
                cursor_on_button = True
            else:
                button["hover"] = False

            color = self.hover_color if button["hover"] else self.button_color
            pygame.draw.rect(self.screen, color, button["rect"], border_radius=8)
            
            text_surface = self.font.render(button["text"], True, self.text_color)
            text_rect = text_surface.get_rect(center=button["rect"].center)
            self.screen.blit(text_surface, text_rect)

        if cursor_on_button:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def handle_events(self, event):
        """Detecta clics en los botones"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for button in self.buttons:
                if button["rect"].collidepoint(mouse_pos):
                    return button["text"]  

        return None
