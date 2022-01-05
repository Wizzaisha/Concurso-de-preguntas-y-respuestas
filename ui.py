import data
from tkinter import *
from quiz_game import QuizGame

THEME_COLOR = "#375362"
FONT_QUESTION = ("Arial", 20, "italic")
FONT_SCORE = ("Arial", 12, "bold")


class QuizInterface:

    def __init__(self, quiz_game: QuizGame):

        self.quiz = quiz_game

        # Window
        self.window = Tk()
        self.window.title("QuizGame!")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Prize label
        self.prize_label = Label(
            text=f"Current Prize: Un gato",
            fg="white",
            bg=THEME_COLOR,
            font=FONT_SCORE
        )
        self.prize_label.grid(column=0, row=0)

        # Round label
        self.round_label = Label(
            text=f"Current Round: 0",
            fg="white",
            bg=THEME_COLOR,
            font=FONT_SCORE
        )
        self.round_label.grid(column=1, row=0)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question here he he",
            font=FONT_QUESTION
        )

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Answer buttons
        # A.
        self.a_button = Button(
            text=f"A. Opcion 1",
            width=30,
            pady=10,
            command=self.a_answer
        )
        self.a_button.grid(column=0, row=2, columnspan=2)

        # B.
        self.b_button = Button(
            text=f"B. Opcion 2",
            width=30,
            pady=10,
            command=self.b_answer
        )
        self.b_button.grid(column=0, row=3, columnspan=2)

        # C.
        self.c_button = Button(
            text=f"B. Opcion 2",
            width=30,
            pady=10,
            command=self.c_answer
        )
        self.c_button.grid(column=0, row=4, columnspan=2)

        # D.
        self.d_button = Button(
            text=f"B. Opcion 2",
            width=30,
            pady=10,
            command=self.d_answer
        )
        self.d_button.grid(column=0, row=5, columnspan=2)

        # Correct answer
        self.answer_label = Label(
            text=f"Psst: pssst",
            fg="white",
            bg=THEME_COLOR,
            font=FONT_SCORE,
            pady=20
        )
        self.answer_label.grid(column=0, row=6)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):

        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.round_label.config(text=f"Round: {self.quiz.round_number + 1}")
            self.prize_label.config(text=f"Current prize: {self.quiz.current_prize}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.a_button.config(text=f"A. {self.quiz.option_a}")
            self.b_button.config(text=f"B. {self.quiz.option_b}")
            self.c_button.config(text=f"C. {self.quiz.option_c}")
            self.d_button.config(text=f"D. {self.quiz.option_d}")

            self.answer_label.config(text=f"Pssst: {self.quiz.correct_answer}")

    def a_answer(self):
        self.give_feedback(self.quiz.check_answer(user_answer=self.quiz.option_a))

    def b_answer(self):
        self.give_feedback(self.quiz.check_answer(user_answer=self.quiz.option_b))

    def c_answer(self):
        self.give_feedback(self.quiz.check_answer(user_answer=self.quiz.option_c))

    def d_answer(self):
        self.give_feedback(self.quiz.check_answer(user_answer=self.quiz.option_d))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")

            if self.quiz.round_number == 4 and self.quiz.question_number == 5:
                self.canvas.itemconfig(self.question_text,
                                       text=f"Congratulations! You've reached the end of the QuizGame!"
                                            f"Your Big Prize is: {self.quiz.current_prize}")

                self.disable_buttons()

            elif self.quiz.question_number == 5:
                self.quiz.round_number += 1
                self.quiz.current_prize += 10000 * 10
                self.quiz.question_number = 0

                self.quiz.question_list = data.data_bank[self.quiz.round_number]

            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text,
                                   text=f"Oh sorry, Wrong answer :(, your current prize is: {self.quiz.current_prize}")
            self.disable_buttons()

    def disable_buttons(self):
        self.a_button.config(state="disabled")
        self.b_button.config(state="disabled")
        self.c_button.config(state="disabled")
        self.d_button.config(state="disabled")
