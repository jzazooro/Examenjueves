import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

class varianza:

    def __init__(self, csv, columna):
        self.csv=csv
        self.columna=columna

    def calcularvarianza(self):
        varianza=self.csv[self.columna].var()
        print("la varianza es: ", varianza)
        