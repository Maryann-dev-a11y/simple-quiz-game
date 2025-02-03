import random

# Function to ask the quiz questions
def ask_question(question, options, correct_answer):
    print(question)
    for option in options:
        print(option)
    user_answer = int(input("Choose 1, 2, or 3: "))
    if user_answer == correct_answer:
        return 1  # Correct answer
    else:
        return 0  # Wrong answer

# Quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["1) Paris", "2) London", "3) Rome"],
        "correct_answer": 1
    },
    {
        "question": "Which language is used for web development?",
        "options": ["1) Python", "2) JavaScript", "3) C++"],
        "correct_answer": 2
    },
    {
        "question": "What is the square root of 64?",
        "options": ["1) 6", "2) 8", "3) 10"],
        "correct_answer": 2
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["1) Mars", "2) Earth", "3) Jupiter"],
        "correct_answer": 1
    },
    {
        "question": "Who developed the theory of relativity?",
        "options": ["1) Isaac Newton", "2) Nikola Tesla", "3) Albert Einstein"],
        "correct_answer": 3
    }
]

# Main function to run the quiz
def run_quiz():
    score = 0
    random.shuffle(questions)  # Shuffle the questions to add variety each time

    for q in questions:
        score += ask_question(q["question"], q["options"], q["correct_answer"])

    print(f"\nYour total score is: {score} out of {len(questions)}")

# Ask if the user wants to play again
def main():
    play_again = "yes"
    while play_again.lower() == "yes":
        print("\nWelcome to the Quiz Game!\n")
        run_quiz()
        play_again = input("\nWould you like to play again? (yes/no): ")

    print("Thanks for playing! See you next time!")

# Run the game
main()
