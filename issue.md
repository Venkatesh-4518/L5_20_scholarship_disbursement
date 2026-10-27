# Static Code Analysis — Issues Report

## Scholarship Disbursement Ledger

The initial version of `scholarship_disbursement.py` was analysed using Pylint, Bandit, and Flake8. The following issues were identified and addressed.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| SQL injection risk | Medium — Security | 10 | SQL query used string formatting to insert student and scheme values directly into the query. | Replaced string formatting with parameterized SQL using `?` placeholders. |
| Unsafe shell command | Low — Security | 26 | `os.system()` launched a shell command even though the operation only printed a message. | Replaced the shell command with a direct `print()` call. |
| Mutable default argument | Code Quality | 9 | The default argument `audit=[]` could share the same list between function calls. | Changed the default to `None` and created a new list inside the function when needed. |
| Global variable usage | Code Quality | 16 | The `global` statement made the disbursement total dependent on mutable global state. | Removed the global counter update and calculated the disbursed total from the database. |
| Inconsistent return statements | Code Quality | 15–21 | `disburse()` returned an amount when an award existed but returned nothing when it did not. | Added an explicit `return None` when the award is not found. |
| Incorrect comparison with `None` | Code Quality | 31 | The expression `scheme == None` did not follow Python's recommended identity comparison style. | Changed it to `scheme is None`. |
| Inconsistent function naming | Style | 30, 40 | `bySchemeCount()` did not follow Python's snake_case naming convention. | Renamed it to `by_scheme_count()` and updated its call. |
| Long lines and formatting problems | Style | 5, 10, 32 | Long SQL statements and inconsistent formatting made the code harder to read and triggered Flake8/Pylint warnings. | Split SQL statements across multiple lines and corrected indentation and whitespace. |

## Verification

After making the changes, the program was executed again and the three analysis tools were rerun.

- **Pylint:** 10.00/10.
- **Bandit:** No issues identified.
- **Flake8:** No style violations reported.

The program continued to execute successfully after the fixes.
