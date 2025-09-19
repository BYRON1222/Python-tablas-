import psycopg2

# Conexión a PostgreSQL
conexion = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="12348"
)

cursor = conexion.cursor()
print("Conexión exitosa a PostgreSQL desde Python")

# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudiantes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    edad INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS cursos (
    id SERIAL PRIMARY KEY,
    nombre_curso VARCHAR(50),
    creditos INT
)
""")
conexion.commit()
print("Tablas 'estudiantes' y 'cursos' creadas con éxito")

# Agregar columnas
cursor.execute("ALTER TABLE estudiantes ADD COLUMN IF NOT EXISTS email VARCHAR(100)")
cursor.execute("ALTER TABLE estudiantes ADD COLUMN IF NOT EXISTS telefono VARCHAR(20)")
cursor.execute("ALTER TABLE estudiantes ADD COLUMN IF NOT EXISTS direccion VARCHAR(200)")
conexion.commit()
print("Columnas 'email', 'telefono' y 'direccion' agregadas a estudiantes")

# Renombrar columna 
cursor.execute("""
SELECT column_name 
FROM information_schema.columns 
WHERE table_name='estudiantes' AND column_name='email'
""")
columna_email = cursor.fetchone()

cursor.execute("""
SELECT column_name 
FROM information_schema.columns 
WHERE table_name='estudiantes' AND column_name='correo'
""")
columna_correo = cursor.fetchone()

if columna_email and not columna_correo:
    cursor.execute("ALTER TABLE estudiantes RENAME COLUMN email TO correo")
    conexion.commit()
    print("Columna 'email' renombrada a 'correo'")
elif columna_correo:
    print("La columna 'correo' ya existe, no se renombrará")
else:
    print("La columna 'email' no existe")

# Eliminar columna
cursor.execute("ALTER TABLE estudiantes DROP COLUMN IF EXISTS direccion")
conexion.commit()
print("Columna 'direccion' eliminada")

# Agregar CHECK
cursor.execute("""
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints 
        WHERE table_name='estudiantes' AND constraint_name='check_edad'
    ) THEN
        ALTER TABLE estudiantes ADD CONSTRAINT check_edad CHECK (edad >= 16);
    END IF;
END
$$;
""")
conexion.commit()
print("Restricción CHECK agregada en estudiantes (edad >= 16)")

# Eliminar tabla
cursor.execute("DROP TABLE IF EXISTS cursos")
conexion.commit()
print("Tabla 'cursos' eliminada")

# Cerrar cursor y conexión
cursor.close()
conexion.close()
print("Conexión cerrada")
