---EXTRA EXERCISE SQL: Crear categorías y ajustar productos---

---Cree la tabla categories con:
---id (PK autoincrement)
---Agregue a products la columna category_id 
---(INTEGER, puede permitir NULL)

CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,        
    description TEXT                       
);

---Inserte al menos 3 filas en categories

---Actualice algunos products asignándoles un category_id

---Verifique con SELECT * FROM products 
---(muestre id, product_name, price, category_id, stock_available)

---Carga de productos y filtros básicos

---Inserte al menos 10 filas en products con 
---product_name, price, stock_available

---Seleccione todos los productos

---Seleccione productos con price > 50000

---Seleccione productos cuyo product_name contenga 
---la palabra “apple” usando LIKE

---Liste los 5 productos más caros con ORDER BY price DESC LIMIT 5

---Correcciones de datos en productos

---Establezca stock_available = 0 donde price <= 0

---Aumente el price en 100 unidades para todos los productos 
---cuando stock_available sea menor a 10

---Disminuya stock_available en 1 para un product_id específico

---Verifique con SELECT * FROM products ORDER BY id ASC LIMIT 10---