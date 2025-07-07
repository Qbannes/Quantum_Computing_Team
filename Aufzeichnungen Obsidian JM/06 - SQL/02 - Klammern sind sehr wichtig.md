
Beispiel:
```
SELECT * FROM pharmacy_sales WHERE 
(manufacturer = 'Eli Lilly' OR manufacturer = 'Biogen' OR manufacturer = 'AbbVie') AND units_sold BETWEEN 100000 AND 105000
```

Ohne Klammern würde das Programm so überprüfen
```
SELECT * FROM pharmacy_sales WHERE 
(manufacturer = 'Eli Lilly') OR (manufacturer = 'Biogen') OR (manufacturer = 'AbbVie' AND units_sold BETWEEN 100000 AND 105000)
```