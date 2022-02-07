from game.hilo import Hilo


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:

        self.card = 0   # keep the card worth generate for Hilo
        is_playing (boolean): Whether or not the game is being played.
        self.card1= 0 : Card genteradted by Hilo.
        self.card2= 0 : Predicted card by the user.
        self.wonPoints : if the prediction of the user ganme is correct.
        self.lostPoints :  if the prediction of the user ganme is correct.
        score (int): The score for one round of play. Starts with 300 points.

    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card = 0   
        self.is_playing = True  # 
        self.card1= 0
        self.card2= 0
        self.wonPoints = 100
        self.lostPoints = 75
        self.score = 300

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            

    
    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """

        self.card1 = self.do_updates()
        print(f"\n--- Your score is --- : {self.score} points\n")
        print(f"*** Your Initial Card is *** : {self.card1}\n")
        
        card_hand = input("The next card will be [h] high or [l] low? ")
        self.card2 = self.do_updates()
        print(f"\n+++ Your Card was +++ : {self.card2}\n")
        
        if card_hand == 'h' and self.card2 > self.card1 : 
            self.score += self.wonPoints 
            print(f"    Yes, was higher, You win points    \n")
        elif card_hand == 'l' and self.card2 < self.card1 :
            self.score += self.wonPoints
            print(f"    Yes, was lower, You win points    \n")
        else:    
            self.score -= self.lostPoints  
            print(f"    Ouch!, You lose points!    \n")
        print(f"=== Your new score is ==== : {self.score}\n")
        self.is_playing = (input('go y or n: ') == 'y')
        if not self.is_playing:
            return 
       
    def do_updates(self):

        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """

        hilo = Hilo()
        hilo.cardhand()
        self.card = hilo.cardnumber
        
        return self.card


