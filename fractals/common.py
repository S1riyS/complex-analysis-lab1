import time
from typing import Callable, List

import imageio
import numpy as np
from generativepy.bitmap import Scaler  # type: ignore
from generativepy.color import Color  # type: ignore
from generativepy.nparray import apply_npcolormap, make_npcolormap  # type: ignore


def colorise(counts, max_count):
    counts = np.reshape(counts, (counts.shape[0], counts.shape[1]))

    colormap = make_npcolormap(
        max_count + 1,
        [
            Color("black"),
            Color("red"),
            Color("orange"),
            Color("yellow"),
            Color("white"),
        ],
    )

    outarray = np.zeros((counts.shape[0], counts.shape[1], 3), dtype=np.uint8)
    apply_npcolormap(outarray, counts, colormap)
    return outarray


def paint(
    image,
    pixel_width: int,
    pixel_height: int,
    zoom: int,
    center_x: float,
    center_y: float,
    generative_function: Callable[[float, float], int],
    max_iterations: int,
) -> None:
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
            count = generative_function(x, y)
            counts[py, px] = count

    colored_image = colorise(counts, max_iterations)
    np.copyto(image, colored_image)


def animate(
    frames: int,
    pixel_width: int,
    pixel_height: int,
    start_zoom: int,
    end_zoom: int,
    center_x: float,
    center_y: float,
    generative_function: Callable[[float, float], int],
    max_iterations: int,
    save_to: str,
    framerate: int,
) -> List[float]:
    times = [time.time() * 1000]
    images = []
    for i in range(frames):
        print(f"Processing frame {i+1}/{frames}...", end=" ")

        zoom = start_zoom * (end_zoom / start_zoom) ** (i / (frames - 1))
        image = np.zeros((pixel_height, pixel_width, 3), dtype=np.uint8)
        paint(image, pixel_width, pixel_height, zoom, center_x, center_y, generative_function, max_iterations)
        images.append(image)

        print(f"(took {time.time()*1000 - times[-1]:.2f} ms)")
        times.append(time.time() * 1000)

    imageio.mimsave(save_to, images, fps=framerate)
    return times
