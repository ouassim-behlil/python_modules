# Module 02: Exceptions

All the content of this project, including code, represent my understanding of the concepts. It may be partially or totally wrong.

## What is an Exception?

An **Exception** is what happens when something goes wrong while your program is running. It's how the language signals that something went wrong during the execution. Python lets you catch, handle, or raise these errors in a controlled way.

An example:

```python
x = 10 / 0
```
This raises:
```python
ZeroDivisionError: division by zero
```
So, common exceptions are:
ZeroDivisionError

- TypeError

- ValueError

- IndexError

- KeyError

- FileNotFoundError

- ImportError

## Catching Exceptions (try / except)

We catch exceptions using `try` and `catch`:
```python
try:
    x = int("abc")
except ValueError:
    print("Conversion failed!")
```
so here, we are trying to convert `"abc"` to int, which raises a `ValueError` for sure. Using `try` tells Python that an exception may occur in this block of code.

Then `except` tells Python: "don't crash the program when this exception occurs, do this instead". In the previous example, we print an error message and the program continue execution.

The next question you may ask, which I asked for sure, is **how to handle multiple exceptions?**

```python
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
```
In this example, we have two possible exceptions, first one is `ValueError` because the user input is not controlled so it may happen while converting the user input to int. The second possible exception is `ZeroDivisionError` which I explained before.

We can catch multiple exception each as time like in the previous example, as we can catch them at onece:

```python
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except (ValueError, ZeroDivisionError):
    print("Something went wrong.")
```

**What if we want to catch all exceptions?**

we can do it using the `Exception` class like this:
```python
try:
    some_operation()
except Exception as e:
    print("Error:", e)
```

this catch all exceptions but it's bad practice. The idea is that all Exceptions inherits from `Exception` class.

Sometimes we want to do something only if no exception occured, we can do it using `else` simply like that:
```python
try:
    x = int("5")
except ValueError:
    print("Invalid number")
else:
    print("Conversion successful:", x)
```

And Sometimes we want to do other things whether an exceptions occurs or not (like closing files or releasing ressources), we can do it also using `finally`:
```python
try:
    file = open("data.txt")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()
```

## Raising Exceptions:

we can raise exceptions manually using `raise` clause. 
```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```
in this example, we raise an `ValueError` exception with the message `"Age cannot be negative"`. This is because exceptions inherits from `Exception` class. So the message is a parameter of the constructor of `ValueError` who's itself calling the constructor of `Exception` class.

Sometimes, we need our custom exceptions, that's why we create our own exceptions.
## Create Custom Exception:

we can define our own Exception classes:
```python
class InvalidAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise InvalidAgeError("Age must be positive")

set_age(-1)
```

Custom exceptions improve clarity and makes debugging easier.

## Best Practices:

- Catch specific exceptions, not generic ones
- Use exceptions for exceptional cases, not normal logic
- Provide meaningful error messages
- Don’t silently ignore exceptions
- Don’t overuse try-except

