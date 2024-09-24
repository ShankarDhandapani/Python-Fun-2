import pandas as pd
import csv

group = {}

group[1] = []

group[2] = []

group[3] = []

group[4] = []

group[5] = []

group[6] = []

group[7] = []

group[8] = []

group[9] = []

group[10] = []

group_a = pd.read_csv('100_Days_of_Code_V2_GroupA.csv')
group_b = pd.read_csv('100_Days_of_Code_V2_GroupB.csv')

column_names = []

for i in group_a:
    column_names.append(i)

students_less_50 = []
students_less_50.append(column_names)

for j in range(len(group_a['percent_complete'])):
    student_caught = []
    if group_a['percent_complete'][j] < 51:
        for i in column_names:
            student_caught.append(group_a[i][j])
        group_id = ""
        for i in group:
            if group_a['email'][j] in group[i]:
                group_id = str(i)
        if group_id == "":
            group_id = "Not Recognised"
        student_caught.append(group_id)
        student_caught.append("A")
        students_less_50.append(student_caught)

for j in range(len(group_b['percent_complete'])):
    student_caught = []
    if group_b['percent_complete'][j] < 51:
        for i in column_names:
            student_caught.append(group_b[i][j])
        group_id = ""
        for i in group:
            if group_b['email'][j] in group[i]:
                group_id = str(i)
        if group_id == "":
            group_id = "Not Recognised"
        student_caught.append(group_id)
        student_caught.append("B")
        students_less_50.append(student_caught)

students_less_50[0].append("Group_Number")
students_less_50[0].append("Group Id")
with open('student_less_than_50.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(students_less_50)
