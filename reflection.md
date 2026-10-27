# Lab 5: Static Code Analysis — Reflection

## 1. What did you learn from static code analysis?

I learned that static code analysis helps identify code quality, style, and security problems without executing the program. Pylint checks code quality and programming practices, Bandit detects common security risks, and Flake8 identifies style violations and formatting issues. Using all three tools helped me improve the reliability and readability of my Python program.

## 2. What were the main issues found in the original program?

The original program had several issues, including a possible SQL injection vulnerability, an unsafe shell command, a mutable default argument, unnecessary global variable usage, inconsistent return values, and formatting problems. These issues could affect security, maintainability, and the correctness of the program.

## 3. How did you fix the issues identified by the tools?

I replaced SQL string formatting with parameterized queries to reduce SQL injection risk. I changed the mutable default argument to `None` and initialized the list inside the function. I replaced the shell command with a direct `print()` statement, removed the global disbursement counter, and calculated the total disbursed amount from the database. I also improved function naming, return values, and code formatting.

## 4. What did you learn from the results before and after fixing the code?

The analysis results improved significantly after the fixes. The final program achieved a Pylint score of 10.00/10, Bandit reported no issues, and Flake8 reported no style violations. I learned that static analysis tools complement one another and that small improvements can make code safer, cleaner, and easier to maintain. I also learned that passing these tools does not guarantee that a program is completely free of bugs, so testing and careful review are still important.
