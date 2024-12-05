import importlib.resources
from multiprocessing import Process

import PySide6.QtWidgets as QtWidgets

from laba_med.players import MediaPlayerReactions
import laba_med.videos
import laba_med.webcam_analyze


def start_webcam_analyze():
    laba_med.webcam_analyze.main()


def main():
    app = QtWidgets.QApplication([])
    player = MediaPlayerReactions()
    player.show()
    path = importlib.resources.files(laba_med.videos).joinpath("monkey.mp4") # сюда вставляешь название сидоса который хочешь запустить

    process = Process(target=start_webcam_analyze)
    process.start()

    player.open_video(path)

    app.exec()

    if process.is_alive():
        process.terminate()


if __name__ == "__main__":
    main()
