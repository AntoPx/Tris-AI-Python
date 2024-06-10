import math
import random

class Tris:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Inizializza la tavola di gioco vuota
        self.current_winner = None

    def print_board(self):
        # Stampa la tavola di gioco attuale
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # Stampa i numeri di riferimento delle caselle
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # Restituisce le mosse disponibili
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        # Restituisce True se ci sono caselle vuote, altrimenti False
        return ' ' in self.board

    def num_empty_squares(self):
        # Restituisce il numero di caselle vuote
        return self.board.count(' ')

    def make_move(self, square, letter):
        # Effettua una mossa sulla casella specificata
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Controlla se c'è un vincitore dopo la mossa
        # Controlla le righe
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        # Controlla le colonne
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # Controlla le diagonali
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # Diagonale principale
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # Diagonale secondaria
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

class AIPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            return random.choice(game.available_moves())  # Scegli una mossa casuale se è il primo turno

        # Utilizza l'algoritmo Minimax con potatura alfa-beta per determinare la mossa migliore
        square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        # Implementazione dell'algoritmo Minimax con potatura alfa-beta
        max_player = self.letter  # L'IA è il giocatore massimo
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                    state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # Inizializza il punteggio massimo
        else:
            best = {'position': None, 'score': math.inf}  # Inizializza il punteggio minimo

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # Simula una partita utilizzando ricorsione

            # Undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score  # Massimizza il punteggio
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score  # Minimizza il punteggio

        return best

class HumanPlayer:
    def get_move(self, game):
        # Ottiene la mossa dall'utente
        valid_square = False
        val = None
        while not valid_square:
            square = input("Enter your move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val

def play(game, x_player, o_player, print_game=True):
    # Funzione principale per giocare una partita
    if print_game:
        game.print_board_nums()

    letter = 'X'  # Il giocatore X inizia sempre per convenzione

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')  # Linea vuota per chiarezza

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # Fine del gioco
            letter = 'O' if letter == 'X' else 'X'  # Cambia il turno

        if print_game:
            print('It\'s a tie!')
    return 'tie'

def main():
    x_player = HumanPlayer()
    o_player = AIPlayer('O')  # L'IA sarà il secondo giocatore
    t = Tris()
    play(t, x_player, o_player, print_game=True)


if __name__ == "__main__":
    main()
