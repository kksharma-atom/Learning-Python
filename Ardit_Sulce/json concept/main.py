import json

with open("Ardit_Sulce/json concept/questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

answers = []
score = 0

for question in data:
    print(question["question_text"])

    for index, value in enumerate(question["alternatives"], start=1):
        print(f"{index} -{value}")
    
    user_input = int(input("Enter the coorect answer: "))

    if user_input == question["correct_answer"]:
        result = "Correct Answer"
        score = score + 1
    else:
        result = "Incorrect Answer"
    
    question["user_input"] = user_input
    question["result"] = result


print("Result")

for index, value in enumerate(data, start=1):
    print(f"{index} - {value['result']} User Answer: {value['user_input']} Correct Answer: {value['correct_answer']}  ")

print("Score: ", score, "/", len(data))

