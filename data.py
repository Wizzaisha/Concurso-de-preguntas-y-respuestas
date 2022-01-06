import requests
from random import shuffle
from question_model import Question

URL = "https://opentdb.com/api.php"


def get_data(difficulty: str, amount: int) -> dict:
    """Toma la dificultad y la cantidad de preguntas que se desean obtener de la API
    y retorna la información recibida de la API en forma de JSON"""

    parameters = {
        "amount": amount,
        "type": "multiple",
        "difficulty": difficulty
    }

    response = requests.get(url=URL, params=parameters)

    response.raise_for_status()

    data = response.json()

    question_data = data["results"]

    return question_data


def create_questions(questions, q_list):
    """Extrae la informacion de las preguntas, respuestas y dificultad; las organiza y adjunta a una lista"""
    for question in questions:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        all_answers = question["incorrect_answers"]
        all_answers.append(question_answer)
        shuffle(all_answers)
        difficulty = question["difficulty"]

        new_question = Question(question_text, question_answer, all_answers, difficulty)

        q_list.append(new_question)


def new_data():
    """Toma todas las peticiones para las 5 rondas, obtiene la informacion, las añade a una lista general de las 5 rondas
    y retorna dicha lista"""
    # Lista con todos los datos
    data_bank = []

    # Variables de la captura de datos para cada una de las rondas
    very_easy_data = []
    easy_data = []
    medium_data = []
    hard_data = []
    very_hard_data = []

    # Datos ronda 1
    ronda1_easy_q = get_data(difficulty="easy", amount=5)
    create_questions(ronda1_easy_q, very_easy_data)

    data_bank.append(very_easy_data)

    # Datos ronda 2
    ronda2_medium_q = get_data(difficulty="medium", amount=2)
    ronda2_easy_q = get_data(difficulty="easy", amount=3)
    create_questions(ronda2_medium_q, easy_data)
    create_questions(ronda2_easy_q, easy_data)

    data_bank.append(easy_data)

    # Datos ronda 3
    ronda3_medium_q = get_data(difficulty="medium", amount=5)
    create_questions(ronda3_medium_q, medium_data)

    data_bank.append(medium_data)

    # Datos ronda 4
    ronda4_hard_q = get_data(difficulty="hard", amount=3)
    ronda4_medium_q = get_data(difficulty="medium", amount=2)
    create_questions(ronda4_hard_q, hard_data)
    create_questions(ronda4_medium_q, hard_data)

    data_bank.append(hard_data)

    # Datos ronda 5
    ronda5_hard_q = get_data(difficulty="hard", amount=5)
    create_questions(ronda5_hard_q, very_hard_data)

    data_bank.append(very_hard_data)

    return data_bank
