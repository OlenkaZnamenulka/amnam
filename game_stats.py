import sqlite3

# создание базы данных SQLlite
conn = sqlite3.connect('players_rating.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS players_rating(
    playername TEXT,
    playerscore INT);
    """)
conn.commit()


class GameStats:
    # """Отслеживание статистики для игры Alien Invasion."""
    def __init__(self, am_game):
        """Инициализирует статистику."""
        self.settings = am_game.settings
        self.reset_stats()
        # Игра Alien Invasion запускается в неактивном состоянии.
        self.game_active = False

    def reset_stats(self):
        # """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ledenec_shot = self.settings.ledenec_limit
        self.game_score = 0
        self.pauk_speed_run = self.settings.pauk_speed  # сброс скорости паука

    def player_rating_save(self, player_info):
        # -----------------------------
        cur.execute("INSERT INTO players_rating VALUES(?, ?);", player_info)
        conn.commit()

    def player_rating_show(self):
        # запрос рейтинга играков с сортировкой по убыванию очков
        cur.execute("SELECT * from players_rating ORDER BY playerscore DESC ")
        self.results = cur.fetchmany(3)  # лимит выборки 3 игрока
        self.results1 = self.unpack(self.results)
        return self.results1

    def unpack(self, vvod_list):
        result_list = []

        for i in vvod_list:
            if type(i) in [int, str] or i is None:
                result_list.append(i)
            elif type(i) == list or type(i) == tuple or type(i) == set:
                result_list.extend(self.unpack(i))
            elif type(i) == dict:
                result_list.extend(self.unpack(i.keys()))
                result_list.extend(self.unpack(i.values()))
        return result_list
