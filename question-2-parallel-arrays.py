students = [ "Doe", "Roe", "Smith", "Jones", "Wang", "Diaz" ]
scores   = [   75,    88,      93,     83,     78,      94  ]
def findTopStudent(students, scores):
    topStudent = ""
    topScore = 0
    for i in range(len(students)):
        if scores[i] > topScore:
            topStudent = students[i]
            topScore = scores[i]
            topstudentlist = [(topStudent, topScore)]
    for i in range(len(students)):
        if scores[i] = topScore and students[i] is not topStudent:
            topstudentlist.append(topStudent, topScore))
    return topstudentlist