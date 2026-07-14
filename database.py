import sqlite3


DATABASE_NAME = "interview_history.db"


def create_database():
    """
    Create the interview history database.
    """
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interviews(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        candidate_name TEXT,
        job_role TEXT,
        interview_type TEXT,
        company TEXT,
        overall_score REAL,
        performance TEXT,
        interview_date DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    connection.commit()
    connection.close()

def save_interview(
        candidate_name,
        job_role,
        interview_type,
        company,
        overall_score,
        performance
):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO interviews(
        candidate_name,
        job_role,
        interview_type,
        company,
        overall_score,
        performance
    )
    VALUES(?,?,?,?,?,?)

    """,
    (
        candidate_name,
        job_role,
        interview_type,
        company,
        overall_score,
        performance
    ))
    connection.commit()
    connection.close()

def get_all_interviews():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute("""
    SELECT *
    FROM interviews
    ORDER BY interview_date DESC
    """)
    rows = cursor.fetchall()
    connection.close()
    return rows