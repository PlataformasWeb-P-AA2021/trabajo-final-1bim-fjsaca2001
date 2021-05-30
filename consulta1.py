from sqlalchemy import create_engine
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
# Filtrado de datos en cuanto a establecimientos de la provincia de loja
establecimientos = session.query(Establecimiento).join(Parroquia, Canton, Provincia).filter(Provincia.provincia == 'LOJA').all()
# Impresion de los valores obtenidos
print("Todos los establecimientos de la provincia de Loja.")
for e in establecimientos:
    print(e, "\n")

# Filtrado de datos en cuanto a establecimientos del canton de loja
establecimientos = session.query(Establecimiento).join(Parroquia, Canton).filter(Canton.canton == 'LOJA').all()
# Impresion de los valores obtenidos
print("Todos los establecimientos del cantón de Loja.")
for e in establecimientos:
    print(e, "\n")