class Mammiferes:
    def __init__(self, nbEnfants):
        self.reproduction = "vivipare"
        self.nbenfants = nbEnfants

    def afficheEnfants(self):
        print("Nombre d'enfants : ", self.nbenfants)

class Herbivores(Mammiferes):
    def __init__(self, nbEnfants):
        super().__init__(nbEnfants)
        self.nourriture = "vegetaux"
    def affiche(self):
        print("Nourriture : ", self.nourriture)

class Carnivores(Mammiferes):
    def __init__(self, nbEnfants):
        super().__init__(nbEnfants)
        self.nourriture = "viande"
    def affiche(self):
        print("Nourriture : ", self.nourriture)

class Loups(Carnivores):
    def __init__(self, nbEnfants, taille, masse):
        super().__init__(nbEnfants)
        self.cri, self.taille, self.masse = "Hurlement", taille, masse

    def affiche(self):
        print("Cri : ", self.cri)
        print("Taille : ", self.taille)
        print("Masse : ", self.masse)
        print("Reproduction : ", self.reproduction)
        self.afficheEnfants()
        super().affiche()

if __name__ == "__main__":
    loup = Loups(5, 1.5, 50)
    loup.affiche()

