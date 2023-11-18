import random

def quiz_game(questions):
    score = 0
    random.shuffle(questions)  # Shuffle the questions for variety

    for i, question in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {question['question']}")
        for j, choice in enumerate(question['choices'], start=1):
            print(f"{j}. {choice}")

        user_answer = get_user_answer()
        if user_answer == question['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}\n")

    print(f"Your final score is {score}/{len(questions)}")

def get_user_answer():
    while True:
        try:
            user_input = int(input("Enter the number of your answer: "))
            if 1 <= user_input <= 4:
                return user_input
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

# Sample questions
quiz_questions = [
    {
        'question': 'What is the capital of France?',
        'choices': ['Berlin', 'Madrid', 'Paris', 'Rome'],
        'answer': 3,
    },
    {
        'question': 'Which programming language is this quiz written in?',
        'choices': ['Java', 'Python', 'C++', 'JavaScript'],
        'answer': 2,
    },
    {
        'question': 'What is the capital of Canada?',
        'choices': ['Ottawa', 'Toronto', 'Vancouver', 'Montreal'],
        'answer': 0,
    },
    {
        'question': 'Who is the first woman to win a Nobel Prize?',
        'choices': ['Marie Curie', 'Rosalind Franklin', 'Ada Lovelace', 'Jane Goodall'],
        'answer': 0,
    },
    {
        'question': 'What is the main ingredient in guacamole?',
        'choices': ['Tomato', 'Avocado', 'Onion', 'Cilantro'],
        'answer': 1,
    },
    {
        'question': 'Which planet is known as the "Red Planet"?',
        'choices': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
        'answer': 0,
    },
    {
        'question': 'Who painted the Mona Lisa?',
        'choices': ['Vincent van Gogh', 'Leonardo da Vinci', 'Pablo Picasso', 'Claude Monet'],
        'answer': 1,
    },
    {
        'question': 'What is the currency of Japan?',
        'choices': ['Won', 'Yuan', 'Yen', 'Ringgit'],
        'answer': 2,
    },
    {
        'question': 'Which element has the chemical symbol "H"?',
        'choices': ['Helium', 'Hydrogen', 'Hassium', 'Hafnium'],
        'answer': 1,
    },
    {
        'question': 'Who wrote "To Kill a Mockingbird"?',
        'choices': ['Harper Lee', 'Ernest Hemingway', 'F. Scott Fitzgerald', 'Mark Twain'],
        'answer': 0,
    },
    {
        'question': 'In what year did the Titanic sink?',
        'choices': ['1912', '1905', '1920', '1931'],
        'answer': 0,
    },
    {
        'question': 'What is the largest ocean on Earth?',
        'choices': ['Atlantic Ocean', 'Indian Ocean', 'Southern Ocean', 'Pacific Ocean'],
        'answer': 3,
    },
    # Add more questions as needed
]

# Start the quiz
quiz_game(quiz_questions)
