# Python-tablas

## Proceso realizado

1. Conectarse desde Python a una base de datos PostgreSQL (se puede usar Docker).  
2. Cree al menos 2 tablas (`estudiantes` y `cursos`) usando Python y psycopg2.  
3. Aplique operaciones DDL desde Python:  
   - Agregar columnas nuevas (`email`, `telefono`, `direccion`).  
   - Renombrar columnas (`email` a `correo`).  
   - Eliminar columnas (`direccion`).  
   - Agregar un CHECK (`edad >= 16`).  
   - Eliminar una tabla (`cursos`).  
4. Cerre la conexión a la base de datos.  
 eso fue todo .