from flask import jsonify, request, Response
from FruitModel import *
from settings import *
import json


DEFAULT_PAGE_LIMIT = 3


# Homepage
@app.route('/')
def get_homepage():
    return 'Hello World!'


# GET /fruits
@app.route('/fruits')
def get_fruits():
    return jsonify({'fruits': Fruit.get_all_fruits()})


# /fruits/stock_number GET request
@app.route('/fruits/<int:stock>')
def get_fruits_by_stock(stock):
    return_value = Fruit.get_fruit(stock)
    return jsonify(return_value)


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
        Fruit.add_fruit(request_data['name'], request_data['price'], request_data['stock'])

        response = Response('', 201, mimetype='application/json')
        response.headers['Location'] = '/fruits/' + str(request_data['stock'])
        return response
    else:
        # handle response for invalid data request
        invalid_fruit_obj_error_msg = {
            "error": "Invalid fruit object passed in request",
            "help_string": "Data passed in similar to this {'name': 'fruitname', 'price': 3.99, 'stock': 2002 }"
        }
        response = Response(json.dumps(invalid_fruit_obj_error_msg), status=400, mimetype='application/json')
        return response


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

    Fruit.replace_fruit(stock, request_data['name'], request_data['price'])

    response = Response("", status=204)
    return response


# Check validity when PATCH request
def valid_patch_request_data(request_data):
    if "name" in request_data or "price" in request_data:
        return True
    else:
        return False

# PATCH /fruits/<int:stock>
@app.route('/fruits/<int:stock>', methods=['PATCH'])
def update_fruit(stock):
    request_data = request.get_json()

    # handle invalid data
    if not valid_patch_request_data(request_data):
        invalid_fruit_obj_error_msg = {
            "error": "Invalid fruit object passed in request",
            "help_string": "Data passed in similar to this {'name': 'fruitname', 'price': 3.99, 'stock': 2002 }"
        }
        response = Response(json.dumps(invalid_fruit_obj_error_msg), status=400, mimetype='application/json')
        return response

    if "name" in request_data:
        Fruit.update_fruit_name(stock, request_data['name'])

    if "price" in request_data:
        Fruit.update_fruit_price(stock, request_data['price'])

    response = Response("", status=204)
    response.headers['Location'] = "/fruits/" + str(stock)
    return response


# DELETE /fruits/<int:stock>
@app.route('/fruits/<int:stock>', methods=['DELETE'])
def delete_fruit(stock):
    if Fruit.delete_fruit(stock):
        response = Response("", status=204)
        return response

    invalid_fruit_obj_error_msg = {
        "error": "Fruit with stock number provided not found, so unable to delete.",
    }
    response = Response(json.dumps(invalid_fruit_obj_error_msg), status=404, mimetype='application/json')
    return response


app.run(port=5000)
