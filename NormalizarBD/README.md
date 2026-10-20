
# Ejercicios de Normalización

# 1. Orders

## Primera Forma Normal (1FN)

| OrderID | CustomerName | CustomerPhone | Address | ItemID | ItemName | Price | Quantity | SpecialRequest | DeliveryTime |
|---|---|---|---|---|---|---|---|---|---|
| O01 | Alice | 123-456-7890 | 123 Main St | 101 | Cheeseburger | $8 | 2 | No onions | 6:00 PM |
| O01 | Alice | 123-456-7890 | 123 Main St | 102 | Fries | $3 | 1 | Extra ketchup | 6:00 PM |
| O02 | Bob | 987-654-3210 | 456 Elm St | 103 | Pizza | $12 | 1 | Extra cheese | 7:30 PM |
| O02 | Bob | 987-654-3210 | 4th Avenue | 102 | Fries | $3 | 2 | None | 7:30 PM |
| O03 | Claire | 555-123-4567 | 789 Oak St | 105 | Salad | $6 | 1 | No croutons | 12:00 PM |
| O04 | Claire | 555-123-4567 | 464 Georgia St | 106 | Water | $1 | 1 | None | 5:00 PM |

## Segunda Forma Normal (2FN)

### Pedidos

| OrderID (PK) | CustomerName | CustomerPhone | Address | DeliveryTime |
|---|---|---|---|---|
| O01 | Alice | 123-456-7890 | 123 Main St | 6:00 PM |
| O02 | Bob | 987-654-3210 | Por confirmar | 7:30 PM |
| O03 | Claire | 555-123-4567 | 789 Oak St | 12:00 PM |
| O04 | Claire | 555-123-4567 | 464 Georgia St | 5:00 PM |

### Productos

| ItemID (PK) | ItemName | Price |
|---|---|---|
| 101 | Cheeseburger | $8 |
| 102 | Fries | $3 |
| 103 | Pizza | $12 |
| 105 | Salad | $6 |
| 106 | Water | $1 |

### Detalle de pedidos

| OrderID (PK, FK) | ItemID (PK, FK) | Quantity | SpecialRequest |
|---|---|---|---|
| O01 | 101 | 2 | No onions |
| O01 | 102 | 1 | Extra ketchup |
| O02 | 103 | 1 | Extra cheese |
| O02 | 102 | 2 | None |
| O03 | 105 | 1 | No croutons |
| O04 | 106 | 1 | None |

## Tercera Forma Normal (3FN)

### Clientes

| CustomerID (PK) | CustomerName | CustomerPhone |
|---|---|---|
| C01 | Alice | 123-456-7890 |
| C02 | Bob | 987-654-3210 |
| C03 | Claire | 555-123-4567 |

### Pedidos

| OrderID (PK) | CustomerID (FK) | Address | DeliveryTime |
|---|---|---|---|
| O01 | C01 | 123 Main St | 6:00 PM |
| O02 | C02 | Por confirmar | 7:30 PM |
| O03 | C03 | 789 Oak St | 12:00 PM |
| O04 | C03 | 464 Georgia St | 5:00 PM |

### Productos

| ItemID (PK) | ItemName | Price |
|---|---|---|
| 101 | Cheeseburger | $8 |
| 102 | Fries | $3 |
| 103 | Pizza | $12 |
| 105 | Salad | $6 |
| 106 | Water | $1 |

### Detalle de pedidos

| OrderID (PK, FK) | ItemID (PK, FK) | Quantity | SpecialRequest |
|---|---|---|---|
| O01 | 101 | 2 | No onions |
| O01 | 102 | 1 | Extra ketchup |
| O02 | 103 | 1 | Extra cheese |
| O02 | 102 | 2 | None |
| O03 | 105 | 1 | No croutons |
| O04 | 106 | 1 | None |

---

# 2. Cars

## Primera Forma Normal (1FN)

| VIN | Make | Model | Year | Color | OwnerID | OwnerName | OwnerPhone | InsuranceCompany | InsurancePolicy |
|---|---|---|---|---|---|---|---|---|---|
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 101 | Alice | 123-456-7890 | ABC Insurance | Fire & Theft |
| 1HGCM82633A | Honda | Accord | 2003 | Silver | 102 | Bob | 987-654-3210 | XYZ Insurance | Full Cover |
| 5J6RM4H79EL | Honda | CR-V | 2014 | Blue | 103 | Claire | 555-123-4567 | DEF Insurance | Collision |
| 1G1RA6EH1FU | Chevrolet | Volt | 2015 | Red | 104 | Dave | 111-222-3333 | GHI Insurance | Basic Legal |

## Segunda Forma Normal (2FN)

### Vehículos

| VIN (PK) | Make | Model | Year | Color |
|---|---|---|---|---|
| 1HGCM82633A | Honda | Accord | 2003 | Silver |
| 5J6RM4H79EL | Honda | CR-V | 2014 | Blue |
| 1G1RA6EH1FU | Chevrolet | Volt | 2015 | Red |

### Propietarios

| OwnerID (PK) | OwnerName | OwnerPhone |
|---|---|---|
| 101 | Alice | 123-456-7890 |
| 102 | Bob | 987-654-3210 |
| 103 | Claire | 555-123-4567 |
| 104 | Dave | 111-222-3333 |

### Propiedad y seguros

| VIN (PK, FK) | OwnerID (PK, FK) | InsuranceCompany | InsurancePolicy |
|---|---|---|---|
| 1HGCM82633A | 101 | ABC Insurance | Fire & Theft |
| 1HGCM82633A | 102 | XYZ Insurance | Full Cover |
| 5J6RM4H79EL | 103 | DEF Insurance | Collision |
| 1G1RA6EH1FU | 104 | GHI Insurance | Basic Legal |

## Tercera Forma Normal (3FN)

### Vehículos

| VIN (PK) | Make | Model | Year | Color |
|---|---|---|---|---|
| 1HGCM82633A | Honda | Accord | 2003 | Silver |
| 5J6RM4H79EL | Honda | CR-V | 2014 | Blue |
| 1G1RA6EH1FU | Chevrolet | Volt | 2015 | Red |

### Propietarios

| OwnerID (PK) | OwnerName | OwnerPhone |
|---|---|---|
| 101 | Alice | 123-456-7890 |
| 102 | Bob | 987-654-3210 |
| 103 | Claire | 555-123-4567 |
| 104 | Dave | 111-222-3333 |

### Propiedad y seguros

| VIN (PK, FK) | OwnerID (PK, FK) | InsuranceCompany | InsurancePolicy |
|---|---|---|---|
| 1HGCM82633A | 101 | ABC Insurance | Fire & Theft |
| 1HGCM82633A | 102 | XYZ Insurance | Full Cover |
| 5J6RM4H79EL | 103 | DEF Insurance | Collision |
| 1G1RA6EH1FU | 104 | GHI Insurance | Basic Legal |
