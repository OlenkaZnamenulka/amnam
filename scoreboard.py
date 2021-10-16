import pygame.font


class Scoreboard:
    # """Класс для вывода игровой информации."""
    def __init__(self, am_game):
        """Инициализирует атрибуты подсчета очков."""
        self.screen = am_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = am_game.settings
        self.stats = am_game.stats
        self.input = am_game.input
        # Настройки шрифта для вывода счета.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 25)
        # Подготовка исходного изображения.
        self.prep_score()

    def prep_score(self):
        """Преобразует Имя графическое изображение"""
        name_str = str("Имя: ")
        name_str += str(self.input.input_name)
        self.name_image = self.font.render(name_str, True,
                                           self.text_color, self.settings.bg_color)
        # Вывод счета в левом верхней части экрана.
        self.name_rect = self.name_image.get_rect()
        self.name_rect.left = self.name_rect.left + 20
        self.name_rect.top = 220
        self.screen.blit(self.name_image, self.name_rect)

        """Преобразует текущий счет в графическое изображение."""
        score_str = str("Счет = ")
        score_str += str(self.stats.game_score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.settings.bg_color)
        # Вывод счета в левом верхней части экрана.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 200

        """Преобразует остаток леденцов в графическое изображение"""
        ledenec_str = str("Леденцов = ")
        ledenec_str += str(self.stats.ledenec_shot)
        self.ledenec_image = self.font.render(ledenec_str, True,
                                              self.text_color, self.settings.bg_color)
        # Вывод счета в левом верхней части экрана.
        self.ledenec_rect = self.score_image.get_rect()
        self.ledenec_rect.right = self.screen_rect.right - 80
        self.ledenec_rect.top = 200

    def show_score(self):
        """Выводит счет на экран."""
        self.prep_score()
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.ledenec_image, self.ledenec_rect)
