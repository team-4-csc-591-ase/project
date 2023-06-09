import os

from src.clustering import show_tree, tree
from src.config import CONSTS, CONSTS_LIST, random_seeds
from src.data import Data
from src.utils import get_project_root


def test_tree():
    project_root = get_project_root()
    for i, random_seed in enumerate(random_seeds):
        CONSTS_LIST[CONSTS.seed.name] = random_seed
        print(f"\nCurrent iteration {i} Random Seed {random_seed}")
        for _f in CONSTS_LIST[CONSTS.file.name]:
            file_path = os.path.join(project_root, "/etc/data/", _f)
            f = str(project_root) + "/" + file_path

            print(f"\nCurrent file {_f}")

            data = Data(f)
            show_tree(tree(data))
        break  # For testing 1 run is enough
