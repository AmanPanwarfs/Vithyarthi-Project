from collections import defaultdict
from modules.data_manager import load_results


def calculate_topic_performance():
    results = load_results()
    topic_totals = defaultdict(lambda: {"correct": 0, "total": 0})

    for result in results:
        for topic, stats in result.get("topic_stats", {}).items():
            topic_totals[topic]["correct"] += stats["correct"]
            topic_totals[topic]["total"] += stats["total"]

    performance = {}

    for topic, stats in topic_totals.items():
        if stats["total"] > 0:
            performance[topic] = round(
                (stats["correct"] / stats["total"]) * 100, 2
            )

    return performance


def show_performance():
    performance = calculate_topic_performance()

    print("\n" + "=" * 45)
    print("           PERFORMANCE REPORT")
    print("=" * 45)

    if not performance:
        print("No quiz data available yet.")
        print("Take a quiz first to generate your report.")
        return

    for topic, score in sorted(performance.items(), key=lambda item: item[1]):
        print(f"{topic:<25} {score:>6.2f}%")

    values = list(performance.values())
    overall = round(sum(values) / len(values), 2)

    strongest = max(performance, key=performance.get)
    weakest = min(performance, key=performance.get)

    print("-" * 45)
    print(f"Overall topic average : {overall}%")
    print(f"Strongest topic       : {strongest}")
    print(f"Weakest topic         : {weakest}")
    print("=" * 45)
