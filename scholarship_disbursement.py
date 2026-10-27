"""Manage scholarship disbursement records."""

import sqlite3


conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE awards ("
    "id INTEGER PRIMARY KEY, "
    "student TEXT, "
    "scheme TEXT, "
    "amount INTEGER, "
    "disbursed INTEGER)"
)
DISBURSED_TOTAL = 0


def grant(student, scheme, amount, audit=None):
    """Grant a scholarship and record the student in the audit list."""
    if audit is None:
        audit = []
    conn.execute(
        "INSERT INTO awards (student, scheme, amount, disbursed) "
        "VALUES (?, ?, ?, 0)",
        (student, scheme, amount),
    )
    audit.append(student)
    return audit


def disburse(award_id):
    """Disburse a scholarship award."""
    row = conn.execute(
        "SELECT amount FROM awards WHERE id = ?", (award_id,)
    ).fetchone()

    if row:
        conn.execute(
            "UPDATE awards SET disbursed = 1 WHERE id = ?", (award_id,)
        )
        return row[0]
    return None


def archive():
    """Archive scholarship awards."""
    print("archiving awards")


def by_scheme_count(scheme):
    """Return the number of awards for a scheme."""
    if scheme is None:
        return 0
    return conn.execute(
        "SELECT COUNT(*) FROM awards WHERE scheme = ?",
        (scheme,),
    ).fetchone()[0]


def main():
    """Run the scholarship disbursement example."""
    grant("Ishaan", "Merit", 50000)
    grant("Divya", "Need-based", 75000)
    print(disburse(1), disburse(9))
    disbursed_total = conn.execute(
        "SELECT COALESCE(SUM(amount), 0) FROM awards WHERE disbursed = 1"
    ).fetchone()[0]
    print(by_scheme_count("Merit"), disbursed_total)
    archive()


main()
