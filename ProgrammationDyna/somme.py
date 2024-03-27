def sommeDyna(n: int, mem=None) -> int:
    if mem == None:
        mem = [None] * (n+1)
    if n == 0:
        return 0
    if mem[n] != None:
        return mem[n]
    mem[n] = n + sommeDyna(n-1, mem)
    print(mem)
    return mem[n]

if __name__ == "__main__":
    n = 5
    print(sommeDyna(n))