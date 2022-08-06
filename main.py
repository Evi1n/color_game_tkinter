# Import Modules
from tkinter import *
import random
from tkinter import messagebox

colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','Purple','Brown'] # list of possible colour.
score = 0
time_left = 10

#------------------------- FUNCTIONS -------------------------#

# Countdown timer function 
def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1   
        time_label.config(text = "Time left: " + str(time_left))
        time_label.after(1000, countdown)
    # end of the game
    else:
        messagebox.showinfo(title="Game Over", message=f"Game Over. Your score is {score}")
        
# Next colour function         
def new_colour():
    global time_left
    global score
    if time_left>0:
        if answer_entry.get().lower() == colours[1].lower(): 
            score += 1
        answer_entry.delete(0,END)
        random.shuffle(colours)
        color_label.config(fg = str(colours[1]), text = str(colours[0]),font=("Courier", 60, "bold"))
        # update the score.
        score_label.config(text=f"Score: {score}")
    
def start_game():
    global time_left
    start_button.grid_remove()
    if time_left==10:
        countdown()
    new_colour()
       
def play(event):
    start_game()      
        
#------------------------ UI SETTINGS -------------------------#

# Window Settings
window = Tk()
window.title("Color Game")
window.geometry("400x300")
window.config(bg="#f2f2f2", padx=20, pady=20)
window.resizable(width=False, height=False)

# Label Settings
game_info_label = Label(text="Type in the colour of the words, and\n not the word text!", font=("Courier", 12))
game_info_label.grid(row=0, column=0)
start_label = Label(text="Press the button or enter to start.", font=("Courier", 12))
start_label.grid(row=1, column=0)
color_label = Label(text="Color Game",bg="#f2f2f2",fg="#f15bb5", font=("Courier", 40, "bold"))
color_label.grid(row=2, column=0)
score_label = Label(font=("Courier", 12))
score_label.grid(row=3, column=0)
time_label = Label(font=("Courier", 12))
time_label.grid(row=4, column=0)
empty_label = Label(text="")
empty_label.grid(row=6)

# Button Settings
start_button = Button(text="Start",font=("Courier", 12, "bold"), width=20, command=start_game)
start_button.grid(row=5, column=0)

# Entry Settings
answer_entry = Entry(width=50)
answer_entry.grid(row=7, column=0)

window.bind('<Return>', play)

window.mainloop()