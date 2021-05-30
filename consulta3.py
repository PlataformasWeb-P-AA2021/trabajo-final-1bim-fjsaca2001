from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

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
# Filtrado de datos en cuanto a cantones cuyos establecimientos tengan un numero de docentes igual a 0
parroquias = session.query(Canton).join(Parroquia, Establecimiento).filter(Establecimiento.nroDocentes == 0).all()
# Impresion de los valores obtenidos
print("Los cantones que tiene establecimientos con 0 número de profesores.")
# Impresion de clos datos obtenidos
for p in parroquias:
    print(p,"\n")


# Filtrado de datos en cuanto a Establecimientos cuyos establecimientos cuya parroquia Catacocha con estudiantes mayores o iguales a 21
cantones = session.query(Establecimiento).join(Parroquia).filter(and_(Parroquia.parroquia == "CATACOCHA", Establecimiento.nroEstudiantes >= 21)).all()
# Impresion de los valores obtenidos
print("Los establecimientos que pertenecen a la parroquia Catacocha con estudiantes mayores o iguales a 21")
# Impresion de los datos obtenidos
for p in cantones:
    print(p,"\n")