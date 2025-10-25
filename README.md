# 🐍 Python Decorators Showcase

A clean, educational repository focused purely on **Python decorators** — how they work, how to build them, and how to apply them in real-world patterns.  
Each example is self-contained and demonstrates one concept clearly.

---

## 📂 Repository Structure

```
python-decorators-showcase/
├── README.md
├── requirements.txt
├── basics/
├── advanced/
├── practical/
└── meta/
```

---

## 🎯 Learning Goals

By exploring this repository, you will understand:

- How function decorators work under the hood
- The difference between function, argument-based, and class-based decorators
- Why `functools.wraps` is important for preserving metadata
- How to chain multiple decorators
- Real-world patterns like memoization, retries, validation, logging, and timing
- How decorators can modify classes and methods

---

## 🧩 Folder Overview

| Folder | Focus | Examples |
|--------|--------|-----------|
| **`basics/`** | Core decorator mechanics | `simple_function_decorator.py`, `functools_wraps_demo.py` |
| **`advanced/`** | Class-based and factory decorators | `class_based_decorator.py`, `retry_decorator.py` |
| **`practical/`** | Real-world utility decorators | `logging_decorator.py`, `authorization_decorator.py` |
| **`meta/`** | Meta-programming & chaining concepts | `decorator_for_methods.py`, `composition_patterns.py` |

---

## 🚀 Quick Start

```bash
git clone https://github.com/<your-username>/python-decorators-showcase.git
cd python-decorators-showcase
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -U pip
```

Run any example:

```bash
python basics/simple_function_decorator.py
```

---

## 🧠 Example: Simple Decorator

```python
def simple_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@simple_decorator
def greet():
    print("Hello, Python!")

greet()
```

**Output:**

```
Before function call
Hello, Python!
After function call
```

---

## 💡 Suggested Learning Path

1. Start with **`basics/`** → Learn how decorators wrap functions.
2. Explore **`advanced/`** → Create reusable and class-based decorators.
3. Move to **`practical/`** → See decorators in action for logging, timing, etc.
4. Finish with **`meta/`** → Understand decorator chaining and meta-patterns.


---


## 👤 Author

**Nitin S. Kulkarni**  
Python Developer
[GitHub](https://github.com/nkpythondeveloper) | [Blog](https://dailypytips.com)
