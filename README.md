# CodeAlpha Task-2

## Table of Contents
1. [Project Overview](#project-overview)
2. [Task 1: Hangman Game](#task-1-hangman-game)
   - [Description](#description)
   - [Usage](#usage)
3. [Task 2: Student Grade Tracker](#task-2-student-grade-tracker)
   - [Description](#description-1)
   - [Usage](#usage-1)

---

## Project Overview
This repository contains two Python projects that help demonstrate Python programming skills through practical applications:

1. **Hangman Game** - A text-based implementation of the classic Hangman game where players must guess letters to reveal a word.
2. **Student Grade Tracker** - A program to manage student grades, track performance, generate reports, and visualize data.

---

## Task 1: Hangman Game

### Description
The **Hangman Game** is a text-based word guessing game in which the player has to guess the letters of a secret word chosen randomly from a predefined list. The player has a limited number of attempts (represented as a "hangman" figure being drawn progressively) to guess the correct word. If the player guesses a letter that exists in the word, that letter is revealed. If the letter is not in the word, an incorrect guess counts as one attempt. The game continues until the player either guesses the word correctly or runs out of attempts.

**Features:**
- A random word is selected from a list of words.
- Players can guess one letter at a time.
- The hangman figure is drawn with each incorrect guess.
- The player wins if they guess the word before running out of attempts.

### Usage
1. To start the Hangman game, follow these steps:
   - Open a terminal or command prompt.
   - Navigate to the directory where you cloned the repository.
   - Run the following command:
     ```bash
     python hangman_game.py
     ```
   
2. The game will prompt you to guess letters. Enter a letter and press Enter. If the letter is correct, it will reveal the letter in the word. If incorrect, your attempts decrease.

3. The game ends when:
   - You guess all letters correctly, winning the game.
   - You run out of attempts, losing the game.

4. You can restart the game or quit based on your preference.

---

## Task 2: Student Grade Tracker

### Description
The **Student Grade Tracker** is a program that allows users (teachers, administrators, or students) to manage and track student grades across various subjects. The program supports functionalities such as adding new students, adding grades for each subject, viewing individual student reports, viewing all students' grades, and exporting the data to a CSV file. Additionally, the program allows for visualizing the average grades of students in a bar chart.

**Features:**
- **Add Student**: Register new students with their unique roll number and name.
- **Add Grades**: Input grades for different subjects for each student.
- **View Report**: View detailed grades and average for a specific student.
- **View All Students**: Display a list of all students along with their grades and average score.
- **Export Data**: Save all student data into a CSV file for external use or record keeping.
- **Visualize Grades**: Generate a bar chart to visualize the average grades of all students.

### Usage
1. To start the Student Grade Tracker, follow these steps:
   - Open a terminal or command prompt.
   - Navigate to the directory where you cloned the repository.
   - Run the following command:
     ```bash
     python student_grade_tracker.py
     ```

2. The program will display a menu with the following options:
   - **1. Add Student**: Add a new student by providing their roll number and name.
   - **2. Add Grades**: Input grades for various subjects for a specific student.
   - **3. View Report**: View grades and the average grade for a specific student.
   - **4. View All Students**: View a summary of all students, including their grades and average score.
   - **5. Export Data**: Export all the student data to a CSV file.
   - **6. Visualize Grades**: Generate and display a bar chart showing the average grade of each student.
   - **7. Exit**: Exit the program.

3. To interact with the program, choose an option by entering the corresponding number. The program will guide you through each process step by step.

4. The data is stored in a CSV file, `student_grades.csv`, so even if the program is closed, the data is saved and can be loaded the next time you start the program.

---

## Conclusion
These tasks demonstrate practical Python skills:
1. **Hangman Game** - Focuses on game development, user input handling, and game logic.
2. **Student Grade Tracker** - Focuses on data management, file handling, and data visualization.
