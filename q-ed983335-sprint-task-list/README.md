# Sprint task list

## Store the sprint's tasks in a list

A **list** holds many values in order, which makes it perfect for the sprint's task titles. You'll build the list, then pull a few facts out of it. The sprint has exactly four tasks, in this order:

1. `"Design login page"`
2. `"Write API tests"`
3. `"Fix payment bug"`
4. `"Deploy release"`

### A quick example

```python
colors = ["red", "green", "blue"]
colors[0]            # "red"   (first item, index 0)
colors[-1]           # "blue"  (last item)
len(colors)          # 3
"green" in colors    # True
```

Indexing reads one item by position, `len` counts them, and `in` checks membership. You'll use those same four tools below — no functions needed.

**Concepts you'll use:** lists, indexing (`[0]`, `[-1]`), `len()`, membership (`in`), booleans.

### What to define
- `task_titles` — a **list** of the four titles above, in the given order.
- `first_task` — the first title in the list (use indexing).
- `last_task` — the last title in the list (use indexing, e.g. `[-1]`).
- `task_count` — how many titles are in the list (use `len`).
- `has_deploy` — a **bool**: is `"Deploy release"` in the list? (use `in`).

### What the grader checks
- `first_task` → `Design login page`
- `task_count` → `4`
- `has_deploy` → `True`

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

> **Runtime:** your code is graded on **Python 3.11**, the same version as the Python in your editor. Modern syntax is fine — `match` statements and `int | None` unions in annotations both work.
>
> **This question is graded on your VARIABLES, not on a function.** Create each name at the top
> level of the editor — `task_id = 101` — and the grader reads its value directly. Printing them
> as well is fine and often asked for, but printing is not what is marked: the variable has to
> exist with the right value.

---
Edit **main.py** in this folder. **Run Test** (in the platform) grades it.
