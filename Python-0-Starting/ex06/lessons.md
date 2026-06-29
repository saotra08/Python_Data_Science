# ex06 — Lessons: list comprehensions, `lambda`, and recoding `filter`

Exercise 06 is your first **two-file** exercise:

- **Part 1 — `ft_filter.py`**: recode the built-in `filter` using a **list comprehension**
  (calling the real `filter` is forbidden). Its docstring must equal `filter.__doc__`.
- **Part 2 — `filterstring.py`**: a program taking a string `S` and an integer `N`, printing the
  words of `S` whose length is **greater than `N`**. It must contain at least one **list
  comprehension** and one **`lambda`**.

Allowed: **`sys`**. Norm is graded (flake8-clean + docstrings, like ex05).

Part 2 target output:
```
$ python filterstring.py 'Hello the World' 4    ->  ['Hello', 'World']
$ python filterstring.py 'Hello the World' 99   ->  []
$ python filterstring.py 3 'Hello the World'    ->  AssertionError: the arguments are bad
$ python filterstring.py                        ->  AssertionError: the arguments are bad
```

---

## 1. List comprehensions

A **list comprehension** builds a list in one expression:

```python
[expr for item in iterable if condition]
```

- `for item in iterable` — loop over the source.
- `if condition` — *(optional)* keep only items that pass.
- `expr` — what to put in the new list for each kept item.

```python
[n * n for n in range(5)]            # [0, 1, 4, 9, 16]
[w for w in ["hi", "yo", "hey"] if len(w) > 2]   # ['hey']
```

(It's the same "loop, but as one expression" idea behind the `sum(... for c in text)` you used
in ex05 — that one was a *generator*; wrap it in `[]` and it's a list.)

---

## 2. Part 1 — recode `filter` as `ft_filter`

**What the built-in does:** `filter(function, iterable)` keeps the items for which
`function(item)` is truthy. **Special case:** if `function is None`, it keeps the items that are
themselves truthy.

```python
list(filter(lambda x: x > 2, [1, 2, 3, 4]))   # [3, 4]
list(filter(None, [0, 1, "", 2, [], 3]))      # [1, 2, 3]   (drops falsy: 0, "", [])
```

Recode that with a comprehension — and **don't call the real `filter`** (forbidden):

```python
def ft_filter(function, iterable):
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]
```

> ℹ️ The built-in returns a lazy *iterator*; your version returns a **list** (that's what the
> comprehension makes, and it's what lets `print(...)` show `['Hello', 'World']` directly).

---

## 3. Making the docstring equal `filter.__doc__`

The subject wants `print(ft_filter.__doc__)` to print the same as `print(filter.__doc__)`. First,
see the exact text:

```python
print(filter.__doc__)
# Return an iterator yielding those items of iterable for which function(item)
# is true. If function is None, return the items that are true.
```

Copy that as your docstring. **But there's a catch:** that first line is **76 characters**, so
once you add 4-space indentation + `"""`, the source line is **83 chars → flake8 `E501`**. Two
clean ways to keep the text exact *and* pass flake8:

**Option A — split the literal across lines (implicit concatenation, no suppression):**
```python
def ft_filter(function, iterable):
    """Return an iterator yielding those items of iterable for which """ \
        """function(item)\nis true. If function is None, return the """ \
        """items that are true."""
    ...
```
Adjacent string literals are joined into one, so `__doc__` is identical — and every source line
stays under 79.

**Option B — tell flake8 to skip just that line:**
```python
def ft_filter(function, iterable):
    """Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""  # noqa: E501
    ...
```
Both keep `ft_filter.__doc__ == filter.__doc__` and are pycodestyle-clean. (A is "purer"; B is
simpler — pick your taste.)

> ⚠️ Use **your own** Python's `filter.__doc__` (ideally 3.10) — the wording can differ slightly
> between versions, and the match must be exact.

---

## 4. `lambda` — an anonymous one-line function

```python
lambda arguments: expression
```

It's a small function with no `def` and no name — the value of `expression` is returned. These
two are equivalent:

```python
def longer(word):
    return len(word) > n

longer = lambda word: len(word) > n
```

You'll pass a `lambda` straight into `ft_filter` as the "function".

---

## 5. Part 2 — `filterstring.py`

**Validate the arguments** → on anything wrong, print exactly
`AssertionError: the arguments are bad`:

```python
args = sys.argv[1:]
assert len(args) == 2, "the arguments are bad"     # exactly two
text, n = args
assert not text.isdigit(), "the arguments are bad" # S must be text, not a number
assert n.isdigit(), "the arguments are bad"         # N must be an integer
n = int(n)
```

Why `isdigit()`? Every `argv` value is a **string**, so the real questions are "is S a number by
mistake?" and "is N actually an integer?". `"3".isdigit()` is `True` (→ rejects S=`3`);
`"Hello the World".isdigit()` is `False`; `"4".isdigit()` is `True`.

**Then filter the words** using a list comprehension + a lambda + `ft_filter`:

```python
words = [word for word in text.split(" ")]              # list comprehension (required)
print(ft_filter(lambda word: len(word) > n, words))     # lambda (required) + reuse Part 1
```

`text.split(" ")` breaks the string into words; `ft_filter` keeps those longer than `n`; `print`
shows the resulting list.

---

## Putting it together

**`ft_filter.py`** (Option B shown — swap in Option A if you prefer no `# noqa`):
```python
def ft_filter(function, iterable):
    """Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""  # noqa: E501
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]
```

**`filterstring.py`:**
```python
import sys
from ft_filter import ft_filter


def main():
    """Print the words of the first argument longer than the second (an int)."""
    try:
        args = sys.argv[1:]
        assert len(args) == 2, "the arguments are bad"
        text, n = args
        assert not text.isdigit(), "the arguments are bad"
        assert n.isdigit(), "the arguments are bad"
        n = int(n)
        words = [word for word in text.split(" ")]
        print(ft_filter(lambda word: len(word) > n, words))
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
```

(Validated: `ft_filter` matches the built-in's behavior and `__doc__`; `filterstring.py` passes
all four subject cases; both are pycodestyle/flake8-clean.)

---

## How it applies to ex06

- **Part 1** → `ft_filter` = list comprehension, with the `function is None` special case;
  returns a list; never calls the real `filter`.
- **Docstring** → copy `filter.__doc__` exactly; dodge `E501` with concatenation or `# noqa`.
- **Part 2** → validate (`len == 2`, S not numeric, N is int) → `AssertionError: the arguments
  are bad`; `split` into words; `ft_filter(lambda w: len(w) > n, words)`; print the list.
- **Reuse** → Part 2 imports and uses your Part 1 `ft_filter`.
- **Norm** → both files flake8-clean, every function has a docstring, `main()` + `if __name__`.
