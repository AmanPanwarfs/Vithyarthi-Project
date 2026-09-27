from modules.data_manager import initialize_data
from modules.study_manager import study_menu
from modules.quiz_manager import quiz_menu
from modules.performance import show_performance
from modules.recommendation import show_recommendations
from modules.analytics import show_dashboard


def main():
    initialize_data()

    while True:
        print("\n" + "=" * 52)
        print("                 STUDYPILOT")
        print("       Student Study & Performance Manager")
        print("=" * 52)
        print("1. Study Manager")
        print("2. Practice Quiz")
        print("3. Performance Report")
        print("4. Personalized Recommendations")
        print("5. Analytics Dashboard")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            study_menu()
        elif choice == "2":
            quiz_menu()
        elif choice == "3":
            show_performance()
        elif choice == "4":
            show_recommendations()
        elif choice == "5":
            show_dashboard()
        elif choice == "6":
            print("\nThank you for using StudyPilot!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()

