import libs.Digimovies as Digimovies
import libs.ZarFilm as ZarFilm
import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()
MY_DOMAIN = os.getenv('MY_DOMAIN')
origins = [MY_DOMAIN]


class url(BaseModel):
    url: str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

dg = Digimovies.DigiMovies()
zar = ZarFilm.Zarfim()

# GET list of movies with search_term (movie name)


@app.get("/v1/zarfilm/search/{search_term}")
def zarfilm_search(search_term: str):
    return {'data': zar.get_detail_from_name(str(search_term))}


@app.get("/v1/digimovies/search/{search_term}")
def digimovies_search(search_term: str):
    return {'data': dg.get_detail_from_name(str(search_term))}


# GET Download links of movie with movie URL (with post json like { url : https://zarfilm.com/free-time-2024 } )

@app.post("/v1/zarfilm/get_movie/")
def zarfilm_get_movie(url: url):
    return {'data': zar.get_detail_from_url(str(url.url))}


@app.post("/v1/digimovies/get_movie/")
def digimovies_get_movie(url: url):
    return {'data': dg.get_detail_from_url(str(url.url))}
