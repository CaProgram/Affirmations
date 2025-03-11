# Affirmation Generator

## Description
This Python script is an interactive affirmation generator that provides personalized affirmations based on the user's name and the day of the week. The program prompts the user for their name and checks if the name is "David" or "Mark". Based on the input, it then asks for the current day of the week and provides a positive affirmation tailored to the day.

## Purpose
The purpose of this script is to motivate and inspire users by providing uplifting and personalized affirmations. It aims to boost the user's mood depending on their name and the day of the week.

## Features
- **Personalization**: The script offers personalized affirmations for users named "David" or "Mark".
- **Day-Based Affirmations**: The program provides a different affirmation depending on the day of the week.
- **Fallback Affirmation**: If the user's name is not recognized (other than "David" or "Mark"), a general, uplifting message is displayed.

## How It Works
1. The program greets the user and asks for their name.
2. It checks if the name is "David" or "Mark" and proceeds to ask for the day of the week.
3. Based on the user's input for the day of the week, the program will display a tailored affirmation.
4. If the user provides a name other than "David" or "Mark", a default affirmation is shown.

### Example Usage:
```bash
Hello. Welcome to your affirmation generator.
What is your name? David
What day of the week is it? Monday
It is going to be a great Monday! David

Sample Output for David:
•	Monday: "It is going to be a great Monday! David"
•	Tuesday: "It is going to be an awesome Tuesday! David"
•	Wednesday: "It is going to be a fabulous Wednesday! David"
•	Thursday: "It is going to be a terrific Thursday! David"
•	Friday: "David, It is the best day of the week, Friday!"
Sample Output for Mark:
•	Monday: "It is going to be a great Monday! Mark"
•	Tuesday: "It is going to be a terrific Tuesday! Mark"
•	Wednesday: "It is going to be a fabulous Wednesday! Mark"
•	Thursday: "It is going to be an awesome Thursday! Mark"
•	Friday: "Mark, It is the best day of the week, Friday!"
Sample Output for an Unknown Name:

I don't know your name, but I hope you are having a wonderful day!
