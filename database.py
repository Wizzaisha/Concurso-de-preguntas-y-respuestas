import datetime
from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://Wizz:Gato123@wizzdatabase.8e9zq.mongodb.net/myFirstDatabase?retryWrites=true&w" \
                    "=majority"

client = MongoClient(CONNECTION_STRING)
db = client["GameQuizHistory"]

collection_name = db["game_record"]


def save_data(player_name, prize, difficulty, current_round):
    """Permite guardar los datos y enviarlos a la base de datos correspondiente del QuizGame"""
    schema_data = {
        "player_name": player_name,
        "prize": prize,
        "difficulty": difficulty,
        "round": current_round,
        "date": datetime.datetime.utcnow()
    }

    collection_name.insert_one(schema_data)

