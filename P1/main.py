from fastapi import FastAPI #Mandas a llamar a la libreria de fastapi

app = FastAPI() #Creación de la aplicación
app.title = "Mi primera aplicación con FasAPI"
app.version = "1.0.0"

@app.get('/', tags=['home']) #mandas a root para que pueda llamar algo
def home(): #Se crea la función que se llamara por parte de root
  return "Section 0" #lo que hará la función

@app.get('/home', tags=['home']) #mandas a root para que pueda llamar algo
def home(): #Se crea la función que se llamara por parte de root
  return "Section 1" #lo que hará la función