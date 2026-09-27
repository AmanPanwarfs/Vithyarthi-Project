# StudyPilot
### Student Study & Performance Manager

StudyPilot is a modular Python application designed to help students organize study tasks, practice CSE1021-style programming questions, track quiz performance, and receive rule-based study recommendations.

## Course Alignment

The project is designed around concepts in CSE1021:
- Problem solving and algorithms
- Python variables, expressions and functions
- Conditional statements and loops
- Counting and summation
- Lists, tuples, sets and dictionaries
- Array/list processing
- Input/output and validation

## Major Functional Modules

1. Study Manager
2. Practice Quiz
3. Performance Analyzer
4. Recommendation Engine
5. Analytics Dashboard

## Project Structure

```text
StudyPilot/
├── main.py
├── modules/
│   ├── data_manager.py
│   ├── study_manager.py
│   ├── quiz_manager.py
│   ├── performance.py
│   ├── recommendation.py
│   ├── analytics.py
│   └── __init__.py
├── data/
│   ├── tasks.json
│   ├── results.json
│   └── questions.json
├── tests/
│   └── test_project.py
├── docs/
├── README.md
└── statement.md
```

## Requirements

- Python 3.9 or later
- No external Python packages are required.

## How to Run

Open a terminal in the StudyPilot folder and run:

```bash
python main.py
```

## Testing

Run:

```bash
python -m unittest discover -s tests -v
```

## Data Storage

StudyPilot uses JSON files so that the project remains simple, transparent and based on Python concepts taught in the course.

## Future Enhancements

- Graphical user interface
- More question banks
- Subject-wise progress charts
- Difficulty levels
- Daily study planner
- Exportable performance reports
