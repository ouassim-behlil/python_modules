# Module 01

## Class method:

A class method is a method that bounds to the class itself. It takes `cls` as argument and operate on the `class` and not the instances.
It is declared using `@classmethod` decorator.

A minimal example is:

```python
class User:
	count = 0

	def __init__(self):
		self.count += 1

	@classmethod
	def how_many_users(cls) -> int:
		return cls.count
```

and then we call it like that:

```python
User.how_many_users()
```

Notice that I can call it like that:
```
user = User()
user.how_many_users()
```
And it works, but it's considered a bad idea for class methods because it looks like it belongs to the `user` instance.

Another questions is: why not just 
```return User.count```?
Answer is **inheritance**. Let's assume we have:
```python
class Admin(User):
	pass
```
Now if we call:
```
Admin.how_many_users()
```
- `cls` is now `Admin` and not `User`
- the class method adapts automatically

If we hardcoded `User.how_many_users()`, inheritance would break.

A real-world example of using class methods is **alternative constructors**.

so let's imagine a class `Point`:
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```
Normally, I'll create points as simple as: `p = Point(1, 2)`.
But if want to create a point from a string `"2,3"` or a tuple `(3, 4)`?

class methods are alternative way to construct the points:
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_string(cls, text):
        x_str, y_str = text.split(",")
        return cls(int(x_str), int(y_str))

    @classmethod
    def from_tuple(cls, coords):
        return cls(coords[0], coords[1])
```

so this:
```python
p1 = Point(3, 4)
p2 = Point.from_string("3,4")
p3 = Point.from_tuple((3, 4))
```
all produces a `Point`.

## Static Method:

Static methods are methods that:
- Needs **no object data**
- Needs **no class data**
- Receives nothing automatically

they are functions related to the class, but independent of any instance. And it's created using the `staticmethod` decorator.

An example is:
```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
```
and we call it like:
```python
MathUtils.add(1, 2)
```
so **why not just use a normal function?**

The answer is **Namespacing**. To avoid name collisions and improve readability. 

Otherwords, we affirms that `add` function belongs to the idea of `MathUtils`.

So, if a method doesn't use `self` and doesn't use `cls`, it should be probably a static method.