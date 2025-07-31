'''

Dictionary Comprehension Example

'''

students = ["Hermione", "Harry", "Ron"]

gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})

# Modification with Dict Comprehension
# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# More pythonic way using Dict Comprehension
# gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)