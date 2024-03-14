def tri_fusion(tab):
    """La fonction tri_fusion prend en entrée une liste de nombre entier tab et renvoie une liste triée par ordre croissant"""
    return fusion(tri_fusion(tab[:len(tab)//2]), tri_fusion(tab[len(tab)//2:])) if len(tab) > 1 else tab

def fusion(tab1, tab2):
    """La fonction fusion prend en entrée deux listes de nombre entier tab1 et tab2 et renvoie une liste triée par ordre croissant"""
    n1 = len(tab1)
    n2 = len(tab2)
    if n1 == 0:
        return tab2
    elif n2 == 0:
        return tab1
    else:
        res = []
        i = 0
        j = 0
        while i < n1 and j < n2:
            if tab1[i] < tab2[j]:
                res.append(tab1[i])
                i += 1
            else:
                res.append(tab2[j])
                j += 1
        if i >= n1:
            res += tab2[j:]
        else:
            res += tab1[i:]
        return res


if __name__ == "__main__":
    from random import randrange
    from time import monotonic
    tab = [randrange(100) for _ in range(100)]
    print(tab)
    start = monotonic()
    print(tri_fusion(tab))
    print(monotonic() - start)