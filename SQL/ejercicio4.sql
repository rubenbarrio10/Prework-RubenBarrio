/* Ejercicio 4 */

/* Nivel de dificultad: Experto */

/* 1. Crea una tabla llamada "Pedidos" con las columnas: "id" (entero, clave primaria), "id_usuario" (entero, clave foránea de la tabla "Usuarios") y "id_producto" (entero, clave foránea de la tabla "Productos"). */

CREATE TABLE Pedidos (
    id SERIAL PRIMARY KEY,
    id_usuario INT,
    id_producto INT,
    CONSTRAINT fk_usuario FOREIGN KEY (id_usuario) REFERENCES public.Usuarios(id),
    CONSTRAINT fk_producto FOREIGN KEY (id_producto) REFERENCES public.Productos(id)
)

/* 2. Inserta al menos tres registros en la tabla "Pedidos" que relacionen usuarios con productos. */

INSERT INTO Pedidos (id_usuario, id_producto) VALUES
(2, 1),
(3, 3),
(10, 2)

/* 3. Realiza una consulta que muestre los nombres de los usuarios y los nombres de los productos que han comprado, incluidos aquellos que no han realizado ningún pedido (utiliza LEFT JOIN y COALESCE). */

SELECT u.nombre AS nombre_usuario, COALESCE(p.nombre, 'Sin pedido') AS nombre_producto
FROM Usuarios u
LEFT JOIN Pedidos pd ON u.id = pd.id_usuario
LEFT JOIN Productos p ON pd.id_producto = p.id

/* 4. Realiza una consulta que muestre los nombres de los usuarios que han realizado un pedido, pero también los que no han realizado ningún pedido (utiliza LEFT JOIN). */

SELECT u.nombre AS nombre_usuario
FROM Usuarios u
LEFT JOIN Pedidos p ON u.id = p.id_usuario
WHERE p.id IS NOT NULL OR p.id IS NULL

/* 5. Agrega una nueva columna llamada "cantidad" a la tabla "Pedidos" y actualiza los registros existentes con un valor (utiliza ALTER TABLE y UPDATE). */

ALTER TABLE Pedidos
ADD COLUMN cantidad INT

UPDATE Pedidos
SET cantidad = 5
