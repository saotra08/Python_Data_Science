# ex01 — Lessons: first use of a package + string formatting

Exercise 01 ("First use of package") asks you to **import a date package** and **format two
pieces of text** exactly like the subject's example. Your numbers/date will differ from the
example — only the **format** must match.

Target output (`python format_ft_time.py | cat -e`):

```
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
Oct 21 2022$
```

Two skills are tested here:
1. Getting the current time from a **package** (`time` or `datetime`).
2. The **format-spec mini-language** (thousands separators, fixed decimals, scientific
   notation, date codes).

---

## 1. Importing a package (explicit imports)

The general rules require **explicit** imports — never `from x import *`:

```python
import time                       # then use time.time(), time.strftime()
from datetime import datetime     # then use datetime.now()
```

Both are allowed for ex01 ("Allowed functions: `time`, `datetime` or any other library that
allows to receive the date").

---

## 2. Seconds since the epoch — `time.time()`

The **epoch** is the reference instant **January 1, 1970, 00:00:00 UTC**. `time.time()` returns
the number of **seconds since the epoch** as a `float`:

```python
import time
seconds = time.time()      # e.g. 1666355857.3622
```

That single float feeds **both** numbers on line 1 — the only difference is how you *format* it.

---

## 3. The format-spec mini-language

Inside an f-string, the part after the `:` is the **format spec**: `f"{value:SPEC}"`.

| Spec        | Meaning                                  | `1666355857.3622` →    |
|-------------|------------------------------------------|------------------------|
| `,`         | thousands separator                      | `1,666,355,857.3622`\* |
| `.4f`       | fixed-point, 4 decimals                  | `1666355857.3622`      |
| `,.4f`      | thousands separator **and** 4 decimals   | `1,666,355,857.3622`   |
| `.2e`       | scientific notation, 2 decimals          | `1.67e+09`             |

\* `,` alone keeps the raw decimals; combine it with `.4f` to pin the decimals too.

So the two numbers on line 1 come from the **same value** with two different specs:

```python
f"{seconds:,.4f}"   # -> '1,666,355,857.3622'
f"{seconds:.2e}"    # -> '1.67e+09'
```

---

## 4. Formatting the date — `strftime`

`strftime` ("string-format-time") turns a date into text using **format codes**:

```python
from datetime import datetime
datetime.now().strftime("%b %d %Y")     # -> 'Oct 21 2022'
# or, with the time module:
import time
time.strftime("%b %d %Y")               # -> 'Oct 21 2022'
```

| Code | Meaning                        | Example |
|------|--------------------------------|---------|
| `%b` | abbreviated month name         | `Oct`   |
| `%d` | day of month, zero-padded      | `21`    |
| `%Y` | year, 4 digits                 | `2022`  |

> ⚠️ Codes are case-sensitive: `%Y` = 4-digit year (`2022`), `%y` = 2-digit year (`22`);
> `%b` = `Oct`, `%B` = `October`, `%m` = `10`.

---

## Putting it together

Each piece of the expected output maps to one tool:

```python
import time
from datetime import datetime

seconds = time.time()
print(f"Seconds since January 1, 1970: {seconds:,.4f} "
      f"or {seconds:.2e} in scientific notation")
print(datetime.now().strftime("%b %d %Y"))
```

- `{seconds:,.4f}` → `1,666,355,857.3622`  (commas + 4 decimals)
- `{seconds:.2e}` → `1.67e+09`  (scientific, 2 decimals)
- `strftime("%b %d %Y")` → `Oct 21 2022`

---

## How it applies to ex01

- **Package use** → `import time` / `from datetime import datetime` (explicit imports).
- **Line 1** → one `time.time()` float, formatted two ways with `,.4f` and `.2e`.
- **Line 2** → today's date via `strftime("%b %d %Y")`.
- ex01 is still a simple script — `main()`, docstrings, and flake8 only become required from
  **ex05**.
