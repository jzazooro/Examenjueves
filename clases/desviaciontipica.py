import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

class desviaciontipica:

    def __init__(self, csv, columna):
        self.csv=csv
        self.columna=columna

    def calculardesviaciontipica(self):
        desviaciontipica=self.csv[self.columna].mad()
        print("la desviacion tipica es: ", desviaciontipica)