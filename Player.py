# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 16:23:24 2020

@author: antho
"""

class Player() :
    def __init__(self) :
        self.lifeMax = 6
        self.currentLife = self.lifeMax
        self.userInput = []
        self.lostGame = False
    
    def loosingLife(self) :
        self.currentLife -= 1
        self.Lost()
    
    def Lost(self) :
        if self.currentLife == 0:
            self.lostGame = True