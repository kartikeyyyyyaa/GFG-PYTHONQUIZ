import json
import random

def downloadquestions(files):
    """Loads questions from the JSON file."""
    try:
        with open(files, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Error: The file 'questions.json' was not found.")
        return []

def run_quiz(questions):
    score = 0
    total_questions = len(questions)

    #Randomize the questions
    random.shuffle(questions)

    print("\n WELCOME TO GFG PYTHON QUIZ \n")

    for index, item in enumerate(questions, 1):
        print(f"Question {index}: {item['question']}")
        
        # Display options
        for i, option in enumerate(item['options'], 1):
            print(f"{i}. {option}")
        
        useranswer = input("\nType the correct option (text): ").strip()

        if useranswer.lower() == item['answer'].lower():
            print("Correct! ✅\n")
            score += 1
        else:
            print(f"Wrong! ❌ The correct answer was: {item['answer']}\n")
    print("Your Response has been recorded")
    print(f"QUIZ FINISHED!")
    print(f"Your Score: {score}/{total_questions}")
    percentage = (score / total_questions) * 100
    print(f"Percentage: {percentage}%")
    print("--------------------------------")

if __name__ == "__main__":
    # Requirement 1: Load questions from JSON
    questiondata = downloadquestions('questions.json')
    
    if questiondata:
        run_quiz(questiondata)