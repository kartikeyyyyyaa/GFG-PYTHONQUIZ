# Python Quiz Application

This repository contains the backend logic for a **Python Quiz Application**, developed as part of **Task 2** for the **GeeksforGeeks Student Chapter** technical round.

The application is a CLI (Command Line Interface) tool that tests a user's knowledge of **Python Fundamentals** (Loops, Control Structures, Functions, and Recursion).

## Task Requirements Achieved
1.  **JSON Loading:** Questions are dynamically loaded from an external `questions.json` file.
2.  **Randomization:** The order of questions is shuffled every time the program runs using the `random` module.
3.  **Score Tracking:** The system tracks correct and incorrect answers in real-time.
4.  **Final Result:** Displays the total score and percentage at the end of the quiz.

## Tech Stack
* **Language:** Python 3.x
* **Data Format:** JSON
* **Key Modules:** `json`, `random`

## Project Structure
```text
├── app.py           # The main Python script containing the quiz logic
├── questions.json   # Database of questions (Loops, Functions, Recursion)
└── README.md        # Project documentation
