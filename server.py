from typing import Union
import libs.Digimovies as Digimovies
import libs.ZarFilm as ZarFilm
dg = Digimovies.DigiMovies()
zar = ZarFilm.Zarfim()
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
    "http://localhost:3000",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]
class Item(BaseModel):
    url: str



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search/{search_term}")
def read_item(search_term: str):
    return {'data' : zar.get_detail_from_name( str(search_term))}
@app.post("/get_movie/")
def read_item(url: Item):
    return {'data' : zar.get_detail_from_url( str(url.url))}