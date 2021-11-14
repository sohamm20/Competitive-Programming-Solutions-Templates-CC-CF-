for t in range(int(input())):
    S = str(input())
    
    S = list(S)
    
    F = str(input())
    
    F = list(F)
    
    count = 0
    
    for i in S:
        dis = 26
        for j in F:
           dis = min(dis, min(abs(ord(j) - ord(i)), 26 - abs(ord(j) - ord(i)))) 
        count += dis
    print("Case #{}: {}".format(t + 1, count))
