import random
from datetime import datetime
from modules.data_manager import load_questions, load_results, save_results


def run_quiz():
    questions = load_questions()

    try:
        count = int(input(f"Number of questions (1-{len(questions)}): "))
    except ValueError:
        print("Please enter a valid number.")
        return

    count = max(1, min(count, len(questions)))
    selected = random.sample(questions, count)

    score = 0
    topic_stats = {}

    print("\n--- QUIZ STARTED ---")

    for number, question in enumerate(selected, start=1):
        print(f"\nQ{number}. {question['question']}")

        for index, option in enumerate(question["options"], start=1):
            print(f"  {index}. {option}")

        try:
            answer = int(input("Your answer: "))
        except ValueError:
            answer = 0

        topic = question["topic"]
        topic_stats.setdefault(topic, {"correct": 0, "total": 0})
        topic_stats[topic]["total"] += 1

        if answer == question["answer"]:
            print("Correct!")
            score += 1
            topic_stats[topic]["correct"] += 1
        else:
            correct_text = question["options"][question["answer"] - 1]
            print(f"Incorrect. Correct answer: {correct_text}")

    percentage = round((score / count) * 100, 2)

    result = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "score": score,
        "total": count,
        "percentage": percentage,
        "topic_stats": topic_stats
    }

    results = load_results()
    results.append(result)
    save_results(results)

    print("\n--- QUIZ RESULT ---")
    print(f"Score    : {score}/{count}")
    print(f"Accuracy : {percentage}%")
    print("Result saved successfully.")


def quiz_menu():
    while True:
        print("\n--- PRACTICE QUIZ ---")
        print("1. Start quiz")
        print("2. Back")

        choice = input("Choice: ").strip()

        if choice == "1":
            run_quiz()
        elif choice == "2":
            break
        else:
            print("Invalid choice.")
