import os

from src import query
from src.config import CONSTS, CONSTS_LIST
from src.contrast_sets import selects, xpln
from src.data import Data
from src.optimization import sway
from src.utils import bootstrap, cliffs_delta, get_project_root


def test_table():
    project_root = get_project_root()
    files = [_f for _f in CONSTS_LIST[CONSTS.file.name]]

    for file in files:
        iteration = 0

        table1_dict = {
            "all": [],
            "sway1": [],
            "sway2": [],
            "xpln1": [],
            "xpln2": [],
            "top": [],
        }

        table2_rows = [
            [["all", "all"], None],
            [["all", "sway1"], None],
            [["sway1", "sway2"], None],
            [["sway1", "xpln1"], None],
            [["sway2", "xpln2"], None],
            [["sway1", "top"], None],
        ]

        while iteration < 20:
            file_path = os.path.join(project_root, "/etc/data/", file)
            f = str(project_root) + "/" + file_path
            data = Data(f)
            best, rest, evals = sway(data)
            rule, most = xpln(data, best, rest)

            if rule:
                top, _ = query.betters(data, len(best.rows))

                table1_dict["top"].append(Data(data, top))

                selected = selects(rule, data.rows)
                data_selects = [s for s in selected if s is not None]
                data1 = Data(data, data_selects)

                table1_dict["xpln1"].append(data1)
                table1_dict["xpln2"].append(data1)
                table1_dict["all"].append(data)
                table1_dict["sway1"].append(best)
                table1_dict["sway2"].append(best)

                for i in range(len(table2_rows)):
                    [base, diff], result = table2_rows[i]
                    if result is None:
                        table2_rows[i][1] = ["=" for _ in range(len(data.cols.y))]
                    for k in range(len(data.cols.y)):
                        try:
                            if table2_rows[i][1][k] == "=":
                                y0, z0 = (
                                    table1_dict[base][iteration].cols.y[k],
                                    table1_dict[diff][iteration].cols.y[k],
                                )
                                is_equal = bootstrap(
                                    y0.col.has, z0.col.has
                                ) and cliffs_delta(y0.col.has, z0.col.has)
                                if not is_equal:
                                    table2_rows[i][1][k] = "≠"
                        except IndexError:
                            break
            iteration += 1

    assert True
