import time
from generativepy.bitmap import Scaler  # type: ignore
from generativepy.nparray import make_nparray  # type: ignore
import numpy as np
import imageio
from generativepy.bitmap import Scaler
import numpy as np
from common import colorise

MAX_COUNT = 256
OUTPUT_FILE = "./images/burning_ship_zoom.gif"
FRAMES = 90  # Number of frames in the animation
FPS = 15  # Number of frames in the animation
PIXEL_WIDTH = 512  # Width of the image
PIXEL_HEIGHT = 512  # Height of the image
START_ZOOM = 1  # Initial zoom level
END_ZOOM = 400  # Final zoom level after all frames
CENTER_X, CENTER_Y = -1.762, -0.028  # Popular region for Burning Ship fractal


def calc(c1, c2):
    x = y = 0
    for i in range(MAX_COUNT):
        x, y = abs(x), abs(y)
        x_new = x * x - y * y + c1
        y = 2 * x * y + c2
        x = x_new
        if x * x + y * y > 4:
            return i + 1
    return 0


def paint(image, pixel_width, pixel_height, zoom, center_x, center_y):
    scaler = Scaler(
        pixel_width,
        pixel_height,
        width=3 / zoom,
        startx=center_x - 1.5 / zoom,
        starty=center_y - 1.5 / zoom,
    )

    counts = np.zeros((pixel_height, pixel_width), dtype=np.uint16)
    for px in range(pixel_width):
        for py in range(pixel_height):
            x, y = scaler.device_to_user(px, py)
            count = calc(x, y)
            counts[py, px] = count

    colored_image = colorise(counts, MAX_COUNT)
    np.copyto(image, colored_image)


def animate(
    frames, pixel_width, pixel_height, start_zoom, end_zoom, center_x, center_y
):
    images = []
    times = [time.time() * 1000]
    for i in range(frames):
        print(f"Processing frame {i+1}/{frames}...", end=" ")
        zoom = start_zoom * (end_zoom / start_zoom) ** (i / (frames - 1))
        image = np.zeros((pixel_height, pixel_width, 3), dtype=np.uint8)
        paint(image, pixel_width, pixel_height, zoom, center_x, center_y)
        images.append(image)
        print(f"(took {time.time()*1000 - times[-1]:.2f} ms)")
        times.append(time.time() * 1000)
    imageio.mimsave(OUTPUT_FILE, images, fps=FPS)
    return times


ans = animate(
    FRAMES, PIXEL_WIDTH, PIXEL_HEIGHT, START_ZOOM, END_ZOOM, CENTER_X, CENTER_Y
)

print(ans)
