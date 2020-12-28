# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 14:03:14 2020

@author: antho
"""
import random

class solution() :
    def __init__(self):
        # print("Solution class called")
        self.ListOfWords = ["HANGMAN", "AWESOME", "SWISS", "CAT", "FRENCH", "PIE", "CAKE", "ABSOLUTE", "SITH", "JEDI"]
        self.x = 0
        self.hiddenSolution = []
        self.LettersIn = []
        self.RandomiseSolution()
        self.FirstDisplay()
    
    def RandomiseSolution(self):
        # print("Randomise Solution here")
        self.x = random.randint(0, len(self.ListOfWords)-1)
        # print(self.x)
        self.Solution = self.ListOfWords[self.x]
        # print(self.Solution)
        
    def FirstDisplay (self) :
        self.hiddenSolution = "-"*len(self.Solution)
        # print(len(self.Solution))
        # print(self.hiddenSolution)
        
    def CheckIfInWord(self, UserInput):
        # print("Test")
        self.LettersIn = [i for i, e in enumerate(self.Solution) if e == UserInput]
        for i in self.LettersIn :
            self.hiddenSolution = self.hiddenSolution[:i] + UserInput + self.hiddenSolution[i+1:]
        # print(self.LettersIn)
        # print(self.hiddenSolution)