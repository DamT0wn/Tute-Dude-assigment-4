from flask import Flask, request, render_template
from datetime import datetime
from dotenv import load_dotenv

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

load_dotenv()


MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI, server_api=ServerApi('1'))


db = client.test
collection = db['Flask']

app = Flask(__name__)

@app.route('/home')
def name():
    Todays_date = datetime.now().strftime("%d %m %y")
    return render_template('index.html', Todays_date=Todays_date)

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)
    collection.insert_one(form_data)
    return ("data entered successfully ")  # Return as string for valid Flask response

@app.route('/view')
def view():
    data = collection.find()

    data = data(list)

    for item in data:

        print(item)

        del item ('_id')

    data = {
    
    'data' : data 
  
       }     
    return data

if __name__ == '__main__':
    app.run(debug=True)




