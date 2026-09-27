from modules.performance import calculate_topic_performance


def get_recommendations():
    performance = calculate_topic_performance()
    recommendations = []

    for topic, score in performance.items():
        if score < 60:
            recommendations.append(
                (topic, score, "High priority: accuracy is below 60%.")
            )
        elif score < 75:
            recommendations.append(
                (topic, score, "Medium priority: more practice is recommended.")
            )

    recommendations.sort(key=lambda item: item[1])
    return recommendations


def show_recommendations():
    recommendations = get_recommendations()

    print("\n" + "=" * 55)
    print("        PERSONALIZED STUDY RECOMMENDATIONS")
    print("=" * 55)

    if not recommendations:
        print("No weak topics detected yet.")
        print("Keep practicing to generate more performance data.")
        return

    for number, (topic, score, reason) in enumerate(recommendations, start=1):
        print(f"\nPriority {number}")
        print(f"Topic   : {topic}")
        print(f"Accuracy: {score}%")
        print(f"Reason  : {reason}")

    print("\nSuggested strategy:")
    print("1. Review the topic.")
    print("2. Practice 5-10 questions.")
    print("3. Retake the quiz and compare your accuracy.")
