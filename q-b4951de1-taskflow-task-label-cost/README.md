# TaskFlow: Task Label & Cost

## Turn task facts into a label and a cost

A task already has its facts filled in. Your job is to combine them into two new values: a readable board label and the billable cost so far. These fixed facts are already assigned for you:

- `task_id = 42`
- `title = "Ship v2"`
- `hourly_rate = 80.0`
- `hours_logged = 3.5`

### A quick example

```python
a = 3
b = 4.0
product = a * b              # 12.0
line = f"Task #{a}: hello"   # "Task #3: hello"
```

An **f-string** (the `f"..."` form) drops a variable's value into text wherever you put `{...}`, and `*` multiplies numbers. You'll build `label` and `cost` the same way — with only variables, arithmetic, and an f-string.

**Concepts you'll use:** variables, arithmetic (`*`), f-strings.

### What to define
- `label` — a string built with an f-string in the form `Task #<id>: <title>`, i.e. `"Task #42: Ship v2"`.
- `cost` — the billable cost so far as a float: `hours_logged * hourly_rate`.

### What the grader checks
- `label` → `"Task #42: Ship v2"`
- `cost` → `280.0`

Do NOT use functions, dictionaries, lists, loops, or conditionals — just top-level statements.

<!--LL-ATTEMPT-->
---

## How to attempt this

1. Open the assignment from your course page. Write your answer **in the code editor on the
   right** — there is no file to create and nothing to name. Create the variables at the top
   level, not inside a function.
2. Click **Run Tests** to grade it. The visible tests run first so you can see where you stand.
3. Read any failure carefully: it shows the **input**, what was **expected**, and what your code
   **actually returned**. That three-way comparison is usually enough to find the bug.
4. Re-run as often as you like. Each value is scored separately, so a partly-correct answer still
   earns marks — submit something rather than nothing.
5. When you are satisfied, **Submit**.

> **Runtime:** your code is graded on **Python 3.9**, which may be
> older than the Python in your editor. Avoid `match` statements and `int | None` style unions
> in annotations — they run fine locally and fail on the grader. Plain `def f(x):` and
> `typing.Optional[int]` are always safe.
>
> **This question is graded on your VARIABLES, not on a function.** Create each name at the top
> level of the editor — `task_id = 101` — and the grader reads its value directly. Printing them
> as well is fine and often asked for, but printing is not what is marked: the variable has to
> exist with the right value.

---
Edit **main.py** in this folder. **Run Test** (in the platform) grades it.
