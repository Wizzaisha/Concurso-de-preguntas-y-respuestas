import html


class QuizGame:

    def __init__(self, q_list):
        self.round_number = 0
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_rounds(self):
        return self.round_number < 6

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1

        q_text = html.unescape(self.current_question.text)

        question = f"Round: {self.round_number}\n" \
                   f"Q. {self.question_number} {q_text}\n" \
                   f"A. {self.current_question.all_answers[0]}\n" \
                   f"B. {self.current_question.all_answers[1]}\n" \
                   f"C. {self.current_question.all_answers[2]}\n" \
                   f"D. {self.current_question.all_answers[3]}\n" \
                   f"Pssst: {self.current_question.answer}"

        user_answer = input(question)
        self.check_answer(user_answer, self.current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("YAY!")
            self.score += 1
        else:
            print("Oh nyo")
