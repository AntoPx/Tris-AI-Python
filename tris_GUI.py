import tkinter as tk
from tkinter import messagebox
from tris_logic_AI import Tris, HumanPlayer, AIPlayer

class TrisGUI:
    def __init__(self, master):
        # Inizializzazione dell'interfaccia grafica e del gioco Tris
        self.master = master
        self.tris_game = Tris()  # Creazione di un'istanza del gioco Tris
        self.x_player = HumanPlayer()  # Giocatore X (umano)
        self.o_player = AIPlayer('O')  # Giocatore O (AI)
        self.buttons = []  # Lista per memorizzare i pulsanti della griglia

        # Creazione dei pulsanti della griglia 3x3
        for i in range(3):
            row = []
            for j in range(3):
                # Crea un pulsante associato alla cella (i, j) della griglia
                button = tk.Button(master, text='', font=('Helvetica', 20), width=5, height=2,
                                   command=lambda i=i, j=j: self.make_move(i * 3 + j))
                button.grid(row=i, column=j)  # Posiziona il pulsante nella finestra
                row.append(button)
            self.buttons.append(row)

        # Creazione del pulsante di reset
        self.reset_button = tk.Button(master, text='Reset', command=self.reset_game)
        self.reset_button.grid(row=3, columnspan=3)  # Posiziona il pulsante di reset nella finestra

    def make_move(self, square):
        # Funzione chiamata quando un giocatore fa una mossa
        if self.tris_game.make_move(square, 'X'):
            # Aggiorna l'interfaccia grafica se la mossa è valida
            self.buttons[square // 3][square % 3].config(text='X', state='disabled')
            if not self.tris_game.current_winner:
                self.ai_move()  # Se la partita non è finita, è il turno dell'AI
            else:
                self.end_game()  # Se la partita è finita, mostra il risultato

    def ai_move(self):
        # Funzione per la mossa dell'AI
        if self.tris_game.empty_squares():
            square = self.o_player.get_move(self.tris_game)  # Ottiene la mossa dall'AI
            if self.tris_game.make_move(square, 'O'):
                # Aggiorna l'interfaccia grafica con la mossa dell'AI
                self.buttons[square // 3][square % 3].config(text='O', state='disabled')
            if self.tris_game.current_winner:
                self.end_game()  # Se la partita è finita, mostra il risultato

    def end_game(self):
        # Funzione chiamata alla fine della partita
        if self.tris_game.current_winner == 'tie':
            messagebox.showinfo("Game Over", "It's a tie!")  # Messaggio di pareggio
        else:
            winner = "You" if self.tris_game.current_winner == 'X' else "AI"
            messagebox.showinfo("Game Over", f"{winner} wins!")  # Messaggio di vincita
        self.disable_buttons()  # Disabilita i pulsanti dopo la fine della partita

    def disable_buttons(self):
        # Funzione per disabilitare tutti i pulsanti della griglia
        for row in self.buttons:
            for button in row:
                button.config(state='disabled')
        #Non disabilitare il pulsante di reset
        self.reset_button.config(state='normal')  # Abilita il pulsante di reset

    def reset_game(self):
        # Funzione per riavviare il gioco
        self.tris_game = Tris()  # Resetta lo stato del gioco
        for i in range(3):
            for j in range(3):
                #Resetta i testi dei pulsanti e li abilita
                self.buttons[i][j].config(text='', state='normal')
        #self.reset_button.config(state='disabled')  # Disabilita il pulsante di reset


def main():
    root = tk.Tk()  # Crea la finestra principale
    root.title("Tris")  # Imposta il titolo della finestra
    tris_gui = TrisGUI(root)  # Crea un'istanza dell'interfaccia grafica del gioco Tris
    root.mainloop()  # Avvia il ciclo di eventi della finestra


if __name__ == "__main__":
    main()
