from tkinter import *

THEME_COLOR = "#375362"


class QuizzInterface:

    def __init__(self):
        #Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0

        # Score Label
        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, highlightthickness=0)
        self.score_label.config(font=("Arial", 10, "bold"), fg="white")
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250)
        self.quest_text = self.canvas.create_text(
            150,
            125,
            text="The HTML5 standard was published in 2014.",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Check Button
        check_img = PhotoImage(file="images/true.png")
        self.check_button = Button(image=check_img, highlightthickness=0)
        self.check_button.grid(row=2, column=0)
        self.check_button = Button()

        # Cross Button
        cross_img = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=cross_img, highlightthickness=0)
        self.cross_button.grid(row=2, column=1)

        self.window.mainloop()
