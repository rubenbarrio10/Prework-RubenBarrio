/* Ejercicio 1 */
/* 1. Crear una tabla llamada "Clientes" con las columnas: id (entero, clave primaria), nombre (texto) y email (texto). */

CREATE TABLE IF NOT EXISTS Clientes(
	id INT PRIMARY KEY,
	nombre TEXT,
	email TEXT
)

/* 2. Insertar un nuevo cliente en la tabla "Clientes" con id=1, nombre="Juan" y email="juan@example.com". */

INSERT INTO public.Clientes(id, nombre, email)
VALUES(1, 'Juan','juan@gmail.com')

/* 3. Actualizar el email del cliente con id=1 a "juan@gmail.com". */

UPDATE public.Clientes
	set email = 'juan@gmail.com'
	WHERE id = 1

/* 4. Eliminar el cliente con id=1 de la tabla "Clientes". */

DELETE FROM public.Clientes
	WHERE id = 1

/* 5. Crear una tabla llamada "Pedidos" con las columnas: id (entero, clave primaria), cliente_id (entero, clave externa referenciando a la tabla "Clientes"), producto (texto) y cantidad (entero). */

CREATE TABLE IF NOT EXISTS Pedidos(
    id INT PRIMARY KEY,
    cliente_id INT NOT NULL,
    producto TEXT,
    cantidad INT,
    CONSTRAINT FK_cliente_id FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
)

/* 6. Insertar un nuevo pedido en la tabla "Pedidos" con id=1, cliente_id=1, producto="Camiseta" y cantidad=2. */

INSERT INTO public.Pedidos (id, cliente_id, producto, cantidad)
VALUES (1, 1, 'Camiseta', 2)

/* 7. Actualizar la cantidad del pedido con id=1 a 3. */

UPDATE public.Pedidos
	set cantidad = 3
	WHERE id = 1

/* 8. Eliminar el pedido con id=1 de la tabla "Pedidos". */

DELETE FROM public.Pedidos
	WHERE id = 1

/* 9. Crear una tabla llamada "Productos" con las columnas: id (entero, clave primaria), nombre (texto) y precio (decimal). */

CREATE TABLE IF NOT EXISTS Productos(
    id INT PRIMARY KEY,
    nombre TEXT,
    precio DECIMAL(10, 2)
)

/* 10. Insertar varios productos en la tabla "Productos" con diferentes valores. */

INSERT INTO public.Productos (id, nombre, precio)
VALUES (1, 'Camiseta', 19.99);

INSERT INTO public.Productos (id, nombre, precio)
VALUES (2, 'Pantalones', 29.99);

INSERT INTO public.Productos (id, nombre, precio)
VALUES (3, 'Zapatos', 49.99);

/* 11. Consultar todos los clientes de la tabla "Clientes". */

SELECT FROM public.Clientes

/* 12. Consultar todos los pedidos de la tabla "Pedidos" junto con los nombres de los clientes correspondientes. */

SELECT Pedidos.id, Clientes.nombre AS nombre_cliente, Pedidos.producto, Pedidos.cantidad
FROM Pedidos
INNER JOIN Clientes ON Pedidos.cliente_id = Clientes.id;

/* 13. Consultar los productos de la tabla "Productos" cuyo precio sea mayor a $50. */

SELECT * FROM public.Productos
	WHERE precio > 50

/* 14. Consultar los pedidos de la tabla "Pedidos" que tengan una cantidad mayor o igual a 5. */

SELECT * FROM public.Pedidos
	WHERE cantidad > 5

/* 15. Consultar los clientes de la tabla "Clientes" cuyo nombre empiece con la letra "A". */

SELECT * FROM public.Clientes
	WHERE nombre ILIKE 'A%'

/* 16. Realizar una consulta que muestre el nombre del cliente y el total de pedidos realizados por cada cliente. */

SELECT c.nombre AS nombre_cliente, COUNT(p.id) AS total_pedidos
FROM public.Clientes c
LEFT JOIN public.Pedidos p ON c.id = p.cliente_id
GROUP BY c.nombre;

/* 17. Realizar una consulta que muestre el nombre del producto y la cantidad total de pedidos de ese producto. */

SELECT a.tipos_producto AS nombre_producto, COUNT(b.id) AS total_pedidos
FROM public.Productos a
LEFT JOIN public.Pedidos b ON a.id = b.id
GROUP BY a.tipos_producto;

/* 18. Agregar una columna llamada "fecha" a la tabla "Pedidos" de tipo fecha. */

ALTER TABLE public.Pedidos
ADD COLUMN fecha DATE;

/* 19. Agregar una clave externa a la tabla "Pedidos" que haga referencia a la tabla "Productos" en la columna "producto". */

ALTER TABLE public.Pedidos
ADD CONSTRAINT fk_producto
FOREIGN KEY (producto)
REFERENCES public.Productos(tipos_producto);

/* 20. Realizar una consulta que muestre los nombres de los clientes, los nombres de los productos y las cantidades de los pedidos donde coincida la clave externa. */

SELECT C.nombre AS Nombre_Cliente, P.tipos_producto AS Nombre_Producto, Pe.cantidad AS Cantidad
FROM public.Pedidos Pe
INNER JOIN public.Clientes C ON Pe.id = C.id
INNER JOIN public.Productos P ON Pe.producto = P.tipos_producto;
