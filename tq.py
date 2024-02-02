import requests
import json

class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def ask_question(self):
        print(self.text)
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")

    def check_answer(self, answer):
        return answer == self.correct_option

def get_trivia_questions():
    api_url = "https://opentdb.com/api.php"
    params = {
        "amount": 3,  # Adjust the number of questions as needed
        "type": "multiple",
    }

    response = requests.get(api_url, params=params)
    data = json.loads(response.text)

    if response.status_code == 200 and data["response_code"] == 0:
        questions = []
        for result in data["results"]:
            text = result["question"]
            options = result["incorrect_answers"] + [result["correct_answer"]]
            correct_option = options.index(result["correct_answer"]) + 1
            questions.append(Question(text, options, correct_option))
        return questions
    else:
        print("Failed to fetch trivia questions.")
        return None

def trivia_quiz():
    print("Welcome to the Trivia Quiz!")

    questions = get_trivia_questions()

    if not questions:
        return

    score = 0

    for question in questions:
        question.ask_question()
        answer = int(input("Your answer (enter the corresponding number): "))
        
        if question.check_answer(answer):
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {question.correct_option}: {question.options[question.correct_option - 1]}\n")

    print(f"Quiz completed! Your final score is {score}/{len(questions)}.")

if __name__ == "__main__":
    trivia_quiz()
