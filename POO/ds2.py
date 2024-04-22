class Satellite:
    def __init__(self, name, masse = 2000, vitesse = 0):
        self.name, self.masse, self.vitesse = name, masse, vitesse

    def impulsion(self, force, duree):
        self.vitesse += force * duree / self.masse

    def energie(self):
        return self.masse * self.vitesse**2 / 2
    
    def affiche_vitesse(self):
        print(f"Nom: {self.name}, vitesse: {format(self.vitesse, '.2f')}m/s")
    
    def affiche_energie(self):
        #format to 2 decimals
        print(f"Nom: {self.name}, energie: {format(self.energie(), '.2f')}J")
    
    def __str__(self):
        return f"Nom: {self.name}, masse: {self.masse}kg, vitesse: {format(self.vitesse, '.2f')}m/s"
    
class TGV:
    def __init__(self, numero:int, arrets:list[str], horaires:list[int]):
        if type(numero) != int:
            raise TypeError("numero must be int")
        if len(arrets) != len(horaires):
            raise ValueError("arrets and horaires must have the same length")
        if type(arrets) != list:
            raise TypeError("arrets must be list")
        if type(horaires) != list:
            raise TypeError("horaires must be list")
        for element in arrets:
            if type(element) != str:
                raise TypeError("arrets must be list of str")
        for element in horaires:
            if type(element) != int:
                raise TypeError("horaires must be list of int")
        self.numero, self.arrets, self.horaires = numero, arrets, horaires

    def getArrets(self):
        return self.arrets

    def heurePassage(self, arret:str)->int:
        try:
            return self.horaires[self.arrets.index(arret)]
        except ValueError:
            return -1

    def duree(self, arret1:str, arret2:str)->int:
        if arret1 not in self.arrets or arret2 not in self.arrets:
            return -1
        else:
            return abs(self.heurePassage(arret2) - self.heurePassage(arret1))
        
    def String_to_String(self) -> str:
        depart, arrive = self.arrets[0], self.arrets[-1]
        return f'{self.numero}: {depart} {self.heurePassage(depart)} -> {arrive} {self.heurePassage(arrive)}'
    
    def nbIntersection(self, other)->int:
        i = 0
        for element in self.arrets:
            if element in other.getArrets():
                i += 1
        return i

    
if __name__ == "__main__":
    # s1 = Satellite('Eutlesat W3', 4400, 10)
    # s2 = Satellite('Ariane5', 750, 80)
    # s1.impulsion(100, 10)
    # s2.impulsion(100, 10)
    # s1.affiche_vitesse()
    # s2.affiche_vitesse()
    # s1.affiche_energie()
    # s2.affiche_energie()
    # #test __str__
    # print(s1)
    # print(s2)

    tgv1 = TGV(8505, ["Bordeaux", "Dax", "Bayonne", "Biarritz", "Saint-Jean-de-Luz", "Hendaye", "Irun"], [625, 697, 730, 742, 755, 767, 774])
    tgv2 = TGV(8506, ["Bordeaux", "Pessac", "Morcenx", "Dax", "Labenne", "Bayonne", "Biarritz", "Saint-Jean-de-Luz", "Irun"], [625, 652, 678, 697, 710, 730, 742, 755, 774])
    print(tgv2.nbIntersection(tgv1))
    print(tgv1.duree("Bordeaux", "Bayonne"))
    print(tgv1.String_to_String())

