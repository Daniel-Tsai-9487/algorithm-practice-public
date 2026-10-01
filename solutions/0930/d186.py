import math

def D186(test_data):
    results = []
    for a, b in test_data:
        # 區間 [a, b] 內的完全平方數數量 = isqrt(b) - isqrt(a - 1)
        count = math.isqrt(b) - math.isqrt(a - 1)
        results.append(count)
    return results

if(__name__=="__main__"):
    test_data = [[1, 4], [1, 10]]
    results = D186(test_data)
    print(results)
    # ans: [2, 3]