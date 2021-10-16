import pygame
from pygame.sprite import Sprite


class Ledenec(Sprite):
    # Класс для управления леденцом.
    def __init__(self, am_game):
        # Инициализирует леденец задает его начальную позицию."""
        super().__init__()
        self.screen = am_game.screen
        self.settings = am_game.settings
        self.screen_rect = am_game.screen.get_rect()
        # Загружает изображение леденца и получает прямоугольник.
        self.image = pygame.image.load('images/ledenec.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый леденец появляется у нижнего края экрана.
        self.rect.midtop = am_game.amnik.rect.midtop
        # Позиция снаряда хранится в вещественном формате.
        self.y = float(self.rect.y)

    def update(self):
        """Перемещает снаряд вверх по экрану."""
        # Обновление позиции снаряда в вещественном формате.

        self.y -= self.settings.ledenec_speed
        # Обновление позиции прямоугольника.
        self.rect.y = self.y

    def blitme(self):
        # вывод леденца на экран.
        self.screen.blit(self.image, self.rect)
