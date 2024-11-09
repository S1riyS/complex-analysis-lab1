from common import animate

MAX_COUNT = 256
OUTPUT_FILE = "./images/burning_ship_zoom.gif"
FRAMES = 90  # Number of frames in the animation
FPS = 15  # Number of frames in the animation
PIXEL_WIDTH = 512  # Width of the image
PIXEL_HEIGHT = 512  # Height of the image
START_ZOOM = 1  # Initial zoom level
END_ZOOM = 400  # Final zoom level after all frames
CENTER_X, CENTER_Y = -1.762, -0.028  # Popular region for Burning Ship fractal


def burning_ship_function(c1: float, c2: float) -> int:
    x = 0.0
    y = 0.0

    for i in range(MAX_COUNT):
        x, y = abs(x), abs(y)
        x_new = x * x - y * y + c1
        y = 2 * x * y + c2
        x = x_new
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
    generative_function=burning_ship_function,
    max_iterations=MAX_COUNT,
    save_to=OUTPUT_FILE,
    framerate=FPS,
)
print(ans)
