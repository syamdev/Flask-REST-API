import json
import datetime
import jwt
from FruitModel import *
from flask import jsonify, request, Response
from settings import *

DEFAULT_PAGE_LIMIT = 3

app.config['SECRET_KEY'] = 'yummy'


# Login '/login'
@app.route('/login')
def get_token():
    expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=100)
    token = jwt.encode({'exp': expiration_date}, app.config['SECRET_KEY'], algorithm='HS256')
    return token


# # GET /fruits/page/1?limit=100
# @app.route('/fruits/page/<int:page_number>')
# def get_paginated_fruits(page_number):
#     print(type(request.args.get('limit')))
#     limit = request.args.get('limit', DEFAULT_PAGE_LIMIT, int)
#     start_index = page_number * limit - limit
#     end_index = page_number * limit
#     print(start_index)
#     print(end_index)
#     return jsonify({'fruits': fruits[start_index:end_index]})


# Homepage
@app.route('/')
def get_homepage():
    return 'Hello World!'


# GET /fruits?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9
@app.route('/fruits')
def get_fruits():
    token = request.args.get('token')
    try:
        jwt.decode(token, app.config['SECRET_KEY'])
    except Exception as e:
        return jsonify({'error': 'Need a valid token to view this page', 'msg': str(e)}), 401

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
