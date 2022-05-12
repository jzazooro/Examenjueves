import pandas as pd
import matplotlib.pyplot as plt 
from leerarchivos import*

class graficos:
    def __init__(self, dataset, columnauno, columnados):
        self.dataset=dataset
        self.columnauno=columnauno
        self.columnados=columnados
    
    def dibujargrafico(self, title):
        self.dataset=fileuno
        self.dataset.groupby(self.columnauno)[self.columnados].sum().plot(tipo="bar")