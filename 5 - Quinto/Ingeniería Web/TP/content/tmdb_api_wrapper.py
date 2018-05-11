from django.conf import settings
from django.utils.http import urlquote
import http.client
import json

MOVIE_SEARCH_URL = '/3/search/movie'
MULTI_SEARCH_URL = '/3/search/multi'
MOVIE_DETAILS_URL = '/3/movie/'
TVSHOW_DETAILS_URL = '/3/tv/'
CONFIGURATION_PARAMETERS_URL = '/3/configuration'
IMAGE_SIZE_POSTER = 'w185'
IMAGE_SIZE_BACKDROP = 'w780'
BASE_QUERYSTRING = '?api_key={}&language={}'.format(settings.TMDB_API_KEY, settings.TMDB_API_LANGUAGE)
IMDB_BASE_URL = 'http://www.imdb.com/title/'

def MakeApiRequest(url):
    # Generar request a la API de TMDB.
    connection = http.client.HTTPSConnection(settings.TMDB_API_URL)
    payload = '{}'
    connection.request('GET', url, payload)

    # Obtener la respuesta y parsearla a JSON.
    data = connection.getresponse().read()
    results = json.loads(data.decode('UTF-8'))

    return results

def GetImageBaseUrl():
    # Realizar consulta a la API.
    api_response = MakeApiRequest('{}{}'.format(CONFIGURATION_PARAMETERS_URL, BASE_QUERYSTRING))

    return api_response['images']['secure_base_url']

def SearchMulti(query):
    # Realizar consulta a la API.
    api_response = MakeApiRequest('{}{}&query={}'.format(MULTI_SEARCH_URL, BASE_QUERYSTRING, urlquote(query)))

    # Generar JSON necesario para Autocomplete.
    response = [{
        'name': result['original_title'] if result['media_type'] == 'movie' else result['original_name'],
        'year': result['release_date'][:4] if result['media_type'] == 'movie' else result['first_air_date'][:4],
        'id': result['id'],
        'type': result['media_type'],
        'type_verbose': 'Película' if result['media_type'] == 'movie' else 'Serie de TV',
    } for result in api_response['results'] if result['media_type'] != 'person']

    return json.dumps(response)

def GetItemTitle(item_id, item_type):
    # Realizar consulta a la API.
    if item_type == 'movie':
        details_url = MOVIE_DETAILS_URL
        title_property_name = 'original_title'
        date_property_name = 'release_date'
    else:
        details_url = TVSHOW_DETAILS_URL
        title_property_name = 'original_name'
        date_property_name = 'first_air_date'

    api_response = MakeApiRequest('{}{}{}'.format(details_url, item_id, BASE_QUERYSTRING))

    # Generar respuesta.
    response = dict(name='{} ({})'.format(api_response[title_property_name], api_response[date_property_name][:4]),
                    id=api_response['id'],
                    title=api_response[title_property_name],
                    type=item_type,
                    type_verbose='Película' if item_type == 'movie' else 'Serie de TV', )

    return response

def GetItemsDetails(item_list):
    image_base_url = GetImageBaseUrl()

    item_details_list = []
    for item_id, item_type in item_list:
        # Realizar consulta a la API.
        if item_type == 'movie':
            details_url = MOVIE_DETAILS_URL
            title_property_name = 'original_title'
            date_property_name = 'release_date'
        else:
            details_url = TVSHOW_DETAILS_URL
            title_property_name = 'original_name'
            date_property_name = 'first_air_date'
        api_response = MakeApiRequest('{}{}{}&append_to_response=external_ids'.format(details_url, item_id, BASE_QUERYSTRING))

        # Generar respuesta.
        imdb_id = api_response['imdb_id'] if item_type == 'movie' else api_response['external_ids']['imdb_id']
        item_details_list.append(dict(id=api_response['id'],
                        title=api_response[title_property_name],
                        year=api_response[date_property_name][:4],
                        overview=api_response['overview'],
                        imdb_url='{}{}'.format(IMDB_BASE_URL, imdb_id),
                        poster_path='{}{}{}'.format(image_base_url, IMAGE_SIZE_POSTER, api_response['poster_path']),
                        backdrop_path='{}{}{}'.format(image_base_url, IMAGE_SIZE_BACKDROP, api_response['backdrop_path']),
                        runtime=api_response['runtime'] if item_type == 'movie' else '',
                        number_of_episodes=api_response['number_of_episodes'] if item_type == 'tv' else '',
                        number_of_seasons=api_response['number_of_seasons'] if item_type == 'tv' else '',
                        genres=', '.join([genre['name'] for genre in api_response['genres']]), ))

    return item_details_list