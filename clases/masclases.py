import pandas as pd 
import matplotlib.pyplot as plt
from leerarchivos import *

conversiones=leerconversiones

class columna:
    def __init__(self, csv):
        self.csv=csv
    def calcularcolumnas(self):
        print("hay", self.csv.shape[1], "columnas")

class fila:
    def __init__(self, csv):
        self.csv=csv
    def calcularfilas(self):
        print("hay", self.csv.shape[0], "filas")
class moda:
    def __init__(self, columna, csv):
        self.columna=columna
        self.csv=csv
    def calcularmoda(self):
        moda=self.csv[self.columna].mode()
        print("la moda es: ", moda)

class mediana:
    def __init__(self, columna, csv):
        self.columna=columna
        self.csv=csv
    def calcularmediana(self):
        moda=self.csv[self.columna].median()
        print("la moda es: ", mediana)

class quartiluno:
    def __init__(self, columna, csv):
        self.csv=csv
        self.columna=columna
    def calcularquartiluno(self):
        cuartiluno=self.csv[self.columna].mad()
        print("el cuartil uno es: ", cuartiluno)

class quartiltres:
    def __init__(self, columna, csv):
        self.csv=csv
        self.columna=columna
    def calcularquartiltres(self):
        cuartiltres=self.csv[self.columna].mad()
        print("el cuartil tres es: ", cuartiltres)    