# Piscine Python for Data Science — 0: Starting

> Training Piscine Python for Data Science — Module 0
> **Version:** 1.3
> **Summary:** Learn the basics of the Python programming language.

This module introduces Python fundamentals (data structures, functions, types,
arguments, generators, packaging) through ten short exercises, `ex00` → `ex09`.
The full assignment is in [en.subject.pdf](en.subject.pdf).

---

## Project Status

🟢 **In progress — 6 / 10 exercises complete.**

| Ex     | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 |
|--------|----|----|----|----|----|----|----|----|----|----|
| Status | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | ⬜ |

- ✅ **ex00** — complete; `Hello.py` tested, output matches `ex00_test.input` and conforms to the subject.
- ✅ **ex01** — complete; `format_ft_time.py` tested, output matches the required format and conforms to the subject.
- ✅ **ex02** — complete; `find_ft_type.py` tested against `tester.py`, output matches the subject byte-for-byte.
- ✅ **ex03** — complete; `NULL_not_found.py` tested against `tester.py`; all Null types detected (returns 0/1) and conforms to the subject.
- ✅ **ex04** — complete; `whatis.py` tested across all six argument cases (odd/even, no-arg, AssertionErrors) and conforms to the subject.
- ✅ **ex05** — complete; `building.py` tested (arg, no-arg prompt, too-many-args) and **flake8/pycodestyle-clean** with docstrings — first norm-graded exercise.
- ⬜ **ex06 – ex09** — not started yet.

---

## General rules

- Use **Python 3.10**.
- Imports must be **explicit** — e.g. `import numpy as np`. Using
  `from pandas import *` is forbidden and scores **0** for that exercise.
- **No global variables.**
- Your code must never terminate unexpectedly (segfault, uncaught crash, etc.),
  except where the exercise asks you to handle an error.
- Only the work committed to your **Git repository** is graded.
- You may use any built-in function unless an exercise explicitly forbids it.
- Writing test programs is encouraged but they are **not submitted or graded**.

## Additional rules (apply from ex05 onward)

- **No code in the global scope** — wrap logic in functions, with a `main()`:
  ```python
  def main():
      # your tests and your error handling
      ...

  if __name__ == "__main__":
      main()
  ```
- Any **uncaught exception** invalidates the exercise.
- Every function must have **documentation** (a `__doc__` docstring).
- Code must follow the norm — `pip install flake8` (`alias norminette=flake8`).

---

## Exercises

| Ex | Directory | Files to turn in | Goal |
|----|-----------|------------------|------|
| 00 | `ex00/` | `Hello.py` | Modify the contents of a list/tuple/set/dict to print greetings. |
| 01 | `ex01/` | `format_ft_time.py` | Format the current date: seconds since epoch (with thousands separators + scientific notation) and `Oct 21 2022` style. |
| 02 | `ex02/` | `find_ft_type.py` | `all_thing_is_obj(object)` prints each object's type and returns `42`. |
| 03 | `ex03/` | `NULL_not_found.py` | `NULL_not_found(object)` prints the type of "Null"-like values; returns `0` on success, `1` on error. |
| 04 | `ex04/` | `whatis.py` | Take one integer argument and print `Odd`/`Even`; raise `AssertionError` on bad input. |
| 05 | `ex05/` | `building.py` | Count upper/lower/punctuation/digit/space characters in a string argument. |
| 06 | `ex06/` | `ft_filter.py`, `filterstring.py` | Recode `filter` with a list comprehension; then filter words of a string by length `> N` using a `lambda`. |
| 07 | `ex07/` | `sos.py` | Encode a string into Morse code using a dictionary (`.`/`-`, words separated by `/`). |
| 08 | `ex08/` | `Loading.py` | `ft_tqdm(lst)` — reimplement a `tqdm`-style progress bar with the `yield` operator. |
| 09 | `ex09/` | `*.py`, `*.txt`, `*.toml`, `README.md`, `LICENSE` | Build your first pip-installable package (`ft_package`) exposing `count_in_list`. |

### Allowed functions per exercise

- **ex00 / ex02 / ex03:** `None`
- **ex01:** `time`, `datetime`, or any library that provides the date
- **ex04 / ex05 / ex06 / ex07:** `sys` or any library to read the args
- **ex08:** `os`
- **ex09:** PyPI or any package-creation library

---

## Submission

Turn in your work via the **Git** repository as usual — only what is inside the
repository is evaluated during the defense. Double-check folder and file names.
The evaluation runs on the evaluated group's computer.
