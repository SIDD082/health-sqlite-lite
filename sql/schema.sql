DROP TABLE IF EXISTS patients;
 
CREATE TABLE patients (

    patient_id     TEXT PRIMARY KEY,   -- P0001, P0002, etc.

    birth_date     DATE,               -- YYYY-MM-DD

    primary_icd10  TEXT,               -- ICD-10 diagnosis code

    last_cpt       TEXT,               -- CPT procedure code

    last_visit_dt  DATE                -- last visit date

);

 