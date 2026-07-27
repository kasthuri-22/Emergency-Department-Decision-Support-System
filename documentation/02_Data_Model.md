# Data Model

The solution follows a Star Schema to support efficient analytical queries.

## Fact Table

- Fact_Emergency_Visit

## Dimension Tables

- Dim_Patient
- Dim_Doctor
- Dim_Department
- Dim_Date
- Dim_Diagnosis

## Relationships

Each dimension table maintains a one-to-many relationship with the fact table.

<img width="1366" height="768" alt="Screenshot (20)" src="https://github.com/user-attachments/assets/fdcf0003-3af5-4d4c-840b-e7d3e9ebdb35" />
