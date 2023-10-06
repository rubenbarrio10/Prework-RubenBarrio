/* Ejercicio 2 */

/* Nivel de dificultad: Fácil */

/* 1. Crea una base de datos llamada "MiBaseDeDatos". */

/* 2. Crea una tabla llamada "Usuarios" con las columnas: "id" (entero, clave primaria), "nombre" (texto) y "edad" (entero). */

CREATE TABLE IF NOT EXISTS Usuarios (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    edad INT
)

/* 3. Inserta dos registros en la tabla "Usuarios". */

INSERT INTO PUBLIC.USUARIOS(nombre, edad) VALUES
  ('Juan', 30),
  ('María', 25);

/* 4. Actualiza la edad de un usuario en la tabla "Usuarios". */

UPDATE public.Usuarios
	SET edad = 35
	WHERE id = 1

/* 5. Elimina un usuario de la tabla "Usuarios". */

DELETE FROM public.Usuarios
	WHERE id = 1

/* Nivel de dificultad: Moderado */

/* 1. Crea una tabla llamada "Ciudades" con las columnas: "id" (entero, clave primaria), "nombre" (texto) y "pais" (texto). */

CREATE TABLE IF NOT EXISTS Ciudades(
	id SERIAL PRIMARY KEY,
	nombre TEXT,
	pais TEXT
)

/* 2. Inserta al menos tres registros en la tabla "Ciudades". */

INSERT INTO public.Ciudades (nombre, pais) VALUES
	('Madrid', 'España'),
	('Málaga', 'España'),
	('Navarra', 'España')

/* 3. Crea una foreign key en la tabla "Usuarios" que se relacione con la columna "id" de la tabla "Ciudades". */

ALTER TABLE public.Usuarios
	ADD CONSTRAINT fk_id
	FOREIGN KEY(id)
	REFERENCES public.Ciudades (id)

/* 4. Realiza una consulta que muestre los nombres de los usuarios junto con el nombre de su ciudad y país (utiliza un LEFT JOIN). */

SELECT u.nombre, c.nombre, c.pais
FROM public.Usuarios u
LEFT JOIN public.Ciudades c ON u.id = c.id

/* 5. Realiza una consulta que muestre solo los usuarios que tienen una ciudad asociada (utiliza un INNER JOIN). */

SELECT u.nombre, c.nombre
FROM public.Usuarios u
INNER JOIN public.Ciudades c ON u.id = c.id
