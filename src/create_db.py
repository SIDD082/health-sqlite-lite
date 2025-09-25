import sqlite3
from pathlib import Path

# Get the absolute path of the script's directory
SCRIPT_DIR = Path(__file__).parent.parent.absolute()

# Define paths relative to the script directory
DB_PATH = SCRIPT_DIR / "clinic_simple.db"
CSV_PATH = SCRIPT_DIR / "data" / "patients.csv"
SCHEMA_PATH = SCRIPT_DIR / "sql" / "schema.sql"

def main():
    # Read the schema SQL file
    schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")

    # Create (or overwrite) the database and apply the schema.
    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript(schema_sql)
        conn.commit()

    print(f"Created database: {DB_PATH}")

if __name__ == "__main__":
    main()