class Question:

    def __init__(self, q_text: str, q_answer: str, all_answers: list, difficulty: str):
        """Modelo de las """

        self.text = q_text
        self.answer = q_answer
        self.all_answers = all_answers
        self.difficulty = difficulty
