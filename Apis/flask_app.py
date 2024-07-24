import libs.Digimovies as Digimovies
import libs.ZarFilm as ZarFilm
from flask import Flask, request


dg = Digimovies.DigiMovies()
zar = ZarFilm.Zarfim()

app = Flask(__name__)
app.json.sort_keys = False


@app.route('/v1/zarfilm/search/<search_term>', methods=['GET'])
def zarfilm_search(search_term):
    return {'data': zar.get_detail_from_name(str(search_term))}


@app.route('/v1/digimovies/search/<search_term>', methods=['GET'])
def digimovies_search(search_term):
    return {'data': dg.get_detail_from_name(str(search_term))}


@app.route('/v1/zarfilm/get_movie/', methods=['POST'])
def zarfilm_get_movie():
    data = request.get_json()

    return {'data': zar.get_detail_from_url(str(data.get('url')))}


@app.route('/v1/digimovies/get_movie/', methods=['POST'])
def digimovies_get_movie():
    data = request.get_json()

    return {'data': dg.get_detail_from_url(str(data.get('url')))}
