import pygame


class InputName:
    def __init__(self, am_game):
        self.screen = am_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = am_game.settings
        # Настройки шрифта для вывода имени.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 25)

        """Инициализирует атрибуты ввода."""
        self.input_name = ""
        self.print_rating = ""

    def _print_text(self):
        # надпись рейтинг топ 3
        rating_str1 = str("Рейтинг ТОП 3:")
        self.name_image_top3 = self.font.render(rating_str1, True,
                                                self.text_color, self.settings.bg_color)
        self.name_rect_top3 = self.name_image_top3.get_rect()
        self.name_rect_top3.left = self.name_rect_top3.left
        self.name_rect_top3.top = 50
        self.screen.blit(self.name_image_top3, self.name_rect_top3)

        #  вывод рейтинга топ 3
        rating_str2 = str(
            f"1: {self.print_rating[0]} = {self.print_rating[1]}, 2: {self.print_rating[2]} = {self.print_rating[3]}, "
            f"3: {self.print_rating[4]} = {self.print_rating[5]}")
        self.name_image_rating = self.font.render(rating_str2, True,
                                                  self.text_color, self.settings.bg_color)
        self.name_rect_rating = self.name_image_rating.get_rect()
        self.name_rect_rating.left = self.name_rect_rating.left
        self.name_rect_rating.top = 80
        self.screen.blit(self.name_image_rating, self.name_rect_rating)

        # вывод надписи
        name_str = str("Введите ваше имя и нажмите Play:  ")
        name_str += str(self.input_name)
        self.name_image = self.font.render(name_str, True,
                                           self.text_color, self.settings.bg_color)
        # Вывод счета в левом верхней части экрана.
        self.name_rect = self.name_image.get_rect()
        self.name_rect.left = self.name_rect.left
        self.name_rect.top = 300
        self.screen.blit(self.name_image, self.name_rect)
