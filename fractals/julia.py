import time

import imageio
import numpy as np
from common import animate, colorise
from generativepy.bitmap import Scaler  # type: ignore
from generativepy.nparray import make_nparray  # type: ignore

MAX_COUNT = 512
OUTPUT_FILE = "./images/julia_zoom.gif"

FRAMES = 60  # Number of frames in the animation
FPS = 20
PIXEL_WIDTH = 512  # Width of the image
PIXEL_HEIGHT = 512  # Height of the image
START_ZOOM = 1  # Initial zoom level
END_ZOOM = 256  # Final zoom level after all frames
CENTER_X, CENTER_Y = -0.5251993, -0.5251993

# julia set constants
# C_RE, C_IM = -0.7, 0.27015
C_RE, C_IM = -0.5251993, -0.5251993


def julia_function(x: float, y: float) -> int:
    for i in range(MAX_COUNT):
        x, y = x * x - y * y + C_RE, 2 * x * y + C_IM
        if x * x + y * y > 4:
            return i + 1
    return 0


ans = animate(
    frames=FRAMES,
    pixel_width=PIXEL_WIDTH,
    pixel_height=PIXEL_HEIGHT,
    start_zoom=START_ZOOM,
    end_zoom=END_ZOOM,
    center_x=CENTER_X,
    center_y=CENTER_Y,
    generative_function=julia_function,
    max_iterations=MAX_COUNT,
    save_to=OUTPUT_FILE,
    framerate=FPS,
)
print(ans)
