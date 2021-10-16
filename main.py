import sys

import pygame

from settings import Settings

from amnik import Amnik

from pauk import Pauk

from ledenec import Ledenec

from game_stats import GameStats

from button import Button

from scoreboard import Scoreboard

from input_name import InputName


class AmAm:
    # Класс для управления ресурсами и поведением игры.

    def __init__(self):
        # Инициализирует игру и создает игровые ресурсы.
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Ам ням ням")
        self.input = InputName(self)  # ------------------
        # Создание экземпляра для хранения игровой статистики.
        self.stats = GameStats(self)

        self.sb = Scoreboard(self)
        self.amnik = Amnik(self)
        self.pauk = Pauk(self)
        self.ledenec = Ledenec(self)
        self.ledenecs = pygame.sprite.Group()
        # Создание кнопки Play.
        self.play_button = Button(self, "Play")

    def run_game(self):

        # Запуск основного цикла игры.
        while True:
            # При каждом проходе цикла перерисовывается экран.
            self._check_events()
            if self.stats.game_active:
                self._update_ledenecs()
                self._ledenec_end()
            self._update_screen()

    def _check_events(self):
        # Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Переместить корабль вправо.
                    self.amnik.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # Переместить корабль влево.
                    self.amnik.moving_left = True
                elif event.key == pygame.K_SPACE:
                    # Если нажат пробел, то создание леденца.
                    self._fire_ledenec()
                elif not self.stats.game_active:  # если игра не активна то ввод имени
                    if event.key == pygame.K_BACKSPACE:
                        self.input.input_name = self.input.input_name[:-1]
                    else:
                        if len(self.input.input_name) < 10:
                            self.input.input_name += event.unicode

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.amnik.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.amnik.moving_left = False

    def _check_play_button(self, mouse_pos):
        # """Запускает новую игру при нажатии кнопки Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:  # статистики только если экран остановлена
            # Сброс игровой статистики и настроек.
            self.stats.reset_stats()
            self.stats.game_active = True

            # Указатель мыши скрывается.
            pygame.mouse.set_visible(False)

    def _fire_ledenec(self):
        if len(self.ledenecs) < self.settings.ledenec_allowed:  # проверка на разрешенное одномременное количество
            # леденцов
            """Создание нового леденца и включение его в группу ledenecs."""
            new_ledenec = Ledenec(self)
            self.ledenecs.add(new_ledenec)
            self.stats.ledenec_shot -= 1

    def _update_ledenecs(self):
        # Удаление леденцов, вышедших за край экрана или столнувшимися с пауком
        self.ledenecs.update()

        for ledenec in self.ledenecs.copy():
            if ledenec.rect.collidepoint(self.pauk.rect.centerx,
                                         self.pauk.rect.centery - 20):  # если точка центра координат паука входит в
                # прямоугольник леденца
                self.stats.game_score += 1  # добавление счета
                self.ledenecs.remove(ledenec)  # Удаление экземпляра леденца
                self.stats.pauk_speed_run += self.settings.pauk_speed_step  # увеличение скорости паука после поподания

            if ledenec.rect.bottom <= 0:  # если координаты нижнего края леденца <= 0
                self.ledenecs.remove(ledenec)  # Удаление экземпляра леденца

    def _ledenec_end(self):
        # процедура проверки окончания разрешенного количества леденцов и запись счета в БД

        if self.stats.ledenec_shot == 0:
            player_info_final = (self.input.input_name, self.stats.game_score)  # создание кортежа ввида(ИМЯ. Счет)
            self.stats.player_rating_save(player_info_final)  # вызов процедуры добавление имени и счета в БД
            self.stats.game_active = False
            pygame.mouse.set_visible(True)  # показать указатель мыши после завершения игры

    def _update_screen(self):
        # При каждом проходе цикла перерисовывается экран. 
        self.screen.fill(self.settings.bg_color)
        if not self.stats.game_active:
            self.input.print_rating = self.stats.player_rating_show()
            self.input._print_text()
        if self.stats.game_active:
            self.amnik.update()
            self.pauk.update()
            self.amnik.blitme()
            self.pauk.blitme()
            # Вывод информации о счете.
            self.sb.show_score()
            for ledenec in self.ledenecs.sprites():
                ledenec.blitme()

        # Кнопка Play отображается в том случае, если игра неактивна.
        if not self.stats.game_active:
            self.play_button.draw_button()
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    am = AmAm()
    am.run_game()
