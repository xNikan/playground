# Coin Flip Simulator against Computer, Nikan Taheri - December 16, 2021

from tkinter import *
from tkinter import ttk
from random import choice
from tkinter.messagebox import showinfo

# FUTURE VERSIONS SHOULD INCLUDE TRY/EXCEPT CLAUSES. NO ERROR HANDLING FEATURES YET.

class Window(Tk):
    """ 
    Window class using Tkinter. Runs the window and sets up the game. Uses the Coin class
    to perform the coin toss 
    """
    def __init__(self):
        Tk.__init__(self)   
        
        # Window
        self.title("Coin Flip") 
        self.geometry('800x500')
        self.configure(background='lightblue')
        
        # Label
        self.label = Label(self, text= "Welcome to Heads or Tails: The Coin Simulator", fg='red', font=('Helvetica", 20')) 
        #self.label.place(x=60,y=50)
        self.label.pack(padx=60, pady=50)

        # Button to prompt user to flip the coin 
        self.button = Button(self, text="Click me to flip the coin", command=self.coin_flip)
        self.button.pack() 
        
        # Radiobuttons (2)
        self.var = StringVar(value=1) # Need to do some more research on this. Not completely sure how it works
        self.heads = Radiobutton(self, text="Heads", variable = self.var,value="Heads", command=self.button_selected)#, tristatevalue=0)#.deselect()
        self.tails = Radiobutton(self, text= 'Tails', variable= self.var, value="Tails", command=self.button_selected)#, tristatevalue=0)#.deselect()
        self.heads.place(x=360, y=200)
        self.tails.place(x=360, y=240)

    def coin_flip(self): 
        """
        Calls the Coin class and shows the results to the user
        """
        flipped = Coin(self.button_selected())
        result = flipped.run_dialogue()            # Tuple type to choose [0] = first dialogue, [1] = winner
        
        showinfo(title=result[0], message=result[1])
    
    def button_selected(self):
        """
        When the user clicks the button, Tkinter returns the option they chose from the Radiobutton (heads/tails).
        """
        return self.var.get()
    

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
        chosen_val = f"You chose {self.flip.capitalize()}."
        
        # Input the user's choice and flip the coin. Take the verdict to return the result
        verdict = self.play() 
        if verdict:
            return (chosen_val, f'{self.flip.capitalize()} wins. Congratulations!')
        else:
            return (chosen_val, f'{self.comp_flip.capitalize()} wins. Try again!')
        
   
    # Not needed with the new implementation of Tkinter
    """
    def replay(self, new_roll): # Re-sets the variables if the usetailsr wants to play again
        self.flip = new_roll"""


if __name__ == "__main__":
    main = Window()
    main.mainloop()
    
    # No longer needed with Tkinter
    """
    coin_start = Coin(input("Heads or tails? "))
    while True:
        coin_start.run_dialogue()

        replay = input("Play again? Y/N: ")
        if replay == "N":
            break
        coin_start.replay(input("Heads or tails? "))"""
    



