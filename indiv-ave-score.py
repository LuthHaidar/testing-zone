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

ave = 0

def indivAveScore(name, scoringItem):
    try:
        if (name != "Lloyd" and name != "Alice" and name != "Tyler") and (scoringItem != "homework" and scoringItem != "quizzes" and scoringItem != "tests"):
            return -1
        name = name.lower()
        name = globals()[name]
        total = 0
        for score in name[scoringItem]:
            total += int(score)
    except:
        return -1
    else:
        return total / len(name[scoringItem])