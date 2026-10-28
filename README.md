# Messy Python Code Improvement

A messy Python script, improved with AI assistance (Cursor AI).

## Files
- `messy_script.py` - the original messy code
- `improved_script.py` - the cleaned-up version

## What was improved
| Problem in the original | Fix in the improved version |
|---|---|
| One-letter names (`d`, `t`, `a`) | Clear names like `students`, `marks`, `average` |
| Index loops (`range(len(d))`, `d[i][1]`) | Direct looping: `for name, marks in STUDENTS` |
| Manual sum with a running total | Built-in `sum()` |
| Deeply nested `if/else` | Flat `if` checks inside a `get_grade()` function |
| Everything at top level | Small functions and a `main()` |
| No docstrings or formatting | Docstrings and formatted output (2 decimal places) |

Both versions give the same grades for the same data.

## How to run
`python improved_script.py`

## Technologies
Python 3, Cursor AI

## Author
Aditya Bansal - [GitHub](https://github.com/aditya3-1-0-8)
