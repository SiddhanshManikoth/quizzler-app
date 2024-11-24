from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
Q_TIMER=NONE
class QuizInterface():

    def __init__(self,quizbrain:QuizBrain):
        #window setup
        self.window = Tk()
        self.window.title("quiz game")
        self.window.config(padx=10, pady=10, bg=THEME_COLOR)
        #fetching data from quizbrain
        self.quiz=quizbrain
        #taking user input from gui
        self.user_input:str
        #labels
        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR,font=("arial",14,"normal"))
        self.score_label.grid(column=1, row=0,padx=20,pady=20)

        #canvas setup
        self.canvas = Canvas()
        self.canvas.config(height=250, width=300)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="question here",
            width=280,
            font=("arial", 14, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2,padx=20,pady=20)
        #image files
        self.correct_btn_img = PhotoImage(file="images/true.png")
        self.wrong_btn_img = PhotoImage(file="images/false.png")

        #buttons

        self.true_button = Button(
            image=self.correct_btn_img,
            highlightthickness=0,
            command=self.user_input_true,
        )
        self.true_button.grid(column=0, row=2,padx=20,pady=20)

        self.false_button = Button(
            image=self.wrong_btn_img,
            highlightthickness=0,
            command=self.user_input_false,
        )
        self.false_button.grid(column=1, row=2,padx=20,pady=20)


        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.color_card()
        self.q_text=self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text=f"Q.{self.q_text[1]}: {self.q_text[0]}")

    def user_input_true(self):
        self.user_input="true"
        self.ui_update()
    def user_input_false(self):
        self.user_input="false"
        self.ui_update()
    def check_answer(self):
        result=self.quiz.check_answer(self.user_input)
        return result
    def color_card(self,color="white"):
        self.canvas.config(bg=color)
    def ui_update(self):
        global  Q_TIMER
        self.window.after_cancel(Q_TIMER)
        if self.quiz.still_has_questions():
            if self.check_answer():
                self.color_card(color="green")
            else:
                self.color_card(color="red")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            Q_TIMER = self.window.after(1001, self.get_next_question)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text="You've completed the quiz"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")