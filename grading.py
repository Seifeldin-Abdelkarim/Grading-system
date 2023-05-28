def Max_M(listscores):
    Max = -20
    for i in range(len(listscores)):
        if Max < listscores[i]:
            Max = listscores[i]
    return Max
    
def Min_M(listscores):
    Min = 120
    for i in range(len(listscores)):
        if Min > listscores[i]:
            Min = listscores[i]
    return Min

def insertionSort(mylist, key=lambda x: x):
    for i in range(1, len(mylist)):
        currentvalue = mylist[i]
        position = i
        while position > 0 and key(mylist[position - 1]) > key(currentvalue):
            mylist[position] = mylist[position - 1]
            position = position - 1
        mylist[position] = currentvalue
    return mylist

def grades(num):
    for i in range(num):
        if 70 <= zipper[i][2] <= 100:
            print(zipper[i][0], zipper[i][1])
            print(Grade_Definition[0])
            print(f"{Degree_Class[0]}\n______________")
        elif 60 <= zipper[i][2] <= 69:
            print(zipper[i][0], zipper[i][1])
            print(Grade_Definition[1])
            print(f"{Degree_Class[1]}\n______________")
        elif 50 <= zipper[i][2] <= 59:
            print(zipper[i][0], zipper[i][1])
            print(Grade_Definition[2])
            print(f"{Degree_Class[2]}\n______________")
        elif 40 <= zipper[i][2] <= 49:
            print(zipper[i][0], zipper[i][1])
            print(Grade_Definition[3])
            print(f"{Degree_Class[3]}\n______________")
        else:
            print(zipper[i][0], zipper[i][1])
            print(Grade_Definition[4])
            print(Degree_Class[4], "\n______________")        

module = input("enter the module name: ")
module_code = input("enter the module code")
assess_num = int(input("enter the number of assessment: "))
student_num = int(input("enter the number of students: "))
assess_wanted = int(input("enter the assessment number you want: "))
first_name = []
last_name = []
student_ID = []
scores1 = []
scores2 = []
assess_weight = []
assess_percent = []
assess_index = []
Totals = []
Totals_percent = []
zipper = []
score_all_assessments = 0
score_all_class = 0
total_student_percent = 0
total_student = 0
for i in range(assess_num):
    assess_weight.append(int(input("enter the weight of assessment: ")))
for i in range(student_num):
    first_name.append(str(input("enter first name of student: ")))
    last_name.append(str(input("enter last name of student: ")))
    student_ID.append(input("enter ID of student: "))
    for i in range(assess_num):
        scores1.append(int(input("enter scores of student: ")))

counter = 0
for i in range(student_num):
    for i in range(assess_num):
        if i == assess_wanted:
            scores2.append(scores1[counter])
        counter = counter + 1
        
for i in range(len(scores2)):
    score_all_class += scores2[i]
for i in range(len(scores1)):
    score_all_assessments += scores1[i]
    
avg_score_assessments = score_all_assessments/assess_num

for i in range(assess_num):
    assess_index.append(i)
counter = 0
for i in range(student_num):
    for i in range(assess_num):
        total_student += scores1[counter]
        assess_percent.append((assess_weight[i]*scores1[counter])/100)
        counter = counter + 1
        if i == assess_index[-1]:
            Totals.append(total_student)
            total_student = 0
counter = 0
for i in range(student_num):
    for i in range(assess_num):
        total_student_percent += assess_percent[counter]
        counter = counter + 1
        if i == assess_index[-1]:
            Totals_percent.append(total_student_percent)
            total_student_percent = 0

Grade_Definition = ["Excellent to Outstanding", "Good to Very Good", "Satisfying", "Sufficient", "Unsatisfactory"]

Degree_Class = ["First", "Upper Second 2:1", "Lower Second 2:2", "Third 3", "Fail"]

Sort = int(input("please enter the sorting option you want, from 1 to 3: "))

for i in range(len(first_name)):
    zipper.append((first_name[i], last_name[i], Totals_percent[i], Totals[i], scores2[i]))

if Sort == 1:
    insertionSort(zipper)
    grades(student_num)
elif Sort == 2:
    insertionSort(zipper, key=lambda x: x[1])
    grades(student_num)
else:
    insertionSort(zipper, key=lambda x: x[3])
    grades(student_num)

        
avg_score_assess = score_all_class/student_num
print("the average score of class for an assessment: ", avg_score_assess, "\nthe average score for all assessments: ", avg_score_assessments, "\nthe total score for each student: ", Totals)
answer = input("enter y/n if you want to see extra details")
if answer == "y":
    maximum_minimum = int(input("enter 1 if you want to see Max and 2 for Min for spec assess or 3 for Max of the module and 4 for the Min: ")) 
    if maximum_minimum == 1:
        print(Max_M(scores2)) 
    elif maximum_minimum == 2:
        print(Min_M(scores2))
    elif maximum_minimum == 3:
        print(Max_M(scores1))
    elif maximum_minimum == 4:
        print(Min_M(scores1))
