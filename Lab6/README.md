# Lab 6 — Python Dictionaries, CRUD Applications and Analysis

## Overview
This lab uses dictionaries to build small console applications and understand dictionary behaviour. The five programs keep their data in memory while they run.

## Program index
| File | Application | Main concepts |
|---|---|---|
| `pythonLabQ1.py` | Student marks manager | Nested dictionaries, CRUD, averages and toppers |
| `pythonLabQ2.py` | Employee payroll | Department grouping, salary reports and comprehensions |
| `pythonLabQ3.py` | Library lending | Inventory, borrower lists, `setdefault()` and reports |
| `pythonLabQ4.py` | Word frequency analyser | Normalization, `.get()` and frequency grouping |
| `pythonLabQ5.py` | Contact directory | Validation, reverse index and O(1) average lookup |
| `SectionB.txt` | Output tracing | Aliasing, copying, hash collisions and safe iteration |
| `SectionC.txt` | Theory | Dictionary operations, hashability and complexity |

## Run a program
From this directory, run one file at a time:
```bash
python pythonLabQ1.py
python pythonLabQ2.py
python pythonLabQ3.py
python pythonLabQ4.py
python pythonLabQ5.py
```

## Implementation notes
- Q1 stores each student under a roll-number key and groups marks by subject.
- Q2 stores employee details under employee IDs and creates department-level reports.
- Q3 tracks total copies, available copies and current borrowers for each ISBN.
- Q4 removes punctuation and normalizes words to lowercase before counting.
- Q5 maintains a separate phone-number index so reverse lookup is average O(1).

## Limitations
These are educational console programs. Data is held in memory and is not saved after the program exits. A real application would add persistent storage, authentication and stronger validation.
