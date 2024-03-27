def fibo(n, mem=None):
    if mem == None:
        mem = ([None] * (n+1))
    if n == 0:
        return 0
    if n == 1:
        return 1
    if mem[n] != None:
        return mem[n]
    mem[n] = fibo(n-1, mem) + fibo(n-2, mem)
    return mem[n]

print(fibo(7))