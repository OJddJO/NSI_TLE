alphaNum={'0' :0,'1' :1,'2' :2,"3" :3,"4" :4,"5" :5,"6" :6,"7" :7,"8" :8,'9' :9,
'a' :10,'b' :11,'c' :12,'d' :13,'e' :14,'f' :15,'g' :16,'h' :17,'i' :18, 'j' :19,'k' :20,'l' :21,'m' :22,
'n' :23,'o' :24,'p' :25,'q' :26,'r' :27,'s' :28, 't' :29,'u' :30,'v' :31,'w' :32,'x' :33,'y' :34,'z' :35}

def vigenere(msg:str, mdp:str) -> str:
    '''Chiffre un message avec le chiffre de Vigenère'''
    msg, mdp = msg.lower(), mdp.lower()
    code = ""
    n = 0
    for i in range(len(msg)):
        if msg.isalnum():
            code += list(alphaNum)[(alphaNum[msg[i]] + alphaNum[mdp[n]])%36]
            n = 0 if n >= len(mdp)-1 else n+1
        else:
            code += msg[i]
    return code

def decodeVigenere(msg:str, mdp:str) -> str:
    '''Déchiffre un message avec le chiffre de Vigenère'''
    msg, mdp = msg.lower(), mdp.lower()
    code = ""
    n = 0
    for i in range(len(msg)):
        if msg.isalnum():
            code += list(alphaNum)[(alphaNum[msg[i]] - alphaNum[mdp[n]])%36]
            n = 0 if n >= len(mdp)-1 else n+1
        else:
            code += msg[i]
    return code

print(vigenere("Hello", "nsi"))
print(decodeVigenere("4638g", "nsi"))