
def get_concept_by_level(level):
    """
    Returns all concepts that match a specific difficulty level.
    Example: 'beginner', 'intermediate', 'advanced'
    """
    knowledge = load_knowledge_base()
    results = {}

    for topic, info in knowledge.items():
        if isinstance(info, dict):
            if info.get("level", "").lower() == level.lower():
                results[topic] = info
    return results


def get_concept_by_category(category):
    """
    Returns all concepts that belong to a specific category.
    """
    knowledge = load_knowledge_base()
    results = {}

    for topic, info in knowledge.items():
        if isinstance(info, dict):
            if info.get("category", "").lower() == category.lower():
                results[topic] = info
    return results

def load_knowledge_base():
    """
    Load the complete knowledge base of programming concepts
    
    Returns:
        dict: A dictionary containing all programming concepts with detailed information
    """
    concepts = {
        "variables": {
            "level": "beginner",
            "category": "fundamentals",
            "definition": "Variables are named containers for storing data values in programming.",
            "explanation": "Think of variables as labeled boxes where you store information. They make your code readable and flexible by letting you use meaningful names for data that can change as your program runs.",
            "quick_tip": "Use descriptive names like 'user_age' instead of 'x' for better code readability!",
            "example": {
                "basic": "# Creating variables\nname = \"Alice\"\nage = 25\nis_student = True\nprice = 19.99",
                "advanced": "# Variable operations and reassignment\nscore = 0\nscore += 10        # Add 10 to score\nscore *= 2          # Double the score\nmessage = f\"Hello {name}, your score is {score}\"\nprint(message)"
            },
            "common_mistakes": [
                "Forgetting to assign a value before using",
                "Using reserved keywords as variable names",
                "Inconsistent naming (camelCase vs snake_case)"
            ],
            "practice_exercise": "Create variables to store your name, age, and favorite color, then print them in a sentence.",
            "icon": "📦",
            "analogy": "Like labeled storage boxes - each has a name and contains items that can be replaced or updated."
        },
        
        "data types": {
            "level": "beginner", 
            "category": "fundamentals",
            "definition": "Data types define what kind of data a variable can hold and what operations you can perform on it.",
            "explanation": "Just like you use different containers for different items (jars for liquids, boxes for solids), programming uses different data types for different kinds of information.",
            "quick_tip": "Use type() function to check any variable's data type!",
            "example": {
                "basic": "# Common data types\n# String - for text\nname = \"John\"\n\n# Integer - whole numbers  \nage = 30\n\n# Float - decimal numbers\nheight = 5.9\n\n# Boolean - True/False\nis_online = True",
                "advanced": "# Type conversion and operations\nnumber_str = \"123\"\nnumber_int = int(number_str)  # Convert to integer\nresult = number_int + 7       # Now we can do math!\n\n# Checking types\nprint(type(name))    # <class 'str'>\nprint(type(age))     # <class 'int'>"
            },
            "common_mistakes": [
                "Treating strings like numbers without converting",
                "Confusing = (assignment) with == (comparison)",
                "Forgetting that input() always returns a string"
            ],
            "practice_exercise": "Ask for user's birth year, convert to integer, calculate their age, and print it.",
            "icon": "🔢",
            "analogy": "Like different kitchen containers - each designed for specific contents and usage."
        },

        "loops": {
            "level": "intermediate",
            "category": "control flow", 
            "definition": "Loops let you repeat code multiple times without copying and pasting.",
            "explanation": "Loops are like assistants that repeat tasks for you. Use them when you need to do the same thing with multiple items or until a condition is met.",
            "quick_tip": "Use for loops when you know how many times to repeat, while loops when you don't!",
            "example": {
                "basic": "# For loop - great for lists\nfruits = [\"apple\", \"banana\", \"cherry\"]\nfor fruit in fruits:\n    print(f\"I like {fruit}\")\n\n# While loop - great for unknown repetitions\ncount = 5\nwhile count > 0:\n    print(count)\n    count -= 1\nprint(\"Blast off!\")",
                "advanced": "# Loop control with break and continue\nnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nfor num in numbers:\n    if num == 3:\n        continue    # Skip number 3\n    if num == 8:\n        break       # Stop at number 8\n    print(num)"
            },
            "common_mistakes": [
                "Infinite while loops (forgetting to update condition)",
                "Modifying list while iterating over it", 
                "Using wrong loop variable name"
            ],
            "practice_exercise": "Create a loop that prints numbers 1-10 but skips 5 and stops after 8.",
            "icon": "🔄",
            "analogy": "Like a recipe instruction 'Repeat steps 3-5 until the dough is smooth'."
        },

        "functions": {
            "level": "intermediate",
            "category": "code organization",
            "definition": "Functions are reusable code blocks that perform specific tasks.",
            "explanation": "Functions are like kitchen appliances - you define them once, then use them whenever needed. They make your code organized, reusable, and easier to fix.",
            "quick_tip": "Each function should do ONE thing well!",
            "example": {
                "basic": "# Simple function\ndef greet(name):\n    \"\"\"Say hello to someone\"\"\"\n    return f\"Hello, {name}!\"\n\n# Using the function\nmessage = greet(\"Alice\")\nprint(message)",
                "advanced": "# Function with default parameters and docstring\ndef calculate_area(length, width=1):\n    \"\"\"\n    Calculate area of rectangle.\n    \n    Args:\n        length: The length of rectangle\n        width: The width of rectangle (default 1 for square)\n    \n    Returns:\n        Area of the rectangle\n    \"\"\"\n    return length * width\n\n# Using with and without default\narea1 = calculate_area(5, 3)   # 15\narea2 = calculate_area(4)      # 4 (uses default width)"
            },
            "common_mistakes": [
                "Forgetting return statement", 
                "Modifying mutable default arguments",
                "Too many responsibilities in one function"
            ],
            "practice_exercise": "Create a function that takes temperature in Celsius and returns Fahrenheit.",
            "icon": "⚙️",
            "analogy": "Like kitchen appliances - define once, use many times with different inputs."
        },

        "conditionals": {
            "level": "beginner",
            "category": "control flow",
            "definition": "Conditionals let your program make decisions and choose different paths.",
            "explanation": "Like daily decisions ('if raining, take umbrella'), conditionals let your code react differently to different situations.",
            "quick_tip": "Use elif for multiple exclusive conditions!",
            "example": {
                "basic": "# Basic if-else\nage = 18\nif age >= 18:\n    print(\"You can vote!\")\nelse:\n    print(\"Wait until you're 18\")\n\n# Multiple conditions\ngrade = 85\nif grade >= 90:\n    print(\"A\")\nelif grade >= 80:\n    print(\"B\") \nelif grade >= 70:\n    print(\"C\")\nelse:\n    print(\"Need improvement\")",
                "advanced": "# Complex conditions with and/or\ntemperature = 25\nis_sunny = True\n\nif temperature > 20 and is_sunny:\n    print(\"Perfect beach day!\")\nelif temperature > 20 and not is_sunny:\n    print(\"Warm but cloudy\")\nelse:\n    print(\"Stay inside\")\n\n# Ternary operator (short if-else)\nresult = \"Adult\" if age >= 18 else \"Minor\""
            },
            "common_mistakes": [
                "Using = instead of == for comparison",
                "Forgetting colon at end of condition",
                "Unnecessary nested if statements"
            ],
            "practice_exercise": "Write a program that suggests activities based on weather and temperature.",
            "icon": "❓",
            "analogy": "Like deciding what to wear based on weather conditions."
        },

        "arrays": {
            "level": "intermediate",
            "category": "data structures",
            "definition": "Arrays store collections of items that you can access by position.",
            "explanation": "Arrays are like numbered storage compartments. Perfect when you have multiple related items and need to access them in order or by position.",
            "quick_tip": "Array indexes start at 0, not 1!",
            "example": {
                "basic": "# Creating and accessing arrays (lists)\ncolors = [\"red\", \"green\", \"blue\"]\nnumbers = [1, 2, 3, 4, 5]\n\n# Access elements\nfirst_color = colors[0]    # \"red\"\nlast_number = numbers[-1]  # 5 (negative index from end)\n\n# Modify arrays\ncolors.append(\"yellow\")    # Add to end\ncolors[1] = \"emerald\"      # Change second element",
                "advanced": "# List operations and slicing\nall_numbers = numbers + [6, 7, 8]  # Combine lists\nsubset = numbers[1:4]               # Slice: [2, 3, 4]\nreversed = numbers[::-1]            # Reverse: [5, 4, 3, 2, 1]\n\n# List comprehension (create lists efficiently)\nsquares = [x**2 for x in numbers]   # [1, 4, 9, 16, 25]\neven_numbers = [x for x in numbers if x % 2 == 0]  # [2, 4]"
            },
            "common_mistakes": [
                "Index out of range error",
                "Modifying list while iterating",
                "Confusing list methods (append vs extend)"
            ],
            "practice_exercise": "Create a list of 5 numbers, double each value, and find the sum.",
            "icon": "🗃️",
            "analogy": "Like an egg carton with numbered compartments - each holds one item."
        },

        "algorithms": {
            "level": "intermediate",
            "category": "problem solving",
            "definition": "Algorithms are step-by-step recipes for solving problems.",
            "explanation": "An algorithm is like a cooking recipe - clear steps that transform ingredients (input) into a dish (output). Good algorithms are correct, efficient, and easy to understand.",
            "quick_tip": "Plan your algorithm with pseudocode before coding!",
            "example": {
                "basic": "# Algorithm to find maximum number\ndef find_max(numbers):\n    \"\"\"\n    Algorithm Steps:\n    1. Start with first number as maximum\n    2. Compare with each next number\n    3. If larger, update maximum\n    4. Return final maximum\n    \"\"\"\n    if not numbers:\n        return None\n    \n    max_num = numbers[0]\n    for num in numbers:\n        if num > max_num:\n            max_num = num\n    return max_num\n\n# Usage\nnumbers = [3, 7, 2, 9, 1]\nprint(f\"Maximum: {find_max(numbers)}\")",
                "advanced": "# Algorithm efficiency comparison\nimport time\n\ndef sum_to_n_slow(n):\n    \"\"\"O(n) time complexity\"\"\"\n    total = 0\n    for i in range(1, n+1):\n        total += i\n    return total\n\ndef sum_to_n_fast(n):\n    \"\"\"O(1) time complexity - mathematical formula\"\"\"\n    return n * (n + 1) // 2\n\n# Both give same result, but different efficiency!\nprint(sum_to_n_slow(1000000))  # Slower\nprint(sum_to_n_fast(1000000))  # Faster"
            },
            "common_mistakes": [
                "Not considering edge cases",
                "Choosing inefficient approach for large data",
                "Over-optimizing too early"
            ],
            "practice_exercise": "Write an algorithm to count how many times a letter appears in a word.",
            "icon": "📊",
            "analogy": "Like a cooking recipe - precise steps that produce consistent results."
        },

        "sorting algorithms": {
            "level": "advanced",
            "category": "algorithms",
            "definition": "Sorting algorithms arrange elements in a specific order.",
            "explanation": "Like organizing books by height, sorting puts data in order. Different algorithms have different speeds and work better in different situations.",
            "quick_tip": "Use built-in sort() for most cases - it's highly optimized!",
            "example": {
                "basic": "# Built-in sorting (usually best choice)\nnumbers = [64, 34, 25, 12, 22, 11, 90]\nsorted_numbers = sorted(numbers)  # Returns new sorted list\nnumbers.sort()                    # Sorts original list\n\nprint(f\"Sorted: {sorted_numbers}\")",
                "advanced": "# Bubble Sort (educational example)\ndef bubble_sort(arr):\n    \"\"\"Simple but slow O(n²) sorting\"\"\"\n    n = len(arr)\n    for i in range(n):\n        for j in range(0, n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap\n    return arr\n\n# Quick Sort (efficient)\ndef quick_sort(arr):\n    \"\"\"Fast O(n log n) sorting on average\"\"\"\n    if len(arr) <= 1:\n        return arr\n    \n    pivot = arr[len(arr) // 2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    \n    return quick_sort(left) + middle + quick_sort(right)"
            },
            "common_mistakes": [
                "Implementing slow algorithms for large datasets",
                "Forgetting that sort() modifies original list",
                "Not considering stability requirements"
            ],
            "practice_exercise": "Implement a function that sorts names alphabetically.",
            "icon": "📈",
            "analogy": "Like arranging books on a shelf by height from shortest to tallest."
        },

        "searching algorithms": {
            "level": "intermediate",
            "category": "algorithms", 
            "definition": "Searching algorithms find items in collections.",
            "explanation": "Like finding a word in a dictionary, searching algorithms help locate data efficiently. The right algorithm depends on whether your data is sorted and how much data you have.",
            "quick_tip": "Use binary search for sorted data - it's much faster!",
            "example": {
                "basic": "# Linear Search - works on any list\ndef linear_search(arr, target):\n    \"\"\"O(n) - check each element one by one\"\"\"\n    for i, item in enumerate(arr):\n        if item == target:\n            return i  # Return index where found\n    return -1  # Not found\n\n# Usage\nnames = [\"Alice\", \"Bob\", \"Charlie\", \"Diana\"]\nindex = linear_search(names, \"Charlie\")  # Returns 2",
                "advanced": "# Binary Search - requires sorted data\ndef binary_search(arr, target):\n    \"\"\"O(log n) - repeatedly divide search space in half\"\"\"\n    low, high = 0, len(arr) - 1\n    \n    while low <= high:\n        mid = (low + high) // 2\n        \n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            low = mid + 1  # Search right half\n        else:\n            high = mid - 1  # Search left half\n    \n    return -1  # Not found\n\n# Binary search is MUCH faster for large sorted data\nsorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]\nindex = binary_search(sorted_numbers, 11)  # Returns 5"
            },
            "common_mistakes": [
                "Using binary search on unsorted data",
                "Off-by-one errors in indices",
                "Not checking empty array case"
            ],
            "practice_exercise": "Implement a function that finds if a number is in a list using binary search.",
            "icon": "🔍",
            "analogy": "Like looking up a word in dictionary by opening to middle and eliminating half each time."
        },

        "recursion": {
            "level": "advanced",
            "category": "programming techniques",
            "definition": "Recursion is when a function calls itself to solve smaller versions of the same problem.",
            "explanation": "Recursion breaks big problems into smaller identical problems. It's elegant but can be tricky - always have a base case to stop the recursion!",
            "quick_tip": "Always define a base case first - when should the recursion stop?",
            "example": {
                "basic": "# Factorial using recursion\ndef factorial(n):\n    \"\"\"\n    n! = n * (n-1) * (n-2) * ... * 1\n    Base case: 0! = 1, 1! = 1\n    Recursive case: n! = n * (n-1)!\n    \"\"\"\n    if n == 0 or n == 1:\n        return 1  # Base case\n    else:\n        return n * factorial(n - 1)  # Recursive case\n\nprint(f\"5! = {factorial(5)}\")  # 120",
                "advanced": "# Fibonacci sequence recursively\ndef fibonacci(n):\n    \"\"\"\n    Returns nth Fibonacci number\n    F(0) = 0, F(1) = 1\n    F(n) = F(n-1) + F(n-2)\n    \"\"\"\n    if n <= 0:\n        return 0\n    elif n == 1:\n        return 1\n    else:\n        return fibonacci(n-1) + fibonacci(n-2)\n\n# More efficient with memoization\nfrom functools import lru_cache\n\n@lru_cache(maxsize=None)\ndef fibonacci_memo(n):\n    \"\"\"Much faster using caching\"\"\"\n    if n <= 0:\n        return 0\n    elif n == 1:\n        return 1\n    else:\n        return fibonacci_memo(n-1) + fibonacci_memo(n-2)"
            },
            "common_mistakes": [
                "No base case (infinite recursion)",
                "Recursive case doesn't progress toward base case", 
                "Forgetting return statements"
            ],
            "practice_exercise": "Write a recursive function to calculate the sum of numbers from 1 to n.",
            "icon": "🎯",
            "analogy": "Like Russian nesting dolls - each contains a smaller version of itself."
        },

        "data structures": {
            "level": "intermediate",
            "category": "data organization",
            "definition": "Data structures are different ways to organize and store data for efficient access.",
            "explanation": "Like choosing the right storage system (shelves, boxes, filing cabinets), different data structures are optimized for different operations like searching, inserting, or sorting.",
            "quick_tip": "Choose data structure based on what operations you need most!",
            "example": {
                "basic": "# Common Python data structures\n\n# List - ordered, mutable\nfruits = [\"apple\", \"banana\", \"cherry\"]\n\n# Dictionary - key-value pairs\nperson = {\"name\": \"Alice\", \"age\": 25, \"city\": \"Paris\"}\n\n# Set - unique, unordered items\nunique_numbers = {1, 2, 3, 2, 1}  # Becomes {1, 2, 3}\n\n# Tuple - ordered, immutable\ncoordinates = (10, 20)",
                "advanced": "# Specialized data structures\nfrom collections import deque, Counter\n\n# Stack (LIFO) using list\nstack = []\nstack.append(1)  # Push\nstack.append(2)\nitem = stack.pop()  # Pop - returns 2\n\n# Queue (FIFO) using deque\nqueue = deque([\"task1\", \"task2\"])\nqueue.append(\"task3\")     # Enqueue\nnext_task = queue.popleft()  # Dequeue - returns \"task1\"\n\n# Counter for frequency counting\nword_count = Counter([\"apple\", \"banana\", \"apple\", \"cherry\"])\nprint(word_count)  # {'apple': 2, 'banana': 1, 'cherry': 1}"
            },
            "common_mistakes": [
                "Using list when set would be better for uniqueness",
                "Choosing wrong data structure for required operations",
                "Not considering time complexity of operations"
            ],
            "practice_exercise": "Use a dictionary to count how many times each letter appears in a word.",
            "icon": "🏗️",
            "analogy": "Like different storage systems - each optimized for specific access patterns."
        },

        "debugging": {
            "level": "beginner", 
            "category": "development skills",
            "definition": "Debugging is finding and fixing errors in your code.",
            "explanation": "Debugging is like being a detective - you look for clues, test theories, and solve the mystery of why your code isn't working as expected.",
            "quick_tip": "Read error messages carefully - they tell you exactly what went wrong!",
            "example": {
                "basic": "# Common debugging techniques\n\n# 1. Print debugging\nnumbers = [1, 2, 3, 4, 5]\nsum = 0\nfor num in numbers:\n    print(f\"Adding {num} to sum\")  # Debug print\n    sum += num\nprint(f\"Total: {sum}\")\n\n# 2. Using try-except\ntry:\n    result = 10 / 0\nexcept ZeroDivisionError as e:\n    print(f\"Error: {e}\")\n    print(\"Cannot divide by zero!\")",
                "advanced": "# Using Python debugger (pdb)\nimport pdb\n\ndef buggy_function(numbers):\n    total = 0\n    pdb.set_trace()  # Set breakpoint here\n    for num in numbers:\n        total += num\n    average = total / len(numbers)\n    return average\n\n# When run, you can:\n# - Type 'n' to go to next line\n# - Type 'p variable' to print variable\n# - Type 'c' to continue\n# - Type 'q' to quit"
            },
            "common_mistakes": [
                "Not reading the full error message",
                "Making multiple changes at once",
                "Not testing fixes thoroughly"
            ],
            "practice_exercise": "Find and fix the bug in this code: numbers = [1,2,3]; print(numbers[3])",
            "icon": "🐛",
            "analogy": "Like being a detective solving a mystery - follow the clues to find the culprit."
        },

        "pseudocode": {
            "level": "beginner",
            "category": "planning",
            "definition": "Pseudocode is a simple way to plan your code using plain language mixed with programming concepts.",
            "explanation": "Pseudocode is like writing a rough draft before the final essay. It helps you focus on the logic without worrying about perfect syntax.",
            "quick_tip": "Write pseudocode first - it saves time and prevents errors!",
            "example": {
                "basic": "# Pseudocode for calculating average\n\"\"\"\nBEGIN\n    READ list of numbers\n    SET total = 0\n    SET count = 0\n    \n    FOR each number IN numbers\n        ADD number to total\n        INCREMENT count by 1\n    END FOR\n    \n    IF count > 0 THEN\n        SET average = total / count\n        PRINT average\n    ELSE\n        PRINT \"No numbers to average\"\n    END IF\nEND\n\"\"\"",
                "advanced": "# Pseudocode for complex algorithm\n\"\"\"\nFUNCTION find_common_items(list1, list2)\n    BEGIN\n        CREATE empty result list\n        \n        FOR each item IN list1\n            IF item IN list2 AND item NOT IN result\n                ADD item to result\n            END IF\n        END FOR\n        \n        RETURN result\n    END\nEND FUNCTION\n\"\"\"\n\n# Then convert to actual code\ndef find_common_items(list1, list2):\n    result = []\n    for item in list1:\n        if item in list2 and item not in result:\n            result.append(item)\n    return result"
            },
            "common_mistakes": [
                "Skipping pseudocode and coding directly",
                "Making pseudocode too detailed (like actual code)",
                "Not updating pseudocode when requirements change"
            ],
            "practice_exercise": "Write pseudocode for a program that finds the largest number in a list.",
            "icon": "📝",
            "analogy": "Like writing a rough draft or outline before the final version."
        },

        "flowcharts": {
            "level": "beginner",
            "category": "visual planning", 
            "definition": "Flowcharts are diagrams that show the steps and decisions in a program using standardized symbols.",
            "explanation": "Flowcharts give you a visual map of your program's logic. They're great for understanding complex processes and spotting potential problems before you start coding.",
            "quick_tip": "Use flowcharts for complex logic with many decisions!",
            "example": {
                "basic": "# Text representation of a simple flowchart\n\"\"\"\n[Start] \n  ↓\n[Input number]\n  ↓\n[Is number even?] ← Diamond decision\n  ↓ Yes        ↓ No\n[Print 'Even'] [Print 'Odd']\n  ↓             ↓\n[End]         [End]\n\"\"\"",
                "advanced": "# Complex flowchart for login system\n\"\"\"\n[Start]\n  ↓\n[Display Login Screen]\n  ↓\n[User enters username/password]\n  ↓\n[Validate credentials] ← Diamond\n  ↓ Valid          ↓ Invalid\n[Grant access]   [Increment attempt count]\n  ↓                ↓\n[Welcome user]   [Attempts < 3?] ← Diamond\n  ↓                ↓ Yes         ↓ No\n[End]             [Show error]  [Lock account]\n                     ↓            ↓\n                  [Return to login] [End]\n\"\"\""
            },
            "common_mistakes": [
                "Too many details making flowchart messy",
                "Inconsistent symbol usage",
                "Not showing all possible paths"
            ],
            "practice_exercise": "Draw a flowchart for a number guessing game.",
            "icon": "📊",
            "analogy": "Like a roadmap showing different routes and decision points."
        },

        "binary search": {
            "level": "intermediate",
            "category": "algorithms",
            "definition": "Binary search efficiently finds items in sorted arrays by repeatedly dividing the search space in half.",
            "explanation": "Binary search is incredibly fast for large sorted datasets. It works like finding a word in a dictionary - you eliminate half the remaining options with each step.",
            "quick_tip": "Binary search only works on SORTED data!",
            "example": {
                "basic": "# Basic binary search implementation\ndef binary_search(arr, target):\n    low, high = 0, len(arr) - 1\n    \n    while low <= high:\n        mid = (low + high) // 2\n        \n        if arr[mid] == target:\n            return mid      # Found!\n        elif arr[mid] < target:\n            low = mid + 1   # Search right half\n        else:\n            high = mid - 1  # Search left half\n    \n    return -1  # Not found\n\n# Usage\nnumbers = [1, 3, 5, 7, 9, 11, 13, 15]\nindex = binary_search(numbers, 9)  # Returns 4",
                "advanced": "# Recursive binary search\ndef binary_search_recursive(arr, target, low, high):\n    if low > high:\n        return -1  # Base case: not found\n    \n    mid = (low + high) // 2\n    \n    if arr[mid] == target:\n        return mid\n    elif arr[mid] < target:\n        return binary_search_recursive(arr, target, mid + 1, high)\n    else:\n        return binary_search_recursive(arr, target, low, mid - 1)\n\n# Using the recursive version\nindex = binary_search_recursive(numbers, 9, 0, len(numbers)-1)"
            },
            "common_mistakes": [
                "Using on unsorted data",
                "Off-by-one errors in indices",
                "Infinite loop with wrong termination condition"
            ],
            "practice_exercise": "Implement binary search to find a name in a sorted list of names.",
            "icon": "🎯",
            "analogy": "Like finding a word in dictionary by opening to middle and eliminating half each time."
        },

        "bubble sort": {
            "level": "intermediate",
            "category": "algorithms",
            "definition": "Bubble sort repeatedly compares adjacent items and swaps them if they're in wrong order.",
            "explanation": "Bubble sort is simple to understand but slow for large lists. It's great for learning how sorting works, but use built-in sort() for real applications.",
            "quick_tip": "Bubble sort is educational but impractical for large data!",
            "example": {
                "basic": "# Basic bubble sort\ndef bubble_sort_basic(arr):\n    n = len(arr)\n    \n    for i in range(n):\n        for j in range(0, n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap\n    \n    return arr\n\nnumbers = [64, 34, 25, 12, 22, 11, 90]\nsorted_numbers = bubble_sort_basic(numbers.copy())\nprint(f\"Sorted: {sorted_numbers}\")",
                "advanced": "# Optimized bubble sort with early termination\ndef bubble_sort_optimized(arr):\n    n = len(arr)\n    \n    for i in range(n):\n        swapped = False\n        \n        for j in range(0, n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n                swapped = True\n        \n        # If no swaps, array is already sorted\n        if not swapped:\n            break\n    \n    return arr\n\n# Much faster if array is partially sorted"
            },
            "common_mistakes": [
                "Using for large datasets (very slow)",
                "Wrong range in inner loop",
                "Not optimizing with early termination"
            ],
            "practice_exercise": "Implement bubble sort and count how many swaps it makes.",
            "icon": "🫧",
            "analogy": "Like bubbles rising in water - lighter elements move up while heavier ones sink."
        },

        "quick sort": {
            "level": "advanced",
            "category": "algorithms", 
            "definition": "QuickSort is a fast, divide-and-conquer algorithm that works by selecting a pivot and partitioning the array.",
            "explanation": "QuickSort is one of the fastest sorting algorithms. It works by breaking the problem into smaller subproblems - perfect example of the divide-and-conquer strategy.",
            "quick_tip": "QuickSort is usually the fastest practical sorting algorithm!",
            "example": {
                "basic": "# Simple QuickSort (easy to understand)\ndef quicksort_simple(arr):\n    if len(arr) <= 1:\n        return arr\n    \n    pivot = arr[len(arr) // 2]  # Choose middle element\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    \n    return quicksort_simple(left) + middle + quicksort_simple(right)\n\nnumbers = [64, 34, 25, 12, 22, 11, 90]\nsorted_numbers = quicksort_simple(numbers)\nprint(f\"Sorted: {sorted_numbers}\")",
                "advanced": "# In-place QuickSort (memory efficient)\ndef quicksort_inplace(arr, low=0, high=None):\n    if high is None:\n        high = len(arr) - 1\n    \n    if low < high:\n        # Partition and get pivot index\n        pivot_index = partition(arr, low, high)\n        \n        # Recursively sort both halves\n        quicksort_inplace(arr, low, pivot_index - 1)\n        quicksort_inplace(arr, pivot_index + 1, high)\n\ndef partition(arr, low, high):\n    \"\"\"Lomuto partition scheme\"\"\"\n    pivot = arr[high]  # Choose rightmost as pivot\n    i = low - 1  # Index of smaller element\n    \n    for j in range(low, high):\n        if arr[j] <= pivot:\n            i += 1\n            arr[i], arr[j] = arr[j], arr[i]  # Swap\n    \n    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot\n    return i + 1"
            },
            "common_mistakes": [
                "Bad pivot choice leading to O(n²) performance",
                "Stack overflow with deeply recursive calls",
                "Not handling duplicate elements properly"
            ],
            "practice_exercise": "Implement QuickSort and test it on different input sizes.",
            "icon": "⚡",
            "analogy": "Like organizing books by picking one as reference, then sorting smaller and larger books separately."
        }
    }
    
    return concepts


def get_concept_by_level(concepts, level):
    """
    Get all concepts for a specific difficulty level
    
    Args:
        concepts (dict): The concepts dictionary
        level (str): The difficulty level ('beginner', 'intermediate', 'advanced')
    
    Returns:
        dict: Concepts filtered by the specified level
    """
    return {name: data for name, data in concepts.items() if data['level'] == level}


def get_concept_by_category(concepts, category):
    """
    Get all concepts in a specific category
    
    Args:
        concepts (dict): The concepts dictionary
        category (str): The category name
    
    Returns:
        dict: Concepts filtered by the specified category
    """
    return {name: data for name, data in concepts.items() if data['category'] == category}


def search_concepts(concepts, search_term):
    """
    Search concepts by name or keywords in definition
    
    Args:
        concepts (dict): The concepts dictionary
        search_term (str): The term to search for
    
    Returns:
        dict: Concepts that match the search term
    """
    results = {}
    search_term = search_term.lower()
    
    for name, data in concepts.items():
        if (search_term in name.lower() or 
            search_term in data['definition'].lower() or
            search_term in data['explanation'].lower()):
            results[name] = data
    
    return results


def get_learning_path(concepts):
    """
    Get concepts in recommended learning order
    
    Args:
        concepts (dict): The concepts dictionary
    
    Returns:
        list: Concepts organized in learning path order
    """
    level_order = ['beginner', 'intermediate', 'advanced']
    learning_path = []
    
    for level in level_order:
        level_concepts = get_concept_by_level(concepts, level)
        learning_path.extend(level_concepts.items())
    
    return learning_path