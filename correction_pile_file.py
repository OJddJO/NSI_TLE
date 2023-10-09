#correction la plus éclatée possible

class Pile:
    def __init__(self, taille):
        self.nb_elements = taille
        self.pile = [0] * taille
        self.pile[0] = 1

    def pileVide(self) -> bool:
        return self.pile[0] == 1

    def empiler(self, alpha):
        if self.nb_elements == self.pile[0]:
            return False
        else:
            self.pile[self.pile[0]] = alpha
            self.pile[0] += 1
            return True
    
    def depiler(self):
        if self.pileVide():
            return False
        else:
            self.pile[0] -= 1
            return True
    
    def __str__(self):
        return str(self.pile[1:self.pile[0]-1])
    

if __name__ == "__main__":
    pile = Pile(5)
    print(pile.pileVide())
    pile.empiler(1)
    pile.empiler(2)
    pile.empiler(3)
    print(pile)
    print(pile.depiler())
    print(pile)
    print(pile.pileVide())
    print(pile)
    pile.empiler(4)
    pile.empiler(5)
    print(pile)
    print(pile.depiler())
    print(pile.pile)
    print(pile.pile[0])
    print(pile)

