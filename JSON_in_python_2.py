#1 saving student details:
import json
student = {
    "name": "vishnu",
    "age": 18,
    "branch": "CSE AI/ML"
}
with open("student.json","w") as file:
    json.dump(student,file,indent=4)
    print("JSON file created successfully")

#2 saving favourite animes list:

import json

anime = {
    "favorites": [
        "One Piece",
        "Attack on Titan",
        "the fragrant flowers blooms with dignity",
        "love unseen beneath the clear night sky"
    ]
}

with open("anime.json", "w") as file:
    json.dump(anime, file, indent=4)

with open("anime.json", "r") as file:
    data = json.load(file)

print("Favorite Anime:")

for show in data["favorites"]:
    print(show)

#3 saving our previous expenses with JSON:

import json

expenses = [
    {
        "category": "Food",
        "amount": 250
    },
    {
        "category": "Travel",
        "amount": 730
    },
    {
        "category": "Books",
        "amount": 1250
    }
]

with open("expenses.json", "w") as file:
    json.dump(expenses, file, indent=4)

with open("expenses.json", "r") as file:
    data = json.load(file)

total = 0

for expense in data:
    print(expense["category"], "$", expense["amount"])
    total += expense["amount"]

print("Total Spending = $", total)
