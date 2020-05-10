from flask import Flask, jsonify, request, Response
import json
from .settings import *

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

DEFAULT_PAGE_LIMIT = 3


# Homepage
@app.route('/')
def get_homepage():
    return 'Hello World!'


# GET /fruits
@app.route('/fruits')
def get_fruits():
    return jsonify({'fruits': fruits})


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


# GET /fruits/page/<int:page_number>
@app.route('/fruits/page/<int:page_number>')
def get_paginated_fruits(page_number):
    print(type(request.args.get('limit')))
    limit = request.args.get('limit', DEFAULT_PAGE_LIMIT, int)
    return jsonify({'fruits': fruits[page_number * limit - limit:page_number * limit]})


# handle validity data request
def valid_fruit_object(fruit_object):
    if "name" in fruit_object and "price" in fruit_object and "stock" in fruit_object:
        return True
    else:
        return False


# POST /fruits/stock_number
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


# Test PUT request
# {
#     "price": 3.99,
#     "stock": 2020
# }

# Check validity when PUT request
def valid_put_request_data(request_data):
    if "name" in request_data and "price" in request_data:
        return True
    else:
        return False


# PUT /fruits/<int:stock>
@app.route('/fruits/<int:stock>', methods=['PUT'])
def replace_fruit(stock):
    request_data = request.get_json()

    # handle invalid data
    if not valid_put_request_data(request_data):
        invalid_fruit_obj_error_msg = {
            "error": "Invalid fruit object passed in request",
            "help_string": "Data passed in similar to this {'name': 'fruitname', 'price': 3.99, 'stock': 2002 }"
        }
        response = Response(json.dumps(invalid_fruit_obj_error_msg), status=400, mimetype='application/json')
        return response

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


# Test PATCH request name or price only
# {
# 	"name": "Avocado"
# }

# PATCH /fruits/<int:stock>
@app.route('/fruits/<int:stock>', methods=['PATCH'])
def update_fruit(stock):
    request_data = request.get_json()
    updated_fruit = {}
    if "name" in request_data:
        updated_fruit["name"] = request_data['name']

    if "price" in request_data:
        updated_fruit["price"] = request_data['price']

    for fruit in fruits:
        if fruit["stock"] == stock:
            fruit.update(updated_fruit)

    response = Response("", status=204)
    response.headers['Location'] = "/fruits/" + str(stock)
    return response


# DELETE /fruits/<int:stock>
@app.route('/fruits/<int:stock>', methods=['DELETE'])
def delete_fruit(stock):
    i = 0
    for fruit in fruits:
        if fruit["stock"] == stock:
            fruits.pop(i)
            response = Response("", status=204)
            return response
        i += 1

    invalid_fruit_obj_error_msg = {
        "error": "Fruit with stock number provided not found, so unable to delete.",
    }
    response = Response(json.dumps(invalid_fruit_obj_error_msg), status=404, mimetype='application/json')
    return response


app.run(port=5000)
