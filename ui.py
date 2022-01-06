from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from quiz_game import QuizGame

THEME_COLOR = "#375362"
FONT_QUESTION = ("Arial", 20, "italic")
FONT_SCORE = ("Arial", 12, "bold")


class QuizInterface:

    def __init__(self, quiz_game: QuizGame):

        # Quiz object
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

        # Difficulty Label
        self.difficulty_label = Label(
            text="",
            fg="white",
            bg=THEME_COLOR,
            font=FONT_SCORE,
            pady=10
        )
        self.difficulty_label.grid(column=0, row=1, columnspan=2)

        # Canvas
        self.canvas = Canvas(width=350, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question here he he",
            font=FONT_QUESTION
        )

        self.canvas.grid(column=0, row=2, columnspan=2, pady=20)

        # Answer buttons
        # A.
        self.a_button = Button(
            text=f"A. Opcion 1",
            width=40,
            pady=10,
            command=self.a_answer
        )
        self.a_button.grid(column=0, row=3, columnspan=2)

        # B.
        self.b_button = Button(
            text=f"B. Opcion 2",
            width=40,
            pady=10,
            command=self.b_answer
        )
        self.b_button.grid(column=0, row=4, columnspan=2)

        # C.
        self.c_button = Button(
            text=f"B. Opcion 2",
            width=40,
            pady=10,
            command=self.c_answer
        )
        self.c_button.grid(column=0, row=5, columnspan=2)

        # D.
        self.d_button = Button(
            text=f"B. Opcion 2",
            width=40,
            pady=10,
            command=self.d_answer
        )
        self.d_button.grid(column=0, row=6, columnspan=2)

        # Correct answer
        self.answer_label = Label(
            text=f"Psst: pssst",
            fg="white",
            bg=THEME_COLOR,
            font=FONT_SCORE,
            pady=20
        )
        self.answer_label.grid(column=0, row=7)

        # Stop game and get the current prize
        self.stop_button = Button(
            text="Claim current prize",
            bg="red",
            width=20,
            pady=10,
            command=self.stop_and_save
        )
        self.stop_button.grid(column=0, row=8)

        # New game
        self.new_game_button = Button(
            text="New game",
            bg="cyan",
            width=20,
            pady=10,
            command=self.new_game
        )
        self.new_game_button.grid(column=1, row=8)
        self.new_game_button.config(state="disable")

        # Show the first question
        self.get_next_question()

        # Window loop
        self.window.mainloop()

    def get_next_question(self):
        """Toma los datos del objeto QuizGame y los muestra en pantalla para obtener la pregunta correspondiente"""
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():

            self.round_label.config(text=f"Round: {self.quiz.round_number + 1}")
            self.prize_label.config(text=f"Current prize: {self.quiz.current_prize}")

            self.quiz.difficulty(self.quiz.round_number)
            self.difficulty_label.config(text=f"Difficulty: {self.quiz.current_difficulty}")

            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.a_button.config(text=f"A. {self.quiz.option_a}")
            self.b_button.config(text=f"B. {self.quiz.option_b}")
            self.c_button.config(text=f"C. {self.quiz.option_c}")
            self.d_button.config(text=f"D. {self.quiz.option_d}")

            self.answer_label.config(text=f"Pssst: {self.quiz.correct_answer}")

    def a_answer(self):
        """Analiza la respuesta 'A' de las opciones dadas, dando un feedback y verificando la respuesta
        con la opcion correcta del QuizGame"""
        self.give_feedback(self.quiz.check_answer(user_answer=self.quiz.option_a))

    def b_answer(self):
        """Analiza la respuesta 'B' de las opciones dadas, dando un feedback y verificando la respuesta
        con la opcion correcta del QuizGame"""
        self.give_feedback(self.quiz.check_answer(user_answer=self.quiz.option_b))

    def c_answer(self):
        """Analiza la respuesta 'C' de las opciones dadas, dando un feedback y verificando la respuesta
        con la opcion correcta del QuizGame"""
        self.give_feedback(self.quiz.check_answer(user_answer=self.quiz.option_c))

    def d_answer(self):
        """Analiza la respuesta 'D' de las opciones dadas, dando un feedback y verificando la respuesta
        con la opcion correcta del QuizGame"""
        self.give_feedback(self.quiz.check_answer(user_answer=self.quiz.option_d))

    def give_feedback(self, is_right):
        """Analiza si la respuesta dada es correcta o no, además analiza la ronda actual en la que se encuentra"""
        if is_right:
            self.canvas.config(bg="green")

            if self.quiz.final_round():
                self.canvas.itemconfig(self.question_text,
                                       text=f"Congratulations! You've reached the end of the QuizGame!"
                                            f"Your Big Prize is: {self.quiz.current_prize}")

                self.disable_buttons()
                self.window.after(2000, self.player_info())
                self.quiz.player_save_data()

            elif self.quiz.next_round():
                messagebox.showinfo(title="Information", message=f"Round Clear, "
                                                                 f"next round: {self.quiz.round_number + 1}")
            self.window.after(1000, self.get_next_question)

        else:
            self.quiz.current_prize = 0
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text,
                                   text=f"Oh sorry, Wrong answer :(, your current prize is: {self.quiz.current_prize}")

            self.disable_buttons()
            self.window.after(2000, self.player_info())
            self.quiz.player_save_data()
            self.new_game_button.config(state="active", bg="cyan")

    def disable_buttons(self):
        """"Desactiva los botones de las respuestas"""
        self.a_button.config(state="disabled")
        self.b_button.config(state="disabled")
        self.c_button.config(state="disabled")
        self.d_button.config(state="disabled")

    def active_buttons(self):
        """"Activa los botones de las respuestas"""
        self.a_button.config(state="active")
        self.b_button.config(state="active")
        self.c_button.config(state="active")
        self.d_button.config(state="active")

    def player_info(self):
        """Guarda el nombre del jugador cuando decide acabar el juego, llega a la ronda final o responde mal una
        pregunta"""
        self.quiz.player_name = simpledialog.askstring(title="Save your data", prompt=f"Save you data\n"
                                                                                      f"What is your name")

    def new_game(self):
        """Permite iniciar un nuevo juego"""
        self.quiz.reset_game()
        self.window.after(1000, self.get_next_question())
        self.active_buttons()
        self.new_game_button.config(state="disable", bg="cyan")

    def stop_and_save(self):
        """Permite retirarse del juego y guardar el progreso actual con el premio actual"""
        self.disable_buttons()
        self.player_info()
        self.quiz.player_save_data()
        self.new_game_button.config(state="active", bg="cyan")
