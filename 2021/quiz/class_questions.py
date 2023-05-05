# Class Questions
import random,json
from urllib.request import urlopen


logo = """
  ______             __           
 /      \           /  |          
/$$$$$$  | __    __ $$/  ________ 
$$ |  $$ |/  |  /  |/  |/        |
$$ |  $$ |$$ |  $$ |$$ |$$$$$$$$/ 
$$ |_ $$ |$$ |  $$ |$$ |  /  $$/  
$$ / \$$ |$$ \__$$ |$$ | /$$$$/__ 
$$ $$ $$< $$    $$/ $$ |/$$      |
 $$$$$$  | $$$$$$/  $$/ $$$$$$$$/ 
     $$$/                         
                                  
                                 
"""


question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

# https://opentdb.com/api.php?amount=3&category=18
question_opentdb_com={"response_code":0,"results":
	[
		{"category":"Science: Computers","type":"multiple","difficulty":"medium","question":"On which day did the World Wide Web go online?","correct_answer":"December 20, 1990","incorrect_answers":["December 17, 1996","November 12, 1990","November 24, 1995"]},
		{"category":"Science: Computers","type":"multiple","difficulty":"hard","question":"Which of the following is the oldest of these computers by release date?","correct_answer":"TRS-80","incorrect_answers":["Commodore 64","ZX Spectrum","Apple 3"]},
		{"category":"Science: Computers","type":"multiple","difficulty":"medium","question":"What does the term GPU stand for?","correct_answer":"Graphics Processing Unit","incorrect_answers":["Gaming Processor Unit","Graphite Producing Unit","Graphical Proprietary Unit"]}
        ]
        }


class Questions:
    """Kelas yang menghandle pertanyaan"""
    nmr = 1

    def __init__(self,l):
        self.all_questions = l
    
    def count(self):
        return len(self.all_questions)

    def next(self):
        if self.nmr < self.count():
            self.nmr += 1
            return True
        else:
            return False
    
    def get_questions_number(self):
        return self.nmr

    def question(self):
        return self.all_questions[self.nmr-1]["text"]
    
    def answer(self):
        return "True" if self.all_questions[self.nmr-1]["answer"] == 'True' else "False"
       

# Umum https://opentdb.com/api.php?amount=30
# Komputer https://opentdb.com/api.php?amount=30&category=18

class QuestionsOpenTDB:
    """Kelas yang menghandle pertanyaan"""

    url = "https://opentdb.com/api.php?amount=30&category=18"
    nmr = 1
    all_possible_answer = []
    lst = []
    all_questions= []    

    def __init__(self):
        self.response = urlopen(self.url)
        self.all_questions = json.loads(self.response.read())
        self.all_questions = self.all_questions["results"]

    
    def count(self):
        return len(self.all_questions)

    def next(self):
        if self.nmr < self.count():
            self.nmr += 1
            return True
        else:
            return False
    
    def get_questions_number(self):
        return self.nmr

    def question(self):
        return self.all_questions[self.nmr-1]["question"]
    
    def possible_answer(self):
        
        self.lst = self.all_questions[self.nmr-1]["incorrect_answers"]
        self.lst.append(self.all_questions[self.nmr-1]["correct_answer"])
        random.shuffle(self.lst)

        return self.lst


    def correct_answer(self):
        return self.all_questions[self.nmr-1]["correct_answer"]
       

