import random

class Hilo:
    """Individual cards are represented as a number from 1 to 13..

    The responsibility of hilo is to keep track of the one ramdom card between 1 through 13 up and calculate the points for 
    it.
   
    Attributes:
        cardNumber (int): The card number.
    """

    def __init__(self):
        """Constructs a new instance of Hilo.

        Args:
            self (Hilo): An instance of Hilo.
        """
        self.cardnumber = 0 # store de data for intearcting with the user

    def cardhand(self):
        """Generates a new random value and calculates the points for the dice.
        
        Args:
            self (Hilo): An instance of Hilo.
        """                                    
        self.cardnumber = random.randint(1, 13)   
