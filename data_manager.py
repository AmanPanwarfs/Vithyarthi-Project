import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
TASKS_FILE = DATA_DIR / "tasks.json"
RESULTS_FILE = DATA_DIR / "results.json"
QUESTIONS_FILE = DATA_DIR / "questions.json"


def _write_json(path, data):
    path.write_text(json.dumps(data, indent=4), encoding="utf-8")


def _read_json(path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        _write_json(path, default)
        return default


def initialize_data():
    DATA_DIR.mkdir(exist_ok=True)

    if not TASKS_FILE.exists():
        _write_json(TASKS_FILE, [])

    if not RESULTS_FILE.exists():
        _write_json(RESULTS_FILE, [])

    if not QUESTIONS_FILE.exists():
        _write_json(QUESTIONS_FILE, default_questions())


def load_tasks():
    return _read_json(TASKS_FILE, [])


def save_tasks(tasks):
    _write_json(TASKS_FILE, tasks)


def load_results():
    return _read_json(RESULTS_FILE, [])


def save_results(results):
    _write_json(RESULTS_FILE, results)


def load_questions():
    return _read_json(QUESTIONS_FILE, default_questions())


def default_questions():
    return [
        {
            "id": 1,
            "topic": "Python Basics",
            "question": "Which symbol is used to start a comment in Python?",
            "options": ["//", "#", "/*", "--"],
            "answer": 2
        },
        {
            "id": 2,
            "topic": "Python Basics",
            "question": "Which of these is an immutable Python data type?",
            "options": ["List", "Dictionary", "Tuple", "Set"],
            "answer": 3
        },
        {
            "id": 3,
            "topic": "Control Flow",
            "question": "Which keyword immediately exits a loop?",
            "options": ["continue", "pass", "break", "exitloop"],
            "answer": 3
        },
        {
            "id": 4,
            "topic": "Control Flow",
            "question": "Which loop is commonly used when the number of iterations is known?",
            "options": ["for", "while", "if", "try"],
            "answer": 1
        },
        {
            "id": 5,
            "topic": "Lists",
            "question": "Which list method adds one item to the end of a list?",
            "options": ["add()", "append()", "push()", "insert_end()"],
            "answer": 2
        },
        {
            "id": 6,
            "topic": "Dictionaries",
            "question": "A Python dictionary stores data mainly as:",
            "options": ["Indexes only", "Key-value pairs", "Ordered pairs only", "Characters"],
            "answer": 2
        },
        {
            "id": 7,
            "topic": "Sets",
            "question": "What is a key property of a Python set?",
            "options": ["It stores duplicate values", "It stores only strings", "It stores unique elements", "It is immutable"],
            "answer": 3
        },
        {
            "id": 8,
            "topic": "Algorithms",
            "question": "Which algorithm finds the greatest common divisor of two numbers?",
            "options": ["Euclidean algorithm", "Binary search", "Bubble sort", "Fibonacci algorithm"],
            "answer": 1
        },
        {
            "id": 9,
            "topic": "Algorithms",
            "question": "What is the next number in the Fibonacci sequence 1, 1, 2, 3, 5, ?",
            "options": ["6", "7", "8", "9"],
            "answer": 3
        },
        {
            "id": 10,
            "topic": "Functions",
            "question": "Which keyword is used to define a function in Python?",
            "options": ["function", "define", "def", "fun"],
            "answer": 3
        }
    ]
