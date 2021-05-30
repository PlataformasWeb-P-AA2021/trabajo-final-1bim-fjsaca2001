from sqlalchemy import create_engine, desc, and_
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
# Filtrado de datos en cuanto a Establecimientos ordenados por nombre de parroquia; que tengan más de 20 profesores y la cadena "Permanente" en tipo de educación.
establecimientos = session.query(Establecimiento).join(Parroquia).filter(and_(Establecimiento.nroDocentes > 20 , Establecimiento.tipo.like("%Permanente%"))).order_by(desc(Parroquia.parroquia)).all()
# Impresion de los valores obtenidos
print("Los establecimientos ordenados por nombre de parroquia que tengan más de 20 profesores y la cadena 'Permanente' en tipo de educación.")
# Impresion de clos datos obtenidos
for p in establecimientos:
    print(p,"\n")


# Filtrado de datos en cuanto a Establecimientos ordenados por sostenimiento y tengan código de distrito 11D02.
establecimientos = session.query(Establecimiento).filter(Establecimiento.nroDistrito == "11D02").order_by(desc(Establecimiento.sostenimiento)).all()
# Impresion de los valores obtenidos
print("Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D02.")
# Impresion de los datos obtenidos
for p in establecimientos:
    print(p,"\n")