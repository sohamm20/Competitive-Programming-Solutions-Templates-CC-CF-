for t in range(int(input())):
    N = int(input())

    P = str(input())

    P = list(P)

    dic = {"U": ["U"], "R": ["R"], "Y": ["Y"], "B": ["B"], "O": ["R", "Y"], "P": ["R", "B"],
           "G": ["Y", "B"], "A" : ["R", "Y", "B"]}

    for i in range(N):
        P[i] = dic.get(P[i])
    
    count = 0
    
    for i in ["R", "Y", "B"]:
        
        j = 0
        while True:  
            
            if j == N:
                break
            
            if i in P[j]:
                count += 1
                while True:
                    if j == N:
                        break
                    if i not in P[j]:
                        break
                    j += 1
                    
            else:
                j += 1
    print("Case #{}: {}".format(t + 1, count))
    
