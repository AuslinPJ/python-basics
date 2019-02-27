s2 = {'name': 'arjun', 'rollno': 2}
s1 = {'name': 'achu', 'rollno': 1}
students = {'s2': s2 , 's1': s1}

print(students)

for i in students:
    print(i)
    print(students[i])
    for details in students[i]:
        print(students[i][details])

for i,j in students.items():
    print("key",i)
    print ("value",j)
    for details in j:
        print(j[details]) 


