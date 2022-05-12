import pandas as pd 
import numpys as np 

leerconversiones=pd.read_csv("conversiones(4).csv")
fileuno=open("conversiones(4).csv", "w")
fileuno.write("date", "hour", "id_lead", "id_user", "gclid", "lead_type", "result")


leernavegacion=pd.read_csv("navegacion(4).csv")
filedos=open("navegacion.csv", "w")
filedos.write("ts", "uuid", "id_user", "gclid", "user_recurrent", "url_landing")