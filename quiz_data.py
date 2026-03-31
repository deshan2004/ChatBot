def load_quiz_questions():
    questions = [
        {
            "question": "What is a variable in programming?",
            "options": [
                "A container for storing data",
                "A type of loop",
                "A mathematical operation",
                "A programming language"
            ],
            "correct": 0,
            "explanation": "Variables act as containers that store data values which can be accessed and manipulated throughout the program."
        },
        {
            "question": "Which data type would you use to store text?",
            "options": [
                "Integer",
                "Float", 
                "String",
                "Boolean"
            ],
            "correct": 2,
            "explanation": "Strings are used to store textual data like names, sentences, or any sequence of characters."
        },
        {
            "question": "What does a 'for' loop do?",
            "options": [
                "Makes decisions",
                "Stores data",
                "Repeats code a specific number of times",
                "Defines functions"
            ],
            "correct": 2,
            "explanation": "For loops are used when you know exactly how many times you want to execute a block of code."
        },
        {
            "question": "What is the purpose of functions?",
            "options": [
                "To make code longer",
                "To create reusable code blocks",
                "To only perform mathematical operations",
                "To display text on screen"
            ],
            "correct": 1,
            "explanation": "Functions help in code organization, reusability, and making programs more modular and maintainable."
        },
        {
            "question": "What is an algorithm?",
            "options": [
                "A programming language",
                "A step-by-step problem-solving procedure",
                "A type of variable",
                "A computer hardware component"
            ],
            "correct": 1,
            "explanation": "An algorithm is a well-defined computational procedure that takes input and produces output."
        },
        {
            "question": "Which sorting algorithm has O(n²) time complexity?",
            "options": [
                "Quick Sort",
                "Merge Sort",
                "Bubble Sort",
                "Binary Search"
            ],
            "correct": 2,
            "explanation": "Bubble Sort has O(n²) time complexity in worst and average cases."
        },
        {
            "question": "What is the base case in recursion?",
            "options": [
                "The first line of function",
                "The stopping condition",
                "The recursive call",
                "The function parameters"
            ],
            "correct": 1,
            "explanation": "The base case prevents infinite recursion by providing a condition to stop."
        },
        {
            "question": "Which data structure follows LIFO principle?",
            "options": [
                "Queue",
                "Stack",
                "Array",
                "Linked List"
            ],
            "correct": 1,
            "explanation": "Stack follows Last-In-First-Out (LIFO) principle."
        },
        
        
        {
            "question": "What is the main advantage of Binary Search?",
            "options": [
                "Works on unsorted arrays",
                "Very simple to implement",
                "Extremely fast for large datasets",
                "Uses minimal memory"
            ],
            "correct": 2,
            "explanation": "Binary Search has O(log n) time complexity, making it very efficient for large sorted datasets."
        }
    ]
    return questions