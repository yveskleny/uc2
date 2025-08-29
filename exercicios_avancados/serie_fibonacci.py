def fibonacci(n_esimo_termo):
    seq = [0 for _ in range(n_esimo_termo)]
        
    for i in range(n_esimo_termo):
        if i == 0:
            seq[i] = 0
        elif i == 1:
            seq[i] = 1
        else:
            seq[i] = seq[i-1] + seq[i-2]
    
    return seq


for i in range(1,20):
    print(fibonacci(i))

