from PIL import Image, ImageTk
import random
from tkinter import messagebox
import sys
import os

#Function that pops a card form the deck and returns it
def what_card(deck):

    card = (deck.pop())[0] 
    return card
 
#When higher button is pressd, if players card is higher then the next card in the deck, giving the streak +1 and chancgin the image of the payers card
def higher(deck,lower_button,streak_button,s2,face_up_card,root):
    
    if c_higher(deck,face_up_card,lower_button,root):
        lower_button.config(image=what_card(deck))
        s2[0]=s2[0]+1
        streak_button.config(text=(f"Your streak is:\n{s2}"))

#When lower button is pressd, if players card is lower then the next card in the deck, giving the streak +1 and chancgin the image of the payers card
def lower(deck,lower_button,streak_button,s2,face_up_card,root):
    
    if c_lower(deck,face_up_card,lower_button,root):
        lower_button.config(image=what_card(deck)) 
        s2[0]=s2[0]+1
        streak_button.config(text=(f"Your streak is:\n{s2}"))

#Checks if players guessed higher correct
def c_higher(deck,face_up_card,lower_button,root):

    if face_up_card[0]>=(deck[-1])[1]:
        face_up_card[0]=(deck[-1])[1]
        return True

    else:
        lower_button.config(image=what_card(deck))
        response = messagebox.askyesno(title="OH NO!",message="YOU LOST!\nWould you like to play again?")
        if response == 1:
            restart_program()
        else:
            root.destroy()

#Checks if players guessed lower correct
def c_lower(deck,face_up_card,lower_button,root):
    if face_up_card[0]<=(deck[-1])[1]:
        face_up_card[0]=(deck[-1])[1]
        return True

    else:
        lower_button.config(image=what_card(deck))
        response = messagebox.askyesno(title="OH NO!",message="YOU LOST!\nWould you like to play again?")
        if response == 1:
            restart_program()
        else:
            root.destroy()
        

#Showing the information of how to play the game
def rules():
    messagebox.showinfo(title="Info",message="Ace has the lowest value\nKing has the highest value\nSame cards has the same value so you will be granted a win no matter what you press\nYour card is on the bottom\nIf you think your card has a higher value then the next card press: Higher\nIf you think your card has a lower value then the next card press : Lower\nAs long as you guess right your streak will go up\nGOOD LUCK!")

#Restart the game function
def restart_program():
    
    python = sys.executable
    os.execl(python, python, * sys.argv)

