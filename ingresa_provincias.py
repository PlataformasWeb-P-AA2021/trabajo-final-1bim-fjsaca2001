from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Provincia
from configuracion import cadena_base_datos

import csv

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# se crean objetos de tipo provincia

# leer el archivo de datos

with open('data/Listado-Instituciones-Educativas.csv') as File:
    read = csv.reader(File, delimiter='|')
    provAux = "Provincia"
    for x in read:
         nuep = x[3]
         if(nuep != provAux):
             prov = Provincia(codigo=str(x[2]), provincia=str(nuep))
             session.add(prov)
             provAux = nuep
            
session.commit()


