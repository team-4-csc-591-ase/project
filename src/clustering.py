import math

import numpy as np

from src import lists, query
from src.config import CONSTS, CONSTS_LIST
from src.data import Data


def half(data, rows=None, cols=None, above=None):
    """
    Cluster `rows` into two sets by
    dividing the data via their distance to two remote points.
    To speed up finding those remote points, only look at
    `some` of the data. Also, to avoid outliers, only look
    `the.Far=.95` (say) of the way across the space.
    Args:
        data:
        rows:
        cols:
        above:

    Returns:

    """

    def gap(r1, r2):
        return query.dist(data, r1, r2, cols)

    def cos(a, b, c):
        if not c == 0:
            return (a**2 + c**2 - b**2) / (2 * c)
        else:
            return 1

    def euclidean_distance(a, b, c):
        """
        Returns the Euclidean distance between points A and C in a triangle with sides a, b, and c, using the Pythagorean theorem.
        """
        if not b == 0:
            x = (a**2 - c**2 + b**2) / (2 * b)
            y = math.sqrt(abs(a**2 - x**2))
            distance = math.sqrt(x**2 + y**2)
            # Calculate the maximum possible distance between points A and C
            max_distance = c / 2
            # Scale the distance to the range [0, 1]
            scaled_distance = distance / max_distance
            return scaled_distance
        else:
            return 1

    def manhattan_distance_scaled(a, b, c):
        """
        Returns the Manhattan distance between points A and C in a triangle with sides a, b, and c, scaled to the range [0, 1].
        """
        if not a == 0:
            # Calculate the x-coordinate of point B
            x = (a**2 + b**2 - c**2) / (2 * a)

            # Calculate the Manhattan distance between points A and C
            distance = abs(a - x) + abs(b)

            # Calculate the maximum possible Manhattan distance between points A and C
            max_distance = a + b

            # Scale the distance to the range [0, 1]
            scaled_distance = distance / max_distance

            return scaled_distance
        else:
            return 1

    def hamming_distance(a, b, c):
        """
        Returns the Hamming distance between the points of a triangle with sides of lengths a, b, and c.
        Assumes that the points are scaled to the range [0, 1].
        """
        if not c == 0:
            x1, y1 = 0, 0  # the first point is always (0, 0)
            x2, y2 = c, 0  # the second point is (c, 0)
            x3 = (a**2 - b**2 + c**2) / (
                2 * c
            )  # use cosine rule to find x-coordinate of third point
            y3 = np.sqrt(
                a**2 - x3**2
            )  # use Pythagorean theorem to find y-coordinate of third point

            # Convert the points to binary vectors
            vec1 = np.round([x1, y1, x2, y2, x3, y3])  # round to 0 or 1
            vec2 = np.round(
                [x2, y2, x3, y3, x1, y1]
            )  # swap the order of points for vec2

            # Calculate the Hamming distance between the binary vectors
            distance = np.sum(vec1 != vec2)

            return distance
        else:
            return 1

    def proj(r):
        return {"row": r, "x": euclidean_distance(gap(r, A), gap(r, B), c)}

    rows = rows or data.rows
    some = lists.many(rows, CONSTS_LIST[CONSTS.Halves.name])
    A = (CONSTS_LIST[CONSTS.Reuse.name] and above) or lists.any(some)
    tmp = sorted([{"row": r, "d": gap(r, A)} for r in some], key=lambda x: x["d"])
    far = tmp[int(len(tmp) * CONSTS_LIST[CONSTS.Far.name]) // 1]
    B, c, left, right = far["row"], far["d"], [], []
    for n, two in enumerate(sorted(map(proj, rows), key=lambda x: x["x"])):
        if n <= (len(rows) - 1) / 2:
            left.append(two["row"])
        else:
            right.append(two["row"])
    evals = 1 if (CONSTS_LIST[CONSTS.Reuse.name] and above) else 2
    return left, right, A, B, c, evals


def tree(data, rows=None, cols=None, above=None):
    """
    Cluster, recursively, some `rows` by  dividing them in two, many times
    Args:
        data:
        rows:
        cols:
        above:

    Returns:

    """
    rows = rows or data.rows
    here = {"data": Data(data, rows)}
    if len(rows) >= 2 * (len(data.rows) ** CONSTS_LIST[CONSTS.min.name]):
        left, right, A, B, _, _ = half(data, rows, cols, above)
        here["left"] = tree(data, left, cols, A)
        here["right"] = tree(data, right, cols, B)
    return here


def show_tree(tree, lvl=0, post=None):
    """
    Cluster can be displayed by this function.
    Args:
        tree:
        lvl:
        post:

    Returns:

    """
    if tree:
        print("{}[{}]".format("|.. " * lvl, len(tree["data"].rows)), end="")
        if lvl == 0 or ("left" not in tree):
            print(query.stats(tree["data"]))
        else:
            print("")
        show_tree(tree["left"] if "left" in tree else None, lvl + 1)
        show_tree(tree["right"] if "right" in tree else None, lvl + 1)
