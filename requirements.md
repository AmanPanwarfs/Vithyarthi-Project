# Requirements

## Functional Requirements

### FR1 — Study Task Management
The system shall allow a user to add, view, complete and delete study tasks.

### FR2 — Quiz Practice
The system shall present questions with multiple-choice answers and calculate the user's score.

### FR3 — Performance Analysis
The system shall calculate topic-wise accuracy from saved quiz results.

### FR4 — Recommendations
The system shall identify topics below defined accuracy thresholds and recommend additional practice.

### FR5 — Analytics Dashboard
The system shall summarize tasks, quiz attempts and topic performance.

## Non-Functional Requirements

### NFR1 — Usability
The interface should use clear menus and readable console output.

### NFR2 — Reliability
Invalid numeric input should not terminate the application.

### NFR3 — Maintainability
Features should be separated into meaningful Python modules.

### NFR4 — Resource Efficiency
The application should use only local JSON files and Python standard-library modules.

### NFR5 — Data Persistence
Tasks and quiz results should remain available after restarting the application.

## Input / Output

Input:
- Menu selections
- Subject/topic/task information
- Quiz answers

Output:
- Task lists
- Quiz scores
- Topic accuracy
- Recommendations
- Dashboard summaries
