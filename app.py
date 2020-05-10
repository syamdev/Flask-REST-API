from flask import Flask, jsonify, request, Response
import json

app = Flask(__name__)

fruits = [
    {
        'name': 'Apple',
        'price': 3.99,
        'stock': 2020
    },
    {
        'name': 'Banana',
        'price': 4.99,
        'stock': 2002
    },
    {
        'name': 'Cherry',
        'price': 2.99,
        'stock': 2003
    },
    {
        'name': 'Durian',
        'price': 4.99,
        'stock': 2004
    },
    {
        'name': 'Elderberry',
        'price': 3.99,
        'stock': 2005
    },
    {
        'name': 'Fig',
        'price': 2.99,
        'stock': 2001
    },
    {
        'name': 'Grape',
        'price': 3.99,
        'stock': 2002
    },
    {
        'name': 'Honeyberry',
        'price': 4.99,
        'stock': 2003
    },
    {
        'name': 'Incaberry',
        'price': 2.99,
        'stock': 2004
    },
    {
        'name': 'Jackfruit',
        'price': 4.99,
        'stock': 2005
    },
    {
        'name': 'Kiwifruit',
        'price': 3.99,
        'stock': 2001
    },
    {
        'name': 'Lemon',
        'price': 2.99,
        'stock': 2002
    },
    {
        'name': 'Mango',
        'price': 4.99,
        'stock': 2003
    },
    {
        'name': 'Nectarine',
        'price': 3.99,
        'stock': 2004
    },
    {
        'name': 'Orange',
        'price': 2.99,
        'stock': 2005
    },
    {
        'name': 'Papaya',
        'price': 3.99,
        'stock': 2001
    },
    {
        'name': 'Quince',
        'price': 4.99,
        'stock': 2002
    },
    {
        'name': 'Raspberry',
        'price': 2.99,
        'stock': 2003
    },
    {
        'name': 'Strawberry',
        'price': 4.99,
        'stock': 2004
    },
    {
        'name': 'Tamarind',
        'price': 3.99,
        'stock': 2005
    },
    {
        'name': 'Watermelon',
        'price': 2.99,
        'stock': 2001
    }
]


# Homepage
@app.route('/')
def get_homepage():
    return 'Hello World!'


# GET /fruits
@app.route('/fruits')
def get_fruits():
    return jsonify({'fruits': fruits})


# handle validity data request
def valid_fruit_object(fruit_object):
    if "name" in fruit_object and "price" in fruit_object and "stock" in fruit_object:
        return True
    else:
        return False


# /fruits/stock_number POST request
@app.route('/fruits', methods=['POST'])
def add_fruits():
    request_data = request.get_json()
    if valid_fruit_object(request_data):
        new_fruit = {
            "name": request_data['name'],
            "price": request_data['price'],
            "stock": request_data['stock']
        }
        fruits.insert(0, new_fruit)
        # send response to body
        response = Response('', 201, mimetype='application/json')
        response.headers['Location'] = '/fruits/' + str(new_fruit['stock'])
        return response
    else:
        # handle response for invalid data request
        invalid_fruit_obj_error_msg = {
            "error": "Invalid fruit object passed in request",
            "help_string": "Data passed in similar to this {'name': 'fruitname', 'price': 3.99, 'stock': 2002 }"
        }
        response = Response(json.dumps(invalid_fruit_obj_error_msg), status=400, mimetype='application/json')
        return response


# /fruits/stock_number GET request
@app.route('/fruits/<int:stock>')
def get_fruits_by_stock(stock):
    return_value = {}
    for fruit in fruits:
        if fruit['stock'] == stock:
            return_value = {
                'name': fruit['name'],
                'price': fruit['price']
            }
    return jsonify(return_value)

# Test PUT request
# {
#     "price": 3.99,
#     "stock": 2020
# }


# PUT /fruits/<int:stock>
@app.route('/fruits/<int:stock>', methods=['PUT'])
def replace_fruit(stock):
    request_data = request.get_json()
    new_fruit = {
        'name': request_data['name'],
        'price': request_data['price'],
        'stock': stock
    }

    i = 0
    for fruit in fruits:
        current_stock = fruit["stock"]
        if current_stock == stock:
            fruits[i] = new_fruit
        i += 1
    response = Response("", status=204)
    return response


app.run(port=5000)
