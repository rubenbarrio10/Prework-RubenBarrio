/* Ejercicio 5 */

/* 1. Crea una tabla llamada "Clientes" con las columnas id (entero) y nombre (cadena de texto). */

CREATE TABLE IF NOT EXISTS clientes(
	id SERIAL PRIMARY KEY,
	nombre TEXT
)

/* 2. Inserta un cliente con id=1 y nombre='John' en la tabla "Clientes". */

INSERT INTO clientes (nombre) VALUES
('John')

/* 3. Actualiza el nombre del cliente con id=1 a 'John Doe' en la tabla "Clientes". */

UPDATE clientes
SET nombre = 'John Doe'
WHERE = id = 1

/* 4. Elimina el cliente con id=1 de la tabla "Clientes". */

DELETE FROM clientes
WHERE id = 1

/* 5. Lee todos los clientes de la tabla "Clientes". */

SELECT c.nombre
FROM clientes c

/* 6. Crea una tabla llamada "Pedidos" con las columnas id (entero) y cliente_id (entero). */

CREATE TABLE IF NOT EXISTS pedidos(
	id SERIAL PRIMARY KEY,
	cliente_id INT
)

/* 7. Inserta un pedido con id=1 y cliente_id=1 en la tabla "Pedidos". */

INSERT INTO pedidos (cliente_id) VALUES
(1)

/* 8. Actualiza el cliente_id del pedido con id=1 a 2 en la tabla "Pedidos". */

UPDATE pedidos
SET cliente_id = 2
WHERE id = 1

/* 9. Elimina el pedido con id=1 de la tabla "Pedidos". */

DELETE FROM pedidos
WHERE id = 1

/* 10. Lee todos los pedidos de la tabla "Pedidos". */

SELECT * FROM pedidos

/* 11. Crea una tabla llamada "Productos" con las columnas id (entero) y nombre (cadena de texto). */

CREATE TABLE IF NOT EXISTS productos(
	id SERIAL PRIMARY KEY,
	nombre TEXT
)

/* 12. Inserta un producto con id=1 y nombre='Camisa' en la tabla "Productos". */

INSERT INTO Productos (nombre) VALUES
('Camisa')

/* 13. Actualiza el nombre del producto con id=1 a 'Pantalón' en la tabla "Productos". */

UPDATE productos
SET nombre = 'Pantalón'
WHERE id = 1

/* 14. Elimina el producto con id=1 de la tabla "Productos". */

DELETE FROM productos
WHERE id = 1

/* 15. Lee todos los productos de la tabla "Productos". */

SELECT p.nombre
FROM productos p

/* 16. Crea una tabla llamada "DetallesPedido" con las columnas pedido_id (entero) y producto_id (entero). */

CREATE TABLE IF NOT EXISTS DetallesPedido (
	pedido_id INT,
	producto_id INT
)

/* 17. Inserta un detalle de pedido con pedido_id=1 y producto_id=1 en la tabla "DetallesPedido". */

INSERT INTO DetallesPedido (pedido_id, producto_id) VALUES 
(1, 1)

/* 18. Actualiza el producto_id del detalle de pedido con pedido_id=1 a 2 en la tabla "DetallesPedido". */

UPDATE detallespedido
SET producto_id = 2
WHERE pedido_id = 1

/* 19. Elimina el detalle de pedido con pedido_id=1 de la tabla "DetallesPedido". */

DELETE FROM detallespedido
WHERE pedido_id = 1

/* 20. Lee todos los detalles de pedido de la tabla "DetallesPedido". */

SELECT * FROM detallespedido

/* 21. Realiza una consulta para obtener todos los clientes y sus pedidos correspondientes utilizando un inner join. */

SELECT c.nombre AS nombre_cliente, p.pedido_id AS id_pedido, p.producto_id
FROM clientes c
INNER JOIN detallespedido p ON c.id = p.pedido_id

/* 22. Realiza una consulta para obtener todos los clientes y sus pedidos correspondientes utilizando un left join. */

SELECT c.nombre AS nombre_cliente, p.pedido_id AS id_pedido
FROM clientes c
LEFT JOIN detallespedido p ON c.id = p.pedido_id;

/* 23. Realiza una consulta para obtener todos los productos y los detalles de pedido correspondientes utilizando un inner join. */

SELECT p.nombre AS nombre_producto, d.pedido_id AS id_pedido
FROM Productos p
INNER JOIN DetallesPedido d ON p.id = d.producto_id;

/* 24. Realiza una consulta para obtener todos los productos y los detalles de pedido correspondientes utilizando un left join. */

SELECT p.nombre AS nombre_producto, d.pedido_id AS id_pedido
FROM Productos p
LEFT JOIN DetallesPedido d ON p.id = d.producto_id;

/* 25. Crea una nueva columna llamada "telefono" de tipo cadena de texto en la tabla "Clientes". */

ALTER TABLE Clientes
ADD COLUMN telefono TEXT

/* 26. Modifica la columna "telefono" en la tabla "Clientes" para cambiar su tipo de datos a entero. */

ALTER TABLE Clientes
ADD COLUMN telefono_temp INT

UPDATE Clientes
SET telefono_temp = CAST(telefono AS INT)

ALTER TABLE Clientes
DROP COLUMN telefono;

ALTER TABLE Clientes
RENAME COLUMN telefono_temp TO telefono

/* 27. Elimina la columna "telefono" de la tabla "Clientes". */

ALTER TABLE Clientes
DROP COLUMN telefono

/* 28. Cambia el nombre de la tabla "Clientes" a "Usuarios". */

ALTER TABLE Clientes
RENAME TO Usuarios

/* 29. Cambia el nombre de la columna "nombre" en la tabla "Usuarios" a "nombre_completo". */

ALTER TABLE Usuarios
RENAME COLUMN nombre TO nombre_completo

/* 30. Agrega una restricción de clave primaria a la columna "id" en la tabla "Usuarios". */

ALTER TABLE Usuarios
ADD CONSTRAINT pk_usuarios PRIMARY KEY (id);
