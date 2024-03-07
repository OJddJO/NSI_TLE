def delta(tab):
	"""Renvoie la liste tab compressé avec le delta encoding"""
	out = [tab[0]]
	for i in range(1, len(tab)):
		out.append(tab[i] - tab[i-1])
	return out

print(delta([1000, 800, 802, 1000, 1003]))

class Noeud:
	"""Classe Noeud qui permet d'implémenter une structure"""
	def __init__(self, left=None, valeur = None, right=None):
		self.left = left
		self.valeur = valeur
		self.right = right
	
	def est_une_feuille(self):
		"""Renvoie True si et seulement si le noeud est une feuille"""
		return self.left is None and self.right is None

def expression_infixe(e):
	s = ""
	if e.left is not None:
		s = str(s) + str(expression_infixe(e.left))
	s = str(s) + str(e.valeur)
	if e.right is not None:
		s = str(s) + str(expression_infixe(e.right))
	if e.est_une_feuille():
		return s
	return '('+s+')'

e = Noeud(Noeud(Noeud(None, 3, None), '*', Noeud(Noeud(None, 8, None), '+', Noeud(None, 7, None))), '-', Noeud(Noeud(None, 2, None), '+', Noeud(None, 1, None)))
print(expression_infixe(e))


