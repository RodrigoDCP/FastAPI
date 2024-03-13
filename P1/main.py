from fastapi import FastAPI #Mandas a llamar a la libreria de fastapi *push1*
from fastapi.responses import HTMLResponse

app = FastAPI() #Creación de la aplicación *push1*
app.title = "Mi primera aplicación con FasAPI" #*push1*
app.version = "1.0.0" #*push1*

movies = [
  {
    "id" : 1,
    "title": "TJOC",
    "overview": "Noche tranquila, cuando entonces...",
    "year": "2024",
    "rating": "5.5",
    "category": "Terror"
  }
]


@app.get('/', tags=['home']) #mandas a root para que pueda llamar algo *push1*
def home(): #Se crea la función que se llamara por parte de root *push1*
  return "Section 0" #lo que hará la función *push1*

@app.get('/home', tags=['home']) #mandas a root para que pueda llamar algo *push1*
def home2(): #Se crea la función que se llamara por parte de  *push1*
  return "Section 1" #lo que hará la función *push1*

@app.get('/index', tags=['home']) #*push2*
def home3(): #*push2*
  return HTMLResponse('<h1>holi</h1>') #*push2*

@app.get('/movies', tags=['home']) #*push2*
def home4(): #*push2*
  return movies #*push2*

