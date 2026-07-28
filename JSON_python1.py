import json
student = {
    "name": "vishnu",
    "age":18,
    "branch":"cse AI/ML",
    "cgpa":9.2
    }
with open("student.json","w")as file:
    json.dump(student,file,indent=4)
print("file created")
