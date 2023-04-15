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


random_seeds = [1861316, 5558115, 6602314, 1705199, 143077, 3794878, 6905227, 7624225, 211415, 3982231, 380543, 9473979,
                2496648, 6192962, 9907226, 6041808, 4822213, 2573038, 1905055, 2054574]
# Base line
CONSTS_LIST: Dict[str, Any] = {
    CONSTS.seed.name: 937162211,
    CONSTS.dump.name: False,
    CONSTS.go.name: "data",
    CONSTS.help.name: False,
    CONSTS.file.name: [
        "auto2.csv",
        "auto93.csv",
        "china.csv",
        "coc1000.csv",
        "coc10000.csv",
        "healthCloseIsses12mths0001-hard.csv",
        "healthCloseIsses12mths0011-easy.csv",
        "nasa93dem.csv",
        "pom.csv",
        "SSM.csv",
        "SSN.csv",
    ],
    CONSTS.p.name: 2,
    CONSTS.Far.name: 0.95,
    CONSTS.min.name: 0.5,
    CONSTS.Sample.name: 512,
    CONSTS.cliffs.name: 0.147,
    CONSTS.bins.name: 16,
    CONSTS.Max.name: 512,
    CONSTS.Reuse.name: True,
    CONSTS.Halves.name: 512,
    CONSTS.rest.name: 4,
    CONSTS.d.name: 0.35,
}

# 1
# CONSTS_LIST: Dict[str, Any] = {
#     CONSTS.seed.name: 937162211,
#     CONSTS.dump.name: False,
#     CONSTS.go.name: "data",
#     CONSTS.help.name: False,
#     CONSTS.file.name: ["auto2.csv", "auto93.csv", "china.csv", "coc1000.csv", "coc10000.csv", "healthCloseIsses12mths0001-hard.csv", "healthCloseIsses12mths0011-easy.csv", "nasa93dem.csv", "pom.csv", "SSM.csv", "SSN.csv"],
#     CONSTS.p.name: 3,
#     CONSTS.Far.name: 0.75,
#     CONSTS.min.name: 0.75,
#     CONSTS.Sample.name: 256,
#     CONSTS.cliffs.name: 0.147,
#     CONSTS.bins.name: 32,
#     CONSTS.Max.name: 512,
#     CONSTS.Reuse.name: True,
#     CONSTS.Halves.name: 512,
#     CONSTS.rest.name: 3,
#     CONSTS.d.name: 0.45,
# }

# 2
# CONSTS_LIST: Dict[str, Any] = {
#     CONSTS.seed.name: 937162211,
#     CONSTS.dump.name: False,
#     CONSTS.go.name: "data",
#     CONSTS.help.name: False,
#     CONSTS.file.name: ["auto2.csv", "auto93.csv", "china.csv", "coc1000.csv", "coc10000.csv", "healthCloseIsses12mths0001-hard.csv", "healthCloseIsses12mths0011-easy.csv", "nasa93dem.csv", "pom.csv", "SSM.csv", "SSN.csv"],
#     CONSTS.p.name: 4,
#     CONSTS.Far.name: 0.90,
#     CONSTS.min.name: 0.95,
#     CONSTS.Sample.name: 1024,
#     CONSTS.cliffs.name: 0.147,
#     CONSTS.bins.name: 48,
#     CONSTS.Max.name: 1024,
#     CONSTS.Reuse.name: True,
#     CONSTS.Halves.name: 1024,
#     CONSTS.rest.name: 4,
#     CONSTS.d.name: 0.65,
# }

# 3
# CONSTS_LIST: Dict[str, Any] = {
#     CONSTS.seed.name: 937162211,
#     CONSTS.dump.name: False,
#     CONSTS.go.name: "data",
#     CONSTS.help.name: False,
#     CONSTS.file.name: ["auto2.csv", "auto93.csv", "china.csv", "coc1000.csv", "coc10000.csv", "healthCloseIsses12mths0001-hard.csv", "healthCloseIsses12mths0011-easy.csv", "nasa93dem.csv", "pom.csv", "SSM.csv", "SSN.csv"],
#     CONSTS.p.name: 2,
#     CONSTS.Far.name: 0.5,
#     CONSTS.min.name: 0.80,
#     CONSTS.Sample.name: 512,
#     CONSTS.cliffs.name: 0.147,
#     CONSTS.bins.name: 16,
#     CONSTS.Max.name: 512,
#     CONSTS.Reuse.name: True,
#     CONSTS.Halves.name: 512,
#     CONSTS.rest.name: 2,
#     CONSTS.d.name: 0.50,
# }

# 4
# CONSTS_LIST: Dict[str, Any] = {
#     CONSTS.seed.name: 937162211,
#     CONSTS.dump.name: False,
#     CONSTS.go.name: "data",
#     CONSTS.help.name: False,
#     CONSTS.file.name: ["auto2.csv", "auto93.csv", "china.csv", "coc1000.csv", "coc10000.csv", "healthCloseIsses12mths0001-hard.csv", "healthCloseIsses12mths0011-easy.csv", "nasa93dem.csv", "pom.csv", "SSM.csv", "SSN.csv"],
#     CONSTS.p.name: 4,
#     CONSTS.Far.name: 0.35,
#     CONSTS.min.name: 0.80,
#     CONSTS.Sample.name: 512,
#     CONSTS.cliffs.name: 0.147,
#     CONSTS.bins.name: 64,
#     CONSTS.Max.name: 512,
#     CONSTS.Reuse.name: True,
#     CONSTS.Halves.name: 512,
#     CONSTS.rest.name: 5,
#     CONSTS.d.name: 0.95,
#     CONSTS.cohen.name: 0.35,
#     CONSTS.cliff.name: 0.4,
#     CONSTS.bootstrap.name: 512,
#     CONSTS.conf.name: 0.35,
#     CONSTS.width.name: 40,
# }

# 5
# CONSTS_LIST: Dict[str, Any] = {
#     CONSTS.seed.name: 937162211,
#     CONSTS.dump.name: False,
#     CONSTS.go.name: "data",
#     CONSTS.help.name: False,
#     CONSTS.file.name: ["auto2.csv", "auto93.csv", "china.csv", "coc1000.csv", "coc10000.csv", "healthCloseIsses12mths0001-hard.csv", "healthCloseIsses12mths0011-easy.csv", "nasa93dem.csv", "pom.csv", "SSM.csv", "SSN.csv"],
#     CONSTS.p.name: 1,
#     CONSTS.Far.name: 0.85,
#     CONSTS.min.name: 0.65,
#     CONSTS.Sample.name: 512,
#     CONSTS.cliffs.name: 0.147,
#     CONSTS.bins.name: 128,
#     CONSTS.Max.name: 512,
#     CONSTS.Reuse.name: True,
#     CONSTS.Halves.name: 512,
#     CONSTS.rest.name: 4,
#     CONSTS.d.name: 0.85,
#     CONSTS.cohen.name: 0.35,
#     CONSTS.cliff.name: 0.4,
#     CONSTS.bootstrap.name: 512,
#     CONSTS.conf.name: 0.35,
#     CONSTS.width.name: 40,
# }
