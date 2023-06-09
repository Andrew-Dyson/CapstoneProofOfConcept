from flask import Flask 
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/data')
def get_data():
    print(f"request received")
    return {"image": "Images/TestImage.png"}

