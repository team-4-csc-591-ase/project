from src.utils import RX, scott_knot, tiles


def test_scottknott():
    print("HorsePower HI")
    for rx in tiles(
        scott_knot(
            [
                RX(
                    {
                        55.0,
                        74.0,
                        82.0,
                        90.0,
                        96.0,
                        105.0,
                        114.0,
                        115.0,
                        130.0,
                        135.0,
                        142.0,
                        151.0,
                        160.0,
                        168.0,
                        200.0,
                        200.0,
                    },
                    "rx1",
                ),
                RX(
                    {
                        96.0,
                        100.0,
                        105.0,
                        110.0,
                        115.0,
                        138.0,
                        142.0,
                        147.0,
                        153.0,
                        155.0,
                        164.0,
                        168.0,
                        172.0,
                        178.0,
                        202.0,
                        210.0,
                        225.0,
                    },
                    "rx2",
                ),
                RX({73.0, 82.0, 115.0, 130.0, 155.0}, "rx3"),
                RX(
                    {
                        82.0,
                        85.0,
                        90.0,
                        93.0,
                        103.0,
                        105.0,
                        110.0,
                        115.0,
                        124.0,
                        130.0,
                        134.0,
                        141.0,
                        153.0,
                        155.0,
                    },
                    "rx4",
                ),
                RX({90.0, 91.0, 92.0, 93.0, 94.0}, "rx5"),
                RX(
                    {55.0, 74.0, 82.0, 90.0, 105.0, 115.0, 130.0, 151.0, 168.0, 200.0},
                    "rx1",
                ),
                RX(
                    {
                        96.0,
                        105.0,
                        115.0,
                        138.0,
                        147.0,
                        153.0,
                        164.0,
                        172.0,
                        210.0,
                        225.0,
                    },
                    "rx2",
                ),
                RX({73.0, 82.0, 115.0, 130.0, 155.0}, "rx3"),
                RX(
                    {82.0, 90.0, 93.0, 103.0, 110.0, 124.0, 130.0, 141.0, 153.0, 155.0},
                    "rx4",
                ),
                RX({90.0, 93.0, 93.0, 93.0, 93.0}, "rx5"),
            ]
        )
    ):
        print(rx["name"], rx["rank"], rx["show"])
