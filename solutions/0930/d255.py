import math

def D255(test_data):
    results = []
    max_n = 500
    
    # f[j] 代表 sum_{i=1}^{j-1} gcd(i, j)
    f = [0] * (max_n + 1)
    for j in range(2, max_n + 1):
        f[j] = sum(math.gcd(i, j) for i in range(1, j))
    
    # G[n] 代表累加至 n 的總和: G[n] = G[n-1] + f[n]
    G = [0] * (max_n + 1)
    for n in range(2, max_n + 1):
        G[n] = G[n - 1] + f[n]
        
    for N in test_data:
        results.append(G[N])
        
    return results

if(__name__=="__main__"):
    test_data = [10, 100, 500]
    results = D255(test_data)
    print(results)
    # ans: [67, 13015, 442011]