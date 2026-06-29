# ex00 — Lessons: `list`, `tuple`, `set`, `dict`

Exercise 00 starts with four built-in collections and asks you to **modify each one** so it
prints a greeting. The whole exercise is really a lesson about **mutability**: which objects
you can change in place, and *how* you change each kind.

The starting objects in [Hello.py](Hello.py):

```python
ft_list  = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set   = {"Hello", "tutu!"}
ft_dict  = {"Hello": "titi!"}
```

Target greetings (mapped to the 42 Antananarivo campus):

| Object     | Becomes                        | Means        |
|------------|--------------------------------|--------------|
| `ft_list`  | `['Hello', 'World!']`          | "World"      |
| `ft_tuple` | `('Hello', 'Madagascar!')`     | country      |
| `ft_set`   | `{'Hello', 'Antananarivo!'}`   | city         |
| `ft_dict`  | `{'Hello': '42Antananarivo!'}` | campus name  |

---

## 1. `list` — ordered, indexed, **mutable**

A list is an **ordered** sequence written with square brackets `[]`. Items are reached by
**index** (starting at `0`), duplicates are allowed, and the list can be **changed in place**.

Because it is mutable and indexable, you simply assign a new value to the position you want:

```python
ft_list = ["Hello", "tata!"]
ft_list[1] = "World!"          # replace item at index 1
# -> ['Hello', 'World!']
```

---

## 2. `tuple` — ordered, indexed, **immutable**

A tuple looks like a list but uses parentheses `()` and is **immutable** — once created you
**cannot** change an item. This fails:

```python
ft_tuple = ("Hello", "toto!")
ft_tuple[1] = "Madagascar!"    # ❌ TypeError: 'tuple' object does not support item assignment
```

Instead you build a **new** tuple from the parts you keep, using **slicing** and
**concatenation**:

```python
ft_tuple = ft_tuple[:1] + ("Madagascar!",)
# ft_tuple[:1] -> ('Hello',)   keeps the first item
# ("Madagascar!",) -> a 1-element tuple (the trailing comma is required!)
# -> ('Hello', 'Madagascar!')
```

> ⚠️ `("Madagascar!")` is just a string in parentheses. A one-element tuple **needs the
> trailing comma**: `("Madagascar!",)`.

---

## 3. `set` — **unordered**, no duplicates, **mutable**

A set uses curly braces `{}` with values only. It is **unordered** and stores **no
duplicates**, so there is **no index** — `ft_set[0]` is an error. It *is* mutable, but you
change it with methods, not by position: remove the old value and add the new one.

```python
ft_set = {"Hello", "tutu!"}
ft_set.discard("tutu!")        # remove (discard = no error if missing; remove = raises if missing)
ft_set.add("Antananarivo!")    # add the new value
# -> {'Hello', 'Antananarivo!'}   (print order may vary — sets are unordered)
```

> ⚠️ `{}` on its own creates an **empty dict**, not an empty set. Use `set()` for an empty set.

---

## 4. `dict` — key → value pairs, **mutable**

A dict stores **key → value** pairs in curly braces `{key: value}`. Keys are **unique**, and
the dict is **mutable**: assigning to a key updates it if it exists, or inserts it if it does
not.

```python
ft_dict = {"Hello": "titi!"}
ft_dict["Hello"] = "42Antananarivo!"   # update the value for key "Hello"
# -> {'Hello': '42Antananarivo!'}
```

---

## Quick comparison

| Type    | Syntax        | Ordered | Indexable | Mutable | Duplicates |
|---------|---------------|:-------:|:---------:|:-------:|:----------:|
| `list`  | `[a, b]`      | ✅      | ✅        | ✅      | ✅         |
| `tuple` | `(a, b)`      | ✅      | ✅        | ❌      | ✅         |
| `set`   | `{a, b}`      | ❌      | ❌        | ✅      | ❌         |
| `dict`  | `{k: v}`      | ✅\*    | by key    | ✅      | unique keys |

\* Since Python 3.7, dicts keep insertion order.

---

## How it applies to ex00

- **list** → mutable + indexed → assign by index: `ft_list[1] = "World!"`
- **tuple** → immutable → rebuild with slicing: `ft_tuple = ft_tuple[:1] + ("Madagascar!",)`
- **set** → no index → `discard()` then `add()`: replace `"tutu!"` with `"Antananarivo!"`
- **dict** → mutable → assign by key: `ft_dict["Hello"] = "42Antananarivo!"`

The right modification technique follows directly from each type's properties — that is the
real takeaway of Exercise 00.
