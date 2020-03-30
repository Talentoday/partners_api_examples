import requests

class PartnersApi:
  def __init__(self, config):
    self.config = config

  def get_embed_link(self, user_id):
    url = '{}/partners-api/v1/members/{}/opmi/embed'.format(self.config['host'], user_id)
    params = { 'skip_registration': 'all', 'scenario': 'motivations', 'show_results_after': False }
    response = self.__request_partners_api('POST', url, params=params)

    return response.json()['url']

  def create_user(self):
    url = '{}/partners-api/v1/members'.format(self.config['host'])
    user_data = {'first_name': 'The', 'last_name': 'Dude'}
    response = self.__request_partners_api('POST', url, data=user_data)

    return response.json()['data']

  def get_user(self, user_id):
    url = '{}/partners-api/v1/members/{}'.format(self.config['host'], user_id)
    response = self.__request_partners_api('GET', url)

    return response.json()['data']

  def get_status(self, user_id):
    url = '{}/partners-api/v1/members/{}/opmi/questionnaire/status'.format(self.config['host'], user_id)
    response = self.__request_partners_api('GET', url)

    return response.json()

  def get_scores(self, user_id):
    url = '{}/partners-api/v1/members/{}/opmi/questionnaires/last/scores'.format(self.config['host'], user_id)
    response = self.__request_partners_api('GET', url)

    return response.json()

  def __request_partners_api(self, verb, url, params={}, data={}):
    print('Requesting partners-api')
    print('{} on {} with {} and {}'.format(verb, url, params, data))

    response = requests.request(
      verb,
      url,
      params=params,
      data=data,
      headers={ 'Authorization': self.config['token'] }
    )

    print('Answered with {}: {}'.format(response.status_code, response.json()))

    return response
