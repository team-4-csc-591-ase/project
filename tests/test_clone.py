# import os
#
# from src.config import CONSTS, CONSTS_LIST
# from src.data import Data
# from src.query import stats
# from src.utils import get_project_root
#
#
# def test_clone():
#     project_root = get_project_root()
#     file_path = os.path.join(project_root, "/etc/data/", CONSTS_LIST[CONSTS.file.name])
#     f = str(project_root) + "/" + file_path
#
#     data1 = Data(f)
#     data2 = Data(data1, data1.rows)
#
#     print(stats(data1))
#     print(stats(data2))
