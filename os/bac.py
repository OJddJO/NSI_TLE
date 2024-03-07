def recherche(tab: list[int]) -> list[tuple[int, int]]:
	"""La fonction recherche prend en entrée une liste de nombre entier tab et renvoie une liste de tuple des couples d'entiers consécutifs successifs
	qu'il peut y avoir dans tab"""
	out = []
	for i in range(len(tab)-1):
		if tab[i]+1 == tab[i+1]:
			out.append((tab[i], tab[i+1]))
	print(out)
	
def recherche1(tab):
	print([(tab[i], tab[i+1]) for i in range(len(tab)-1) if tab[i]+1 == tab[i+1]])


def propager(M: list[list[int]], i: int, j: int, val: int) -> None:
	if M[i][j] == 0:
		return
	M[i][j] = val
	if (i-1) >= 0 and M[i-1][j] == 1:
		propager(M, i-1, j, val)
	if (i+1) < len(M) and M[i][j-1] == 1:
		propager(M, i+1, j, val)
	if (j-1) >= 0 and M[i][j-1] == 1:
		propager(M, i, j-1, val)
	if (j+1) <= len(M) and M[i][j+1] == 1:
		propager(M, i, j+1, val)


if __name__ == "__main__":
	recherche1([1, 4, 3, 5])
	recherche1([1, 4, 5, 3])
	recherche1([7, 1, 2, 5, 3, 4])
	recherche1([5, 1, 2, 3, 8, -5, -4, 7])
	
	M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
	propager(M, 2, 1, 3)
	print(M)
