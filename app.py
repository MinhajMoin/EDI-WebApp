##from flask import Flask
from flask import Flask, render_template,jsonify,abort
import pymongo

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

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


##-------------Main Function-------------------------------##
@app.route("/")
def main():
    uri = 'mongodb://minhaj:minhaj123@ds129344.mlab.com:29344/edi-gs4-app'
    client = pymongo.MongoClient(uri,
                     connectTimeoutMS=30000,
                     socketTimeoutMS=None,
                     socketKeepAlive=True)
    db = client.get_default_database()
    data = db['Data']
    return str(db.collection_names())
##    print (data)
##    data.insert_many(SEED_DATA)
##    return  render_template('index.html')
##---------------------------------------------------------##

##-------------POST Method---------------------------------##
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201
##---------------------------------------------------------##

if __name__ == "__main__":
    app.run()
    
