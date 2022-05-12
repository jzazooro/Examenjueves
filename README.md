# Examenjueves

El enlace al repositorio de GitHub de este examen es el siguiente: [GitHub](https://github.com/jzazooro/Examenjueves.git)

He resuelto un examen de manejo de datos donde respondemos a las siguientes preguntas: Cuántas visitas recibe en el día el cliente y de estas,   cuántas de ellas convierten y cuántas no (en %); Por tipo de conversión (CALL o FORM), ¿Cuántas hay de cada una?; Porcentaje de usuarios recurrentes sobre el total de usuarios; Coche más visitado. ¿Es el que más convierte?.

He analizado las estadisticas de los dos datasets dados para poder printear sus graficas correspondientes que describen el comportamiento de los datos.

Mi codigo es el siguiente: 

### Leerarchivos

```
import pandas as pd 
import numpys as np 

leerconversiones=pd.read_csv("conversiones(4).csv")
fileuno=open("conversiones(4).csv", "w")
fileuno.write("date", "hour", "id_lead", "id_user", "gclid", "lead_type", "result")


leernavegacion=pd.read_csv("navegacion(4).csv")
filedos=open("navegacion(4).csv", "w")
filedos.write("ts", "uuid", "id_user", "gclid", "user_recurrent", "url_landing")
```

### Desviaciontipica

```
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
```

### Media

```
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 

class media:

    def __init__(self, csv, columna):
        self.columna=columna

    def calcularmedia(self):
        media=self.csv[self.columna].mean()
        print("la media es: ", media)   
```

### Varianza

```
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
```

### Mas clases

```
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
    def calcularquartiluno(self):
        cuartiltres=self.csv[self.columna].mad()
        print("el cuartil tres es: ", cuartiltres) 
```

### grafico

```
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
```
