# problems = [
#     ["Problem 1", "Sum of Multiples",
#         "Write a program that takes a positive integer N and computes the sum of all multiples of 3 or 5 that are less than N. For example, for N = 10, the sum is 23 (3 + 5 + 6 + 9).", 10, 2],
#     ["Problem 2", "Fibonacci Sequence", "Write a program that prints the Fibonacci sequence up to a given number N. The Fibonacci sequence is defined as follows: the first two numbers are 0 and 1, and each subsequent number is the sum of the previous two numbers. For example, for N = 8, the sequence is 0, 1, 1, 2, 3, 5, 8.", 8, 1],
#     ["Problem 3", "Reverse String", "Write a program that takes a string as input and prints its reverse. For example, for the input 'Hello', the program should output 'olleH'.", 'Hello', 'olleH', 1],
#     ["Problem 4", "Even or Odd", "Write a program that takes an integer as input and determines whether it is even or odd. For example, for the input 6, the program should output 'Even'.", 6, 'Even', 1],
#     ["Problem 5", "Factorial", "Write a program that calculates the factorial of a given positive integer N. The factorial of N is the product of all positive integers less than or equal to N. For example, for N = 5, the factorial is 5 * 4 * 3 * 2 * 1 = 120.", 5, 120, 2],
#     ["Problem 6", "Prime Numbers", "Write a program that prints all prime numbers less than a given positive integer N. For example, for N = 20, the program should output '2, 3, 5, 7, 11, 13, 17, 19'.", 20, '2, 3, 5, 7, 11, 13, 17, 19', 2],
#     ["Problem 7", "Palindrome", "Write a program that takes a string as input and determines whether it is a palindrome or not. A palindrome is a word, phrase, number, or other sequence of characters that reads the same backward as forward. For example, for the input 'racecar', the program should output 'True'.", 'racecar', True, 2],
#     ["Problem 8", "Anagram Checker", "Write a program that takes two strings as input and determines whether they are anagrams or not. An anagram is a word or phrase formed by rearranging the letters of another word or phrase. For example, for the inputs 'listen' and 'silent', the program should output 'True'.", 'listen', 'silent', True, 3],
#     ["Problem 9", "Unique Elements", "Write a program that takes a list of integers as input and removes any duplicate elements, returning a new list with only unique elements. For example, for the input [1, 2, 2, 3, 4, 4, 5], the program should output [1, 2, 3, 4, 5].", [1, 2, 2, 3, 4, 4, 5], [1, 2, 3, 4, 5], 2],
#     ["Problem 10", "Word Count", "Write a program that takes a string as input and counts the number of occurrences of each word in the string. The program should output a dictionary where the keys are the words and the values are the corresponding counts. For example, for the input 'hello world hello', the program should output {'hello': 2, 'world': 1}.", 'hello world hello', {
#         'hello': 2, 'world': 1}, 2],
#     ["Problem 11", "Armstrong Number", "Write a program that takes a positive integer as input and determines whether it is an Armstrong number or not. An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits. For example, for the input 153, the program should output 'True' since 1^3 + 5^3 + 3^3 = 153.", 153, True, 1],
#     ["Problem 12", "Leap Year", "Write a program that takes a year as input and determines whether it is a leap year or not. A leap year is a year that is divisible by 4 but not divisible by 100, unless it is also divisible by 400. For example, for the input 2020, the program should output 'True' since 2020 is a leap year.", 2020, True, 1],
#     ["Problem 13", "String Compression", "Write a program that takes a string as input and compresses it by replacing consecutive repeated characters with a single instance of the character followed by the number of repetitions. For example, for the input 'aabbbcccc', the program should output 'a2b3c4'.", 'aabbbcccc', 'a2b3c4', 1],
#     ["Problem 14", "Matrix Transpose", "Write a program that takes a matrix (2D list) as input and returns its transpose. The transpose of a matrix flips the matrix over its main diagonal, switching the row and column indices. For example, for the input [[1, 2, 3], [4, 5, 6]], the program should output [[1, 4], [2, 5], [3, 6]].", [
#         [1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]], 2],
#     ["Problem 15", "Caesar Cipher", "Write a program that takes a string and a shift value as input and applies a Caesar cipher to the string. The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down the alphabet. For example, for the input 'hello' with a shift value of 3, the program should output 'khoor'.", 'hello', 3, 'khoor', 2],
#     ["Problem 16", "Matrix Multiplication", "Write a program that takes two matrices (2D lists) as input and computes their matrix product. The matrix product of two matrices A and B is a matrix C such that C[i][j] is the dot product of the ith row of A and the jth column of B. For example, for the inputs A = [[1, 2], [3, 4]] and B = [[5, 6], [7, 8]], the program should output [[19, 22], [43, 50]].", [
#         [1, 2], [3, 4]], [[5, 6], [7, 8]], [[19, 22], [43, 50]], 2],
#     ["Problem 17", "Fibonacci Sequence",
#         "Write a program that takes a positive integer n as input and returns the nth Fibonacci number. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. For example, for n = 6, the program should output 8 since the 6th Fibonacci number is 8 (0, 1, 1, 2, 3, 5, 8).", 6, 8, 1],
#     ["Problem 18", "Reverse Words", "Write a program that takes a sentence as input and reverses the order of the words. The program should not reverse the individual characters within each word. For example, for the input 'Hello world', the program should output 'world Hello'.", 'Hello world', 'world Hello', 1],
#     ["Problem 19", "Anagrams", "Write a program that takes two strings as input and determines whether they are anagrams or not. Anagrams are two strings that have the same characters but in a different order. For example, for the inputs 'listen' and 'silent', the program should output 'True'.", 'listen', 'silent', True, 1],
#     ["Problem 20", "Matrix Spiral Print", "Write a program that takes a matrix (2D list) as input and prints its elements in spiral order, starting from the top-left corner and moving in a clockwise direction. For example, for the input [[1, 2, 3], [4, 5, 6], [7, 8, 9]], the program should output '1 2 3 6 9 8 7 4 5'.", [
#         [1, 2, 3], [4, 5, 6], [7, 8, 9]], '1 2 3 6 9 8 7 4 5', 2]

#     ["Problem 21", "Palindrome Number", "Write a program that takes a positive integer as input and determines whether it is a palindrome number or not. A palindrome number is a number that remains the same when its digits are reversed. For example, for the input 121, the program should output 'True' since 121 is a palindrome number.", 121, True, 1],
#     ["Problem 22", "Binary Search", "Write a program that implements the binary search algorithm to find the index of a given target value in a sorted list of numbers. If the target value is found, the program should return its index; otherwise, it should return -1. For example, for the input list [2, 5, 7, 10, 15] and target value 7, the program should output 2.", [2, 5, 7, 10, 15], 7, 2, 1],
#     ["Problem 23", "Greatest Common Divisor",
#      "Write a program that takes two positive integers as input and computes their greatest common divisor (GCD). The GCD is the largest positive integer that divides both numbers without leaving a remainder. For example, for the input numbers 12 and 18, the program should output 6.", 12, 18, 6, 1],
#     ["Problem 24", "Pascal's Triangle", "Write a program that takes an integer n as input and prints the first n rows of Pascal's triangle. Pascal's triangle is a triangular array of binomial coefficients, where each number is the sum of the two numbers directly above it. For example, for n = 5, the program should output the following:\n1\n1 1\n1 2 1\n1 3 3 1\n1 4 6 4 1", 5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], 2],
#     ["Problem 25", "Longest Common Prefix", "Write a program that takes a list of strings as input and returns the longest common prefix among those strings. The longest common prefix is the longest string that is common to all strings in the list. For example, for the input ['flower', 'flow', 'flight'], the program should output 'fl'.", ['flower', 'flow', 'flight'], 'fl', 1],
#     ["Problem 26", "Valid Parentheses",
#      "Write a program that takes a string containing only parentheses (e.g., '()[]{}') as input and determines whether the parentheses are valid or not. Valid parentheses must be opened and closed in the correct order. For example, for the input '()[]{()}', the program should output 'True'.", "()[]{()}", True, 1],
#     ["Problem 27", "Sieve of Eratosthenes", "Write a program that takes a positive integer n as input and returns a list of all prime numbers less than or equal to n using the Sieve of Eratosthenes algorithm. The Sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to a given limit.", 10, [2, 3, 5, 7], 2],
#     ["Problem 28", "Reverse Linked List", "Write a program that takes a linked list as input and reverses the order of its nodes. The program should return the new head of the reversed linked list. Each linked list node has a value and a pointer to the next node. For example, for the input 1 -> 2 -> 3 -> 4 -> 5, the program should output 5 -> 4 -> 3 -> 2 -> 1.", linked_list, reversed_linked_list, 3]
# ]


import sqlite3
problems = [
    ["Problem 1", "Sum of Multiples",
        "Write a program that takes a positive integer N and computes the sum of all multiples of 3 or 5 that are less than N. For example, for N = 10, the sum is 23 (3 + 5 + 6 + 9).", 10, 2, 23, 68],
    ["Problem 2", "Fibonacci Sequence", "Write a program that prints the Fibonacci sequence up to a given number N. The Fibonacci sequence is defined as follows: the first two numbers are 0 and 1, and each subsequent number is the sum of the previous two numbers. For example, for N = 8, the sequence is 0, 1, 1, 2, 3, 5, 8.", 8, 1, [0, 1, 1, 2, 3, 5, 8], 21],
    ["Problem 3", "Reverse String", "Write a program that takes a string as input and prints its reverse. For example, for the input 'Hello', the program should output 'olleH'.", 'Hello', 'olleH', 'olleH', 'world'],
    ["Problem 4", "Even or Odd", "Write a program that takes an integer as input and determines whether it is even or odd. For example, for the input 6, the program should output 'Even'.", 6, 'Even', 3, 'Odd'],
    ["Problem 5", "Factorial", "Write a program that calculates the factorial of a given positive integer N. The factorial of N is the product of all positive integers less than or equal to N. For example, for N = 5, the factorial is 5 * 4 * 3 * 2 * 1 = 120.", 5, 120, 10, 3628800],
    ["Problem 6", "Prime Numbers", "Write a program that prints all prime numbers less than a given positive integer N. For example, for N = 20, the program should output '2, 3, 5, 7, 11, 13, 17, 19'.",
        20, '2, 3, 5, 7, 11, 13, 17, 19', 10, '2, 3, 5, 7'],
    ["Problem 7", "Palindrome", "Write a program that takes a string as input and determines whether it is a palindrome or not. A palindrome is a word, phrase, number, or other sequence of characters that reads the same backward as forward. For example, for the input 'racecar', the program should output 'True'.", 'racecar', True, 'hello', False],
    ["Problem 8", "Anagram Checker", "Write a program that takes two strings as input and determines whether they are anagrams or not. An anagram is a word or phrase formed by rearranging the letters of another word or phrase. For example, for the inputs 'listen' and 'silent', the program should output 'True'.", 'listen', 'silent', True, 'hello', False],
    # ["Problem 9", "Unique Elements", "Write a program that takes a list of integers as input and removes any duplicate elements, returning a new list with only unique elements. For example, for the input[1, 2, 2, 3, 4, 4, 5], , 103 messages hidden[1, 2, 2, 3, 4, 4, 5], [1, 2, 3, 4, 5], [5, 5, 5, 5, 5], [5], [], [], [], []],
    ["Problem 10", "Binary to Decimal", "Write a program that takes a binary number as input and converts it to its decimal equivalent. The binary number is represented as a string of 0s and 1s. For example, for the input '1010', the program should output 10.", '1010', 10, '1111', 15],
    ["Problem 11", "Common Elements", "Write a program that takes two lists of integers as input and returns a new list containing the common elements between the two lists. For example, for the inputs [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8], the program should output [4, 5].", [
        1, 2, 3, 4, 5], [4, 5, 6, 7, 8], [4, 5], [1, 2, 3], []],
    ["Problem 12", "Pascal's Triangle", "Write a program that prints the first N rows of Pascal's Triangle. Pascal's Triangle is a triangular array of numbers in which each number is the sum of the two numbers directly above it. For example, for N = 5, the program should output:\n1\n1 1\n1 2 1\n1 3 3 1\n1 4 6 4 1",
        5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], 3, [[1], [1, 1], [1, 2, 1]]],
    ["Problem 13", "Greatest Common Divisor",
        "Write a program that takes two positive integers as input and calculates their greatest common divisor (GCD). The GCD is the largest positive integer that divides both numbers without leaving a remainder. For example, for the inputs 12 and 18, the program should output 6.", 12, 18, 6, 25, 5],
    ["Problem 14", "Armstrong Number", "Write a program that takes a positive integer as input and determines whether it is an Armstrong number or not. An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits. For example, for the input 153, the program should output 'True' because 1^3 + 5^3 + 3^3 = 153.", 153, True, 370, True, 123, False],
    ["Problem 15", "Largest Element", "Write a program that takes a list of integers as input and returns the largest element in the list. For example, for the input [5, 9, 2, 1, 7], the program should output 9.", [5, 9, 2, 1, 7], 9, [3, 1, 8, 4, 5], 8],
    ["Problem 16", "Palindrome Check", "Write a program that takes a string as input and determines whether it is a palindrome or not. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward. For example, for the input 'racecar', the program should output 'True'.", "racecar", True, "hello", False],
    ["Problem 17", "FizzBuzz", "Write a program that prints the numbers from 1 to N. But for multiples of three, print 'Fizz' instead of the number, and for the multiples of five, print 'Buzz'. For numbers that are multiples of both three and five, print 'FizzBuzz'.",
        15, "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz"],
    ["Problem 18", "Reverse String", "Write a program that takes a string as input and returns the string in reversed order. For example, for the input 'Hello, World!', the program should output '!dlroW ,olleH'.",
        "Hello, World!", "!dlroW ,olleH", "Python", "nohtyP"],
    ["Problem 19", "Factorial", "Write a program that takes a positive integer as input and calculates its factorial. The factorial of a number is the product of all positive integers less than or equal to the number. For example, for the input 5, the program should output 120.", 5, 120, 0, 1],
    ["Problem 20", "Anagram Check", "Write a program that takes two strings as input and determines whether they are anagrams or not. Anagrams are words or phrases formed by rearranging the letters of another word or phrase. For example, for the inputs 'listen' and 'silent', the program should output 'True'.", "listen", "silent", True, "hello", "world", False],
    ["Problem 21", "Count Characters", "Write a program that takes a string as input and counts the number of occurrences of each character in the string. The program should then print the characters along with their respective counts in alphabetical order. For example, for the input 'hello', the program should output:\ne: 1\nh: 1\nl: 2\no: 1",
        "hello", "e: 1\nh: 1\nl: 2\no: 1", "python", "p: 1\nh: 1\nn: 1\no: 1\nt: 1\ny: 1"],
    ["Problem 22", "Find Missing Number", "Write a program that takes a list of integers from 1 to N with one number missing, and returns the missing number. For example, for the input [1, 2, 4, 5], the program should output 3.", [
        1, 2, 4, 5], 3, [10, 8, 7, 6, 5, 4, 2, 1], 3],
    ["Problem 23", "Fibonacci Sequence", "Write a program that takes a positive integer N as input and prints the first N numbers in the Fibonacci sequence. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. For example, for N = 6, the program should output:\n0\n1\n1\n2\n3\n5", 6, "0\n1\n1\n2\n3\n5", 10, "0\n1\n1\n2\n3\n5\n8\n13\n21\n34"],
    ["Problem 24", "Unique Elements", "Write a program that takes a list of integers as input and returns a new list containing only the unique elements from the original list. The order of the elements in the new list should be the same as the original list. For example, for the input [1, 2, 2, 3, 4, 4, 5], the program should output [1, 2, 3, 4, 5].", [1, 2, 2, 3, 4, 4, 5], [1, 2, 3, 4, 5], [5, 5, 5, 5, 5], [5], [], []],
    ["Problem 25", "Binary to Decimal", "Write a program that takes a binary number as input and converts it to its decimal equivalent. The binary number is represented as a string of 0s and 1s. For example, for the input '1010', the program should output 10.", "1010", 10, "1111", 15],
    ["Problem 26", "Common Elements", "Write a program that takes two lists of integers as input and returns a new list containing the common elements between the two lists. For example, for the inputs [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8], the program should output [4, 5].", [
        1, 2, 3, 4, 5], [4, 5, 6, 7, 8], [4, 5], [1, 2, 3], []],
    ["Problem 27", "Pascal's Triangle", "Write a program that prints the first N rows of Pascal's Triangle. Pascal's Triangle is a triangular array of numbers in which each number is the sum of the two numbers directly above it. For example, for N = 5, the program should output:\n1\n1 1\n1 2 1\n1 3 3 1\n1 4 6 4 1",
        5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], 3, [[1], [1, 1], [1, 2, 1]]],
    ["Problem 28", "Greatest Common Divisor",
        "Write a program that takes two positive integers as input and calculates their greatest common divisor (GCD). The GCD is the largest positive integer that divides both numbers without leaving a remainder. For example, for the inputs 12 and 18, the program should output 6.", 12, 18, 6, 25, 5],
    ["Problem 29", "Longest Increasing Subsequence", "Write a program that takes a list of integers as input and finds the length of the longest increasing subsequence within the list. A subsequence is a sequence of numbers that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. An increasing subsequence is a subsequence in which the numbers are in strictly increasing order. For example, for the input [10, 22, 9, 33, 21, 50, 41, 60, 80], the program should output 6 because the longest increasing subsequence is [10, 22, 33, 50, 60, 80].", [10, 22, 9, 33, 21, 50, 41, 60, 80], 6, [3, 10, 2, 1, 20], 2]

]

conn = sqlite3.connect('racing.db')
cursor = conn.cursor()

for problem in problems:
    question_title = problem[1]
    question_description = problem[2]

    cursor.execute('''
    INSERT INTO tblQuestion (questionTitle, questionDescription)
    VALUES (?, ?);
    ''', (question_title, question_description))

    question_id = cursor.lastrowid

    # Insert test inputs into tblTestInput
    test_input = str(problem[3])
    test_output = str(problem[4])

    cursor.execute('''
    INSERT INTO tblTestInput (input, output, questionID)
    VALUES (?, ?, ?);
    ''', (test_input, test_output, question_id))

    # Commit the changes and close the connection
conn.commit()
conn.close()
