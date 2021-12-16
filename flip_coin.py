# Coin Flip Simulator against Computer

from random import choice
class Coin():

    def __init__(self, first_flip):
        self.options = ('heads', 'tails')
        self.flip = first_flip.lower() # Stores the first flip to compare to computer flip


    def play(self): # Flips a coin
         # Choose computer flip from remaining option
        coin_flip = choice(self.options) # Choose either heads or tails randomly
        return True if coin_flip == self.flip else False


    def run_dialogue(self):
        self.comp_flip = self.options[0] if self.flip == self.options[1] else self.options[1]
        print(f"You chose {self.flip.capitalize()} and the computer's choice was {self.comp_flip.capitalize()}.") 
        verdict = self.play() # Input the user's choice and flip the coin. Take the verdict to return the result
        if verdict:
            print(f'{self.flip.capitalize()} wins. Congratulations!')
        else:
            print(f'{self.comp_flip.capitalize()} wins. Try again!')
        return
    
    def replay(self, new_roll): # Re-sets the variables if the user wants to play again
        self.flip = new_roll


if __name__ == "__main__":
    coin_start = Coin(input("Heads or tails? "))
    while True:
        coin_start.run_dialogue()

        replay = input("Play again? Y/N: ")
        if replay == "N":
            break
        coin_start.replay(input("Heads or tails? "))
    



