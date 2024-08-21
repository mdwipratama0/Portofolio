CREATE TABLE DimDate(
    dateid INTEGER PRIMARY KEY NOT NULL,
    date DATE NOT NULL,
    year INTEGER NOT NULL,
    quarter INTEGER NOT NULL,
    quarter_name VARCHAR(2) NOT NULL,
    month INTEGER NOT NULL,
    month_name VARCHAR(10),
    day INTEGER NOT NULL,
    weekday VARCHAR(20),
    weekday_name VARCHAR(20)
);

