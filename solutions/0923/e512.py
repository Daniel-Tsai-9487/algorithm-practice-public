
def E512(test_data):
    results = []

    for data in test_data:
        # 將 8 個數字分成 4 個點
        x1, y1, x2, y2, x3, y3, x4, y4 = data

        # 前兩個點與後兩個點，找出共同端點
        if x1 == x3 and y1 == y3:
            x, y = x2 + x4 - x1, y2 + y4 - y1

        elif x1 == x4 and y1 == y4:
            x, y = x2 + x3 - x1, y2 + y3 - y1

        elif x2 == x3 and y2 == y3:
            x, y = x1 + x4 - x2, y1 + y4 - y2

        else:
            # 剩下的情況：第二個點與第四個點相同
            x, y = x1 + x3 - x2, y1 + y3 - y2

        # 保留小數點後 3 位，加入結果
        results.append([round(x, 3), round(y, 3)])

    return results


if __name__ == "__main__":
    test_data = [
        [0.000, 0.000, 0.000, 1.000, 0.000, 1.000, 1.000, 1.000],
        [1.000, 0.000, 3.500, 3.500, 3.500, 3.500, 0.000, 1.000],
        [1.866, 0.000, 3.127, 3.543, 3.127, 3.543, 1.412, 3.145]
    ]

    results = E512(test_data)
    print(results)

    # ans: [[1.0, 0.0], [-2.5, -2.5], [0.151, -0.398]]


