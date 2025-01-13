import json

# Open and read the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Print the data
print(type(data))

for quiz in data:
    print("quizzes",quiz)
    print("subjects",data[quiz])