class Move:
    """A maneuver in the game. The responsibility of Move is to keep track of the stones to remove and which guess to remove them from.
    
    Stereotype: 
        Information Holder

    Attributes:
        _guess (string): The string to remove from.
    """
    def __init__(self, guess):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._guess = guess

    def get_guess(self):
        """Returns the guess to remove from.

        Args:
            self (Move): an instance of Move.
        """
        return self._guess
