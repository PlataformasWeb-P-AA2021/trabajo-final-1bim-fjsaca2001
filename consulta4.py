from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import *
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()
# Filtrado de datos en cuanto a Establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores.
establecimientos = session.query(Establecimiento).filter(Establecimiento.nroDocentes > 100).order_by(desc(Establecimiento.nroEstudiantes)).all()
# Impresion de los valores obtenidos
print("Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores.")
# Impresion de clos datos obtenidos
for p in establecimientos:
    print(p,"\n")


# Filtrado de datos en cuanto a Establecimientos ordenados por número de profesores; que tengan más de 100 profesores.
establecimientos = session.query(Establecimiento).filter(Establecimiento.nroDocentes > 100).order_by(desc(Establecimiento.nroDocentes)).all()
# Impresion de los valores obtenidos
print("Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores.")
# Impresion de los datos obtenidos
for p in establecimientos:
    print(p,"\n")