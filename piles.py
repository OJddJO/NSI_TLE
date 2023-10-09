class Pile:
    """Pile represents a pile of n object, where n is the size of the pile.

    Elements are added to the top of the pile and removed from the top of the pile.
    The pile is empty when the top is 0.

    An empty slot of a pile is represented by None.

    >>> myPile = Pile(5)
    >>> print(myPile)
    [None, None, None, None, None]
    
    >>> myPile.add(1)
    1
    >>> print(myPile)
    [1, None, None, None, None]"""
    def __init__(self, size: int):
        self._size = size
        self._pile = [None] * size
        self._top = 0

    def emptyPile(self) -> bool:
        """Returns True if the pile is empty."""
        return self._top == 0

    def add(self, element) -> object:
        """Adds an element to the top of the pile. Returns the element added."""
        if self._top == self._size:
            raise IndexError("Pile is full.")
        else:
            self._pile[self._top] = element
            self._top += 1
            return element

    def remove(self) -> object:
        """Removes the top element from the pile. Returns the element removed."""
        if self.emptyPile():
            raise IndexError("Pile is empty.")
        else:
            self._top -= 1
            element = self._pile[self._top]
            self._pile[self._top] = None
            return element

    def __str__(self) -> str:
        """Returns a string representation of the pile."""
        return str(self._pile)

    def __len__(self) -> int:
        """Returns the size of the pile."""
        return self._size

    def __iter__(self) -> object:
        """Returns an iterator for the pile."""
        return _PileIterator(self._pile, self._top)


class _PileIterator:
    """An iterator for the pile."""
    def __init__(self, pile, top):
        self._pile = pile
        self._top = top
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._top:
            element = self._pile[self._index]
            self._index += 1
            return element
        else:
            raise StopIteration


if __name__ == '__main__':
    pile = Pile(5)
    print(pile.emptyPile())
    pile.add(1)
    pile.add(2)
    pile.add(3)
    print(pile)
    print(pile.remove())
    print(pile)
    print(pile.emptyPile())
    print(len(pile))
    for element in pile:
        print(element)
    print(pile)
    pile.add(4)
    pile.add(5)
    print(pile)
    print(pile.remove())
    print(pile)