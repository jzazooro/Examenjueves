# Examenjueves

El enlace al repositorio de GitHub de este examen es el siguiente: [GitHub](https://github.com/jzazooro/Examenjueves.git)

He resuelto un examen de manejo de datos donde respondemos a las siguientes preguntas: Cuántas visitas recibe en el día el cliente y de estas,   cuántas de ellas convierten y cuántas no (en %); Por tipo de conversión (CALL o FORM), ¿Cuántas hay de cada una?; Porcentaje de usuarios recurrentes sobre el total de usuarios; Coche más visitado. ¿Es el que más convierte?.

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
