
---EXTRA EXERCISE SQL: Crear categorías y ajustar productos---

---Cree la tabla categories con:
---id (PK autoincrement)

CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,        
    description TEXT                       
);

---Agregue a products la columna category_id 
---(INTEGER, puede permitir NULL)

ALTER TABLE products ADD COLUMN category_id INTEGER;

---Inserte al menos 3 filas en categories

INSERT INTO categories (name, description) VALUES
('Electrónica', 'Dispositivos y accesorios electrónicos'),
('Alimentos', 'Productos comestibles y bebidas'),
('Hogar', 'Artículos para el hogar y limpieza');

---Actualice algunos products asignándoles un category_id

UPDATE products SET category_id = 1 WHERE id IN (1, 2, 3);
UPDATE products SET category_id = 2 WHERE id IN (4, 5, 6);
UPDATE products SET category_id = 3 WHERE id IN (7, 8);

---Verifique con SELECT * FROM products 
---(muestre id, product_name, price, category_id, stock_available)

SELECT id, product_name, price, category_id, stock_available
FROM products;


---Carga de productos y filtros básicos---

---Inserte al menos 10 filas en products con 
---product_name, price, stock_available

INSERT INTO products (product_name, price, stock_available) VALUES
('Apple iPhone 14', 650000, 15),
('Apple Watch Series 9', 250000, 8),
('Samsung Galaxy S23', 580000, 20),
('Sony Headphones WH-1000XM5', 180000, 5),
('Dell Laptop XPS 13', 850000, 3),
('Logitech Mouse MX Master', 45000, 30),
('Apple MacBook Air M2', 950000, 6),
('Keyboard Mechanical RGB', 60000, 12),
('Monitor LG 27 pulgadas', 220000, 9),
('External Hard Drive 1TB', 55000, 25);

---Seleccione todos los productos

SELECT * FROM products;

---Seleccione productos con price > 50000

SELECT * FROM products WHERE price > 50000;

---Seleccione productos cuyo product_name contenga 
---la palabra "apple" usando LIKE

SELECT * FROM products WHERE product_name LIKE '%apple%';

---Liste los 5 productos más caros con ORDER BY price DESC LIMIT 5

SELECT * FROM products ORDER BY price DESC LIMIT 5;


---Correcciones de datos en productos---

---Establezca stock_available = 0 donde price <= 0

UPDATE products SET stock_available = 0 WHERE price <= 0;

---Aumente el price en 100 unidades para todos los productos 
---cuando stock_available sea menor a 10

UPDATE products SET price = price + 100 WHERE stock_available < 10;

---Disminuya stock_available en 1 para un product_id específico

UPDATE products SET stock_available = stock_available - 1 WHERE id = 1;

---Verifique con SELECT * FROM products ORDER BY id ASC LIMIT 10---

SELECT * FROM products ORDER BY id ASC LIMIT 10;