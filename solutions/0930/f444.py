def F444(test_data):
    results = []
    for item in test_data:
        x = item[0]
        coeffs = item[1:]
        n = len(coeffs) - 1
        
        # 常數多項式（次數為 0 或無係數）的微分為 0
        if n <= 0:
            results.append(0)
            continue
        
        # 使用霍納法則（Horner's method）計算微分值
        val = 0
        for k in range(n):
            val = val * x + (n - k) * coeffs[k]
        results.append(val)
        
    return results

if(__name__=="__main__"):
    test_data = [[7, 1, -1], [2, 1, 1, 1]]
    results = F444(test_data)
    print(results)
    # ans: [1, 5]