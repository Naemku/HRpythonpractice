python_students=[]
score_list=[]
low_student_list=[]
for _ in range(int(input())):
    name=input()
    score=float(input())
    score_list.append(score)
    python_students.append([name,score])
sorted_score=sorted(set(score_list))
second_low_score=sorted_score[1]
for i in python_students:
    if i[1]==second_low_score:
        low_student_list.append(i[0])
sorted_low_student_list=sorted(low_student_list)
for x in sorted_low_student_list:
    print(x)
