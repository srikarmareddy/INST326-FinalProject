"""Run a UMD trivia game with one player.
"""
import ArgumentParser
import pandas
import sys

class Player:
    """Creates a Player object.
    
        Attributes:
            name (string) - Name of the player.
            score (int) - Current score of the player.
    """
    
    def __init__(self, name, score):
        """ Initalizes the player object

            Args:
                name (String) - Name of the player
                score (Int) - Current score of the player
            Side Effects:
                Sets all attributes for the Player class
        """

        self.name = name
        self.score = score
        
    def getScore(self):
        """ Return the current score of the player

            Returns:
                Return the current highscore for the player
        """

        return self.score
    
    def updateScore(self):
        """ Update the player score

            Side Effect:
                Compares current highscore to most recent score and updates
                the highscore.
        """

        self.score += 1
    
    def resetScore(self):
        """Resets the player's score to zero

            Side Effect:
                the attribute score is set to zero
        """

        self.score = 0

class Questions:
    """Reads in the questions from the given file

        Attributes:
            questions(dict): a dictionary where keys are questions and values are answers
            filename(str): name of the file
    """
    
    def __init__(self, filename):
        """Initiailzes the dictionary of questions

            Args:
                filename(str): name of the file
            
            Side effects:
                reads the given file and puts the data into the questions dictionary
        """
    
    def selectQuestion(self):
       """Selects a random question to ask the player

        Returns:
            returns a tuple with the question and the answer
       """ 

def main():  
    """
    """

def parseargs(arglist):
    """
    """

if __name__ == "__main__":