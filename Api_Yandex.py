import requests


def add_folder(token='************'):
  response = requests.put(
    'https://cloud-api.yandex.net/v1/disk/resources',
    headers = {
      'Authorization' : token
    },
    params = {
     'path' : '/Photo'
    }
  )
  return response.status_code
