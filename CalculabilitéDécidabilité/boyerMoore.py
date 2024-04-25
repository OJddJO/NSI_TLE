def jumpDict(key:str) -> dict[str:int]:
    jumps = {}
    for i in range(len(key)-1, -1, -1):
        if key[i] not in jumps:
            jumps[key[i]] = len(key) - i
    return jumps

def boyerMoore(text, key):
    jumps = jumpDict(key)
    for i in range(len(text)-len(key)+1):
        found = True
        for j in range(len(key)):
            if text[i+j] != key[j]:
                if text[i+j] in jumps:
                    i += jumps[text[i+j]]
                else:
                    i += len(key)
                found = False
                break
        if found:
            return i
    return -1


print(boyerMoore("lkjfljkqhlhgjlkfjbjlefkvqioefhqjbfvkjzhepfiojhdqkjvhqkjzhdlijfqlkzje", "jbf"))