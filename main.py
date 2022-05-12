from clases.desviaciontipica import *
from clases.media import *
from clases.masclases import *
from clases.grafico import *
from clases.varianza import *
from leerarchivos import *
import pandas as pd 

filas=fila(conversiones)
fila.calcularfilas

column=columna(conversiones)
column.calcularcolumnas

medi=media(conversiones)
medi.calcularmedia

desviaciontipic=desviaciontipica(conversiones)
desviaciontipic.calculardesviaciontipica

cuartilun=quartiluno(conversiones)
cuartilun.calcularquartiluno

cuartildo=quartiltres(conversiones)
cuartildo.calcularquartiltres




