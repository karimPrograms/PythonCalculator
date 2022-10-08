import pygame


class Button:

    def __init__(self, text, width, height, pos, elevation, surface, font):
        # general attributes:
        self.clicked = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]
        self.surface = surface

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = '#354B5E'

        # text
        self.text_surf = font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    # drawing the button
    def draw(self):
        self.selected_button = False
        # elevation
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(self.surface, self.bottom_color, self.bottom_rect, border_radius=5)
        pygame.draw.rect(self.surface, self.top_color, self.top_rect, border_radius=5)
        self.surface.blit(self.text_surf, self.text_rect)
        self.selected_button = self.check_click()

        return self.selected_button

    # checking if the button is pressed
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#334252'
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.dynamic_elevation = 0
                self.clicked = True
                # your code
                self.selected_button = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.dynamic_elevation = self.elevation
                self.clicked = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#475F77'

        return self.selected_button
