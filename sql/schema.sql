CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    diagnosis TEXT,
    admission_date DATE
);
