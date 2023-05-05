# Grading

student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62
}

# Rubah angka tadi ke91-100 outstanding, 81-90 Exceeds \
# Expeptations, 71-80 Acceptable, < 70 Fail

def grading(i):
    if i > 91:
        return "Outstanding"
    elif i >= 81 and i <= 90:
        return "Exceeds Expectations"
    elif i >= 71 and i <= 80:
        return "Acceptable"
    else:
        return "Fail"



print(student_scores) 

for key in student_scores:
    student_scores[key] = grading(student_scores[key])

print(student_scores) 