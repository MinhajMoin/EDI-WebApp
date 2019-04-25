##from flask import Flask
from flask import Flask, render_template,jsonify,abort,request,make_response
import pymongo

app = Flask(__name__)

def get_db():
    uri = 'mongodb://minhaj:minhaj123@ds129344.mlab.com:29344/edi-gs4-app'
    client = pymongo.MongoClient(uri,
                     connectTimeoutMS=30000,
                     socketTimeoutMS=None,
                     socketKeepAlive=True)
    db = client.get_default_database()
    return db['Data']

##-------------Main Function-------------------------------##
@app.route("/")
def main():
##    uri = 'mongodb://minhaj:minhaj123@ds129344.mlab.com:29344/edi-gs4-app'
##    client = pymongo.MongoClient(uri,
##                     connectTimeoutMS=30000,
##                     socketTimeoutMS=None,
##                     socketKeepAlive=True)
##    global db = client.get_default_database()
##    data = db['Data']
##    return str(db.collection_names())
##    print (data)
##    data.insert_many(SEED_DATA)
    return  render_template('index.html')
##---------------------------------------------------------##

##-------------GET Method----------------------------------##
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
##---------------------------------------------------------##

##-------------GET Method----------------------------------##
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})
##---------------------------------------------------------##

##-------------POST Method---------------------------------##
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'patient' in request.json:
        abort(400)
    log = {
        'patient': request.json['name'],
        'time': request.json['title'],
        'date': request.json['date'],
        'spO2': requests.json['sp02'],
        'temp': requests.json['temp'],
        'pulse': requests.json['pulse']
    }
    data = get_db()
    data.insert_many(log)
    return jsonify({'task': task}), 201
##---------------------------------------------------------##

if __name__ == "__main__":
    app.run()
    
