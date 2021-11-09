try:
    T = int(input())
    for t in range(T):
        
        N, D = tuple(input().split())
        
        N, D = int(N), int(D)
        
        string = str(N)
        
        length = len(string)
        
        original = int(N)
        
        answer = 0
        
        def fun(length, string, D):
            for i in range(length):
                if int(string[i]) == D:
                    string = str(int(string[:i])+1) + "0"*(length-i)
        
        if D == 0:
            for i in range(length):
                if int(string[i]) == D:
                    string = string[:i] + "1"*(length-i)
        elif D == 9:
            
            while "9" in string:
                for i in range(length):
                    if int(string[i]) == D and i == 0:
                        string = "0" + string
                        string = str(int(string[:i+1])+1) + "0"*(length-i)

                    elif int(string[i]) == D:
                        string = str(int(string[:i])+1) + "0"*(length-i)
                        
                        
        else:
            for i in range(length):
                if int(string[i]) == D:
                    string = string[:i] + str(int(string[i])+1) + "0"*(length-i-1)
                
                
        print(int(string) - N)
        
except:
    pass
