from typing import Tuple
import numpy as np

# Tile graphics structured type compatible with Console.tiles_rgb
graphic_dt = np.dtype(
    [
         ('ch', np.int32), # Unicode codepoint.
         ('fg', '3B'),     # 3 Bytes for RGB values
         ('bg', '3B'),
    ])

# Tile strucz used for statically defined tile data
tile_dt = np.dtype(
    [
         ('walkable', np.bool),
         ('transparent', np.bool),
         ('dark', graphic_dt), # Graphics fpr when this tile is not in FOV
         ('light', graphic_dt), # Graphics fpr when this tile is in FOV
     ])

def new_tile(
        *, # Enforce the use of keywords(parameter order doesn't matter)
        walkable: bool,
        transparent: bool,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
        light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
        ) -> np.ndarray:
        """ Helper function for defining individual tile types """
        return np.array((walkable, transparent, dark, light), dtype=tile_dt)


# SHROUD represents unexplored, unseen tiles
SHROUD = np.array((ord(' '), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)
    
floor = new_tile(
    walkable=True, transparent=True, 
    dark=(ord(' '), (255, 255, 255), (50, 50, 150)),
    light=(ord(' '), (255, 255, 255), (200, 180, 50)),
    )
wall = new_tile(
    walkable=False, transparent=False,
    dark=(ord(' '), (225, 225, 225), (0, 0, 100)),
    light=(ord(' '), (7, 59, 66), (130, 110, 50)),
    )
