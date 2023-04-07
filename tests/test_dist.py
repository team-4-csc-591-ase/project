# import os
#
# from src.config import CONSTS, CONSTS_LIST
# from src.data import Data
# from src.num import Num
# from src.query import dist, mid
# from src.update import add
# from src.utils import get_project_root, rnd
#
#
# def test_dist():
#     project_root = get_project_root()
#     file_path = os.path.join(project_root, "/etc/data/", CONSTS_LIST[CONSTS.file.name])
#     f = str(project_root) + "/" + file_path
#
#     data = Data(f)
#     num = Num()
#     for row in data.rows:
#         add(num, dist(data, row, data.rows[1]))
#     # print({"lo": num.lo, "hi": num.hi, "mid": rnd(mid(num)), "div": rnd(num)})
#     print({"lo": num.lo, "hi": num.hi, "mid": rnd(mid(num)), "div": rnd(num.n)})
