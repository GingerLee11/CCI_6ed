# python3
# master_mind.py - The Game Mastermind. 
# The computer generates a pattern of four colors (the solution) from the available colors: "Red" (R),  "Yellow" (Y), "Green" (G), "Blue" (B)
# and the user attempts to guess the pattern. 
# The computer will then return how many hits and pseudo hits the user had.
# A hit is generated when the guessed color is the same color and in the same spot as the solution.
# A Pseudo hit occurs when the guessed color is present in the solution, but the location is not correct.
# The same slot cannot generate a hit and a pseudo hit. 
# Ex: Guess: RRGG,  
#  Solution: YRBR. 
# This would result in one hit and one pseudo hit.
# The R in the second slot lines up, but the first R, while in the solution is not in the right location.

from random import randint
import pyinputplus as pyip
import re

class Slot:
    """
    Creates the slots for the solution in the Master Mind game.
    """
    def __init__(self, slot_num, color):
        self.number = slot_num
        self.color = color
        self.hit = False
        self.pseudo_hit = False

    
class MasterMind:
    """
    The Game Mastermind. 
    The computer generates a pattern of four colors (the solution) from the available colors: "Red" (R),  "Yellow" (Y), "Green" (G), "Blue" (B)
    and the user attempts to guess the pattern. 
    The computer will then return how many hits and pseudo hits the user had.
    A hit is generated when the guessed color is the same color and in the same spot as the solution.
    A Pseudo hit occurs when the guessed color is present in the solution, but the location is not correct.
    The same slot cannot generate a hit and a pseudo hit. 
    Ex: Guess: RRGG,  
     Solution: YRBR. 
    This would result in one hit and one pseudo hit.
    The R in the second slot lines up, but the first R, while in the solution is not in the right location.
    """
    def __init__(self) -> None:
        self.colors = ['R', 'Y', 'G', 'B']

    def _generate_solution(self):
        """
        Generates a new random solution for each play through.
        """
        solution = []
        colors = self.colors
        for i in range(1, 5):
            indx = randint(0, 3)
            color = colors[indx]
            slot = Slot(i, color)
            solution.append(slot)

        return solution

    def validate_colors(self, text):
        color_regex = re.compile(r"[^RGBY]")
        if len(text) > 4:
            raise Exception("Pattern is too long, must be a combination of four colors.")
        if len(text) < 4:
            raise Exception("Pattern is too short, must be a combination of four colors.")
        mo = color_regex.search(text)
        if mo != None:
            raise Exception("Must only use these four colors: Red (R), Yellow (Y), Green (G), and Blue (B).")


    def play_game(self):
        """
        One player game against the computer.
        """
        solution = self._generate_solution()
        guess = []
        solution_colors = ''
        for slot in solution:
            solution_colors += slot.color 
        print("""
        Welcome to Master Mind!
        Please input a four letter pattern of colors using only these four colors: 
        Red (R), Yellow (Y), Green (G), and Blue (B).
        You are trying to guess the computer generated solution.
        The computer will tell you how many hits and pseudo hits you get correct.
        A hit is generated when the guessed color is the same color and in the same spot as the solution.
        A Pseudo hit occurs when the guessed color is present in the solution, but the location is not correct.
        Good Luck!""")
        # Keep iterating until all the colors have been correctly guessed.
        while guess != solution_colors:
            prompt = "Input a four color pattern like so: RYGB.\n"
            guess = pyip.inputCustom(self.validate_colors, prompt)

            if guess == solution_colors:
                print("You guessed correctly. Congratulations!")
                break
            remainder = ''
            hits, pseudo_hits = 0, 0
            for color, slot in zip(guess, solution):
                if color == slot.color:
                    slot.hit = True
                    hits += 1
                else:
                    remainder += color

            for color in remainder:
                for slot in solution:
                    if color == slot.color and slot.hit == False and slot.pseudo_hit == False:
                        slot.pseudo_hit = True
                        pseudo_hits += 1

            print(f"Hits: {hits}, Pseudo hits: {pseudo_hits}.")

            for slot in solution:
                slot.hit = False
                slot.pseudo_hit = False
            

def example():

    master_mind = MasterMind()
    master_mind.play_game()


if __name__ == "__main__":
    example()
