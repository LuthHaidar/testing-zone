'''
Define a function called get_class_average that has one argument, students. This function returns the class average which is computed from individual average score from previous question. Your answer should be round up to the nearest whole number.
'''

import math

lloyd = {
  "name": "Lloyd",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}


students = [lloyd, alice, tyler]

def get_average(student):
    homework = sum(student["homework"]) / len(student["homework"])
    quizzes = sum(student["quizzes"]) / len(student["quizzes"])
    tests = sum(student["tests"]) / len(student["tests"])
    return math.ceil((0.1 * homework) + (0.3 * quizzes) + (0.6 * tests))

def get_class_average(students):
    class_total = 0
    for i in students:
        class_total += get_average(i)
    return math.ceil(class_total / len(students))
