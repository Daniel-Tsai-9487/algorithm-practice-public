def E555(test_data):
    results = []

    for S, D in test_data:
        # S：目前旅行團的人數
        # D：要查詢的日期

        # 如果 D 大於目前旅行團的住宿天數
        # 就扣掉這團的天數，換下一團
        while D > S:
            D -= S
            S += 1

        # 找到第 D 天入住的旅行團人數
        results.append(S)

    return results


if __name__ == "__main__":
    test_data = [[1, 6], [3, 10], [3, 14]]

    results = E555(test_data)
    print(results)

    # ans: [3, 5, 6]