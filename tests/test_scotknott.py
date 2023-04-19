from src.utils import RX, scott_knot, tiles


def test_scottknott():  # noqa: C901
    print()
    print("auto2.csv")
    for rx in tiles(
        scott_knot(
            [
                RX({34.3, 10.075, 39.3, 2122.25}, "sway1"),
                RX(
                    {
                        29.4,
                        13.885,
                        35.3,
                        2513,
                    },
                    "sway2",
                ),
                RX({22.15, 17.915, 29.75, 3012}, "sway3"),
                RX({21.8, 18.535, 28.35, 3066.75}, "sway4"),
                RX({29.7, 14.045, 35.55, 2526.75}, "sway5"),
                RX({28.1, 12.985, 33.5, 2447.25}, "sway6"),
            ]
        )
    ):
        print(rx["name"], rx["rank"], rx["show"])

    for rx in tiles(
        scott_knot(
            [
                RX([29, 8.3, 37, 2325], "xpln1"),
                RX([29, 12.2, 33, 2295], "xpln2"),
                RX([20, 31.9, 29, 2920], "xpln3"),
                RX([29, 12.2, 33, 2295], "xpln4"),
                RX([33, 8.4, 37, 2045], "xpln5"),
                RX([29, 8.3, 37, 2325], "xpln6"),
            ]
        )
    ):
        print(rx["name"], rx["rank"], rx["show"])

    print()
    print("auto93.csv")
    for rx in tiles(
        scott_knot(
            [
                RX({15.97222222, 2115.944444, 33.33333333}, "sway1"),
                RX({16.445, 2468.85, 29.5}, "sway2"),
                RX({16.24736842, 2705.9, 26.5}, "sway3"),
                RX({15.07, 3727.35, 17.5}, "sway4"),
                RX({15.48, 2510.25, 29}, "sway5"),
                RX({16.365, 2230.9, 32.5}, "sway6"),
            ]
        )
    ):
        print(rx["name"], rx["rank"], rx["show"])

    for rx in tiles(
        scott_knot(
            [
                RX({17.5, 2375, 30}, "xpln1"),
                RX({14, 2246, 30}, "xpln2"),
                RX({22.2, 2035, 30}, "xpln3"),
                RX({13.5, 2330, 20}, "xpln4"),
                RX({13.5, 2330, 20}, "xpln5"),
                RX({18.3, 2635, 30}, "xpln6"),
            ]
        )
    ):
        print(rx["name"], rx["rank"], rx["show"])

    # print()
    # print("china.csv")
    # for rx in tiles(
    #         scott_knot(
    #             [
    #                 RX({897.8}, "sway1"),
    #                 RX({2464.4}, "sway2"),
    #                 RX({1708.3}, "sway3"),
    #                 RX({5042.1}, "sway4"),
    #                 RX({1432.35}, "sway5"),
    #                 RX({1640.25}, "sway6"),
    #             ]
    #         )
    # ):
    #     print(rx["name"], rx["rank"], rx["show"])
    #
    # for rx in tiles(
    #         scott_knot(
    #             [
    #                 RX({1986}, "xpln1"),
    #                 RX({2372}, "xpln2"),
    #                 RX({1987}, "xpln3"),
    #                 RX({1987}, "xpln4"),
    #                 RX({4428}, "xpln5"),
    #                 RX({2372}, "xpln6"),
    #             ]
    #         )
    # ):
    #     print(rx["name"], rx["rank"], rx["show"])

    print()
    print("coc1000.out")
    for rx in tiles(
        scott_knot(
            [
                RX([2.7, 17514.1, 914.45, 2.9, 3.45], "sway1"),
                RX([3.15, 20761.95, 1044.55, 2.95, 2.9], "sway2"),
                RX([3.3, 21575.35, 887.45, 3.35, 8.1], "sway3"),
                RX([2.7, 26368.05, 1076.1, 3.05, 4.1], "sway4"),
                RX([2.6, 29706.65, 1018.85, 2.95, 7.5], "sway5"),
                RX([3.45, 27717.3, 1229.9, 2.65, 5.2], "sway6"),
            ]
        )
    ):
        print(rx["name"], rx["rank"], rx["show"])
    for rx in tiles(
        scott_knot(
            [
                RX([3, 25334, 1345, 3, 1], "xpln1"),
                RX([3, 35516, 1970, 4, 10], "xpln2"),
                RX([5, 60885, 1504, 2, 6], "xpln3"),
                RX([3, 25334, 1345, 3, 1], "xpln4"),
                RX([5, 37716, 1587, 3, 4], "xpln5"),
                RX([3, 35516, 1970, 4, 18], "xpln6"),
            ]
        )
    ):
        print(rx["name"], rx["rank"], rx["show"])

    print()
    print("coc10000.out")
    for rx in tiles(
        scott_knot(
            [
                RX({17580.65, 1075.05, 5.3}, "sway1"),
                RX({24432.75, 937.3, 6.45}, "sway2"),
                RX({18299.9, 921.25, 8.05}, "sway3"),
                RX({21547.4, 1091.6, 5.7}, "sway4"),
                RX({28506.4, 991.7, 6.4}, "sway5"),
                RX({23425.35, 699.1, 7}, "sway6"),
            ]
        )
    ):
        print(rx["name"], rx["rank"], rx["show"])
    for rx in tiles(
        scott_knot(
            [
                RX({8960, 673, 2}, "xpln1"),
                RX({4396, 1439, 0}, "xpln2"),
                RX({37072, 1091, 1}, "xpln3"),
                RX({58268, 1938, 1}, "xpln4"),
                RX({21835, 1711, 0}, "xpln5"),
                RX({27869, 1173, 13}, "xpln6"),
            ]
        )
    ):
        print(rx["name"], rx["rank"], rx["show"])

    print()
    print("healthCloseIsses12mths0001-easy.out")
    for rx in tiles(
        scott_knot(
            [
                RX({-0.61, 30.7565, 58.331}, "sway1"),
                RX({-2.065, 43, 49.998}, "sway2"),
                RX({-6.7, 65.8, 37.4985}, "sway3"),
                RX({-7.335, 86.8, 20.8325}, "sway4"),
                RX({-4.295, 62.75, 38.332}, "sway5"),
                RX({-1, 36.3, 54.1645}, "sway6"),
            ]
        )
    ):
        print(rx["name"], rx["rank"], rx["show"])
    for rx in tiles(
        scott_knot(
            [
                RX({-0.52, 100.53, 0}, "xpln1"),
                RX({-0.52, 100.53, 0}, "xpln2"),
                RX([0, 0, 83.33], "xpln3"),
                RX({-0.52, 100.53, 0}, "xpln4"),
                RX({-0.52, 100.53, 0}, "xpln5"),
                RX({-0.52, 100.53, 0}, "xpln6"),
            ]
        )
    ):
        print(rx["name"], rx["rank"], rx["show"])

    print()
    print("healthCloseIsses12mths0001-hard.out")
    for rx in tiles(
        scott_knot(
            [
                RX({7.6215, 74.2785, 17.5}, "sway1"),
                RX({7.8805, 73.1015, 20}, "sway2"),
                RX({5.0245, 82.517, 25}, "sway3"),
                RX({4.22, 85.3155, 23.125}, "sway4"),
                RX({6.586, 77.0955, 21.875}, "sway5"),
                RX({7.1875, 75.056, 15.625}, "sway6"),
            ]
        )
    ):
        print(rx["name"], rx["rank"], rx["show"])
    for rx in tiles(
        scott_knot(
            [
                RX({7.19, 74.84, 25}, "xpln1"),
                RX({7.51, 73.8, 25}, "xpln2"),
                RX({7.34, 74.36, 25}, "xpln3"),
                RX({9.99, 70.38, 25}, "xpln4"),
                RX({9.99, 70.38, 25}, "xpln5"),
                RX({7.51, 73.8, 25}, "xpln6"),
            ]
        )
    ):
        print(rx["name"], rx["rank"], rx["show"])

    print()
    print("nasa93dem.out")
    for rx in tiles(
        scott_knot(
            [
                RX([1481.15, 195.27, 45.865, 16.89], "sway1"),
                RX([2106.1, 186.65, 55.485, 19.245], "sway2"),
                RX([3705.95, 681.01, 115.22, 26.98], "sway3"),
                RX([2816.65, 584.05, 95.395, 24.245], "sway4"),
                RX([1234.7, 477.57, 31.49, 14.62], "sway5"),
                RX([2870.1, 349.78, 104.93, 24.095], "sway6"),
            ]
        )
    ):
        print(rx["name"], rx["rank"], rx["show"])
    for rx in tiles(
        scott_knot(
            [
                RX([2077, 352.8, 66.6, 21], "xpln1"),
                RX([470, 48, 15, 13.6], "xpln2"),
                RX([324, 50, 10.4, 11.2], "xpln3"),
                RX([2007, 252, 47.5, 22.5], "xpln4"),
                RX([765, 70, 15.4, 14.5], "xpln5"),
                RX([2077, 352.8, 66.6, 21], "xpln6"),
            ]
        )
    ):
        print(rx["name"], rx["rank"], rx["show"])

    print()
    print("pom.out")
    for rx in tiles(
        scott_knot(
            [
                RX([0.908, 181.774, 0.2935], "sway1"),
                RX([6.7005, 202.419, 2.112], "sway2"),
                RX([2.2075, 245.4075, 0.682], "sway3"),
                RX([3.709, 236.0105, 1.174], "sway4"),
                RX([3.718, 226.9675, 1.198], "sway5"),
                RX([3.109, 208.4025, 0.974], "sway6"),
            ]
        )
    ):
        print(rx["name"], rx["rank"], rx["show"])
    for rx in tiles(
        scott_knot(
            [
                RX([1, 189.79, 0.43], "xpln1"),
                RX([0.88, 177.85, 0.56], "xpln2"),
                RX([1, 193.72, 0.29], "xpln3"),
                RX([0.94, 181.45, 0.19], "xpln4"),
                RX([0.89, 131.02, 0.06], "xpln5"),
                RX([0.9, 432.69, 0.09], "xpln6"),
            ]
        )
    ):
        print(rx["name"], rx["rank"], rx["show"])

    # print()
    # print("SSM.out")
    # for rx in tiles(
    #         scott_knot(
    #             [
    #                 RX([5.05, 113.2315], "sway1"),
    #                 RX([4.669, 49.546], "sway2"),
    #                 RX([3.699, 46.6405], "sway3"),
    #                 RX([5.0505, 42.8875], "sway4"),
    #                 RX([4.3905, 35.9015], "sway5"),
    #                 RX([6.815, 111.748], "sway6"),
    #             ]
    #         )
    # ):
    #     print(rx["name"], rx["rank"], rx["show"])
    # for rx in tiles(
    #         scott_knot(
    #             [
    #                 RX([4, 88.17], "xpln1"),
    #                 RX([1.95, 22.97], "xpln2"),
    #                 RX([0.58, 8.46], "xpln3"),
    #                 RX([5.07, 36.27], "xpln4"),
    #                 RX([1.02, 14.5], "xpln5"),
    #                 RX([1.87, 28.16], "xpln6"),
    #             ]
    #         )
    # ):
    #     print(rx["name"], rx["rank"], rx["show"])
    #
    # print()
    # print("SSN.out")
    # for rx in tiles(
    #         scott_knot(
    #             [
    #                 RX({1244.333, 43.3}, "sway1"),
    #                 RX({450.932, 43.192}, "sway2"),
    #                 RX({219.9, 17.4555}, "sway3"),
    #                 RX({905.1805, 42.7275}, "sway4"),
    #                 RX({201.569, 43.921}, "sway5"),
    #                 RX({1910.633, 62.679}, "sway6"),
    #             ]
    #         )
    # ):
    #     print(rx["name"], rx["rank"], rx["show"])
    # for rx in tiles(
    #         scott_knot(
    #             [
    #                 RX([211.64, 14.96], "xpln1"),
    #                 RX([139.05, 7.2], "xpln2"),
    #                 RX([299.03, 11.1], "xpln3"),
    #                 RX([159.88, 11.24], "xpln4"),
    #                 RX([156.6, 5.54], "xpln5"),
    #                 RX([146.76, 18.63], "xpln6"),
    #             ]
    #         )
    # ):
    #     print(rx["name"], rx["rank"], rx["show"])
