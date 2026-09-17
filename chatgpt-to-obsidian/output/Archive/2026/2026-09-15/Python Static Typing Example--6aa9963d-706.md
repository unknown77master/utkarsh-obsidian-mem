---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6aa9963d-7060-83ee-ae16-fbe8bdf7e015"
created: 1789498942.665971
updated: 1789500098.857595
resource_section: true
---

# Python Static Typing Example

## User

Give example code of statically type var in python language

## Assistant

Worked for a couple of seconds

## Assistant

In Python, you can use **type hints** to specify the expected type of a variable:

```python
age: int = 21
name: str = "Utkarsh"
salary: float = 50000.0
is_student: bool = True
```

For example:

```python
x: int = 10

print(x)
```

Output:

```text
10
```

Note: Python is still **dynamically typed**. `x: int` is a type annotation, not strict static typing at runtime. Tools such as **mypy** or **Pyright** can statically check these annotations.

## User

So I got this reply, fact check it

rovingdev replied to your comment on rovingdev's post:

@utkw_pvt_ There is a difference in type hinting and static typing. Python has type hinting not static typing. It's just a suggestion. It helps your code editor catch bugs and give you autocomplete, but Python doesn't care at runtime. If you pass a string into an integer hint, it runs anyway!

## Assistant

Worked for a couple of seconds

## Assistant

Yes — that reply is essentially correct.

Python is a **dynamically typed language**. An annotation like:

```python
x: int = 10
```

is a **type hint**, not a runtime-enforced static type.

This is still valid Python:

```python
x: int = 10
x = "hello"

print(x)
```

It runs and prints:

```text
hello
```

Python itself does not reject the reassignment. Static type checkers such as **mypy**, **Pyright**, or an IDE may flag it before execution.

The only nuance is terminology: Python supports **optional static type checking through type annotations**, so people sometimes loosely say “statically typed Python code.” But Python's runtime type system remains dynamic.

So if your original claim was “`x: int = 10` creates a statically typed variable in Python,” then **their correction is right**. A more precise statement would be:

> “Python supports type annotations that can be checked statically by external tools, but the language itself remains dynamically typed.”

## Resources

No structured attachments or external references were present in this conversation.
