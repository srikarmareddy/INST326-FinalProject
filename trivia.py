"""Run a UMD trivia game with one player.
"""
from argparse import ArgumentParser
import json
import pandas as pd
import sys
import random
import matplotlib.pyplot as plt


class Player:
    """Creates a Player object.
    
        Attributes:
            name (string) - Name of the player.
            score (int) - Current score of the player.
    """
    
    def __init__(self, name = "Bob", score = 0):
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
        to_return = self.score
        return to_return
    
    
    def updateScore(self):
        """ Update the player score

            Side Effect:
                Compares current highscore to most recent score and updates
                the highscore.
        """

        self.score += 1
    
    def resetScore(self, name):
        """
        """

        self.score = 0

class Questions:
    """Reads in the questions from the given file

        Attributes:
            questions(dict): a dictionary where keys are questions and values are answers
    """
    
    def __init__(self, filename):
        """Initiailzes the dictionary of questions

            Args:
                filename(str): name of the file
            
            Side effects:
                reads the given file and puts the data into the questions dictionary
        """

        with open(filename, "r", encoding="utf-8") as f:
            questiondata = json.load(f)
            self.questions = questiondata['questions']
    
    def selectQuestion(self):
       """Selects a random question to ask the player

        Returns:
            returns a tuple with the question and the answer
       """
       question = random.choice(list(self.questions)) 
       answer = self.questions[question]
       del self.questions[question]
       tuple_return = (question, answer)
       return tuple_return

def main(filepath, name):  
    """
    Starts and hosts a new trivia game
    
    Args:
        name (string): name of the player
        filepath (string): string containing a filepath to questions and answers
        
    Side effects: prints the player's current score and high score to stdout
    """

    trivia_questions = Questions(filepath)
    player1 = Player(name)
    length = len(trivia_questions.questions)
    while length != 0:
        q = trivia_questions.selectQuestion()
        print(q[0])
        response = input("What is your answer? ")
        if q[1] == response:
            player1.updateScore()
            print("Correct!")
        else:
            print(f"Incorrect! The Answer is {q[1]}.")   
        length-=1
        print(f"Current Score: {player1.getScore()}")
    print(f"{name} scored {player1.getScore()} points")
    print("")

    df = pd.read_csv('trivia.csv')
    highscore = df.sort_values('score', ascending = False)
    print(highscore)

    plt.bar(df["name"], df["score"], data = df)
    plt.title("highscore", fontsize = 14)
    plt.xlabel('Name', fontsize = 14)
    plt.ylabel('Score', fontsize = 14)
    plt.show()

def parseargs(arglist):
    """
    Parses through command-line arguments
    
    Args:
         arglist (list): a list of command-line arguments
         
    Returns: parsed arguments, as a namespace
    """

    parser = ArgumentParser()
    parser.add_argument("filepath", type=str,help="Path to the json file")
    parser.add_argument("name", type=str, help="name of the person compete in the triva")

    args = parser.parse_args(arglist)
    return args
    
if __name__ == "__main__":
    args = parseargs(sys.argv[1:])
    main(args.filepath, args.name)