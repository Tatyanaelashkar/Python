from tkinter import *
import random
import pandas
import time

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
       data = pandas.read_csv("data/word_to_learn.csv")
except:
       original = pandas.read_csv("data/french_words.csv")
       to_learn = original.to_dict(orient="records")
else:
       to_learn = data.to_dict(orient="records")



def nextcard():
       global current_card, flip_timer
       window.after_cancel(flip_timer)
       current_card = random.choice(to_learn)
       canvas.itemconfig(language, text="French", fill="black")
       canvas.itemconfig(word, text=current_card["French"], fill="black")
       canvas.itemconfig(card_background, image=front_image)
def isknown():
       to_learn.remove(current_card)
       data= pandas.DataFrame(to_learn)
       data.to_csv("data/words_to_learn.csv", index=0)
       nextcard()
def flip_card():

       canvas.itemconfig(language, text="English", fill="white")
       canvas.itemconfig(word, text=current_card["English"])
       canvas.itemconfig(card_background, image=back_image)
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image =  PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 260, image=front_image)
language = canvas.create_text(400, 100, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


button1_image = PhotoImage(file="images/right.png")
button1 = Button(image=button1_image, command= isknown)
button1.grid(column=0, row=1)

button2_image = PhotoImage(file="images/wrong.png")
button2 = Button(image=button2_image, command= nextcard)
button2.grid(column=1, row=1)

nextcard()
window.mainloop()