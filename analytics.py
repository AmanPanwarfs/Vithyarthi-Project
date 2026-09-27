from modules.data_manager import load_tasks, load_results
from modules.performance import calculate_topic_performance


def show_dashboard():
    tasks = load_tasks()
    results = load_results()
    performance = calculate_topic_performance()

    completed = sum(1 for task in tasks if task["status"] == "Completed")
    pending = sum(1 for task in tasks if task["status"] == "Pending")

    print("\n" + "=" * 55)
    print("                 ANALYTICS DASHBOARD")
    print("=" * 55)
    print(f"Total study tasks     : {len(tasks)}")
    print(f"Completed tasks       : {completed}")
    print(f"Pending tasks         : {pending}")
    print(f"Quizzes attempted     : {len(results)}")
    print(f"Topics assessed       : {len(performance)}")

    if performance:
        average = round(sum(performance.values()) / len(performance), 2)
        print(f"Average topic accuracy: {average}%")

    print("=" * 55)
