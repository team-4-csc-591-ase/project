import os

from src.config import CONSTS, CONSTS_LIST, random_seeds

# from src.data import read
from src.data import Data
from src.discretization import bins
from src.optimization import sway
from src.query import value
from src.utils import get_project_root, o


def test_bins():
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
            print(
                "all", "", "", "", o({"best": len(best.rows), "rest": len(rest.rows)})
            )
            b4 = None
            result = bins(data.cols.x, {"best": best.rows, "rest": rest.rows})
            for t in result:
                for _range in t:
                    if _range.txt != b4:
                        print("")
                    b4 = _range.txt
                    print(
                        _range.txt,
                        _range.lo,
                        _range.hi,
                        round(
                            value(_range.y.has, len(best.rows), len(rest.rows), "best")
                        ),
                        o(_range.y.has),
                    )
        break  # For testing 1 run is enough
