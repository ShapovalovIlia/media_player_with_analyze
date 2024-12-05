import json
import importlib.resources
from collections import defaultdict

import matplotlib.pyplot as plt
from PySide6.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
)

import laba_med.reactions
from .media_player import MediaPlayer


class MediaPlayerPlots(MediaPlayer):
    def __init__(self):
        super().__init__()
        self._likes = defaultdict(int)
        self._dislikes = defaultdict(int)

        # Канвас для графика с увеличенной высотой (вытянутый по вертикали)
        self._figure, self._ax = plt.subplots(
            figsize=(5, 6)
        )  # Увеличиваем высоту графика
        self._canvas = FigureCanvas(self._figure)
        self._canvas.setGeometry(
            800, 10, 780, 500
        )  # Увеличиваем высоту канваса
        self._canvas.setParent(self)

        # Таймер для обновления графика каждую секунду
        self._timer = QTimer(self)
        self._timer.timeout.connect(self.update_graph)
        self._timer.start(1000)  # Обновление каждую секунду

        # Список для хранения меток времени
        self._timestamps = []

    def open_video(self, filename):
        super().open_video(filename)
        self.__load_reactions()

    def __load_reactions(self):
        file_path = str(
            importlib.resources.files(laba_med.reactions).joinpath(
                f"{self._video_name}.txt"
            ),
        )

        with open(file_path, "r") as file:
            for line in file:
                json_data = json.loads(line)
                timestamp = int(json_data["timestamp"])
                if json_data["reaction"] == 0:
                    self._dislikes[timestamp] += 1
                else:
                    self._likes[timestamp] += 1

    def update_graph(self):
        """
        Обновляет график каждую секунду,
        показывая количество лайков и дизлайков за последние 2 секунды.
        """
        if self._player.get_time() == -1:
            return

        current_time = int(
            self._player.get_time() / 1000
        )

        recent_likes = 0
        recent_dislikes = 0

        for i in range(max(0, current_time - 2), current_time + 1):
            recent_likes += self._likes[i]
            recent_dislikes += self._dislikes[i]

        # Обновляем график
        self._ax.clear()
        self._ax.bar(
            ["Likes", "Dislikes"],
            [recent_likes, recent_dislikes],
            color=["green", "red"],
        )
        self._ax.set_title(f"Likes and Dislikes in last 2 seconds")
        self._ax.set_ylabel("Count")

        self._canvas.draw()

        self._canvas.flush_events()
