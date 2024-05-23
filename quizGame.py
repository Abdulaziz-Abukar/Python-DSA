"""
Quiz Game!
"""

questions = {
    "Q1": {
        "question": "How much does Abdul love you?: ",
        "options": {
            "A": "A little",
            "B": "A lot",
            "C": "Infinity",
            "D": "A bit"
        },
        "answer": "C"
    },
    "Q2": {
        "question": "Whats Abdul's favourite thing about you?: ",
        "options": {
            "A": "Your hair",
            "B": "Your eyes",
            "C": "Your Smile",
            "D": "Your Character, and maybe your titties too"
        },
        "answer": "D"
    },
    "Q3": {
        "question": "If Abdul could go to one place with you right now, where would it be?: ",
        "options": {
            "A": "France",
            "B": "Italy",
            "C": "Greece",
            "D": "Anywhere as long as it's with you"
        },
        "answer": "D"
    },
    "Q4": {
        "question": "What helps Abdul relax?: ",
        "options": {
            "A": "Video games",
            "B": "Anime",
            "C": "Anime video games",
            "D": "Sucking Tittes while watching anime"
        },
        "answer": "D"
    },
    "Q5": {
        "question": "How tall is Abdul?: ",
        "options": {
            "A": "4'10",
            "B": "5'6",
            "C": "6'2",
            "D": "5'10"
        },
        "answer": "C"
    },
    "Q6": {
        "question": "Whats Abdul's favourite animal?: ",
        "options": {
            "A": "Panda",
            "B": "Lion",
            "C": "Monkey",
            "D": "Bear"
        },
        "answer": "C"
    },
    "Q7": {
        "question": "Whats one thing Abdul loves about you?: ",
        "options": {
            "A": "Everything about you",
            "B": "Your mustache",
            "C": "Your tittes",
            "D": "Your nails"
        },
        "answer": "A"
    },
    "Q8": {
        "question": "If abdul could change one thing about you, what would it be?: ",
        "options": {
            "A": "For you to stop asking to go out past 8pm",
            "B": "your attitude sometimes",
            "C": "Nothing :)",
            "D": "Overthinking"
        },
        "answer": "C"
    },
    "Q9": {
        "question": "Does Abdul ever cry?: ",
        "options": {
            "A": "Sometimes",
            "B": "Yes, all the time",
            "C": "NO!",
            "D": "Not infront of me"
        },
        "answer": "D"
    },
    "Q10": {
        "question": "Abdul's favourite anime?: ",
        "options": {
            "A": "Bleach",
            "B": "Dragonball Z",
            "C": "Attack on Titan",
            "D": "Naruto"
        },
        "answer": "B"
    },
    "Q11": {
        "question": "In Naruto the anime, who is Abdul's favourite character?: ",
        "options": {
            "A": "Naruto",
            "B": "Itachi",
            "C": "Sasuke",
            "D": "Kakashi"
        },
        "answer": "B"
    },
    "Q12": {
        "question": "What is Abdul's favourite colour?: ",
        "options": {
            "A": "Black",
            "B": "Blue",
            "C": "Purple",
            "D": "Red"
        },
        "answer": "D"
    },
    "Q13": {
        "question": "Is Abdul an overthinker?: ",
        "options": {
            "A": "No",
            "B": "Yes",
            "C": "Yes, but he doesn't show it",
            "D": "Yes, only when he's trying his best to make me happy"
        },
        "answer": "D"
    },
    "Q14": {
        "question": "What is Abdul's favourite choice of deameanor?: ",
        "options": {
            "A": "Excitment",
            "B": "Worry",
            "C": "Edgy",
            "D": "Sad"
        },
        "answer": "C"
    },
    "Q15": {
        "question": "What's Abdul's favourite thing to ask you all the time?: ",
        "options": {
            "A": "Let me eat ur ass pls",
            "B": "Hey Babe, I'm hungry",
            "C": "Can you please be quiet",
            "D": "WHATS THE MATTER WITH YOU"
        },
        "answer": "A"
    },
    "Q16": {
        "question": "What helps abdul fall asleep?: ",
        "options": {
            "A": "A warm blanket",
            "B": "Hearing noises",
            "C": "Cuddling with you <3",
            "D": "Nothing, he is nocturnal"
        },
        "answer": "C"
    },
    "Q17": {
        "question": "What goes on in Abdul's mind when someone is talking to him?: ",
        "options": {
            "A": "Random thoughts",
            "B": "Nothing",
            "C": "What he's going to eat for his next meal",
            "D": "Tittes"
        },
        "answer": "D"
    },
    "Q18": {
        "question": "What drives Abdul to keep pushing?: ",
        "options": {
            "A": "fulfillment",
            "B": "Satisfaction",
            "C": "A comfortable future with you",
            "D": "Money"
        },
        "answer": "C"
    },
    "Q19": {
        "question": "What kind of car will Abdul buy you in the future?: ",
        "options": {
            "A": "Range Rover",
            "B": "Honda Civic",
            "C": "Toyota Camry",
            "D": "Jeep Wrangler"
        },
        "answer": "B"
    },
    "Q20": {
        "question": "Ask Abdul to kiss you right now. How does he look after?: ",
        "options": {
            "A": "Sad",
            "B": "Angry",
            "C": "Hurt",
            "D": "Happy"
        },
        "answer": "D"
    },
    "Q21": {
        "question": "What's one thing Abdul looks forward to in our future?: ",
        "options": {
            "A": "a Big House",
            "B": "Big Family",
            "C": "Money",
            "D": "Anal"
        },
        "answer": "B"
    },
    "Q22": {
        "question": "Ask Abdul a question right now. What did he say?: ",
        "options": {
            "A": "Monkey",
            "B": "Negro",
            "C": "REEEEEeeeeEEEEeEeEEeEeEe",
            "D": "LOL"
        },
        "answer": "C"
    },
    "Q23": {
        "question": "What is Abdul's favourite game?: ",
        "options": {
            "A": "League of Legends",
            "B": "Gang Beasts",
            "C": "Cyberpunk 2077",
            "D": "Rocket League"
        },
        "answer": "D"
    },
    "Q24": {
        "question": "What's one thing you could say right now to hurt Abdul's feelings?: ",
        "options": {
            "A": "You'll never become Grand Champion in Rocket League",
            "B": "I don't care about your silly cartoon animes",
            "C": "You are not Goku and you'll never be Goku",
            "D": "Go kill yourself"
        },
        "answer": "C"
    },
    "Q25": {
        "question": "What's your answer?: ",
        "options": {
            "A": "No",
            "B": "Yes",
            "C": "Ew",
            "D": "I'm calling the cops"
        },
        "answer": "B"
    },
}

guesses = []
score = 0

for question_key, question_data in questions.items():
    print("----------------------")
    print(question_data["question"])
    for option, choice in question_data["options"].items():
        print(f"{option}. {choice}")

    while True:
        guess = input("Enter (A, B, C, D): ").strip().upper()
        if guess in {"A", "B", "C", "D"}:
            break
        else:
            print("Invalid input. Please enter A, B, C, or D.")

    guesses.append(guess)
    if guess == question_data["answer"]:
        score += 1
        print("\n")
        print("CORRECT!")
        print("\n")
    else:
        print("INCORRECT!")
        print(f"The correct answer is {question_data['answer']}")

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print(
    f"Answers: {' '.join([question_data['answer'] for question_data in questions.values()])}")
print(f"Guesses: {' '.join(guesses)}")

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
