CREATE TABLE IF NOT EXISTS Products (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Code TEXT NOT NULL,
    Name TEXT NOT NULL,
    Price NUMERIC NOT NULL,
    Entry_date TEXT NOT NULL,
    Brand TEXT
);

INSERT INTO Products (Code, Name, Price, Entry_date, Brand)
VALUES
    ('0001', 'Spoon', 2.99, '2026-01-01', 'Spoon_brand'),
    ('0010', 'Phone', 999, '2026-01-02', 'Apple'),
    ('0011', 'Keyboard', 139, '2026-01-03', 'Razer'),
    ('0100', 'Mouse', 119, '2026-01-04', 'Logitech'),
    ('0101', 'Pencil', 0.99, '2026-01-05', 'Pencil_brand');

DELETE FROM Products;
DELETE FROM sqlite_sequence WHERE name = 'Products';