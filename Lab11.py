import matplotlib.pyplot as plt
import os
import math


assignmentsRaw = open("data/assignments.txt", "r")
assignments = []

counter = 0
count = 0
ass = []
for content in assignmentsRaw:
    count += 1
    if counter < 3:
        counter += 1
        ass.append(content[:-1])
    else:
        counter = 1
        assignments.append(ass)
        ass = []
        ass.append(content[:-1])
    if (count == 57):
        assignments.append(ass)
studentsRaw = open("data/students.txt", "r")
students = []
for content in studentsRaw:
    students.append(content[:-1])
students[len(students)-1] = "462Elizabeth Butcher"
submissions = []
for (r,d,f) in os.walk("data/submissions"):
    for i in range(0, len(f)):
        sub = open("data/submissions/" + f[i])
        for content in sub:
            submissions.append(content.split("|"))

def FindAssignmentPoints(assid):
    for i in range(0, len(assignments)):
        if assignments[i][1] == assid:
            return assignments[i][2]
        else:
            pass
    pass

def FindAssignmentScores(assName):
    scores = []
    for i in assignments:
        if i[0] == assName:
            assid = i[1]
    if assid == "":
        print("Assignment not found")
        return None
    for i in range(0, len(submissions)):
        if submissions[i][1] == assid:
            scores.append(int(submissions[i][2]))

    return scores

def GradeCalc(student):
    totalPoints = 0
    sid = ""
    for i in students:
        if student in i:
            sid = i[:3]
    if sid == "":
        print("Student not found")
        return None
    for i in submissions:
        if i[0] == sid:
            points = FindAssignmentPoints(i[1])
            totalPoints += int(points) / 100 * int(i[2])
    grade = totalPoints / 1000 * 100
    return round(grade)

print("1. Student grade")
print("2. Assignment statistics")
print("3. Assignment graph")
print("\n")
opt = input("Enter your selection: ")
if opt == "1":
    name = input("What is the student's name: ")
    if GradeCalc(name) != None:
        print(f"{GradeCalc(name)}%")
if opt == "2":
    assignment = input("What is the assignment name: ")
    if FindAssignmentScores(assignment) != None:
        scores = FindAssignmentScores(assignment)
        minimum = math.floor(min(scores))
        maximum = math.floor(max(scores))
        average = math.floor(sum(scores) / len(scores))
        print(f"Min: {minimum}%")
        print(f"Avg: {average}%")
        print(f"Max: {maximum}%")
if opt == "3":
    assignment = input("What is the assignment name: ")
    if FindAssignmentScores(assignment) != None:
        scores = FindAssignmentScores(assignment)
        plt.hist(scores, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
        plt.show()
