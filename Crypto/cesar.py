def cypher(key:int, file:str) -> str:
    message = list(open(file, "r").read().lower())
    cyphered = ""
    for element in message:
        if element.isalpha():
            c = chr(ord(element) + key)
            if not c.isalpha():
                c = chr(ord(c) - 26)
        else:
            c = element
        cyphered += c
    open("cyphered.txt", "w").write(cyphered)
    return message, cyphered

def decypher(key:int, file:str) -> str:
    message = list(open(file, "r").read().lower())
    decyphered = ""
    for element in message:
        if element.isalpha():
            c = chr(ord(element) - key)
            if not c.isalpha():
                c = chr(ord(c) + 26)
        else:
            c = element
        decyphered += c
    open("decyphered.txt", "w").write(decyphered)
    return message, decyphered


if __name__ == "__main__":
    print(cypher(3, "text.txt")[1])
    print(decypher(3, "cyphered.txt")[1])