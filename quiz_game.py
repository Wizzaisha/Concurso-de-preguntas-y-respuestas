import data
import html


class QuizGame:

    def __init__(self):
        # Round
        self.round_number = 0
        # No. Question
        self.question_number = 0

        # Prizes
        self.current_prize = 0

        # Question data
        self.question_list = data.data_bank[self.round_number]

        # Question text and answers
        self.current_question = None
        self.correct_answer = None
        self.option_a = None
        self.option_b = None
        self.option_c = None
        self.option_d = None

        # Player name
        self.player_name = ""

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):

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

        if user_answer == self.correct_answer:
            return True
        else:
            return False

    def final_round(self):
        return self.round_number == 4 and self.question_number == 5

    def next_round(self):
        if self.question_number == 5:
            self.current_prize += 10000 * 10
            self.question_number = 0
            self.round_number += 1
            self.question_list = data.data_bank[self.round_number]

            return True
