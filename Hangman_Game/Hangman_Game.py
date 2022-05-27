# Packages and Window creation

from tkinter import *
from tkinter.messagebox import showinfo
import random as rdm

root = Tk()
root.title('Hangman Game')
root.geometry('800x500+400+200')
root.config(bg='lightgreen')
root.iconbitmap('Hangman_Icon.ico')

# Functions - Hangman Game

word_list = ['vouch', 'glass', 'scrap', 'gamer', 'olive', 'royal', 'natal', 'epoxy', 'india', 'tipsy', 'dodge', 'cynic', 'ultra']
photos = [PhotoImage(file="images/9th.png"), PhotoImage(file="images/8th.png"), PhotoImage(file="images/7th.png"), PhotoImage(file="images/6th.png"), PhotoImage(file="images/5th.png"), PhotoImage(file="images/4th.png"), PhotoImage(file="images/3rd.png"), PhotoImage(file="images/2nd.png"), PhotoImage(file="images/1st.png"), PhotoImage(file="images/0th.png")]

def chooseword():
    global word_list
    global rem_guesses
    global word_found
    global word_chosen
    word_chosen = rdm.choice(word_list)
    word_found = ['*' for i in word_chosen]
    rem_guesses = 2 * len(word_chosen) + 2
    # Incomplete (maybe)
    
def getguess():
    global rem_guesses
    global word_found
    global word_chosen
    
    word_str = ''.join(word_found)
    wordLabel.config(text = word_str)
    
    if rem_guesses > 0:
        guess_entered = list(guess.get())
        if len(guess_entered) == 1:
            pass
        elif len(guess_entered) == len(word_chosen):
            pass
        else:
            msgLabel.config(text = 'Wrong Number of Letters ...')
            rem_guesses -= 1
    else:
        showinfo('Hangman Game Over', 'Sorry, You ran out of guesses ... Please try Again')
    
    guessesLeft.config(text = f'Guesses Left : {rem_guesses}')
    # Incomplete
    # Button Command

# Function Call

chooseword()

# Labels

introLabel = Label(root, text = 'Welcome to Hangman Game', font = ('arial', 35, 'bold'), bg = 'lightgreen', fg = 'red')
introLabel.pack()                 

wordLabel = Label(root, font = ('arial', 55, 'bold'), bg = 'lightgreen', fg = 'red')
wordLabel.place(relx = 0.55, rely = 0.3, anchor = 'ne')

infoLabel = Label(root, text = 'Enter a letter or the guessed word :', font = ('arial', 20), bg = 'lightgreen', fg = 'red')
infoLabel.place(relx = 0.75, rely = 0.5, anchor = 'ne')

guessesLeft = Label(root, text = f'Guesses Left : {rem_guesses}',font = ('arial', 20, 'bold'), bg = 'lightgreen', fg = 'red')
guessesLeft.place(relx = 0.95, rely = 0.2, anchor = 'ne')

imgLabel = Label(root)
imgLabel.place(relx = 0.95, rely = 0.4, anchor = 'ne')

msgLabel = Label(root, font = ('arial', 25, 'bold'), bg = 'lightgreen', fg = 'red')
msgLabel.pack(side = 'bottom')

# Entry Box

guess = StringVar()
guessInput = Entry(root, textvariable = guess, width = 15, font = ('algerian', 20), relief = RIDGE, bd = 5, bg = 'lightblue', justify = 'center')
guessInput.place(relx = 0.63, rely = 0.6, anchor = 'ne', height = 50)

# Button

enterButton = Button(root, text = 'Enter Guess', font = ('arial', 15, 'bold'), activebackground = 'blue', activeforeground = 'pink', command = getguess)
enterButton.place(height = 40, width = 128, relx = 0.55, rely = 0.75, anchor = 'ne')

# Mainloop

root.mainloop()