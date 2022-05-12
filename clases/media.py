import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 

class media:

    def __init__(self, csv, columna):
        self.columna=columna

    def calcularmedia(self):
        media=self.csv[self.columna].mean()
        print("la media es: ", media)    