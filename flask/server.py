from flask import Flask, render_template, jsonify
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
@app.route('/<user_id>')
def embed(user_id=None):
  service = PartnersApi(CONFIG['partners_api'])
  user = service.get_user(user_id) if user_id != None else service.create_user()
  link = service.get_embed_link(user['id'])

  return render_template('embed.html', link=link, user=user)

@app.route('/status/<member_id>')
def status(member_id):
  service = PartnersApi(CONFIG['partners_api'])
  status = service.get_status(member_id)

  return jsonify(status)

@app.route('/scores/<member_id>')
def scores(member_id):
  service = PartnersApi(CONFIG['partners_api'])
  scores = service.get_scores(member_id)

  return jsonify(scores)

if __name__ == '__main__':
   app.run(debug = True)
