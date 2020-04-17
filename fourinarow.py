#------------------------------------------------------------------------------------------------------------------
#   Tic Tac Toe game.
#
#   This code is an adaptation of the Tic Tac Toe bot described in:
#   Artificial intelligence with Python. Alberto Artasanchez and Prateek Joshi. 2nd edition, 2020, 
#   editorial Pack. Chapter 13.
#
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------------------------------------------

from easyAI import TwoPlayersGame, Human_Player, AI_Player, Negamax

#------------------------------------------------------------------------------------------------------------------
#   Class definitions
#------------------------------------------------------------------------------------------------------------------

class FourInARowController(TwoPlayersGame):
    """ Class that is used to play 4 in a row game. """

    def __init__(self, players):
        """ 
            This constructor initializes the game according to the specified players.

            players : The list with the player objects.
        """

        # Define the players
        self.players = players
        self.NUMROWS = 6
        self.NUMCOLS = 7

        # Define who starts the game
        self.nplayer = 1 

        # Define the board
        self.board = [[0] * 7] * 6
    
    def show(self):
        """ This method prints the current game state. """
        print('\n'+'\n'.join([' '.join([['.', 'O', 'X'][self.board[7*j + i]]
                for i in range(7)]) for j in range(6)]))

    def possible_moves(self):
        """ This method returns the possible moves according to the current game state. """ 
               
        return [a + 1 for a in range(self.NUMCOLS) if board[0][a] == '0']
    
    def make_move(self, move):
        """ 
            This method executes the specified move.

            move : The move to execute.
        """
        self.board[int(move) - 1] = self.nplayer

    
    def loss_condition(self):
        """ This method returns whether the opponent has three in a line. """
        possible_combinations = [[1,2,3], [4,5,6], [7,8,9],
            [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

        return any([all([(self.board[i-1] == self.nopponent)
                for i in combination]) for combination in possible_combinations]) 
    
    def is_over(self):
        """ This method returns whether the game is over. """
        return (self.possible_moves() == []) or self.loss_condition()
        
    def scoring(self):
        """ This method computes the game score (-100 for loss condition, 0 otherwise). """
        return -100 if self.loss_condition() else 0

#------------------------------------------------------------------------------------------------------------------
#   Main function
#------------------------------------------------------------------------------------------------------------------
def main():

    # Search algorithm of the AI player
    algorithm = Negamax(7)

    # Start the game
    FourInARowController([Human_Player(), AI_Player(algorithm)]).play()

if __name__ == '__main__':
    main()

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------