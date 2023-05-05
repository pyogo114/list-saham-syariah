#Quiz bikin sendiri

from class_questions import *
from class_score import *

#ambil pertanyaan dari list
pertanyaan = Questions(question_data)

skor = Scoring()

print(logo)

play = True

while play:

    tf = input(f"Q.{pertanyaan.get_questions_number()}: {pertanyaan.question()} (True/False)? ")

    if tf == pertanyaan.answer():
        print("You got it right!")        
        skor.score_up()

    else:
        print("That's wrong!")

    print(f"The correct answer was :{pertanyaan.answer()}")
    print(f"Your current score is {skor.get_score()}/{pertanyaan.get_questions_number()}")
    
    print("")
    print("")

    play = pertanyaan.next()

print("Bye")
