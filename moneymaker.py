import tkinter  
import random

# main application window
window = tkinter.Tk()  #
window.geometry("300x200") 
window.title("MoneyMaker$$$")  
window.config(bg="#DDF1D1")  

# score variable
score = 0  

# label to display the score
score_label = tkinter.Label(
    window, text="Score: 0", font=("Arial", 16), bg="#DDF1D1", fg="black"
)  
score_label.pack(pady=20)  

emojis = ["💰", "🤑", "💸", "💵", "💴", "💶", "💷"]  # Add more emojis as desired


# function to handle button clicks
def increase_score():
    global score
    score += 1
    score_label.config(text=f"Score: {score}")  # Update the score
    
    random_emoji = random.choice(emojis)  
    x = random.randint(0, 1500)  
    y = random.randint(0, 1000)  
    
    # random positions for emojis
    new_emoji_label = tkinter.Label(
        window, text=random_emoji, font=("Arial", 40), bg="#DDF1D1"
    )
    new_emoji_label.place(x=x, y=y)  

# Function for rainbow-shifting button text color
def cycle_button_text_color():
    rainbow_colors = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#8B00FF"]

    def cycle():
        current_color = rainbow_colors[cycle_button_text_color.index % len(rainbow_colors)]
        shuffle_button.config(fg=current_color)
        cycle_button_text_color.index += 1
        window.after(100, cycle)

    cycle_button_text_color.index = 0
    cycle()  


# button for the clicker game
shuffle_button = tkinter.Button(
    window, 
    text="CLICK 4 MONEY NOW$$$ ", 
    font=("Arial", 30 ), 
    width=30, 
    height=2, 
    bg="#DDF1D1", 
    fg="blue", 
    command=increase_score  
)

shuffle_button.pack()
cycle_button_text_color()


window.mainloop()

