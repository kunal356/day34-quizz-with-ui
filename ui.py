from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, highlightthickness=0)
        self.score_label.config(font=("Arial", 10, "bold"), fg="white")
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250)
        self.quest_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Check Button
        check_img = PhotoImage(file="images/true.png")
        self.check_button = Button(image=check_img, highlightthickness=0, command=self.answer_true)
        self.check_button.grid(row=2, column=0)

        # Cross Button
        cross_img = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=cross_img, highlightthickness=0, command=self.answer_false)
        self.cross_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score:{self.quiz.score}")
        if self.quiz.still_has_questions():
            q_txt = self.quiz.next_question()
            self.canvas.itemconfig(self.quest_text, text=q_txt)
        else:
            self.canvas.itemconfig(self.quest_text, text=f"You've reached to the end. Your final score is: ({self.quiz.score}/10)")
            self.check_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)
