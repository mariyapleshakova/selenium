import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '553f626a2b9f1cb95fc270caabe6ef54'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '11802'
TRAINER_NAME = 'Spring'


def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Kikki'

@pytest.mark.parametrize('key, value', [('name', 'Kikki'), ('trainer_id', TRAINER_ID), ('id', '167255')])
def test_parametrize(key,value):
     response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
     assert response_parametrize.json()["data"][0][key] == value


def test_name():
    response_get = requests.get(url = f'{URL}/me', headers = HEADER, params = TRAINER_ID)
    assert response_get.json()["data"][0]["trainer_name"] == 'Spring'