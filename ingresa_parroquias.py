from re import A
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Parroquia, Canton
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
    parrAux = "Parroquia"
    for x in read:
         nuep = x[7]
         if(nuep != parrAux):
             with session.no_autoflush:
                aux = session.query(Canton).filter_by(codigo = x[4]).first()
                parro = Parroquia(codigo=x[6], parroquia=nuep, canton=aux)
                session.add(parro)
             parrAux = nuep
            
session.commit()