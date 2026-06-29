# ex05 — Lessons: a real program (`main`), input, and counting characters

Exercise 05 ("First standalone program") is the first **real autonomous program**. It takes a
single string and prints how many **upper-case**, **lower-case**, **punctuation**, **space**,
and **digit** characters it contains.

Allowed: **`sys`** (for the args). Info box from the subject: *"Don't reinvent the wheel, use
the language features."* — that's a big hint to use Python's string methods.

Target output (argument given):
```
$ python building.py "Python 3.0, released in 2008, ... in 2020."
The text contains 171 characters:
2 upper letters
121 lower letters
7 punctuation marks
26 spaces
15 digits
```

Target output (no argument → prompt):
```
$ python building.py
What is the text to count?
Hello World!
The text contains 13 characters:
2 upper letters
8 lower letters
1 punctuation marks
2 spaces
0 digits
```

---

## 0. ⚠️ New mandatory rules start HERE (ex05+)

From this exercise on, the Chapter VII rules are graded:

- **A real `main()`** — no logic in the global scope:
  ```python
  def main():
      ...

  if __name__ == "__main__":
      main()
  ```
- **Every function needs a docstring** (`"""..."""` = its `__doc__`).
- **Any uncaught exception invalidates the exercise** → wrap risky logic in `try/except`.
- **flake8-clean** (`pip install flake8`): **4-space indentation (no tabs)**, **no space before
  `:`**, two blank lines between top-level functions, lines ≤ 79 chars, no empty f-strings.

(Those are exactly the nits flagged on ex02–ex04 — now they count.)

---

## 1. Getting the text — argument *or* prompt

```python
args = sys.argv[1:]
assert len(args) <= 1, "more than one argument is provided"   # >1 arg → AssertionError
if len(args) == 0:
    print("What is the text to count?")
    text = sys.stdin.read()      # no arg → read from the keyboard
else:
    text = args[0]               # exactly one arg → use it
```

> ℹ️ **Why `sys.stdin.read()` and not `input()`?** The subject says *"the carriage return counts
> as a space; if you don't want one, use Ctrl-D."* `sys.stdin.read()` reads until **EOF
> (Ctrl-D)** and **keeps the trailing newline** — so pressing Enter adds a `\n` that gets counted
> as a space. `input()` would strip that newline. (That's why `Hello World!` + Enter counts as
> **13** characters and **2** spaces, not 12 and 1.)

And catch the assertion so the program prints a clean line instead of a traceback:
```python
except AssertionError as error:
    print(f"AssertionError: {error}")
```

---

## 2. Counting — use string methods (don't reinvent the wheel)

Every character "knows" what it is, via built-in `str` methods:

| Method        | True for…              |
|---------------|------------------------|
| `c.isupper()` | `A`–`Z`                |
| `c.islower()` | `a`–`z`                |
| `c.isdigit()` | `0`–`9`                |
| `c.isspace()` | space, tab, **newline**|
| `c in string.punctuation` | `!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~` |

`string.punctuation` is a ready-made constant — `import string` and use it (that's a "language
feature", not reinventing the wheel).

> 💡 The newline being whitespace is *why* `c.isspace()` makes the typed Enter count as a space.

---

## 3. The elegant counting trick: sum booleans

Remember from ex02/ex03 that **`bool` is an `int`** (`True == 1`, `False == 0`). So you can
**sum a generator of booleans** to count how many are `True`:

```python
upper = sum(c.isupper() for c in text)     # counts the upper-case characters
```

No manual `counter += 1` loop needed — `sum(...)` over `True/False` *is* the count. Do the same
for each category. Total characters is just `len(text)`.

---

## 4. Output — exact format

Order and wording matter (the grader compares text):

```python
print(f"The text contains {len(text)} characters:")
print(f"{upper} upper letters")
print(f"{lower} lower letters")
print(f"{punct} punctuation marks")
print(f"{spaces} spaces")
print(f"{digits} digits")
```

> ⚠️ It's always `"... punctuation marks"` — **plural even for 1** (`1 punctuation marks`).
> Order is **upper → lower → punctuation → spaces → digits**.

---

## Putting it together

```python
import sys
import string


def count_text(text):
    """Count and print the character categories of the given text."""
    print(f"The text contains {len(text)} characters:")
    print(f"{sum(c.isupper() for c in text)} upper letters")
    print(f"{sum(c.islower() for c in text)} lower letters")
    print(f"{sum(c in string.punctuation for c in text)} punctuation marks")
    print(f"{sum(c.isspace() for c in text)} spaces")
    print(f"{sum(c.isdigit() for c in text)} digits")


def main():
    """Get the text from the CLI argument or a prompt, then count it."""
    try:
        args = sys.argv[1:]
        assert len(args) <= 1, "more than one argument is provided"
        if len(args) == 0:
            print("What is the text to count?")
            text = sys.stdin.read()
        else:
            text = args[0]
        count_text(text)
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
```

(Validated against both subject examples — `171`-char arg case and the `Hello World!` prompt
case — and it's **pycodestyle/flake8-clean**.)

---

## How it applies to ex05

- **Standalone program** → `main()` + `if __name__ == "__main__":` (now required).
- **Input** → one arg → use it; no arg → prompt + `sys.stdin.read()`; >1 arg → `AssertionError`.
- **Counting** → `sum(c.isXXX() for c in text)` (booleans are 1/0) + `string.punctuation`.
- **Newline = space** → `sys.stdin.read()` keeps it, `c.isspace()` counts it.
- **Format** → exact labels/order; `punctuation marks` stays plural.
- **Norm** → docstrings on both functions, 4-space indent, no space before `:`, ≤ 79-char lines.
