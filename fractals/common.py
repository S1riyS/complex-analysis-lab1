import numpy as np
from generativepy.nparray import (  # type: ignore
    make_npcolormap,
    apply_npcolormap,
)
from generativepy.color import Color  # type: ignore
import numpy as np


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
