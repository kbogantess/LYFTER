
# Ejercicios de JOINs — Parte 1

## Investigación de comandos SQL

SQL (Structured Query Language) es un lenguaje utilizado para consultar y gestionar información almacenada en bases de datos relacionales.

La instrucción SELECT permite recuperar información, mientras que ORDER BY, LIMIT y GROUP BY permiten organizar, limitar y agrupar los resultados. Los JOIN permiten relacionar registros de diferentes tablas.

## Tabla informativa

| Comando | Funcionalidad | Sintaxis básica | Ejemplo de uso |
|---|---|---|---|
| SELECT | Recupera información de una o varias columnas de una tabla. El símbolo * permite seleccionar todas las columnas. | `SELECT columna FROM tabla;` | `SELECT Name FROM Books;` |
| ORDER BY | Ordena los resultados según una o varias columnas. ASC indica orden ascendente y DESC descendente. | `SELECT columna FROM tabla ORDER BY columna ASC;` | `SELECT Name FROM Books ORDER BY Name ASC;` |
| LIMIT | Establece el número máximo de filas que devolverá una consulta. Es útil para mostrar una cantidad específica de resultados. | `SELECT columna FROM tabla LIMIT cantidad;` | `SELECT * FROM Books LIMIT 3;` |
| GROUP BY | Agrupa registros que comparten un mismo valor. Se utiliza frecuentemente con funciones como COUNT, SUM, AVG, MIN y MAX. | `SELECT columna, COUNT(*) FROM tabla GROUP BY columna;` | `SELECT CustomerID, COUNT(*) FROM Rents GROUP BY CustomerID;` |
| INNER JOIN | Combina únicamente las filas de dos tablas que cumplen la condición de unión. Los registros sin coincidencias se excluyen. | `SELECT * FROM tablaA INNER JOIN tablaB ON tablaA.id = tablaB.id;` | `SELECT Books.Name, Authors.Name FROM Books INNER JOIN Authors ON Books.Author = Authors.ID;` |
| LEFT JOIN | Devuelve todas las filas de la tabla izquierda y los datos coincidentes de la derecha. Si no existe coincidencia, devuelve NULL en las columnas de la derecha. | `SELECT * FROM tablaA LEFT JOIN tablaB ON tablaA.id = tablaB.id;` | `SELECT Books.Name, Authors.Name FROM Books LEFT JOIN Authors ON Books.Author = Authors.ID;` |
| RIGHT JOIN | Devuelve todas las filas de la tabla derecha y los datos coincidentes de la izquierda. Si no existe coincidencia, devuelve NULL en las columnas de la izquierda. | `SELECT * FROM tablaA RIGHT JOIN tablaB ON tablaA.id = tablaB.id;` | `SELECT Books.Name, Authors.Name FROM Books RIGHT JOIN Authors ON Books.Author = Authors.ID;` |

---

## Ejemplos y resultados

### 1. SELECT

```sql
SELECT ID, Name
FROM Books;
```

| ID | Name |
|---|---|
| 1 | Don Quijote |
| 2 | La Divina Comedia |
| 3 | Vagabond 1-3 |
| 4 | Dragon Ball 1 |
| 5 | The Book of the 5 Rings |

### 2. ORDER BY

```sql
SELECT ID, Name
FROM Books
ORDER BY Name ASC;
```

| ID | Name |
|---|---|
| 1 | Don Quijote |
| 4 | Dragon Ball 1 |
| 2 | La Divina Comedia |
| 5 | The Book of the 5 Rings |
| 3 | Vagabond 1-3 |

### 3. LIMIT

```sql
SELECT ID, Name
FROM Books
ORDER BY ID ASC
LIMIT 3;
```

| ID | Name |
|---|---|
| 1 | Don Quijote |
| 2 | La Divina Comedia |
| 3 | Vagabond 1-3 |

### 4. GROUP BY

```sql
SELECT CustomerID, COUNT(*) AS TotalRentas
FROM Rents
GROUP BY CustomerID
ORDER BY CustomerID;
```

| CustomerID | TotalRentas |
|---|---|
| 1 | 2 |
| 2 | 3 |

### 5. INNER JOIN

```sql
SELECT Books.Name AS Libro,
       Authors.Name AS Autor
FROM Books
INNER JOIN Authors
ON Books.Author = Authors.ID;
```

| Libro | Autor |
|---|---|
| Don Quijote | Miguel de Cervantes |
| La Divina Comedia | Dante Alighieri |
| Vagabond 1-3 | Takehiko Inoue |
| Dragon Ball 1 | Akira Toriyama |

### 6. LEFT JOIN

```sql
SELECT Books.Name AS Libro,
       Authors.Name AS Autor
FROM Books
LEFT JOIN Authors
ON Books.Author = Authors.ID;
```

| Libro | Autor |
|---|---|
| Don Quijote | Miguel de Cervantes |
| La Divina Comedia | Dante Alighieri |
| Vagabond 1-3 | Takehiko Inoue |
| Dragon Ball 1 | Akira Toriyama |
| The Book of the 5 Rings | NULL |

### 7. RIGHT JOIN

```sql
SELECT Books.Name AS Libro,
       Authors.Name AS Autor
FROM Books
RIGHT JOIN Authors
ON Books.Author = Authors.ID;
```

| Libro | Autor |
|---|---|
| Don Quijote | Miguel de Cervantes |
| La Divina Comedia | Dante Alighieri |
| Vagabond 1-3 | Takehiko Inoue |
| Dragon Ball 1 | Akira Toriyama |
| NULL | Walt Disney |

---

## Referencias

1. SQLite. (s. f.). *SELECT*. https://www.sqlite.org/lang_select.html

2. PostgreSQL Global Development Group. (s. f.). *Queries*. https://www.postgresql.org/docs/current/queries.html
