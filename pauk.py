import pygame


class Pauk:
    # Класс для управления пауком.
    def __init__(self, am_game):
        # Инициализирует паука задает его начальную позицию."""
        self.screen = am_game.screen
        self.settings = am_game.settings
        self.stats = am_game.stats
        self.screen_rect = am_game.screen.get_rect()
        # Загружает изображение амняма и получает прямоугольник.
        self.image = pygame.image.load('images/pauk.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый амням появляется у нижнего края экрана.
        self.rect.topleft = self.screen_rect.topleft
        self.x = float(self.rect.x)
        self.moving = False

    def update(self):
        # Перемещает паука влево или вправо."""

        if not self.moving:
            if self.rect.right < self.screen_rect.right:
                self.x += self.stats.pauk_speed_run
            else:
                self.moving = True
        else:
            if self.moving:
                if self.rect.left > 0:
                    self.x -= self.stats.pauk_speed_run
                else:
                    self.moving = False
            else:
                self.moving = False

        self.rect.x = self.x

    def blitme(self):
        # Рисует амняма в текущей позиции.
        self.screen.blit(self.image, self.rect)
