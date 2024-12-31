import json

datas = {"sid": 66, "name": "bobby", "grade": "D"}

#print(datas['sid'])
mylist = [11, 2, 3, 4, 1]
#print(len(mylist))

myl = (mylist.copy())
students = \
    [
        {"id": 1,
         "name": "Bobby",
         "Grade": ["A","B"]
         },
        {"id": 2,
         "name": "Kumar",
         "Grade": ["C","A"]
         },
        {"id": 3,
         "name": "Chikkala",
         "Grade": ["C", "D"]
         }
    ]
studentData = '{"id": 3,"name": "Chikkala","Grade": ["C", "D"]}'



jsonresult = json.loads(studentData)

print(jsonresult)
# for student in students:
#     print(student["id"])
#     print(student["name"])
#     print(student["Grade"][1])

