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
    p = [record for record in get_db().find()]
    for i in p:
        i.pop('_id')
    return jsonify(p)
##---------------------------------------------------------##

##-------------GET Method----------------------------------##
@app.route('/todo/api/v1.0/tasks/<string:name>', methods=['GET'])
def get_task(name):
    data = get_db()
    names = data.find({'name':name})
##    if len(names) == 0:
##        abort(404)
##    for name in names:
##    print (names[0])
    p = [name for name in names]
    for i in p:
        i.pop('_id')
    print(p)
    return jsonify(p)
##---------------------------------------------------------##

##-------------POST Method---------------------------------##
@app.route('/todo/api/v1.0/logger', methods=['POST'])
def create_task():
    if not request.json or not 'name' in request.json:
        abort(400)
    log = {
        'name': request.json['name'],
        'time': request.json['time'],
        'date': request.json['date'],
        'spO2': request.json['sp02'],
        'temp': request.json['temp'],
        'pulse': request.json['pulse']
    }
    get_db().insert(log)
    return "<p>Done</p>", 201
##---------------------------------------------------------##

if __name__ == "__main__":
    app.run()
    
