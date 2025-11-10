import customtkinter as ctk
import tkinter as tk
import random
from logic import *
from app import *
from logic import *
from PIL import Image

class windows:
    def __init__ (self, root):
        """Initialize the window class."""
        self.root = root
        self.mode = ""
        self.num1, self.num2, self.num3, self.num4, self.operator, self.answer, self.currentOp, self.currentMode, self.xPos, self.xNeg = None, None, None, None, None, None, None, None, None, None



    def settingsWindow(self):
        settingsFrame = ctk.CTkFrame(self.root, corner_radius = 15)
        settingsFrame.grid(row=0, column=0, padx=20, pady=20)
        def goBack():
            """Go Back"""
            settingsFrame.grid_forget()
            self.root.firstWindow()
        backButton = ctk.CTkButton(settingsFrame,
                                text = "Back",
                                width = 200,
                                height = 100,
                                font = ("Helvetica Neue", 24, "bold"),
                                command=goBack)
        backButton.grid(row=1, column=0, padx=10, pady=10)

        lightButton = ctk.CTkButton(settingsFrame,
                                    text = "Light Mode",
                                    width = 200,
                                    height = 100,
                                    font = ("Helvetica Neue", 24, "bold"),
                                    fg_color = "White",
                                    command=lambda: ctk.set_appearance_mode("Light"))
        darkButton = ctk.CTkButton(settingsFrame,
                                    text = "Dark Mode",
                                    width = 200,
                                    height = 100,
                                    font = ("Helvetica Neue", 24, "bold"),
                                    fg_color = "Black",
                                    command=lambda: ctk.set_appearance_mode("Dark"))
        
        lightButton.grid(row=0, column=0, padx=10, pady=10)
        darkButton.grid(row=0, column=1, padx=10, pady=10)

    def formulaWindow(self):
        formulaFrame = ctk.CTkFrame(self.root, corner_radius = 15)
        formulaFrame.grid(row=0, column=0, padx=20, pady=20)
        # Create a scrollable frame to hold the formulas
        scrolling = ctk.CTkScrollableFrame(formulaFrame, width = 600, height = 400, corner_radius = 15)
        scrolling.grid(row = 0, column = 0, padx = 10, pady = 10)

        # Quadratic formula
        quadImage = ctk.CTkImage(light_image = Image.open('images/Quadratic.png'), size = (600, 400))
        quadLabel = ctk.CTkLabel(scrolling,
                                 image = quadImage,
                                 text = "")
        quadLabel.grid(row = 0, column = 0)   

        # Pythagorean formula
        pythImage = ctk.CTkImage(light_image = Image.open('images/Pythagorean.png'), size = (600, 400))
        pythLabel = ctk.CTkLabel(scrolling,
                                 image = pythImage,
                                 text = "")
        pythLabel.grid(row = 1, column = 0)


        # Logarithm formula
        logImage = ctk.CTkImage(light_image = Image.open('images/Logarithm.png'), size = (600, 400))
        logLabel = ctk.CTkLabel(scrolling,
                                 image = logImage,
                                 text = "")
        logLabel.grid(row = 2, column = 0)        


        def goBack():
            """Go Back"""
            formulaFrame.grid_forget()
            self.root.firstWindow()
        backButton = ctk.CTkButton(formulaFrame,
                                text = "Back",
                                width = 200,
                                height = 100,
                                font = ("Helvetica Neue", 24, "bold"),
                                command=goBack)
        backButton.grid(row=1, column=0, padx=10, pady=10)
        

    def GameWindow(self):
        self.mode = ""
        gameFrame = ctk.CTkFrame(self.root, corner_radius = 15)
        gameFrame.grid(row=0, column=0, padx=20, pady=20)
        def goBack():
            """Go Back"""
            gameFrame.grid_forget()
            self.root.firstWindow()

        def mode(choice):
            self.mode = choice
            gameFrame.grid_forget()
            if self.mode == "Elementary":
                self.elementaryGame(random.randint(0, 3))
            elif self.mode == "Advanced":
                self.advancedGame()

        elementaryButton = ctk.CTkButton(gameFrame, #Window it is placed in
                                    text = "Elementary", # Text
                                    width = 200,
                                    height = 100,
                                    font = ("Helvetica Neue", 24, "bold"),
                                    fg_color="Green",
                                    command=lambda: mode("Elementary")) #when
        elementaryButton.grid(row=0, column=0, padx=10, pady=10)

        upperButton = ctk.CTkButton(gameFrame,
                                    text = "Advanced",
                                    width = 200,
                                    height = 100,
                                    font = ("Helvetica Neue", 24, "bold"),
                                    fg_color="Red",
                                    command=lambda: mode("Advanced"))
        upperButton.grid(row=0, column=1, padx=10, pady=10)

        goBackButton = ctk.CTkButton(gameFrame,
                                text = "Back",
                                width = 200,
                                height = 100,
                                font = ("Helvetica Neue", 24, "bold"),
                                command=goBack)
        goBackButton.grid(row = 1, column=0, padx=10, pady=10)

        endButton = ctk.CTkButton(gameFrame, #Window it is placed in
                                text = "End Game", # Text
                                width = 200,
                                height = 100,
                                font = ("Helvetica Neue", 24, "bold"),
                                fg_color="Black",
                                command=exit) #when
        endButton.grid(row=1, column=1, padx=10, pady=10)

    def elementaryGame(self, corner_radius = 15):

        # Mode selection

        def goBack():
            """Go Back"""
            elemFrame.grid_forget()
            questionFrame.grid_forget()
            selectFrame.grid_forget()
            enterFrame.grid_forget()
            answerFrame.grid_forget()
            self.GameWindow()

        
        elemFrame = ctk.CTkFrame(self.root)
        elemFrame.grid(row=1, column=0, padx=20, pady=20)

        # Wrapper frame to hold the questions and answers
        wrapFrame = ctk.CTkFrame(elemFrame, corner_radius = 15, width = 500, height = 100)
        wrapFrame.grid(row=0, column=0)
        # Holds the question
        questionFrame = ctk.CTkFrame(wrapFrame)
        questionFrame.grid(row=0, column=0)

        # Holds the answer input
        answerFrame = ctk.CTkFrame(wrapFrame, corner_radius=15, height = 100, width = 200)
        answerFrame.grid(row=0, column = 1)

        answerInput = ctk.CTkEntry(answerFrame, corner_radius=15, height = 100, width = 200, font = ("Arial", 48, "bold"))
        answerInput.grid(row=0, column=0)

        # Question Selector
        selectFrame = ctk.CTkFrame(self.root, corner_radius=15, height = 100, width = 300)
        selectFrame.grid(row=3, column = 0, padx=20, pady=20)

        # Frames to go back or to enter
        enterFrame = ctk.CTkFrame(self.root, corner_radius=15, height = 100, width = 400)
        enterFrame.grid(row=2, column = 0, padx=20, pady=20)

        #For the textFrame, insert correct if the answer correct. Insert incorrect of wrong
        # Text frame display if the answer was correct
        textFrame = ctk.CTkFrame(enterFrame, corner_radius = 15, width = 75, height = 100)
        textFrame.grid(row=1)

        # Checks answer
        def submitAnswer():
            goButton.configure(state = "disabled")
            try:
                answer = float(answerInput.get())
                if answer == self.answer:
                    display = "CORRECT!"
                    color = "Green"
                else:
                    display = "INCORRECT!"
                    color = "Red"

            except ValueError:
                display = "Input a Number"
                color = "Gray"

            # Set result color and text
            result.configure(text = display, fg_color = color)

        result = ctk.CTkLabel(textFrame,
                                corner_radius = 15,
                                font = ("Arial", 24, "bold"),
                                text = "",
                                fg_color="Gray")
        result.grid(row=1,column=0, padx = 10, pady=10)

        # Buttons to enter or to go back
        goButton = ctk.CTkButton(enterFrame,
                                 text = "Enter",
                                 width = 75,
                                 height = 100,
                                 font = ("Helvetica Neue", 24, "bold"),
                                 command=submitAnswer)
        goButton.grid(row=0, column=1, padx=0, pady=10)

        def random(op):
            goButton.configure(state = "normal")
            result.configure(text = "", fg_color = "Gray")
            self.currentOp = op

            def declareFrame():
                expressionValue = ctk.CTkLabel(questionFrame,
                                  text = f"{self.num1} {self.operator} {self.num2} = ",
                                  width = 200,
                                  height = 100,
                                  font = ("Helvetica Neue", 24, "bold"))
                expressionValue.grid(row = 0, column = 0, padx=20, pady=20)

            if op == "+":
                self.num1, self.num2 = elementary(0)
                self.operator = "+"
                self.answer = self.num1 + self.num2
                declareFrame()

            elif op == "-":
                self.num1, self.num2 = elementary(1)
                self.operator = "-"
                self.answer = self.num1 - self.num2
                declareFrame()
                

            elif op == "*":
                self.num1, self.num2 = elementary(2)
                self.operator = "*"
                self.answer = self.num1 * self.num2
                declareFrame()

            elif op == "/":
                self.num1, self.num2 = elementary(3)
                self.operator = "/"
                self.answer = self.num1/self.num2
                declareFrame()

        random("+")
            
            


        backButton = ctk.CTkButton(enterFrame,
                                text = "Back",
                                width = 75,
                                height = 100,
                                font = ("Helvetica Neue", 24, "bold"),
                                command=goBack)
        backButton.grid(row=0, column=0, padx=10, pady=10)

        # Buttons that are needed to switch modes
        additionButton = ctk.CTkButton(selectFrame,
                                       text = "+",
                                       width = 50,
                                       height = 50,
                                       font = ("Helvetica Neue", 24, "bold"),
                                       command = lambda: random("+"))
        additionButton.grid(row=0, column = 0, padx=20, pady=10)

        subtractButton = ctk.CTkButton(selectFrame,
                                       text = "-",
                                       width = 50,
                                       height = 50,
                                       font = ("Helvetica Neue", 24, "bold"),
                                       command = lambda: random("-"))
        subtractButton.grid(row=0, column = 1, padx=20, pady=10)

        multiplyButton = ctk.CTkButton(selectFrame,
                                       text = "*",
                                       width = 50,
                                       height = 50,
                                       font = ("Helvetica Neue", 24, "bold"),
                                       command = lambda: random("*"))
        multiplyButton.grid(row=0, column = 2, padx=20, pady=10)

        divideButton = ctk.CTkButton(selectFrame,
                                       text = "/",
                                       width = 50,
                                       height = 50,
                                       font = ("Helvetica Neue", 24, "bold"),
                                       command = lambda: random("/"))
        divideButton.grid(row=0, column = 3, padx=20, pady=10)





        # In text frame, make a random button that keeps operator, changes numbers
        randomButton = ctk.CTkButton(enterFrame,
                                     text = "Next",
                                     font = ("Arial", 24, "bold"),
                                     corner_radius = 15,
                                     width = 75,
                                     height = 100,
                                     command = lambda: random(self.currentOp))
        randomButton.grid(row=1, column=1, padx=10, pady=10)



        

    def advancedGame(self):

        """Window to select the mode for advanced section"""
        # Every frame used in declared below:
        
        # Making the frame to hold everything
        advFrame = ctk.CTkFrame(self.root, corner_radius = 15)
        advFrame.grid(row=0, column=0, padx=20, pady=20)

        # Buttons for modes
        quadButton = ctk.CTkButton(advFrame,
                                    text = "Quadratic",
                                    width = 75,
                                    height = 100,
                                    font = ("Helvetica Neue", 24, "bold"),
                                    command=lambda: selectMode("quad"))
        quadButton.grid(row=0, column=0, padx=10, pady=10)

        pythButton = ctk.CTkButton(advFrame,
                                    text = "Pythagorean",
                                    width = 75,
                                    height = 100,
                                    font = ("Helvetica Neue", 24, "bold"),
                                    command=lambda: selectMode("pythagorean"))
        pythButton.grid(row=0, column=1, padx=10, pady=10)

        logButton = ctk.CTkButton(advFrame,
                                    text = "Logarithm",
                                    width = 75,
                                    height = 100,
                                    font = ("Helvetica Neue", 24, "bold"),
                                    command=lambda: selectMode("log"))
        logButton.grid(row=1, column=0, padx=10, pady=10)

        # Question Selector
        # selectFrame = ctk.CTkFrame(self.root, corner_radius=15, height = 100, width = 300)
        # selectFrame.grid(row=3, column = 0, padx=20, pady=20)

        # Frames to go back or to enter
        enterFrame = ctk.CTkFrame(self.root, corner_radius=15, height = 100, width = 400)
        enterFrame.grid(row=2, column = 0, padx=20, pady=20)

        #For the textFrame, insert correct if the answer correct. Insert incorrect of wrong
        # Text frame display if the answer was correct
        textFrame = ctk.CTkFrame(enterFrame, corner_radius = 15, width = 75, height = 100)
        textFrame.grid(row=1)

        def selectMode(mode):
            self.currentMode = mode
            advFrame.grid_forget()
            enterFrame.grid_forget()
            # Holds the question
            question = None
            
            if mode == "quad":
                self.num1, self.num2, self.num3, discriminant, self.xPos, self.xNeg = advanced(0)
                question = f"{self.num1}x^2 + {self.num2}x + {self.num3}"
                self.quadraticWindow(self.xPos, self.xNeg, question)

            elif mode == "pythagorean":
                self.num1, self.num2, self.answer = advanced(1)
                question = f"{self.num1}^2 + {self.num2}^2 = "
                self.pythagoreanWindow(question)

            elif mode == "log":
                self.num1, self.num3, self.answer = advanced(2)
                question = f"log base {self.num1} of {self.num3}"
                self.logWindow(question)

            elif mode == "derivative":
                self.num1, self.num2, self.num3, self.num4 = advanced(3)
                question = f"{self.num1}x^{self.num2} + {self.num3}x^{self.num4}"
                self.derivativeWindow(question)


        # Initial state
        # advancedGame = selectMode("quad")


        # Button to go back
        def goBack():
            """Go Back"""
            advFrame.grid_forget()
            self.GameWindow()
            # wrapFrame.grid_forget()
            # questionFrame.grid_forget()
            # answerFrame.grid_forget()
            # selectFrame.grid_forget()
            enterFrame.grid_forget()

        


        backButton = ctk.CTkButton(enterFrame,
                                text = "Back",
                                width = 200,
                                height = 100,
                                font = ("Helvetica Neue", 24, "bold"),
                                command=goBack)
        backButton.grid(row=1, column=0, padx=10, pady=10)


    # ---------------------------------------------------------------------#
    # Advanced game modes:

    def quadraticWindow(self, xPos, xNeg, question):
        """A Window for the quadratic portion"""
        quadFrame = ctk.CTkFrame(self.root, corner_radius = 15)
        quadFrame.grid(row=0, column=0, padx=20, pady=20)
        # Frame to hold the enter and random buttons
        actionFrame = ctk.CTkFrame(quadFrame,corner_radius = 15, width = 100, height = 200)
        actionFrame.grid(row=3, column = 0)

        print(round(xPos, 2))
        print(round(xNeg, 2))


        labelFrame = ctk.CTkFrame(quadFrame,
                                  width = 300,
                                  height = 100,
                                  corner_radius = 15)
        labelFrame.grid(row = 0, column = 0)

        instructionText = ctk.CTkLabel(labelFrame,
                                       text = "Find x. Round to the nearest hundredth",
                                       corner_radius=15,
                                       width = 250,
                                       height = 75,
                                       font = ("Helvetica Nueue", 24, "bold"))
        instructionText.grid(row=0,column = 0)

        labelText = ctk.CTkLabel(labelFrame,
                                 width = 250,
                                 height = 75,
                                 corner_radius=15,
                                 text = question,
                                 font = ("Helvetica Neue", 24, "bold"))
        labelText.grid(row=1,column=0)


        # Entries for the greater x value and the lesser

        # Instructions
        XLabel = ctk.CTkLabel(quadFrame,
                              text = "input the x values plus or minus the discriminant",
                              width = 200,
                              height = 75,
                              font = ("Helvetica Nueue", 24, "bold"),
                              corner_radius=15)
        XLabel.grid(row=1, column = 0)

        # First make a frame
        entryFrame = ctk.CTkFrame(quadFrame,
                                  width = 300,
                                  height = 300,
                                  corner_radius=15)
        entryFrame.grid(row=2, column = 0)

        xPosEntry = ctk.CTkEntry(entryFrame,
                                 width = 100,
                                 height = 75,
                                 corner_radius=15,
                                 font = ("Arial", 24, "bold"))
        xPosEntry.grid(row=1, column = 0, padx = 10)

        xNegEntry = ctk.CTkEntry(entryFrame,
                                 width = 100,
                                 height = 75,
                                 corner_radius=15,
                                 font = ("Arial", 24, "bold"))
        xNegEntry.grid(row=1, column = 1, padx = 10)

        # Button to randomize
        def random():
            # Re-enable button, makes sure no cheating
            enterButton.configure(state = "normal")
            # Randomly generate the equations
            self.num1, self.num2, self.num3, discriminant, self.xPos, self.xNeg = advanced(0)
            # Store it in question
            question = f"{self.num1}x^2 + {self.num2}x + {self.num3}"
            # Print to debug
            print(self.xPos)
            print(self.xNeg)
            # Change the label
            labelText.configure(text = question)

            # Make sure the result is blank
            display = ""
            color = "Gray"
            result.configure(text = display, fg_color = color)



        # Checks answer
        def submitAnswer():
            enterButton.configure(state = "disabled")
            try:
                # Get the values
                answer = float(xPosEntry.get())
                answer2 = float(xNegEntry.get())

                # See if they are correctly aligning, prepare for both cases
                if (answer == round(self.xPos, 2) and answer2 == round(self.xNeg, 2)) or (answer == round(self.xNeg, 2) and answer2 == round(self.xPos, 2)):
                    display = "CORRECT!"
                    color = "Green"
                else:
                    if answer == xPos and answer2 != xPos:
                        display = "-X is Wrong!"
                        color = "Red"
                    elif answer != xPos and answer2 == xPos:
                        display = "+X is Wrong!"
                        color = "Red"
                    else:
                        display = "INCORRECT!"
                        color = "Red"

            except ValueError:
                display = "Input a Number"
                color = "Gray"
            result.configure(text = display, fg_color = color)
        result = ctk.CTkLabel(actionFrame,
                        corner_radius = 15,
                        font = ("Arial", 24, "bold"),
                        text = "",
                        fg_color="Gray")
        result.grid(row=0,column=0, padx = 10, pady=10)

        # Random button
        randomButton = ctk.CTkButton(actionFrame,
                                     width = 100,
                                     height = 100,
                                     corner_radius = 15,
                                     text = "Randomize",
                                     command = random)
        randomButton.grid(row=1, column = 0)

        # Button to enter the answer
        enterButton = ctk.CTkButton(actionFrame,
                                    width = 100,
                                    height = 100,
                                    corner_radius = 15,
                                    text = "Enter",
                                    command = submitAnswer)
        enterButton.grid(row=1, column = 1)


        # Button to enter answers

        # Button to go back
        def goBack():
            """Go Back"""
            quadFrame.grid_forget()
            entryFrame.grid_forget()
            labelFrame.grid_forget()
            self.advancedGame()

        backButton = ctk.CTkButton(quadFrame,
                                text = "Back",
                                width = 200,
                                height = 100,
                                font = ("Helvetica Neue", 24, "bold"),
                                command=goBack)
        backButton.grid(row=4, column=0, padx=10, pady=10)
        
    def pythagoreanWindow(self, question):
        """A Window for the pythagorean portion"""

        # Frame holding everything
        pythFrame = ctk.CTkFrame(self.root, corner_radius = 15)
        pythFrame.grid(row=0, column=0, padx=20, pady=20)
        
        # debugging
        print(self.answer)


        # Holds the question
        questionFrame = ctk.CTkFrame(pythFrame, corner_radius = 15, width = 200, height = 200)
        questionFrame.grid(row=0, column = 0)

        actionFrame = ctk.CTkFrame(pythFrame, corner_radius = 15, width = 200, height = 100)
        actionFrame.grid(row = 2)
        # Unchanged, tells what to find
        directions = ctk.CTkLabel(questionFrame, corner_radius = 15, text = "Find C. Round to the nearest hundredth")
        directions.grid(row = 0)

        # The question itself
        questionText = ctk.CTkLabel(questionFrame, width = 300, height = 75, text = question)
        questionText.grid(row = 1)

        # Box for answer entry
        entryBox = ctk.CTkEntry(questionFrame,
                                width = 75,
                                height = 75,
                                font = ("Arial", 24, "bold"))
        entryBox.grid(row = 1, column = 1)

        def submitAnswer():
            enterButton.configure(state = "disabled")
            answer = float(entryBox.get())
            try:
                if answer == self.answer:
                    display = "CORRECT!"
                    color = "Green"
                else:
                    display = "INCORRECT!"
                    color = "Red"
            except ValueError:
                display = "Input a Number"
                color = "Gray"

            label.configure(text = display, fg_color = color)

        label = ctk.CTkLabel(actionFrame,
                             width = 100,
                             height = 100,
                             corner_radius = 15,
                             text = "",
                             fg_color = "Gray")
        label.grid(row = 0, column = 1)


        def random():

            # Re-enable button, makes sure no cheating
            enterButton.configure(state = "normal")
            # Randomly generate the equations
            self.num1, self.num2, self.answer = advanced(1)
            # Store it in question
            question = f"{self.num1}^2 + {self.num2}^2 = "
            # Print to debug
            print(self.answer)
            # Change the label
            questionText.configure(text = question)

            # Make sure the result is blank
            display = ""
            color = "Gray"
            label.configure(text = display, fg_color = color)

        # Button to randomize
        # Enter button
        # Random button
        randomButton = ctk.CTkButton(actionFrame,
                                     width = 100,
                                     height = 100,
                                     corner_radius = 15,
                                     text = "Randomize",
                                     command = random)
        randomButton.grid(row=1, column = 0)

        # Button to enter the answer
        enterButton = ctk.CTkButton(actionFrame,
                                    width = 100,
                                    height = 100,
                                    corner_radius = 15,
                                    text = "Enter",
                                    command = submitAnswer)
        enterButton.grid(row=1, column = 1)


        def goBack():
            """Go Back"""
            questionFrame.grid_forget()
            pythFrame.grid_forget()
            self.advancedGame()

        backButton = ctk.CTkButton(pythFrame,
                                text = "Back",
                                width = 200,
                                height = 100,
                                font = ("Helvetica Neue", 24, "bold"),
                                command=goBack)
        backButton.grid(row=3, column=0, padx=10, pady=10)
        
    def logWindow(self, question):
        """A Window for the log portion"""
        logFrame = ctk.CTkFrame(self.root, corner_radius = 15)
        logFrame.grid(row=0, column=0, padx=20, pady=20)

        # Holds the question
        questionFrame = ctk.CTkFrame(logFrame, corner_radius = 15, width = 300, height = 200)
        questionFrame.grid(row=0, column = 0)

        # Debugging
        print(self.answer)

        # Text of the question
        questionText = ctk.CTkLabel(questionFrame,
                                     width = 300,
                                     height = 75,
                                     text = question,
                                     font = ("Helvetica Neue", 24, "bold"))
        questionText.grid(row=0,column=0)


        # The actual entry box
        entryBox = ctk.CTkEntry(logFrame,
                                width = 75,
                                height = 75,
                                font = ("Arial", 24, "bold"))
        entryBox.grid(row = 0, column = 1)


        def submitAnswer():
            entryBox.configure(state = "disabled")
            answer = float(entryBox.get())
            try:
                if answer == self.answer:
                    display = "CORRECT!"
                    color = "Green"
                else:
                    display = "WRONG!"
                    color = "Red"
            except ValueError:
                display = "Input a number"
                color = "Gray"

            label.configure(text = display, fg_color = color)

        # Label for the answer
        label = ctk.CTkLabel(questionFrame,
                             width = 200,
                             height = 100,
                             corner_radius = 15,
                             text = "",
                             font = ("Helvetica Neue", 24, "bold"),
                             fg_color = "Gray")
        label.grid(row = 1, column = 0)


        # Button to enter
        # Button to enter the answer
        enterButton = ctk.CTkButton(logFrame,
                                    width = 100,
                                    height = 100,
                                    corner_radius = 15,
                                    text = "Enter",
                                    font = ("Helvetica Neue", 24, "bold"),
                                    command = submitAnswer)
        enterButton.grid(row=1, column = 1)

        def random():
            """Random Button"""
            label.configure(text = "", fg_color = "Gray")
            entryBox.configure(state = "normal")
            self.num1, self.num3, self.answer = advanced(2)
            question = f"log base {self.num1} of {self.num3}"
            questionText.configure(text = question)
            print(self.answer)

        randomButton = ctk.CTkButton(logFrame,
                                text = "Random",
                                width = 100,
                                height = 100,
                                font = ("Helvetica Neue", 24, "bold"),
                                command=random)
        randomButton.grid(row = 1, column = 0)


        def goBack():
            """Go Back"""
            logFrame.grid_forget()
            self.advancedGame()

        backButton = ctk.CTkButton(logFrame,
                                text = "Back",
                                width = 200,
                                height = 100,
                                font = ("Helvetica Neue", 24, "bold"),
                                command=goBack)
        backButton.grid(row=2, column=0, padx = 10, pady = 10)