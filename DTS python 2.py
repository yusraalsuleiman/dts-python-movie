import random

# Constants
MAX_SCORE_PER_DIFFICULTY = 15

# Quiz question data (grouped by difficulty)
movie_quiz = {
    "easy": [
        {"question": "Which movie features the character Jack Sparrow?", "options": ["A) Harry Potter", "B) Pirates of the Caribbean", "C) Titanic", "D) Avatar"], "answer": "B"},
        {"question": "Who is the snowman in 'Frozen'?", "options": ["A) Olaf", "B) Sven", "C) Kristoff", "D) Hans"], "answer": "A"},
        {"question": "Which movie is about toys that come to life?", "options": ["A) Cars", "B) Toy Story", "C) Monsters Inc.", "D) Shrek"], "answer": "B"},
        {"question": "What animal is 'Finding Nemo' about?", "options": ["A) Whale", "B) Clownfish", "C) Shark", "D) Dolphin"], "answer": "B"},
        {"question": "Which Disney movie features a genie?", "options": ["A) Mulan", "B) Aladdin", "C) Moana", "D) Tangled"], "answer": "B"},
        {"question": "Which superhero is known as the 'Caped Crusader'?", "options": ["A) Superman", "B) Iron Man", "C) Batman", "D) Spider-Man"], "answer": "C"},
        {"question": "What is the name of the cowboy in Toy Story?", "options": ["A) Buzz", "B) Woody", "C) Andy", "D) Rex"], "answer": "B"},
        {"question": "In 'The Lion King', who is Simba’s father?", "options": ["A) Scar", "B) Rafiki", "C) Mufasa", "D) Zazu"], "answer": "C"},
        {"question": "Which character wears glass slippers?", "options": ["A) Belle", "B) Elsa", "C) Ariel", "D) Cinderella"], "answer": "D"},
        {"question": "Which animal is Shrek's sidekick?", "options": ["A) Cat", "B) Dog", "C) Donkey", "D) Pig"], "answer": "C"},
        {"question": "Which film features a talking snowman?", "options": ["A) Frozen", "B) Tangled", "C) Brave", "D) Luca"], "answer": "A"},
        {"question": "Who is the main villain in 'The Little Mermaid'?", "options": ["A) Ursula", "B) Maleficent", "C) Cruella", "D) Scar"], "answer": "A"},
        {"question": "What kind of animal is Bambi?", "options": ["A) Rabbit", "B) Fox", "C) Deer", "D) Bear"], "answer": "C"},
        {"question": "Which superhero is from Wakanda?", "options": ["A) Thor", "B) Black Panther", "C) Hulk", "D) Ant-Man"], "answer": "B"},
        {"question": "Which film is about a house lifted by balloons?", "options": ["A) Up", "B) Bolt", "C) Inside Out", "D) Ratatouille"], "answer": "A"}
    ],
    "medium": [
        {"question": "Who directed 'Jurassic Park'?", "options": ["A) James Cameron", "B) Steven Spielberg", "C) Tim Burton", "D) George Lucas"], "answer": "B"},
        {"question": "Which movie is based on a book by J.R.R. Tolkien?", "options": ["A) Harry Potter", "B) The Hobbit", "C) Narnia", "D) Eragon"], "answer": "B"},
        {"question": "What is the name of the lead female character in 'Titanic'?", "options": ["A) Anna", "B) Rose", "C) Emily", "D) Sarah"], "answer": "B"},
        {"question": "Which actor played Iron Man?", "options": ["A) Chris Hemsworth", "B) Chris Evans", "C) Robert Downey Jr.", "D) Tom Holland"], "answer": "C"},
        {"question": "Which movie popularized the phrase 'May the Force be with you'?", "options": ["A) Star Trek", "B) The Matrix", "C) Star Wars", "D) Guardians of the Galaxy"], "answer": "C"},
        {"question": "What’s the name of the kingdom in 'Frozen'?", "options": ["A) Arendelle", "B) Narnia", "C) Wakanda", "D) Agrabah"], "answer": "A"},
        {"question": "Which movie features a DeLorean time machine?", "options": ["A) The Matrix", "B) Back to the Future", "C) Inception", "D) Blade Runner"], "answer": "B"},
        {"question": "Which musical is set in New York City and features rival gangs?", "options": ["A) Hairspray", "B) Chicago", "C) West Side Story", "D) Cats"], "answer": "C"},
        {"question": "Which film is about dreams within dreams?", "options": ["A) Interstellar", "B) Inception", "C) Tenet", "D) Shutter Island"], "answer": "B"},
        {"question": "Which character is the main villain in Avengers: Infinity War?", "options": ["A) Loki", "B) Thanos", "C) Ultron", "D) Red Skull"], "answer": "B"},
        {"question": "Who played the main character in 'Forrest Gump'?", "options": ["A) Brad Pitt", "B) Tom Cruise", "C) Tom Hanks", "D) Leonardo DiCaprio"], "answer": "C"},
        {"question": "In which movie does a robot clean Earth?", "options": ["A) WALL-E", "B) Big Hero 6", "C) Robots", "D) I, Robot"], "answer": "A"},
        {"question": "Which wizard was played by Ian McKellen?", "options": ["A) Gandalf", "B) Dumbledore", "C) Merlin", "D) Saruman"], "answer": "A"},
        {"question": "What is the highest-grossing movie of all time (as of 2024)?", "options": ["A) Avatar", "B) Endgame", "C) Titanic", "D) Star Wars: The Force Awakens"], "answer": "A"},
        {"question": "Which movie is set on Pandora?", "options": ["A) Avatar", "B) Dune", "C) Star Trek", "D) The Martian"], "answer": "A"}
    ],
    "hard": [
        {"question": "Who composed the score for 'Inception'?", "options": ["A) John Williams", "B) Hans Zimmer", "C) James Newton Howard", "D) Danny Elfman"], "answer": "B"},
        {"question": "Which Japanese director is known for 'Spirited Away'?", "options": ["A) Akira Kurosawa", "B) Hayao Miyazaki", "C) Mamoru Hosoda", "D) Makoto Shinkai"], "answer": "B"},
        {"question": "Which film won Best Picture at the 2020 Oscars?", "options": ["A) 1917", "B) Parasite", "C) Joker", "D) Ford v Ferrari"], "answer": "B"},
        {"question": "Which actor has the most Oscar nominations?", "options": ["A) Meryl Streep", "B) Jack Nicholson", "C) Daniel Day-Lewis", "D) Leonardo DiCaprio"], "answer": "A"},
        {"question": "Which sci-fi film did Denis Villeneuve direct?", "options": ["A) Interstellar", "B) Arrival", "C) Gravity", "D) Ad Astra"], "answer": "B"},
        {"question": "Which country produced the movie 'Roma'?", "options": ["A) Spain", "B) Mexico", "C) Brazil", "D) Argentina"], "answer": "B"},
        {"question": "Which movie features the quote 'I drink your milkshake'?", "options": ["A) No Country for Old Men", "B) The Departed", "C) There Will Be Blood", "D) Gangs of New York"], "answer": "C"},
        {"question": "What language is spoken in most of the movie 'Pan’s Labyrinth'?", "options": ["A) English", "B) French", "C) Spanish", "D) Italian"], "answer": "C"},
        {"question": "Which 1980 film starred Jack Nicholson as Jack Torrance?", "options": ["A) Chinatown", "B) One Flew Over the Cuckoo's Nest", "C) The Shining", "D) Misery"], "answer": "C"},
        {"question": "Which film features a character named Tyler Durden?", "options": ["A) Memento", "B) Fight Club", "C) Se7en", "D) Snatch"], "answer": "B"},
        {"question": "What is the name of the AI in '2001: A Space Odyssey'?", "options": ["A) EVA", "B) HAL", "C) SAM", "D) ALI"], "answer": "B"},
        {"question": "Which country is the movie 'Amélie' set in?", "options": ["A) Italy", "B) Germany", "C) Spain", "D) France"], "answer": "D"},
        {"question": "Who directed 'The Grand Budapest Hotel'?", "options": ["A) Wes Anderson", "B) Tim Burton", "C) Noah Baumbach", "D) Paul Thomas Anderson"], "answer": "A"},
        {"question": "Which animated film has no spoken dialogue for its first 20 minutes?", "options": ["A) WALL-E", "B) Up", "C) Soul", "D) Inside Out"], "answer": "A"},
        {"question": "Which movie was banned in multiple countries due to its portrayal of religion?", "options": ["A) The Da Vinci Code", "B) Life of Brian", "C) The Last Temptation of Christ", "D) All of the above"], "answer": "D"}
    ]
}

# Function to get user input and validate it
def get_valid_answer(prompt, valid_options):
    while True:
        answer = input(prompt).strip().upper()
        if answer in valid_options:
            return answer
        print(f"Invalid input. Choose from: {', '.join(valid_options)}")

# Function to run the quiz
def run_quiz():
    print("\n🎬 Welcome to the Movie and Film Trivia Quiz!")
    name = input("What's your name? ").strip() or "Player"

    # Ask user for difficulty
    print("\nChoose a difficulty level: easy / medium / hard")
    difficulty = get_valid_answer("Your choice: ", ["EASY", "MEDIUM", "HARD"]).lower()
    print(f"\nHi {name}! You selected {difficulty} difficulty. You will answer 15 questions.\n")

    total_score = 0
    questions = movie_quiz[difficulty]
    random.shuffle(questions)

    for q in questions:
        print(f"\n{q['question']}")
        for opt in q['options']:
            print(opt)
        answer = get_valid_answer("Your answer (A/B/C/D): ", ['A', 'B', 'C', 'D'])
        if answer == q['answer']:
            print("✅ Correct!")
            total_score += 1
        else:
            print(f"❌ Wrong. The correct answer was {q['answer']}.")

    print("\n=== QUIZ COMPLETE ===")
    print(f"{name}, your total score is {total_score}/{MAX_SCORE_PER_DIFFICULTY}.")

    # Feedback based on performance
    if total_score == MAX_SCORE_PER_DIFFICULTY:
        print("💯 Incredible! You're a movie trivia master!")
    elif total_score >= 12:
        print("🌟 Excellent work! You really know your films.")
    elif total_score >= 8:
        print("👍 Good job! You have solid movie knowledge.")
    else:
        print("🎬 Keep watching and learning – plenty of films to explore!")

# Run the quiz
if __name__ == "__main__":
    run_quiz()


