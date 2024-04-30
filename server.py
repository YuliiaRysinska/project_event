#create app Flask 
from flask import Flask, jsonify, request, abort
from eventDAO import eventDAO

app = Flask(__name__, static_url_path='', static_folder='.')

# @app.route('/')
# def index():
    # return "Hello, World!"

#curl "http://127.0.0.1:5000/event"
@app.route('/event')
def getAll():
    #print("in getall")
    results = eventDAO.getAll()
    
    return jsonify(results)

#curl "http://127.0.0.1:5000/event/2"
@app.route('/event/<int:id>')
def findById(id):
    foundEvent = eventDAO.findByID(id)

    return jsonify(foundEvent)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/events
@app.route('/event', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    
    event = {
        "Title": request.json['Title'],
        "Place": request.json['Place'],
        "Date": request.json['Date'],
        "Fee": request.json['Fee'],
    }
    addedEvent = eventDAO.create(event)
    
    return jsonify(addedEvent)


@app.route('/event/<int:id>', methods=['PUT'])
def update(id):
    foundEvent = eventDAO.findByID(id)
    if not foundEvent:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Fee' in reqJson and type(reqJson['Fee']) is not int:
        abort(400)

    if 'Title' in reqJson:
        foundEvent['Title'] = reqJson['Title']
    if 'Place' in reqJson:
        foundEvent['Place'] = reqJson['Place']
    if 'Date' in reqJson:
        foundEvent['Date'] = reqJson['Date']    
    if 'Fee' in reqJson:
        foundEvent['Fee'] = reqJson['Fee']
    eventDAO.update(id,foundEvent)
    return jsonify(foundEvent)
        

@app.route('/event/<int:id>' , methods=['DELETE'])
def delete(id):
    eventDAO.delete(id)
    return jsonify({"done":True})


if __name__ == '__main__' :
    app.run(debug= True)