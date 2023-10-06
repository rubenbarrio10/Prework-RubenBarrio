/* Ejercicio 3 */

/* Nivel de dificultad: Difícil */

/* 1. Crea una tabla llamada "Productos" con las columnas: "id" (entero, clave primaria), "nombre" (texto) y "precio" (numérico). */

CREATE TABLE IF NOT EXISTS Productos(
	id SERIAL PRIMARY KEY,
	nombre TEXT,
	precio NUMERIC
)

/* 2. Inserta al menos cinco registros en la tabla "Productos". */

INSERT INTO public.Productos (nombre, precio) VALUES
	('Camiseta', 19.99),
	('Pantalones', 29.99),
	('Zapatillas', 49.99),
	('Chaqueta', 59.99),
	('Sombrero', 9.99)

/* 3. Actualiza el precio de un producto en la tabla "Productos". */

UPDATE public.Productos
	SET precio = 50.00
	WHERE id = 5

/* 4. Elimina un producto de la tabla "Productos". */

DELETE FROM public.Productos
  WHERE id = 1

/* 5. Realiza una consulta que muestre los nombres de los usuarios junto con los nombres de los productos que han comprado (utiliza un INNER JOIN con la tabla "Productos"). */

SELECT u.nombre, p.nombre
FROM public.Usuarios u
INNER JOIN public.productos p ON u.id = p.id