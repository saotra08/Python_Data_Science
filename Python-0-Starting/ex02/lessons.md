# ex02 — Lessons: your first function + `type()`

Exercise 02 ("First function python") asks you to write **one function** that **prints an
object's type** and **returns `42`**. The file `find_ft_type.py` only *defines* the function —
the provided `tester.py` imports and calls it.

Prototype (from the subject):
```python
def all_thing_is_obj(object: any) -> int:
    # your code here
```

Target output when running `python tester.py | cat -e`:
```
List : <class 'list'>$
Tuple : <class 'tuple'>$
Set : <class 'set'>$
Dict : <class 'dict'>$
Brian is in the kitchen : <class 'str'>$
Toto is in the kitchen : <class 'str'>$
Type not found$
42$
```

> ℹ️ "Running your function alone does nothing." `python find_ft_type.py` prints **nothing** —
> the file just *defines* `all_thing_is_obj`; nothing calls it. The output above comes from
> `tester.py`.

---

## 1. Defining a function

```python
def all_thing_is_obj(object: any) -> int:   # name, parameter, return-type hint
    print("...")                             # body (indented)
    return 42                                # hands a value back to the caller
```

- `def` starts the definition; the body is the indented block.
- `object` is the **parameter** — the value passed in when the function is called.
- The hints `object: any` and `-> int` are **annotations only**: Python does **not** enforce
  them at runtime. Keep the subject's prototype exactly as written (yes, even the parameter
  name `object`, which technically shadows the built-in `object`).

---

## 2. The `type()` built-in

`type(x)` returns the **type object** of `x`. Printing it shows `<class '...'>`:

| Expression     | `type(...)` prints   |
|----------------|----------------------|
| `type([])`     | `<class 'list'>`     |
| `type(())`     | `<class 'tuple'>`    |
| `type(set())`  | `<class 'set'>`      |
| `type({})`     | `<class 'dict'>`  ← `{}` is a **dict**, not a set |
| `type("hi")`   | `<class 'str'>`      |
| `type(10)`     | `<class 'int'>`      |

That `<class 'str'>` text is exactly what the expected output prints — so you can drop
`type(object)` straight into an f-string.

---

## 3. Comparing a type — `type(x) == T` vs `isinstance`

Two ways to test what something is:

```python
type(object) == list          # exact type match
isinstance(object, list)      # True for list AND any subclass of list
```

> ⚠️ `isinstance` counts subclasses, and in Python **`bool` is a subclass of `int`**:
> `isinstance(True, int)` → `True`, while `type(True) == int` → `False`.
> For this kind of "report the exact type" task, `type(x) == T` is the precise check.
> (You'll feel this difference in ex03, where `False` must be told apart from `0`.)

---

## 4. Branching with `if / elif / else`

Route each type to the right line, with a catch-all default:

```python
if type(object) == list:
    ...
elif type(object) == tuple:
    ...
elif type(object) == str:
    ...
else:
    print("Type not found")
```

Only **one** branch runs. The first matching `elif` wins; `else` handles anything not listed
(that's where `10` lands → `Type not found`).

---

## 5. Exact formatting (mind the spaces!)

The grader compares text literally, so spacing matters:

```python
f"List : {type(object)}"                          # 'List : <class 'list'>'   (space-colon-space)
f"{object} is in the kitchen : {type(object)}"    # 'Brian is in the kitchen : <class 'str'>'
"Type not found"                                  # no type, no colon
```

The **string** case is special: it prints the **value** of the object (`Brian`, `Toto`), not a
fixed label.

---

## 6. Return vs print

```python
return 42
```

`return` hands a value back to whoever called the function — it does **not** print. That's why
the tester wraps the last call in `print(...)`:

```python
print(all_thing_is_obj(10))   # the function prints "Type not found", then this prints 42
```

The first six calls aren't wrapped in `print`, so their returned `42` is silently discarded —
only what the function itself prints shows up.

---

## Putting it together

```python
def all_thing_is_obj(object: any) -> int:
    """Print the type of the given object and return 42."""
    if type(object) == list:
        print(f"List : {type(object)}")
    elif type(object) == tuple:
        print(f"Tuple : {type(object)}")
    elif type(object) == set:
        print(f"Set : {type(object)}")
    elif type(object) == dict:
        print(f"Dict : {type(object)}")
    elif type(object) == str:
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print("Type not found")
    return 42
```

Each branch maps to one line of the expected output; the final `return 42` is what
`print(all_thing_is_obj(10))` displays.

---

## How it applies to ex02

- **First function** → `def ... -> int:` with a parameter and a `return`.
- **Print the types** → `type(object)` inside f-strings, one `if/elif` branch per type.
- **str is special** → print the value + `is in the kitchen`.
- **Unknown types** → `else: print("Type not found")`.
- **Return 42** → returning ≠ printing; the tester's `print(...)` reveals it.
- ex02 is still a plain module (no `main()` required until ex05), but the `__doc__` docstring
  shown above is harmless and good practice for what's coming.
