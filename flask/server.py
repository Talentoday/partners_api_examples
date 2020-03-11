from flask import Flask, render_template
import os
from talentoday.partners_api import PartnersApi

app = Flask(__name__)

CONFIG = {
  'partners_api': {
    'host': os.getenv('PARTNERS_API_HOST'),
    'token': os.getenv('PARTNERS_API_TOKEN'),
  }
}

@app.route('/')
def embed():
  service = PartnersApi(CONFIG['partners_api'])
  user = service.create_user()
  link = service.get_embed_link(user)

  print(CONFIG['partners_api']['host'])

  return render_template('embed.html', link=link, user=user)

if __name__ == '__main__':
   app.run(debug = True)
