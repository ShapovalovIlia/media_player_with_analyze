import time
from collections import deque

import numpy as np
import matplotlib.pyplot as plt


def set_face_reaction_plot():
    plt.ion()
    fig, ax = plt.subplots()
    time_window = 100
    emotions = ["Smiling", "Surprised", "Angry", "Neutral"]
    data = {
        emotion: deque([0] * time_window, maxlen=time_window)
        for emotion in emotions
    }
    lines = {
        emotion: ax.plot([], [], label=emotion)[0] for emotion in emotions
    }
    ax.set_ylim(0, 100)
    ax.set_xlim(0, time_window)
    ax.legend()

    try:
        while True:
            data["Smiling"].append(
                np.clip(data["Smiling"][-1] + np.random.uniform(-5, 5), 0, 100)
            )
            data["Surprised"].append(
                np.clip(
                    data["Surprised"][-1] + np.random.uniform(-7, 7),
                    0,
                    100,
                )
            )
            data["Angry"].append(
                np.clip(data["Angry"][-1] + np.random.uniform(-4, 4), 0, 100)
            )
            data["Neutral"].append(
                100
                - max(
                    data["Smiling"][-1],
                    data["Surprised"][-1],
                    data["Angry"][-1],
                )
            )

            for emotion, line in lines.items():
                line.set_ydata(data[emotion])
                line.set_xdata(range(len(data[emotion])))

            fig.canvas.draw()
            fig.canvas.flush_events()

            time.sleep(0.1)

    except KeyboardInterrupt:
        print("График завершён.")

    finally:
        plt.ioff()
        plt.show()
