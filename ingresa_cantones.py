from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Canton, Provincia
from configuracion import cadena_base_datos

import csv

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# se crean objetos de tipo cantones

# leer el archivo de datos

with open('data/Listado-Instituciones-Educativas.csv') as File:
    read = csv.reader(File, delimiter='|')
    canAux = "Cantón"
    for x in read:
         nuec = x[5]
         if(nuec != canAux):
             aux = session.query(Provincia).filter_by(codigo = x[2]).first()
             cant = Canton(codigo=x[4], canton=nuec, provincia=aux)
             session.add(cant)
             canAux = nuec
            
session.commit()