# Number Ninja

This Python script generates a list of numbers within a specified range, with options to exclude multiples of a number, include only multiples of a number, exclude prime numbers, or include only prime numbers. It then displays the list, the count of numbers, or both, and optionally calculates the sum of the numbers.

## Short Description

A versatile number generator and manipulator that allows users to define a range, filter by multiples and primality, and display results in various ways.

## Features

*   **Range Input:** Takes starting and ending numbers as input, ensuring the ending number is greater than the starting number.  Handles non-numeric input.
*   **Multiple Exclusion/Inclusion:** Allows the user to exclude or include multiples of a specific number.
*   **Prime Number Handling:** Provides options to exclude or include only prime numbers within the range.
*   **Display Options:**  Lets the user choose to display the list of numbers, the count of numbers, or both.
*   **Sum Calculation:** Offers an option to calculate and display the sum of the numbers in the generated list.
*   **Input Validation:** Robust input validation to ensure correct data types and prevent errors.
*   **User-Friendly Interface:** Clear prompts and messages to guide the user.
*   **Restart/Exit:** Options to restart the process or exit the program.

## Requirements

*   Python 3.x

## How to Use

1.  Save the Python code as a `.py` file (e.g., `number_machine.py`).
2.  Open a terminal or command prompt and navigate to the directory where you saved the file.
3.  Run the script using the command: `python number_machine.py`
4.  Follow the prompts to enter the starting and ending numbers, choose filtering options, and select the display format.

## Example

```bash
$ python number_machine.py

============================================
============*-Number Machine-*==============
============================================

👍 This Machine uses only WHOLE numbers 👍

Starting number: 10
Last number: 50
Do you want exclude multiples of a certain number?
Yes/No: yes
Which number do you want to remove the multiples of: 5
Do you want exclude prime numbers?
Yes/No: yes

Type "LIST" to see just the list of numbers.
Type "LENGTH" to see just how many numbers match your criteria in the given range.
Type "BOTH" to see both the lict of numbers and how many numbers there are.
==================list
11
13
17
19
23
29
31
37
41
43
47
Would you also like the to have the sum of all the numbers in your list?
Yes/No: yes
Total sum of numbers between 10 to 50 inclusive that meets your criterion is 368
Thank you
