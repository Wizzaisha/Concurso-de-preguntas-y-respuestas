import data
from quiz_game import QuizGame


round1_questions = data.very_easy_data

round1 = QuizGame(round1_questions)

while round1.still_has_rounds():
    round1.next_question()

# round2_questions = data.easy_data
#
# round3_questions = data.medium_data
#
# round4_questions = data.hard_data
#
# round5_questions = data.very_hard_data