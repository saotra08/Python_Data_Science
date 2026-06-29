# ex03 — Lessons: "Null" values, types & truthiness traps

Exercise 03 ("NULL not found") asks you to write a function that recognises **every kind of
"Null"-like value** in Python, prints its type, and returns **0 on success / 1 on error**. The
file `NULL_not_found.py` only *defines* the function — the provided `tester.py` calls it.

Prototype (from the subject):
```python
def NULL_not_found(object: any) -> int:
    # your code here
```

Target output (`python tester.py | cat -e`):
```
Nothing: None <class 'NoneType'>$
Cheese: nan <class 'float'>$
Zero: 0 <class 'int'>$
Empty:  <class 'str'>$
Fake: False <class 'bool'>$
Type not Found$
1$
```

This is the trickiest exercise so far — it's a tour of Python's type and truthiness gotchas.

---

## 1. The five "Null" values

Each "empty/nothing" value has a **different type** and a **fixed label** to print:

| Value          | `type(...)`        | Label     |
|----------------|--------------------|-----------|
| `None`         | `NoneType`         | `Nothing` |
| `float("NaN")` | `float`            | `Cheese`  |
| `0`            | `int`              | `Zero`    |
| `""`           | `str`              | `Empty`   |
| `False`        | `bool`             | `Fake`    |

Anything else → `Type not Found` and return `1`.

---

## 2. Detecting `None` — use `is`, not `==`

`None` is a **singleton** (there is exactly one `None` in the whole program), so test it by
**identity**:

```python
if object is None:
    print(f"Nothing: {object} {type(object)}")
```

`object is None` is the idiomatic, reliable check. (`== None` usually works too, but `is` is the
correct tool for singletons.)

---

## 3. The bool-vs-int trap

In Python, **`bool` is a subclass of `int`**, and `False` behaves like `0`:

```python
False == 0              # True
isinstance(False, int)  # True   ← would wrongly match False as an int
type(False) == int      # False  ← exact type tells them apart
type(0) == bool         # False
```

So to separate `0` from `False`, you **must** use `type(x) == int` / `type(x) == bool` — never
`isinstance` here. (This is the warning from the ex02 lesson, now biting for real.)

---

## 4. NaN — the odd one out

`float("NaN")` ("not a number") breaks the usual rules:

```python
nan = float("NaN")
nan == nan    # False  ← NaN is the only value not equal to itself!
bool(nan)     # True   ← NaN is TRUTHY, unlike the other Null values
```

Because of this, neither `==` nor truthiness can find it. The classic detection is its
self-inequality:

```python
elif type(object) == float and object != object:   # only NaN satisfies object != object
    print(f"Cheese: {object} {type(object)}")
```

---

## 5. The real trap: check the *value*, not just the type

Only the **empty** string is "Null" — `"Brian"` is a perfectly normal `str` and must fall
through to `Type not Found`. If you branch on type alone:

```python
elif type(object) == str:                 # ❌ catches "Brian" too!
    print(f"Empty: {object} ...")         #    -> prints 'Empty: Brian', returns 0  (WRONG)
```

So every branch must also test the **null value**:

```python
elif type(object) == str and object == "":    # ✅ only the empty string
    ...
elif type(object) == int and object == 0:     # ✅ only zero, not 5
    ...
```

This is exactly what the tester's `"Brian"` case is there to catch.

---

## 6. Falsy vs truthy — why `if not object` isn't enough

`None`, `0`, `""`, `False` are all **falsy**… but `NaN` is **truthy**:

```python
bool(None), bool(0), bool(""), bool(False)   # all False
bool(float("nan"))                           # True  ← missed by `if not object`
```

So a single `if not object` would skip NaN *and* couldn't tell the five types apart anyway.
ex03 is about **types + specific values**, not plain truthiness.

---

## 7. Formatting & return value

```python
f"Nothing: {object} {type(object)}"     # 'Nothing: None <class 'NoneType'>'
f"Empty: {object} {type(object)}"       # 'Empty:  <class 'str'>'  ← {object} is "" → two spaces
"Type not Found"                        # ⚠️ capital F  (ex02 used lowercase 'Type not found')
```

- Recognised Null → `print(...)` then `return 0`.
- Anything else → `print("Type not Found")` then `return 1`.

The tester wraps only the last call in `print(...)`, which is why the `1` shows up:
```python
print(NULL_not_found("Brian"))   # function prints 'Type not Found', then this prints 1
```

---

## How it applies to ex03

- **None** → `object is None`.
- **NaN** → `type == float and object != object` (NaN is truthy and `!=` itself).
- **0 vs False** → exact `type(x) == int` / `type(x) == bool` (bool is a subclass of int).
- **"" vs "Brian"** → check the *value* (`object == ""`), not just the type.
- **Unknown** → `print("Type not Found")` (capital F!) and `return 1`; otherwise `return 0`.
- ex03 is still a plain module — `main()`/docstrings/flake8 only become required at **ex05** —
  but the docstring above is good practice for what's coming.
