import os
import sys

from src import query
from src.config import CONSTS, CONSTS_LIST, random_seeds
from src.contrast_sets import selects, show_rule, xpln
from src.data import Data
from src.optimization import sway
from src.utils import get_project_root

sys.setrecursionlimit(10**6)


def test_xpln():

    top, _ = query.betters([1,5,9,0,8], 3)

    print(
        query.stats(top),
        query.stats(top, query.div),
    )

