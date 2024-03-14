def rendue_monnaie_rec(pieces, a_rendre): #Force brute
    if a_rendre == 0:
        return 0
    else:
        mini = 9999
        for i in range(len(pieces)):
            if pieces[i] <= a_rendre:
                nb = 1 + rendue_monnaie_rec(pieces, a_rendre-pieces[i])
                if nb < mini:
                    mini = nb
    return mini


def rendue_monnaie_dynamique(pieces, a_rendre, rendu_memo=None):
    if rendu_memo is None:
        rendu_memo = [0]*(a_rendre+1)
    if a_rendre == 0:
        return 0
    elif rendu_memo[a_rendre] > 0:
            return rendu_memo[a_rendre]
    else:
        mini = 9999
        for i in range(len(pieces)):
            if pieces[i] <= a_rendre:
                nb = 1 + rendue_monnaie_dynamique(pieces, a_rendre-pieces[i], rendu_memo)
                if nb < mini:
                    mini = nb
                    rendu_memo[a_rendre] = mini
        return mini

if __name__ == "__main__":
    print(rendue_monnaie_rec([2, 5, 10], 11))
    print(rendue_monnaie_dynamique([2, 5, 10], 11))