scores = []

def intro(): #basic intro with instructions
    print('Welcome to your database of marks!\n')
    print('To add new marks use the following format:')
    print('write_score(student, subject, score)\n')
    print('To read the students who passedthe minimum score use the following format:')
    print('read_minscore(subject, minscore)\n')
    print('Ensure that the student and subject is a string and the score is an integer or float.')
    print('For example:')
    print('write_score("Bob", "Maths", 80)')
    print('write_score("Alice", "Maths", 40)')
    print('read_minscore("Maths", 50)')
    print("Output: Here is everyone who passed the minimum score: ['Bob']")

def write_score(student, subject, score): #function to write a score to the database
    scores.append((student, subject, score))

def read_minscore(subject, minscore): #function to read students who passed the minimum score
    passes = []
    for i in scores:
        if i[1] == subject and i[2] >= minscore:
            passes.append(i[0])
    print( 'Here is everyone who passed the minimum score: ' + str(passes))

intro() #call the intro function
