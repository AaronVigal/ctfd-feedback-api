from flask import Flask, jsonify, request
from flask_talisman import Talisman
import firebase_admin
from flask_cors import CORS
from firebase_admin import credentials
from firebase_admin import firestore
import uuid

app = Flask(__name__)
# Talisman(app)
# CORS(app)

cred = credentials.Certificate('hsctf-feedback-53e1011913d3.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route('/feedback', methods=['POST'])
def feedback():
    content = request.get_json()

    challenge = content['challenge']
    difficulty = content['difficulty']
    enjoyment = content['enjoyment']
    learned = content['learned']
    try:
        difficulty = int(content['difficulty'])
        enjoyment = int(content['enjoyment'])
    except:
        print('Invalid int conversion.')

    doc_ref = db.collection(u'responses').document(uuid.uuid4().hex)
    doc_ref.set({
        u'challenge': challenge,
        u'difficulty': difficulty,
        u'enjoyment': enjoyment,
        u'learned': learned,
    })

    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=False)