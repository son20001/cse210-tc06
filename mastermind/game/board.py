import random

class Board:
    """A designated playing surface. The responsibility of Board is to keep track of the pieces in play.
    
    Stereotype: 
        Information Holder

    Attributes:
        _piles (list): The number of piles of stones.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._code = ""
        self._prepare()
    def to_string(self, roster):
        """Converts the board data to its string representation.

        Args:
           self (Board): an instance of Board.

        Returns:
            string: A representation of the current board.
        """ 
        text = '\n--------------------'
        player = roster.get_current()
        player_name = player.get_name()
        move = player.get_move()
        if move is None:
            text += (f'\nPlayer{player_name}: ----, ****  ')
        else:
            guess = move.get_guess()
            hint = self._create_hint(self._code, guess)
            text += (f'\nPlayer{player_name}: {guess}, {hint}  ')            

        roster.next_player()
        player = roster.get_current()
        player_name = player.get_name()
        move = player.get_move()
        if move is None:
            text += (f'\nPlayer {player_name}: ----, ****  ')
        else:
            guess = move.get_guess()
            hint = self._create_hint(self._code, guess)
            text += (f'\nPlayer {player_name}: {guess}, {hint}  ')            

        text += '\n--------------------'
        roster.next_player()
        return text
        

    def _create_hint(self, code, guess):
        """Generates a hint based on the given code and guess.

        Args:
            self (Board): An instance of Board.
            code (string): The code to compare with.
            guess (string): The guess that was made.

        Returns:
            string: A hint in the form [xxxx]
        """ 
        hint = ""
        for index, letter in enumerate(guess):
            if code[index] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        return hint
    
    def is_win(self, roster):
        """Determines if all the stones have been removed from the board.
        
        Args:
            self (Board): an instance of Board.

        Returns:
            boolean: True if the board has no stones on it; false if otherwise.
        """
        player = roster.get_current()
        guess = player.get_move().get_guess()
        if guess == self._code:
            return True
        else:
            return False

    def _prepare(self):
        """Sets up the board with a random number of piles containing a random 
        number of stones.
        
        Args:
            self (Board): an instance of Board.
        """
        for n in range(4):
            self._code += str(random.randint(1, 9))