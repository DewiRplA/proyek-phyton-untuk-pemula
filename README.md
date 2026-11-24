# 🐍 Python for Beginners Project

This repository serves as a comprehensive documentation of my learning journey in **Python** programming fundamentals—from basic syntax to Object-Oriented Programming (OOP) and development environment management (*Virtual Environment* & `pip`). Each module includes hands-on practice scripts and screenshots of the program execution outputs.

---

## 📑 Table of Contents
- [Project Directory Structure](#-project-directory-structure)
- [System Prerequisites](#-system-prerequisites)
- [Installation & Configuration Guide](#-installation--configuration-guide)
- [Curriculum Summary & Code Examples](#-curriculum-summary--code-examples)
  - [1. Introduction & Basic Output (`hello.py`)](#1-introduction--basic-output-hellopy)
  - [2. Variables & Data Types (`variable.py`)](#2-variables--data-types-variablepy)
  - [3. Operators (`operator.py`)](#3-operators-operatorpy)
  - [4. Conditional Statements (`if_else.py`)](#4-conditional-statements-if_elsepy)
  - [5. Loops (`lopping.py`)](#5-loops-loppingpy)
  - [6. Data Structures: Lists & Dictionaries (`lists_and_dictionaries.py`)](#6-data-structures-lists--dictionaries-lists_and_dictionariespy)
  - [7. Functions (`function.py`)](#7-functions-functionpy)
  - [8. Object-Oriented Programming / OOP (`class_and_object.py`)](#8-object-oriented-programming--oop-class_and_objectpy)
  - [9. Package Management with PIP (`pip.py`)](#9-package-management-with-pip-pippy)
- [Running the Programs](#-running-the-programs)
- [Screenshot Documentation](#-screenshot-documentation)

---

## 📂 Project Directory Structure

```text
proyek-phyton-untuk-pemula/
├── python-untuk-pemula/          # Main directory containing all Python practice scripts
│   ├── hello.py                  # First program (Hello Python)
│   ├── variable.py               # Implementation of variables and basic data types
│   ├── operator.py               # Arithmetic, comparison, and logical operators
│   ├── if_else.py                # Conditional branching using if, elif, and else
│   ├── lopping.py                # For loops, while loops, and break control statements
│   ├── lists_and_dictionaries.py # Manipulation of List and Dictionary data structures
│   ├── function.py               # Creating functions, parameters, *args, and **kwargs
│   ├── class_and_object.py       # OOP concepts: Class, Object, Constructor, and Method
│   └── pip.py                    # Using external libraries (camelcase) via PIP
├── screenshot/                   # Collection of setup and program execution screenshots
│   ├── inisiasi_pertama.png
│   ├── install_pycharm.png
│   ├── ide.png
│   ├── virtual_environment.png
│   ├── cek_pip.png
│   ├── variable .png
│   ├── operator.png
│   ├── if-elif.png
│   ├── perulangan.png
│   ├── list_dictionaries.png
│   ├── function.png
│   └── class and object.png
├── .gitignore                    # List of files/folders ignored by Git (venv/, __pycache__/, .env)
├── README.md                     # Main project documentation
└── requirements.txt              # List of external library dependencies
```

---

## 💻 System Prerequisites

Before running the code in this repository, ensure your system meets the following requirements:
- **Python 3.x** (Python 3.10 or newer is recommended) installed and added to your system *PATH*.
- **PIP** (*Python Package Installer*) enabled to manage third-party packages.
- **Code Editor / IDE** such as PyCharm or Visual Studio Code.
- **Git** for version control.

---

## ⚙️ Installation & Configuration Guide

Follow these steps to set up an isolated workspace using a *Virtual Environment*:

### 1. Clone the Repository
```bash
git clone https://github.com/DewiRplA/proyek-phyton-untuk-pemula.git
cd proyek-phyton-untuk-pemula
```

### 2. Create & Activate the Virtual Environment (`venv`)
Using a *virtual environment* ensures that project dependencies remain isolated from your global Python installation.

- **Windows (Command Prompt / PowerShell):**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- **Linux / macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
  *(Once activated, `(venv)` will appear at the beginning of your terminal prompt).*

### 3. Install Dependencies from `requirements.txt`
Install all required third-party libraries for this project by running:
```bash
pip install -r requirements.txt
```

---

## 📚 Curriculum Summary & Code Examples

Below is a detailed breakdown of each topic covered and implemented inside the `python-untuk-pemula/` folder:

### 1. Introduction & Basic Output (`hello.py`)
Learned the fundamental syntax structure of Python and how to display text output to the terminal using the built-in `print()` function.
- **Key Concepts:** Semicolon-free syntax, using double quotes for *strings*, and executing Python scripts.
- **Code Snippet:**
  ```python
  print("Halo Python")
  ```

### 2. Variables & Data Types (`variable.py`)
Learned how to store values in variables without explicitly declaring their data types (*dynamic typing*).
- **Key Concepts:**
  - **Integer (`int`):** Whole numbers (e.g., `x = 5`, `y = 3`).
  - **Float (`float`):** Decimal numbers (e.g., `a = 7.5`).
  - **String (`str`):** Text enclosed in single quotes (`'...'`), double quotes (`"..."`), or triple quotes (`"""..."""`) for *multiline strings*, as well as string concatenation using the `+` operator.
  - **Boolean (`bool`):** Logical truth values `True` and `False` (*case-sensitive*).

### 3. Operators (`operator.py`)
Learned various operational symbols to manipulate values and variables:
- **Arithmetic Operators:** Addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), modulus (`%`), and exponentiation (`**`).
- **Comparison Operators:** Comparing two values to return `True` or `False`, including equal to (`==`), not equal to (`!=`), less than (`<`), less than or equal to (`<=`), greater than (`>`), and greater than or equal to (`>=`).
- **Logical Operators:** Combining conditional expressions using `and` (true if both are true), `or` (true if at least one is true), and `not` (inverts the boolean value).

### 4. Conditional Statements (`if_else.py`)
Learned decision-making control flow based on specific conditions while adhering to Python's strict indentation rules.
- **Key Concepts:**
  - `if`: Executes a code block if the primary condition evaluates to `True`.
  - `elif`: Checks alternative conditions if the preceding condition evaluates to `False`.
  - `else`: Executes a fallback code block if none of the above conditions are met.

### 5. Loops (`lopping.py`)
Learned how to repeatedly execute code blocks to automate iteration processes:
- **`for` Loops:**
  - Using `range(5)` to repeat an instruction a specific number of times.
  - Iterating directly over elements inside a `list` (`fruits`) or individual characters in a `string` (`"indonesia"`).
- **`while` Loops:** Repeating a code block as long as a specified condition remains `True` (e.g., `while counter < 5:`).
- **Loop Control (`break`):** Prematurely terminating a loop cycle when a specific condition is met (e.g., stopping when `x == 3`).

### 6. Data Structures: Lists & Dictionaries (`lists_and_dictionaries.py`)
Learned how to store and manage complex collections of data:
- **List (Ordered Collection):**
  - *Indexing:* Accessing items using positive indexing (starting at `0`) and negative indexing (`-1` for the last item).
  - *Adding Items:* Using `.append()` to add to the end of a list and `.insert(index, item)` to insert at a specific position.
  - *Removing Items:* Using `.remove(value)`, `.pop()` (removes the last item), `.pop(index)` (removes by index), and `.clear()` (empties the list).
  - *Combining Lists:* Using `.extend()` or the `+` operator.
- **Dictionary (Key-Value Pairs):**
  - *Accessing Data:* Retrieving values using square brackets `dict['key']` or the safe `.get('key')` method, as well as listing all keys with `.keys()` and values with `.values()`.
  - *Modifying Data:* Adding or updating entries via direct assignment (`dict['key'] = val`) or the `.update({...})` method.
  - *Removing Data:* Deleting specific key-value pairs with `.pop('key')` or clearing the entire dictionary with `.clear()`.

### 7. Functions (`function.py`)
Learned code modularization for reusability using the `def` keyword:
- **Basic Functions & Parameters:** Defining functions without arguments as well as with one or more positional arguments.
- **Keyword Arguments:** Calling functions by explicitly specifying parameter names (`age=25, name="Fika"`) so argument order does not matter.
- **Default Parameter Values:** Assigning fallback values to parameters (e.g., `name="Alien"`) when no argument is passed during a call.
- **Arbitrary Arguments (`*args`):** Accepting an arbitrary number of positional arguments as a *tuple*.
- **Arbitrary Keyword Arguments (`**kwargs`):** Accepting an arbitrary number of labeled (*key-value*) arguments as a *dictionary*.

### 8. Object-Oriented Programming / OOP (`class_and_object.py`)
Learned the *Object-Oriented Programming* (OOP) paradigm in Python:
- **Class & Object:** Creating object blueprints (`class Cat:`) and instantiating real objects from them (`cat1 = Cat()`).
- **Properties / Attributes:** Defining object characteristics (such as `color = "black"`).
- **Constructor (`__init__`):** A special method automatically invoked upon object instantiation to initialize object attributes.
- **Methods & `self` Parameter:** Defining functions inside a class (such as `say()`) to establish object behavior and understanding the first parameter (`self` or custom naming like `myParam`) as a reference to the current instance.

### 9. Package Management with PIP (`pip.py`)
Learned how to work with Python's third-party package ecosystem:
- Installing the external `camelcase` package via terminal (`pip install camelcase`).
- Importing external modules (`import camelcase`) and utilizing `CamelCase().hump()` to capitalize the first letter of each word in a string.

---

## ▶️ Running the Programs

Ensure your terminal is located in the root directory (`proyek-phyton-untuk-pemula/`) with the *virtual environment* activated, then execute any script using the following commands:

```bash
# 1. Basics & Variables
python python-untuk-pemula/hello.py
python python-untuk-pemula/variable.py

# 2. Operators & Control Flow
python python-untuk-pemula/operator.py
python python-untuk-pemula/if_else.py
python python-untuk-pemula/lopping.py

# 3. Data Structures & Functions
python python-untuk-pemula/lists_and_dictionaries.py
python python-untuk-pemula/function.py

# 4. OOP & External Packages
python python-untuk-pemula/class_and_object.py
python python-untuk-pemula/pip.py
```

---

## 🖼️ Screenshot Documentation

All proof of work—including initial Git setup, PyCharm installation, *virtual environment* configuration, `pip` verification, and execution outputs for every script—is neatly stored in the [`screenshot/`](./screenshot/) directory.