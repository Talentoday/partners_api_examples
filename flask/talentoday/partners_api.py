import requests

class PartnersApi:
  def __init__(self, config):
    self.config = config

  def get_embed_link(self, user):
    response = requests.post(
      '{}/partners-api/v1/members/{}/opmi/embed'.format(self.config['host'], user['id']),
      params={ 'skip_registration': 'all', 'scenario': 'motivations', 'show_results_after': False },
      headers={ 'Authorization': self.config['token'] }
    )

    return response.json()['url']

  def create_user(self):
    user_data = {
      'first_name': 'The',
      'last_name': 'Dude'
    }

    response = requests.post(
      '{}/partners-api/v1/members'.format(self.config['host']),
      data=user_data,
      headers={ 'Authorization': self.config['token'] }
    )

    return response.json()['data']
