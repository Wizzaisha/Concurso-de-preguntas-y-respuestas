import data
import html
import database


class QuizGame:

    def __init__(self):
        # Round
        self.round_number = 0
        # No. Question
        self.question_number = 0

        # Prizes
        self.current_prize = 0

        # Question data
        self.data_game = data.new_data()
        self.question_list = self.data_game[self.round_number]

        # Question text and answers
        self.current_question = None
        self.correct_answer = None
        self.current_difficulty = None
        self.option_a = None
        self.option_b = None
        self.option_c = None
        self.option_d = None

        # Player name
        self.player_name = ""

    def still_has_questions(self):
        """Retorna la condicion sobre las preguntas restantes"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Incorpora la informacion de la pregunta actual y sus respuestas"""
        self.current_question = self.question_list[self.question_number]

        self.option_a = html.unescape(self.current_question.all_answers[0])
        self.option_b = html.unescape(self.current_question.all_answers[1])
        self.option_c = html.unescape(self.current_question.all_answers[2])
        self.option_d = html.unescape(self.current_question.all_answers[3])
        self.correct_answer = html.unescape(self.current_question.answer)

        q_text = html.unescape(self.current_question.text)

        self.question_number += 1

        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        """Verfica si la respuesta data por el usuario es correcta; retornando verdadero si es la respuesta o falso
        si no es"""
        if user_answer == self.correct_answer:
            return True
        else:
            return False

    def final_round(self):
        """Vertifica si el usuario se encuentra en la ronda final"""
        return self.round_number == 4 and self.question_number == 5

    def next_round(self):
        """Actualiza los valores para pasar a la siguiente ronda"""
        if self.question_number == 5:
            self.current_prize += 10000 * 10
            self.question_number = 0
            self.round_number += 1
            self.question_list = self.data_game[self.round_number]

            return True

    def difficulty(self, round_num):
        """Obtiene la dificultan en la que se encuentra el usuario"""
        if round_num == 0:
            self.current_difficulty = "Very Easy"
        elif round_num == 1:
            self.current_difficulty = "Easy"
        elif round_num == 2:
            self.current_difficulty = "Medium"
        elif round_num == 3:
            self.current_difficulty = "Hard"
        elif round_num == 4:
            self.current_difficulty = "Very Hard"

    def player_save_data(self):
        """Guarda la informacion de los valores actuales del premio, dificultad y la ronda; usando el esquema de
        la base de datos"""
        database.save_data(
            player_name=self.player_name,
            prize=self.current_prize,
            difficulty=self.current_difficulty,
            current_round=self.round_number+1,
        )

    def reset_game(self):
        """"Resetea a los valores por defecto del juego para iniciar uno nuevo"""
        self.current_prize = 0
        self.question_number = 0
        self.round_number = 0
        self.data_game = data.new_data()
        self.question_list = self.data_game[self.round_number]
