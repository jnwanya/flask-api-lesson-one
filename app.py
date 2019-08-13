from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'Soap',
        'items': [
            {
                'name': 'My Item',
                'price': 12.90
            }
        ]
    }
]

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/{string-name}
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if name == store['name']:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:store_name>/item', methods=['POST'])
def create_store_item(store_name):
    request_data = request.get_json()
    print(request_data)
    # item = {'name': request_data['name'], 'price': request_data['price']}

    for store in stores:
        if store['name'] == store_name:
            item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(item)
            return jsonify(store)
    return jsonify({'message': 'store not found'})


# GET /store/<string:name>/item
@app.route('/store/<string:store_name>/item')
def get_store_items(store_name):
    for store in stores:
        if store['name'] == store_name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


app.run(port=5000)
