---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6a742762-e908-83ee-81fd-168beb49cf16"
created: 1785997156.366524
updated: 1785999668.401536
resource_section: true
---

# Interview Prep from Resume

## User

Prepare me from this resume

## Assistant

Based on your resume, I would prepare you for interviews in the exact order of what you've claimed, because interviewers will ask questions from every line of it. fileciteturn0file0L5-L49

## 1. Introduction (Most Important)

Be able to answer confidently:

> "Hi, I'm Utkarsh Wadalkar, an Artificial Intelligence and Data Science undergraduate at Savitribai Phule Pune University. I have experience building AI applications, machine learning models, and workflow automation solutions. My key skills include Python, SQL, Machine Learning, Docker, Firebase, and Git. I've developed an AI Video Generation SaaS, a Fake News Detection ML model, and completed an AI & Automation internship. I'm looking for an AI Engineer role where I can build scalable AI products." fileciteturn0file0L5-L39

---

# 2. Technical Skills

You should be comfortable answering questions on:

### Python
- OOP
- Lists, Tuples, Dictionaries
- Functions
- File Handling
- Exception Handling
- Modules
- Virtual Environment

### SQL
- SELECT
- WHERE
- GROUP BY
- HAVING
- JOINS
- Subqueries
- Views
- Indexes
- Normalization

### Machine Learning
- Supervised vs Unsupervised Learning
- Classification vs Regression
- Train/Test Split
- Overfitting
- Underfitting
- Cross Validation
- Confusion Matrix
- Precision
- Recall
- F1 Score
- ROC-AUC

### Docker
- Images
- Containers
- Dockerfile
- Docker Compose
- Volumes
- Ports

### Git
- clone
- commit
- push
- pull
- branch
- merge
- rebase
- merge conflicts

These are all directly reflected in your listed skills. fileciteturn0file0L14-L20

---

# 3. Project Questions

## AI Video Generation SaaS

Expect questions like:

- Explain the architecture.
- Why React?
- Why Node.js?
- What is Express?
- Why Firebase?
- How does Firestore work?
- What is Authentication?
- Why use n8n?
- Explain the API flow.
- Biggest challenge?
- If 10,000 users join, what changes?

Know every bullet in your resume because interviewers often ask about them in detail. fileciteturn0file0L21-L28

---

## Fake News Detection

Be ready to explain:

- Dataset source
- Data preprocessing
- Feature extraction
- TF-IDF
- Logistic Regression
- Decision Tree
- Random Forest
- Accuracy comparison
- Why one model performed better
- Future improvements

fileciteturn0file0L29-L33

---

# 4. Internship

Prepare answers for:

- What REST APIs did you build?
- What workflow automation did you create?
- Which cloud database did you use?
- How did Git help your team?
- What was your biggest contribution?

fileciteturn0file0L34-L39

---

# 5. Computer Science Fundamentals

Since your coursework includes these subjects, revise:

- Data Structures
- DBMS
- Operating Systems
- Computer Networks
- Cloud Computing

Typical questions include:
- Difference between process and thread
- Deadlock
- TCP vs UDP
- OSI model
- ACID properties
- Normalization
- Time complexity

fileciteturn0file0L47-L49

---

# 6. Behavioral Questions

Practice answers for:

- Tell me about yourself.
- Why should we hire you?
- Why AI?
- Biggest challenge?
- Biggest failure?
- Team conflict?
- Leadership experience?
- Strengths and weaknesses?
- Where do you see yourself in five years?

---

# 7. Coding

Practice solving:

- Arrays
- Strings
- Hash Maps
- Linked Lists
- Stacks
- Queues
- Trees
- Binary Search
- Sliding Window
- Two Pointers

Use Python for coding interviews.

---

# 8. HR Questions

Prepare for:

- Expected salary
- Notice period
- Relocation
- Remote vs office
- Higher studies
- Questions for the interviewer

---

## 10-Day Preparation Plan

1. Resume + Introduction + HR questions
2. Python + SQL
3. Machine Learning basics
4. Fake News Detection project
5. AI Video Generation SaaS project
6. DBMS + Operating Systems
7. Computer Networks + Docker + Git
8. DSA practice
9. Mock interview
10. Revise everything and practice speaking aloud

With this preparation, you'll be well-equipped for AI Engineer, AI/ML Intern, Data Analyst, and Software Engineer interviews based on the experience and skills presented in your resume.

## User

What is git ammend

## Assistant

`git commit --amend` is used to **modify your most recent commit** instead of creating a new one.

You can use it to:

1. **Change the commit message**
2. **Add files you forgot to include**
3. **Remove or fix files in the last commit**

### Example 1: Change the last commit message
```bash
git commit --amend -m "Updated README with installation steps"
```

This replaces the previous commit message with the new one.

### Example 2: Add a forgotten file to the last commit
Suppose you committed your code but forgot to include `config.py`.

```bash
git add config.py
git commit --amend
```

Git opens your editor so you can keep or edit the commit message. The new commit will contain both the original changes and `config.py`.

### What actually happens?
Git creates a **new commit** that replaces the previous one. The old commit is no longer part of the branch history (unless someone else has already pulled it).

### Important
If you have **already pushed** the commit to a shared remote repository, amending changes the commit history. You'll need to force-push:

```bash
git push --force-with-lease
```

`--force-with-lease` is safer than `--force` because it checks that you don't accidentally overwrite someone else's work.

### When should you use `git commit --amend`?
- ✅ Fix a typo in the commit message.
- ✅ Include a file you forgot to add.
- ✅ Make a small correction to the most recent commit.
- ❌ Avoid using it on commits that others have already based work on unless everyone agrees to rewrite history.

In interviews, you can describe it simply:

> **"`git commit --amend` is used to modify the most recent commit, either by changing its message or by adding/removing changes, instead of creating a new commit."**

## User

Unit testing?

## Assistant

**Unit testing** is a software testing technique where you test the **smallest individual unit of code** (such as a function, method, or class) in isolation to verify that it works correctly.

### Simple definition (interview answer)

> **Unit testing is the process of testing individual units of code independently to ensure they produce the expected output.**

### Example

Suppose you have a Python function:

```python
def add(a, b):
 return a + b
```

A unit test for it:

```python
import unittest

def add(a, b):
 return a + b

class TestAdd(unittest.TestCase):
 def test_add(self):
 self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
 unittest.main()
```

The test checks whether `add(2, 3)` returns `5`. If it does, the test passes.

### Why is unit testing important?

- Finds bugs early in development.
- Ensures code works as expected after changes.
- Makes refactoring safer.
- Improves code quality and reliability.
- Saves debugging time.

### Popular unit testing frameworks

- **Python:** `unittest`, `pytest`
- **Java:** JUnit
- **JavaScript:** Jest, Mocha
- **C#:** NUnit
- **C++:** Google Test

### Interview follow-up: Unit Testing vs Integration Testing

| Unit Testing | Integration Testing |
|--------------|---------------------|
| Tests a single function or class | Tests how multiple modules work together |
| Fast and isolated | Slower because multiple components are involved |
| Written by developers | Written by developers or QA |

### One-line interview answer

> **Unit testing verifies that individual functions, methods, or classes work correctly in isolation before they are integrated with the rest of the application.**

## User

Always give one line answer for this chat from now

## Assistant

Understood—I’ll keep my answers to **one concise line** in this chat unless you ask for a detailed explanation.

## User

What are react hooks

## Assistant

**React Hooks are special functions that let functional components use state and lifecycle features without writing class components.**

## Assistant

Got it—I'll answer each of these in **one interview-ready line**. Ask them one by one.

## User

What is git config used for

## Assistant

**`git config` is used to configure Git settings such as your username, email, editor, and default behavior at the system, global, or repository level.**

## Resources

### Local attachments
- [resume_1.pdf](../../../Raw/Export/file_0000000027c08211b1272f4a03be7b89.dat)
