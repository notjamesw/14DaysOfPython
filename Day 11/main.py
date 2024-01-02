# Declare variables
score = 0
streak = False
messages = {
    "welcome":"Answer correctly to win a point.\nBonuses for winning streaks",
    "correct":"Well done! You got it!",
    "incorrect":"That is incorrect, sorry :(",
    "another_question": "Do you want another question?\n"
}

# Print welcome message
print(messages["welcome"])
print(f"Your current score is : {score}")

# Define questions 
question1 = {
    "question":"What shape has no sides?",
    "choices":["a) Square","b) Rectangle","c) Circle"],
    "answer":"c"
}   
question2 = {
    "question":"What shape has 3 sides?",
    "choices":["a) Square","b) Triangle","c) Circle"],
    "answer":"b"
}
question3 = {
    "question":"What shape has 6 sides?",
    "choices":["a) Hexagon","b) Triangle","c) Circle"],
    "answer":"a"
}

# Create list of all questions
all_questions = [question1,question2,question3]

# Loop through all questions and display questions
for each_question in all_questions:
    print(each_question["question"])
    for choice in each_question["choices"]:
        print(choice)
    answer = input("What is your answer a, b or c: \n").lower()
    if answer == each_question["answer"]:
        print(messages["correct"])
        if streak == True:
            score *= 10
        else:
            score += 10
        print(f"Your current score is {score}")
        streak = True
    else:
        print(messages["incorrect"])
        print(f"Your current score is still {score}")
        streak = False
    another_question = input(messages["another_question"]).lower()
    if another_question == "yes":
        continue
    else:
        break