---Kevin Bogantes. Ejercicio 1. SQL---

/*---Searched by my own how to delete tables if they exist before creating them,
 because I was getting duplicate table errors when running the script multiple times*/

DROP TABLE IF EXISTS cart_products;
DROP TABLE IF EXISTS receipt_products;
DROP TABLE IF EXISTS carts;
DROP TABLE IF EXISTS receipts;
DROP TABLE IF EXISTS Products;

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
    ('0002', 'Phone', 999, '2026-01-02', 'Apple'),
    ('0003', 'Keyboard', 139, '2026-01-03', 'Razer'),
    ('0004', 'Mouse', 119, '2026-01-04', 'Logitech'),
    ('0005', 'Pencil', 0.99, '2026-01-05', 'Pencil_brand');

----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS receipts (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    receipt_number TEXT NOT NULL,
    purchase_date TEXT NOT NULL,
    email TEXT NOT NULL,
    total_amount NUMERIC NOT NULL
);

INSERT INTO receipts (receipt_number, purchase_date, email, total_amount)
VALUES
    ('0001', '2026-01-01', 'A@gmail.com', 2.99),
    ('0002', '2026-01-02', 'B@gmail.com', 999), 
    ('0003', '2026-01-03', 'C@gmail.com', 139),
    ('0004', '2026-01-04', 'D@gmail.com', 119),
    ('0005', '2026-01-05', 'E@gmail.com', 0.99);

----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS carts (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL
);

INSERT INTO carts (email)
VALUES
    ('A@gmail.com'),
    ('B@gmail.com'),
    ('C@gmail.com'),
    ('D@gmail.com'),
    ('E@gmail.com');

----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS receipt_products (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    receipt_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    amount NUMERIC NOT NULL,
---Fks here---
    FOREIGN KEY (receipt_id) REFERENCES receipts (ID),
    FOREIGN KEY (product_id) REFERENCES Products (ID)
);
 
INSERT INTO receipt_products (receipt_id, product_id, quantity, amount)
VALUES
    (1, 1, 1, 2.99),
    (2, 2, 2, 1998),
    (3, 3, 1, 139),
    (4, 4, 1, 119),
    (5, 5, 2, 1.98);
 
----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS cart_products (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    amount NUMERIC NOT NULL,
    ---Fks here again---
    FOREIGN KEY (cart_id) REFERENCES carts (ID),
    FOREIGN KEY (product_id) REFERENCES Products (ID)
);
 
INSERT INTO cart_products (cart_id, product_id, quantity, amount)
VALUES
    (1, 1, 1, 2.99),
    (1, 3, 1, 139),
    (2, 2, 1, 999),
    (3, 4, 1, 119),
    (4, 5, 2, 1.98);

----------------------------------------------------------------------------

---Empty columns???---
ALTER TABLE receipts ADD COLUMN buyer_phone TEXT;
ALTER TABLE receipts ADD COLUMN cashier_employee_code TEXT;

---If not empty...---

/*UPDATE receipts SET buyer_phone = '8888-1111', cashier_employee_code = 'EMP001' WHERE ID = 1;
UPDATE receipts SET buyer_phone = '8888-2222', cashier_employee_code = 'EMP010' WHERE ID = 2;
UPDATE receipts SET buyer_phone = '8888-3333', cashier_employee_code = 'EMP011' WHERE ID = 3;
UPDATE receipts SET buyer_phone = '8888-4444', cashier_employee_code = 'EMP100' WHERE ID = 4;
UPDATE receipts SET buyer_phone = '8888-5555', cashier_employee_code = 'EMP101' WHERE ID = 5;*/



- SELECTS pedidos------------------------------------------------------------
 
--- 1.Obtenga todos los productos almacenados
SELECT * FROM Products;
 
--- 2.Obtenga todos los productos que tengan un precio mayor a 50000
SELECT * FROM Products WHERE Price > 50000;
 
--- 3.Obtenga todas las compras de un mismo producto por id
SELECT * FROM receipt_products WHERE product_id = 2;
 
--- 4.Obtenga todas las compras agrupadas por producto, con el total comprado entre todas las compras
SELECT
    product_id,
    SUM(quantity) AS total_quantity,
    SUM(amount) AS total_amount
FROM receipt_products
GROUP BY product_id;
 
--- 5.Obtenga todas las facturas realizadas por el mismo comprador
SELECT * FROM receipts WHERE email = 'A@gmail.com';
 
--- 6.Obtenga todas las facturas ordenadas por monto total de forma descendente
SELECT * FROM receipts ORDER BY total_amount DESC;
 
---Obtenga una sola factura por número de factura
SELECT * FROM receipts WHERE receipt_number = '0001';