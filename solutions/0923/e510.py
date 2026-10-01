def E510(test_data):
    results = []

    for N, p, i in test_data:
        # p = 0 時，所有玩家都不可能獲勝
        if p == 0:
            results.append(0.0)
            continue

        # 計算第 i 位玩家的獲勝機率
        ans = (1 - p)**(i - 1) * p / (1 - (1 - p)**N)

        # 四捨五入至小數點後 4 位
        results.append(round(ans, 4))

    return results


if __name__ == "__main__":
    test_data = [[2, 0.166666, 1], [2, 0.166666, 2]]
    results = E510(test_data)
    print(results)
    # ans: [0.5455, 0.4545]
    