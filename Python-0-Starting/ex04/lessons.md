# ex04 — Lessons: command-line args, `assert`, odd/even

Exercise 04 ("The Even and the Odd") is your first **standalone script that reads a
command-line argument**. It takes one number and prints whether it's odd or even — and it must
raise a clean **`AssertionError`** for bad input.

Allowed: **`sys`** (or any library that gives you the args).

Target behaviour (`python whatis.py <arg>`):
```
python whatis.py 14      ->  I'm Even.
python whatis.py -5      ->  I'm Odd.
python whatis.py         ->  (nothing)
python whatis.py 0       ->  I'm Even.
python whatis.py Hi!     ->  AssertionError: argument is not an integer
python whatis.py 13 5    ->  AssertionError: more than one argument is provided
```

---

## 1. Reading arguments — `sys.argv`

`sys.argv` is a **list of strings**: the script name first, then each argument you typed.

```python
import sys
# $ python whatis.py 14
# sys.argv == ['whatis.py', '14']
```

- `sys.argv[0]` → the script name (`whatis.py`) — ignore it.
- `sys.argv[1:]` → the **real arguments**.
- Everything is a **string**, even `'14'` — you convert it yourself.

```python
args = sys.argv[1:]      # just the user's arguments
len(args)                # how many were given
```

---

## 2. The "no argument" case

With no argument, the program does **nothing** and exits cleanly (no output, no error):

```python
if len(args) == 0:
    return
```

---

## 3. `assert` — raising an error on a bad condition

```python
assert condition, "message"
```

If `condition` is **falsy**, Python raises `AssertionError("message")`. You use it to reject
bad input:

```python
assert len(args) == 1, "more than one argument is provided"
```

> ⚠️ Order matters: check the **count first**. With `13 5` the subject wants
> `more than one argument is provided`, *not* the "not an integer" message.

---

## 4. Printing a *clean* AssertionError (no traceback)

If an `assert` is left **uncaught**, Python dumps a multi-line **traceback** to the screen:
```
Traceback (most recent call last):
  ...
AssertionError: argument is not an integer
```
But the subject shows just **one line**. So you **catch** it and print it yourself:

```python
try:
    ...
    assert len(args) == 1, "more than one argument is provided"
    ...
except AssertionError as error:
    print(f"AssertionError: {error}")     # -> 'AssertionError: more than one argument is provided'
```

`str(error)` is exactly the message you passed to `assert`, so `f"AssertionError: {error}"`
reproduces the subject's output precisely.

---

## 5. Checking "is it an integer?"

The argument is a **string**. `int()` converts it — and raises **`ValueError`** if it can't:

```python
int("14")    # 14
int("-5")    # -5   ← negatives work fine
int("Hi!")   # ValueError!
int("3.5")   # ValueError!  (not an *integer*)
```

So convert inside the `try` and turn a failed conversion into the required message:

```python
try:
    number = int(args[0])
except ValueError:
    print("AssertionError: argument is not an integer")
```

> 💡 Alternative with pure `assert`: `assert args[0].lstrip("-").isdigit(), "argument is not an
> integer"`. It reads nicely, but note `"14".isdigit()` is `True` while `"-5".isdigit()` is
> `False` — hence the `lstrip("-")`. The `int()`-and-catch approach handles signs for free.

---

## 6. Odd or even — the `%` operator

`%` gives the remainder. Even ⇔ remainder `0`:

```python
if number % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
```

Two cases worth knowing:
- **`0`** → `0 % 2 == 0` → **Even**.
- **Negatives** → Python's `%` always returns a result with the divisor's sign, so
  `-5 % 2 == 1` → **Odd**. (No special handling needed.)

---

## Putting it together

```python
import sys


def main():
    """Print whether the single integer argument is odd or even."""
    try:
        args = sys.argv[1:]
        if len(args) == 0:
            return
        assert len(args) == 1, "more than one argument is provided"
        number = int(args[0])
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
```

(Validated against all six subject cases — output matches exactly.)

---

## How it applies to ex04

- **Read args** → `sys.argv[1:]` (strings); `len()` for the count.
- **No arg** → `return` (print nothing).
- **Too many args** → `assert len(args) == 1, "more than one argument is provided"` (checked first).
- **Not an integer** → `int(args[0])` raises `ValueError` → print `AssertionError: argument is not an integer`.
- **Clean error line** → `try/except` + `print(f"AssertionError: {error}")` (no traceback).
- **Odd/even** → `number % 2` (works for `0` and negatives).

> 🔜 **ex04 is the last "simple script" exercise.** From **ex05** the additional rules kick in:
> a `main()` with `if __name__ == "__main__":`, a docstring on every function, and
> flake8-clean code. The solution above already uses `main()` + a docstring — so you're set up
> for what's next. (Also: remember **4-space indentation**, not tabs, from here on.)
