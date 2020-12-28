"""
Oxford Dictionnaries has an API to pull what is needed, but it's paid so won't do it!

@author: antho
"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, QInputDialog, QHBoxLayout, 
                             QGroupBox, QVBoxLayout, QLineEdit, QMessageBox, 
                             QGridLayout, QWidget, QPushButton, QDialog)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore
import sys
import string
import Player
import Solution

class GlobalElements():
        special_chars = string.punctuation

class FirstWindow(QDialog): #First window the user opens
    def __init__(self) : #Initiate the window, the size and the UI
        super (FirstWindow, self).__init__()
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("The Hangman")
        self.initUI()
        
    def initUI(self):
        #Put some text in to ask the player what he wants to do
        self.textin = QtWidgets.QLabel(self)
        self.textin.setText("Do you want to start a new Hangman game ?")
        # self.textin.move(50,50)
        
        #Button to start the game
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("New Game")
        # self.b1.move(25,100)
        self.b1.clicked.connect(self.windowMyWindow)
        
        #Button to quit the game
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Quit Game")
        # self.b2.move(125,100)
        self.b2.clicked.connect(self.GameQuit)
        
        #Gridline
        self.horizontalGroupBox = QGroupBox("The Hangman in PYQT5")
        layout = QGridLayout()
        #Sorting the gridlines based on hangman, solution, label from user and the button to enter new stuffs
        layout.addWidget(self.textin, 0,0,1,0)
        layout.addWidget(self.b1, 1,0)
        layout.addWidget(self.b2, 1,1)
        
        self.horizontalGroupBox.setLayout(layout)

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        
        self.show()
    
    def windowMyWindow(self):
        #Function Opening the "MyWindow" class and hiding this one
        self.w = MyWindow()
        self.w.show()
        self.hide()
        
    def GameQuit (self):
        self.close()

class MyWindow(QDialog):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.x = 200
        self.y = 200
        self.Width = 300
        self.Height = 300
        global User 
        User = Player.Player()
        global SolutionMain
        SolutionMain = Solution.solution()
        self.initUI() #All the stuff we're putting inside our window goes in there
        #We refrence self because we're changing the value of the instance instead of changing the value of the "win" object
        #All bottom variables are used later on
        self.resetVariables()

        
    def resetVariables(self) :
        self.UserInput = ""
        self.done1 = True
        self.alreadyThere = False
        
    def initUI(self) :

        self.setGeometry(self.x,self.y,self.Width, self.Height) #Start on top left of the window itself
        self.setWindowTitle("The Hangman")
        
        #Button to enter the input
        self.b1 = QtWidgets.QPushButton(self) #Add a button to the window
        self.b1.setText("Enter a letter") #Set the text inside the button
        self.b1.clicked.connect(self.clicked)#Connects the button to the function below
        
        #Button for the solution
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Solution")
        self.b2.clicked.connect(self.clickedSolution)
        
        #Label that includes what the user did so far
        self.label = QtWidgets.QLabel(self) #You say wheer you want the label to be placed, which is the QMainWindow method
        #It's self because we create an instance of the MyWindow class
        self.label.setText("")
        
        #PlaceHolder for Hungyboi
        self.img = QPixmap("./HangmanPics/6.png")
        self.labelimg = QLabel()
        self.labelimg.setPixmap(self.img)
        
        #PlaceHolder for the word
        self.solution = QtWidgets.QLabel(self)
        self.solution.setText(SolutionMain.hiddenSolution)
        
        #Gridline
        self.horizontalGroupBox = QGroupBox("")
        layout = QGridLayout()
        #Sorting the gridlines based on hangman, solution, label from user and the button to enter new stuffs
        layout.addWidget(self.labelimg, 0,0)
        layout.addWidget(self.solution, 1,0)
        layout.addWidget(self.label,2,0)
        layout.addWidget(self.b1,3,0, 1,2)
        layout.addWidget(self.b2, 3, 2)
        
        self.horizontalGroupBox.setLayout(layout)

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        
        self.show()
    
    def clickedSolution(self) :
        self.errormessage("You choosed to reveal the word : " + SolutionMain.Solution)
        self.solution.setText(SolutionMain.Solution)
        self.b1.setText("Quit the game")
        User.lostGame = True
        User.currentLife = 0
        self.Hangman()
    
    def clicked(self): #When the button is clicked
        if SolutionMain.Solution == SolutionMain.hiddenSolution or User.lostGame == True :
            self.close()
        else :
            self.resetVariables()
            self.UserInput, self.done1 = QInputDialog.getText(self, "Enter your answer", "Letter you want")
            # print(done1) #Done1 is "False" if clicked on "cancel"
            self.inputcheck(self.UserInput, self.done1)
    
    def update(self):
        self.label.adjustSize()#So if you print something bigger than what is was before, it can update itself
        self.solution.adjustSize()
    
    def errormessage(self, errormsg): #Manage the structure of the error message
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle ("ERROR")
        msg.setText(errormsg)
        msg.setStandardButtons (QMessageBox.Ok)
        msg.exec_()
        
    def LostTheGame(self):
        if User.lostGame == True :
            self.errormessage("You Lost the game because you don't have any life left!")
            self.b1.setText("Quit")
        else :
            self.errormessage("The letter wasn't in the word !")
    
    def Hangman(self):
        self.img = QPixmap("./HangmanPics/"+str(User.currentLife)+".png")
        self.labelimg.setPixmap (self.img)
    
    def inputcheck(self, UserInput, done1) : #Function checking if the users actuall input something correct
        # self.alreadyThere = False #Reset to False in order to make sure the letter is there or not
        if any(list(map(lambda char : char in GlobalElements.special_chars, UserInput))) :
            #Check if special character
            self.errormessage("This is a special character!")
        else :
            try :
                #If there's an error, it means it's a letter
                int(self.UserInput)
                self.errormessage("This is not a letter")
            except :
                if done1==True and len(self.UserInput) == 1:
                    #To make sure it's not cancel and there's exactly 1 letter
                    self.UserInput = str(self.UserInput).upper() 
                    for i in User.userInput :
                        #For loop to check if the User already did input that, which will change the value allowing you to change the list
                        if (i == self.UserInput) :
                            self.errormessage("You already put this letter")
                            # print("This is the letter already there",i)
                            self.alreadyThere = True
                            break
                        else :
                            self.alreadyThere = False
                            # print("This is when the letter is not already there")
                    if self.alreadyThere == False :
                        #In case the letter wasn't already there
                        User.userInput.append(self.UserInput)
                        # Replace the label of Player Input
                        self.label.setText(' '.join(str(i) for i in User.userInput))
                        #Raplace the solution
                        SolutionMain.CheckIfInWord(self.UserInput) #len will be 0 if the solution is not inside
                        #Checking if the solution is inside!
                        if len(SolutionMain.LettersIn) == 0:
                            User.loosingLife()
                            self.Hangman()
                            self.LostTheGame()
                        else :
                            self.solution.setText(SolutionMain.hiddenSolution)
                            self.update()
                            if SolutionMain.hiddenSolution == SolutionMain.Solution :
                                self.errormessage("You won the game! CONGRATS !")
                                self.b1.setText("Close to quit the game")
                                
                elif done1 == True and len(self.UserInput) > 1 :
                    self.errormessage("More than 1 letter")
                elif done1 == True and len(self.UserInput) < 1 :
                    self.errormessage("Less than 1 letter")


def window():
    app = QApplication(sys.argv) #know on what OS running and what type of window to open
    win = FirstWindow()
    # win = MyWindow()
    win.show()
    sys.exit(app.exec_())
    
window()