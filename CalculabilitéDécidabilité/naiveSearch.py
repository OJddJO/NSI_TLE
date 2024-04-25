def naiveSearch(text:str, key:str) -> bool:
    '''Search the key in text, if key is in text return the index of the first occurence, else return -1'''
    if len(text) < len(key):
        return -1
    for i in range(len(text)):
        if len(text[i:]) < len(key):
            return -1
        found = True
        for j in range(len(key)):
            if text[i+j] != key[j]:
                found = False
                break
        if found:
            return i
    return -1

print(naiveSearch("lkjfljkqhlhgjlkfjbjlefkvqioefhqjbfvkjzhepfiojhdqkjvhqkjzhdlijfqlkzje", "jbf"))