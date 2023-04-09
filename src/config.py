from enum import Enum
from typing import Any, Dict


class CONSTS(Enum):
    seed = "seed"
    dump = "dump"
    go = "go"
    help = "help"
    file = "file"
    p = "p"
    Sample = "Sample"
    Far = "Far"
    min = "min"
    cliffs = "cliffs"
    bins = "bins"
    Max = "Max"
    Reuse = "Reuse"
    Halves = "Halves"
    rest = "rest"
    d = "d"

#
# CONSTS_LIST: Dict[str, Any] = {
#     CONSTS.seed.name: 937162211,
#     CONSTS.dump.name: False,
#     CONSTS.go.name: "data",
#     CONSTS.help.name: False,
#     CONSTS.file.name: [
#         "auto2.csv",
#         "auto93.csv",
#         "china.csv",
#         "coc1000.csv",
#         "coc10000.csv",
#         "healthCloseIsses12mths0001-hard.csv",
#         "healthCloseIsses12mths0011-easy.csv",
#         "nasa93dem.csv",
#         "pom.csv",
#         "SSM.csv",
#         "SSN.csv",
#     ],
#     CONSTS.p.name: 2,
#     CONSTS.Far.name: 0.95,
#     CONSTS.min.name: 0.5,
#     CONSTS.Sample.name: 512,
#     CONSTS.cliffs.name: 0.147,
#     CONSTS.bins.name: 16,
#     CONSTS.Max.name: 512,
#     CONSTS.Reuse.name: True,
#     CONSTS.Halves.name: 512,
#     CONSTS.rest.name: 4,
#     CONSTS.d.name: 0.35,
# }
CONSTS_LIST: Dict[str, Any] = {
    CONSTS.seed.name: 937162211,
    CONSTS.dump.name: False,
    CONSTS.go.name: "data",
    CONSTS.help.name: False,
    CONSTS.file.name: ["auto2.csv", "auto93.csv", "china.csv", "coc1000.csv", "coc10000.csv", "healthCloseIsses12mths0001-hard.csv", "healthCloseIsses12mths0011-easy.csv", "nasa93dem.csv", "pom.csv", "SSM.csv", "SSN.csv"],
    CONSTS.p.name: 3,
    CONSTS.Far.name: 0.75,
    CONSTS.min.name: 0.75,
    CONSTS.Sample.name: 256,
    CONSTS.cliffs.name: 0.147,
    CONSTS.bins.name: 32,
    CONSTS.Max.name: 512,
    CONSTS.Reuse.name: True,
    CONSTS.Halves.name: 512,
    CONSTS.rest.name: 3,
    CONSTS.d.name: 0.45,
}

