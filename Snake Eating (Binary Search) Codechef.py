try:
    
    import sys
    input=sys.stdin.readline
    
    def req():
        return K*(j - m) - (prefix_sum[j - 1] - prefix_sum[m - 1])
    
    import bisect
    T = int(input())
    for t in range(T):
        
        N, Q = map(int, input().split())
        
        L = list(map(int, input().split()))
        
        L.sort()
        
        length = len(L)
        
        prefix_sum = [L[0]]
        for i in range(1, N):
            prefix_sum.append(prefix_sum[i - 1] + L[i])
            
            
        # print(prefix_sum)
        
        for q in range(Q):
            
            K = int(input())
            
            if L[0] > K:
                print(length)
                continue
            
            j = bisect.bisect_left(L, K)
            
            l = 0
            r = int(j)
            
            count = length - j
            
            while r - l > 1:
                m = (l + r) // 2
                
                temp = req()
                
                if m >= req():
                    r = int(m)
                else:
                    l = int(m)
            
            if r < j:
                count += (j - r)
            
            print(count)
            
except:
    pass
