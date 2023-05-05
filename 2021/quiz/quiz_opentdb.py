#Quiz bikin sendiri

from class_questions_v2 import *
from class_score import *

print(logo)

q_category = input("Pilih kategori? 1-Film 2-Musik 3-Video Games 4-Science Nature 5-Computer 6-Geography? ")

if q_category == "1":
    q_category = "11"
elif q_category == "2":
    q_category = "12"
elif q_category == "3":
    q_category = "15"
elif q_category == "4":
    q_category = "17"
elif q_category == "5":
    q_category = "18"
elif q_category == "6":
    q_category = "22"

q_amount = input("How many questions? (1)10 (2)20 (3)30 ")

if q_amount == "1":
    q_amount = "10"
elif q_amount == "2":
    q_amount = "20"
elif q_amount == "3":
    q_amount = "30"

q_diff = input("Difficulty? (1)easy (2)medium (3)hard (4)mixed ")

if q_diff == "1":
    q_diff = "easy"
elif q_diff == "2":
    q_diff = "medium"
elif q_diff == "3":
    q_diff = "hard"
else:
    q_diff = ""

pertanyaan = QuestionsOpenTDB(q_amount, q_category, q_diff)

skor = Scoring()

play = True

while play:
    
    print(f"Q.{pertanyaan.get_questions_number()}: {pertanyaan.question()}? ")
        
    possible_answer = pertanyaan.possible_answer()

    if len(possible_answer)== 4:
        
        print(f"1. {possible_answer[0]}")
        print(f"2. {possible_answer[1]}")
        print(f"3. {possible_answer[2]}")
        print(f"4. {possible_answer[3]}")

        tf = int(input("Choose 1, 2, 3, 4? "))
    
    elif len(possible_answer) == 2:
        
        print(f"1. {possible_answer[0]}")
        print(f"2. {possible_answer[1]}")

        tf = int(input("Choose 1, 2? "))
    

    if possible_answer[tf-1] == pertanyaan.correct_answer():
        print("You got it right!")        
        skor.score_up()

    else:
        print("That's wrong!")

    print(f"The correct answer was : {pertanyaan.correct_answer()}")
    print(f"Your current score is {skor.get_score()}/{pertanyaan.get_questions_number()}")
    
    print("")
    print("")

    play = pertanyaan.next()

print("Bye")
