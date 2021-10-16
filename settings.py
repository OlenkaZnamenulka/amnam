class Settings:
    ledenec_limit: int

    # Класс для хранения всех настроек игры.
    def __init__(self):
        # Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 400
        self.screen_height = 400
        self.bg_color = (254, 255, 198)
        self.amnik_speed = 0.1 # скорость амняма
        self.pauk_speed = 0.1  # начальная скорость паука
        self.pauk_speed_step = 0.01  # шаг увеличение скорости паука при попадании леденцом
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        # параметры леденца
        self.ledenec_speed = 0.25

        # переменная разрешенного количества одновременных леденцов
        self.ledenec_allowed = 1
        # переменная общего количества леденцов
        self.ledenec_limit = 30

