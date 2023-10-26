def mi():
    return map(int, input().split())
def li():
    return list(mi())
def si():
    return str(input())
def ni():
    return int(input())

for t in range(int(input())):
    
    n, k = map(int, input().split())
    
    A = list(map(int, input().split()))
    
    edges = dict()
    SUM = dict()
    
    g = []
    
    for i in range(n + 1):
        g.append([])
    
    for i in range(n - 1):
        
        x, y = map(int, input().split())
        
        edges[(x, y)] = -1
        edges[(y, x)] = -1
        
        SUM[(x, y)] = -1
        SUM[(y, x)] = -1
        
        # edges.append((x, y))
        # edges.append((y, x))
        
        g[x].append(y)
        g[y].append(x)
        
    
    
    def dfs(a, b):
        
        # if edges[(a, b)] != -1:
        #     return 
        #     return edges[(a, b)]
        
        s = int(A[b - 1])
        
        ans = 0
        
        for i in g[b]:
            if i != a:
                
                dfs(b, i)
                
                s += SUM[(b, i)]
                ans += edges[(b, i)]
        
        edges[(a, b)] = ans + s
        SUM[(a, b)] = int(s)
        
        # return s
        
    for i in edges:
        if edges[i] == -1:
            
            dfs(i[0], i[1])
    
    # print(edges)
    
    final = []
    
    for i in range(1, len(g)):
        
        curr = 0
        for j in range(len(g[i])):
            curr += edges[(i, g[i][j])]
            
        final.append(curr)
    
    final.sort()
    # print(final)
    
    print(final[k - 1])
    
    # Finally print the answer
    
