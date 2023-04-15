import os

from src.config import CONSTS, CONSTS_LIST, random_seeds
from src.data import Data
from src.optimization import sway
from src.query import div, stats
from src.utils import diffs, get_project_root, o


def test_sway():
    project_root = get_project_root()
    for i, random_seed in enumerate(random_seeds):
        CONSTS_LIST[CONSTS.seed.name] = random_seed
        print(f"\nCurrent iteration {i} Random Seed {random_seed}")
        for _f in CONSTS_LIST[CONSTS.file.name]:
            file_path = os.path.join(project_root, "/etc/data/", _f)
            f = str(project_root) + "/" + file_path

            print(f"\nCurrent file {_f}")
            data = Data(f)
            best, rest, _ = sway(data)
            print(rest)
            print("\nall ", o(stats(data)))
            print("    ", o(stats(data, div)))
            print("\nbest", o(stats(best)))
            print("    ", o(stats(best, div)))
            print("\nrest", o(stats(rest)))
            print("    ", o(stats(rest, div)))
            print("\nall ~= best?", o(diffs(best.cols.y, data.cols.y)))
            print("best ~= rest?", o(diffs(best.cols.y, rest.cols.y)))
