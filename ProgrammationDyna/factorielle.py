def fact(n, mem=None):
    if mem == None:
        mem = [None] * (n+1)
    if n == 0:
        return 1
    if mem[n] != None:
        return mem[n]
    mem[n] = n * fact(n-1, mem)
    return mem[n]

print(fact(5))