from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
  {
    'name': 'My Wonderful Store',
    'items': [
      {
        'name': 'My Item',
        'price': 15.99
      }
    ]
  }
]

def find_store(name):
  for store in stores:
    if store['name'] == name:
      return store

@app.route('/store', methods=['POST'])
def create_store():
  request_data = request.get_json()
  new_store = {
    'name': request_data['name'],
    'items': []
  }
  stores.append(new_store)
  return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store(name):
  return jsonify(find_store(name) or { 'message': 'store not found' })

@app.route('/store')
def get_stores():
  return jsonify({ 'stores': stores })

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
  found_store = find_store(name)
  if (found_store == None):
    return jsonify({ 'message': 'store not found' })
  request_data = request.get_json()
  new_item = {
    'name': request_data['name'],
    'price': request_data['price']
  }
  found_store['items'].append(new_item)
  return jsonify(new_item)

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
  return jsonify( find_store(name)['items'] or { 'message': 'store not found' })

app.run(port=5000)
