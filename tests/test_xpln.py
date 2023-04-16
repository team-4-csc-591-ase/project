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
    project_root = get_project_root()
    for i, random_seed in enumerate(random_seeds):
        CONSTS_LIST[CONSTS.seed.name] = random_seed
        print(f"\nCurrent iteration {i} Random Seed {random_seed}")
        for _f in CONSTS_LIST[CONSTS.file.name]:
            file_path = os.path.join(project_root, "/etc/data/", _f)
            f = str(project_root) + "/" + file_path

            print(f"\nCurrent file {_f}")
            try:
                data = Data(f)

                best, rest, evals = sway(data)
                rule, _ = xpln(data, best, rest)
                if rule is None:
                    continue
                print("\n-----------\nexplain=", show_rule(rule))
                data1 = Data(data, selects(rule, data.rows))

                print("all               ", query.stats(data), query.stats(data, query.div))
                print(
                    f"sway with   {evals} evals",
                    query.stats(best),
                    query.stats(best, query.div),
                )
                print(
                    f"xpln on     {evals} evals",
                    query.stats(data1),
                    query.stats(data1, query.div),

                )
            except Exception as e:
                print(f"Error at file {_f}, {e}")

            top, _ = query.betters(data, len(best.rows))
            top = Data(data, top)
            print(
                f"sort with {len(data.rows)} evals",
                query.stats(top),
                query.stats(top, query.div),
            )

