# Architecture

StudyPilot follows a simple modular architecture:

User
  |
  v
main.py
  |
  +--> Study Manager --------+
  |                          |
  +--> Quiz Manager ---------+--> Data Manager --> JSON files
  |                          |
  +--> Performance ----------+
  |
  +--> Recommendation
  |
  +--> Analytics Dashboard

The design separates user interaction, business logic and persistent storage.
