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


class File:
    """Une file est définie par sa tete, sa queue et son nombre d'éléments"""
    def __init__(self, tete, queue, nb_elements):
        self.tete, self.queue = tete, queue
        self.taille = 0
        self.file = [self.tete, self.queue, self.taille] + [0] * nb_elements

    def fileVide(self) -> bool:
        return self.taille == 0
    
    def filePleine(self) -> bool:
        return self.taille == len(self.file) - 3

    def enfiler(self, e):
        if self.filePleine():
            return False
        else:
            self.file[self.queue] = e
        if self.queue == len(self.file) - 1:
            self.queue = 3
        else:
            self.queue += 1
            self.taille += 1
        self.file[1] = self.queue
        self.file[2] = self.taille
        return True
    
    def defiler(self):
        self.taille = self.file[2]
        self.tete = self.file[0]
        if self.taille == 0:
            return 'File vide'
        else:
            e = self.file[self.tete]
            if self.tete == len(self.file) - 1:
                self.tete = 3
            else:
                self.tete += 1
            self.taille -= 1
            self.file[0] = self.tete
            self.file[2] = self.taille
            return e
        
    def __str__(self):
        return str(self.file)


if __name__ == "__main__":
    file = File(3, 3, 5)
    print(file)
    print(file.fileVide())
    print(file.filePleine())
    file.enfiler(1)
    file.enfiler(2)
    file.enfiler(3)
    file.enfiler(4)
    file.enfiler(5)
    print(file)
    print(file.defiler())
    print(file)
    print(file.defiler())
    print(file)