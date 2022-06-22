# cook your dish here
k = [10, 12, 20]
f = [34, 8, 50]
dp = dict()

def solve(k, f, i, j):
    
    if i > j:
        return 0
    
    if i == j:
        return f[i]
    
    ans = 1000000007
    
    for x in range(i, j + 1):
        
        if (i, x - 1) in dp:
            a1 = dp[(i, x - 1)]
        else:
            a1 = solve(k, f, i, x - 1)
            dp[(i, x - 1)] = a1
        
        if (x + 1, j) in dp:
            a2 = dp[(x + 1, j)]
        else:
            a2 = solve(k, f, x + 1, j)
            dp[(x + 1, j)] = a2
        
        ans = min(ans, a1 + a2)
        
    ans += sum(f[i:j+1])
    
    return ans

print(solve(k, f, 0, 2))
