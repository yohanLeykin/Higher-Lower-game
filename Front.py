from tkinter import *
from PIL import Image, ImageTk
import Back


#Front of the GUI, the screen that you see when the app opens

class GUI(Frame):

    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        self.root.geometry('960x600')
        self.root.title('Yagan - Higher lower game')
        self.root.iconbitmap(r'C:\Users\User\Desktop\Python\Lower_Higher\BLACKJACKICON.ico')
        self.mainframe = Frame(self.root, bg='Green')
        self.mainframe.pack(fill=BOTH, expand=True)
        self.deck = Game_Cards()

        #self.restart_button = Button(self.root, bg="red", width=12, height=1, text="Restart game", font = "Calibri 24", command= Back.restart_program)
        #self.restart_button.place(relx=.8, rely=.6, anchor="c")

        #Button to show the back of a card on top of the screen
        self.hiddenimg = self.deck.hiddenCard_img
        self.top_deck_button = Button(self.mainframe, image=self.hiddenimg, bg="Green")
        self.top_deck_button.place(x=400,y=50)

        #sec ==> getting the first card in the deck for a player and getting its value
        self.sec = self.deck.ccdeck.pop()
        self.deck.cardvalue[0] = (self.sec)[1]
        self.cardimg2 = (self.sec)[0]

        #Player card button
        self.player_card_button = Button(self.mainframe, image=self.cardimg2, bg="Green")
        self.player_card_button.place(x=400,y=300)

        #Tutrial button
        self.how_to_play_button = Button(self.root, bg="red", width=12, height=1, text="How to play", font = "Calibri 24", command= Back.rules)
        self.how_to_play_button.place(relx=.8, rely=.8, anchor="c")

        #Title button
        self.titlebutton = Button(self.root, bg="green", width=12, height=1, text="Your card is: ", font = "Calibri 36")
        self.titlebutton.place(relx=.2, rely=.2, anchor="c")

        #higher button
        self.higherbutton = Button(self.root, bg="red",width=12, height=1, text="Higher", font = "Calibri 36", command= lambda: Back.higher(self.deck.ccdeck,self.player_card_button,self.streakbutton,self.deck.streak,self.deck.cardvalue,self.root))
        self.higherbutton.place(relx=.2, rely=.4, anchor="c")

        #lower button
        self.lowerbutton = Button(self.root, bg="red",width=12, height=1, text="Lower", font = "Calibri 36", command= lambda: Back.lower(self.deck.ccdeck,self.player_card_button,self.streakbutton,self.deck.streak,self.deck.cardvalue,self.root))
        self.lowerbutton.place(relx=.2, rely=.6, anchor="c")

        #streak button
        self.streakbutton = Button(self.root, bg="green",width=12, height=1, text=(f"Your streak is:\n{self.deck.streak[0]}"), font = "Calibri 36")
        self.streakbutton.place(relx=.8, rely=.2, anchor="c")






class Game_Cards():

    def __init__(self):

        #Images for all the cards
        self.nocard_img = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Green.png"))
        self.hiddenCard_img = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Hidden2.png"))

        self.AceOfSpades = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Ace of Spades.png"))
        self.AceOfHearts = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Ace of Hearts.png"))
        self.AceOfClubs = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Ace of Clubs.png"))
        self.AceOfDiamonds = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Ace of Diamonds.png"))

        self.TowOfSpades = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Tow of Spades.png"))
        self.TowOfHearts = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Tow of Hearts.png"))
        self.TowOfClubs = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Tow of Clubs.png"))
        self.TowOfDiamonds = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Tow of Diamonds.png"))

        self.ThreeOfSpades = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Three of Spades.png"))
        self.ThreeOfHearts = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Three of Hearts.png"))
        self.ThreeOfClubs = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Three of Clubs.png"))
        self.ThreeOfDiamonds = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Three of Diamonds.png"))

        self.FourOfSpades = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Four of Spades.png"))
        self.FourOfHearts = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Four of Hearts.png"))
        self.FourOfClubs = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Four of Clubs.png"))
        self.FourOfDiamonds = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Four of Diamonds.png"))

        self.FiveOfSpades = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Five of Spades.png"))
        self.FiveOfHearts = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Five of Hearts.png"))
        self.FiveOfClubs = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Five of Clubs.png"))
        self.FiveOfDiamonds = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Five of Diamonds.png"))

        self.SixOfSpades = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Six of Spades.png"))
        self.SixOfHearts = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Six of Hearts.png"))
        self.SixOfClubs = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Six of Clubs.png"))
        self.SixOfDiamonds = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Six of Diamonds.png"))

        self.SevenOfSpades = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Seven of Spades.png"))
        self.SevenOfHearts = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Seven of Hearts.png"))
        self.SevenOfClubs = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Seven of Clubs.png"))
        self.SevenOfDiamonds = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Seven of Diamonds.png"))

        self.EightOfSpades = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Eight of Spades.png"))
        self.EightOfHearts = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Eight of Hearts.png"))
        self.EightOfClubs = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Eight of Clubs.png"))
        self.EightOfDiamonds = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Eight of Diamonds.png"))

        self.NineOfSpades = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Nine of Spades.png"))
        self.NineOfHearts = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Nine of Hearts.png"))
        self.NineOfClubs = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Nine of Clubs.png"))
        self.NineOfDiamonds = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Nine of Diamonds.png"))

        self.TenOfSpades = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Ten of Spades.png"))
        self.TenOfHearts = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Ten of Hearts.png"))
        self.TenOfClubs = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Ten of Clubs.png"))
        self.TenOfDiamonds = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Ten of Diamonds.png"))

        self.JackOfSpades = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Jack of Spades.png"))
        self.JackOfHearts = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Jack of Hearts.png"))
        self.JackOfClubs = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Jack of Clubs.png"))
        self.JackOfDiamonds = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Jack of Diamonds.png"))

        self.QueenOfSpades = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Queen of Spades.png"))
        self.QueenOfHearts = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Queen of Hearts.png"))
        self.QueenOfClubs = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Queen of Clubs.png"))
        self.QueenOfDiamonds = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\Queen of Diamonds.png"))

        self.KingOfSpades = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\King of Spades.png"))
        self.KingOfHearts = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\King of Hearts.png"))
        self.KingOfClubs = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\King of Clubs.png"))
        self.KingOfDiamonds = ImageTk.PhotoImage(Image.open(r"C:\Users\User\Desktop\Python\Lower_Higher\Cards image\PNG\King of Diamonds.png"))

        #full list of 52 cards,each card has a picture and a value
        self.ccdeck = [[self.AceOfClubs,1],[self.AceOfDiamonds,1],[self.AceOfHearts,1],[self.AceOfSpades,1],
                 [self.TowOfClubs,2],[self.TowOfDiamonds,2],[self.TowOfHearts,2],[self.TowOfSpades,2],
                 [self.ThreeOfClubs,3],[self.ThreeOfDiamonds,3],[self.ThreeOfHearts,3],[self.ThreeOfSpades,3],
                 [self.FourOfClubs,4],[self.FourOfDiamonds,4],[self.FourOfHearts,4],[self.FourOfSpades,4],
                 [self.FiveOfClubs,5],[self.FiveOfDiamonds,5],[self.FiveOfHearts,5],[self.FiveOfSpades,5],
                 [self.SixOfClubs,6],[self.SixOfDiamonds,6],[self.SixOfHearts,6],[self.SixOfSpades,6],
                 [self.SevenOfClubs,7],[self.SevenOfDiamonds,7],[self.SevenOfHearts,7],[self.SevenOfSpades,7],
                 [self.EightOfClubs,8],[self.EightOfDiamonds,8],[self.EightOfHearts,8],[self.EightOfSpades,8],
                 [self.NineOfClubs,9],[self.NineOfDiamonds,9],[self.NineOfHearts,9],[self.NineOfSpades,9],
                  [self.TenOfClubs,10], [self.TenOfDiamonds,10], [self.TenOfHearts,10], [self.TenOfSpades,10],
                  [self.JackOfClubs,11], [self.JackOfDiamonds,11], [self.JackOfHearts,11], [self.JackOfSpades,11],
                  [self.QueenOfClubs,12], [self.QueenOfDiamonds,12], [self.QueenOfHearts,12], [self.QueenOfSpades,12],
                  [self.KingOfClubs,13], [self.KingOfDiamonds,13], [self.KingOfHearts,13], [self.KingOfSpades,13]]

        #Shuffle the deck
        Back.random.shuffle(self.ccdeck)

        #streak counter
        self.streak = [0]

        #Card value for compering
        self.cardvalue = [0] 
    

       
