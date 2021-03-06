'''
Write a function called get_average that takes a student dictionary (like lloyd, alice, or tyler) as input and returns his/her weighted average.

Define a function called get_average that takes one argument called student.
Make a variable homework that stores the average() of student["homework"].
Repeat step 2 for "quizzes" and "tests".
Multiply the 3 averages by their weights and return the sum of those three. Homework is 10%, quizzes are 30% and tests are 60%. Round up your answer to the nearest whole number.
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