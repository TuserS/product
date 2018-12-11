from flask import Flask, jsonify, request, Response
from ProductModel import *
from settings import *
import json


def valid_request_data(request_data):
    if("name" in request_data and "price" in request_data and "quantity" in request_data):
        return True
    else:
        return False


#post /product
@app.route('/product', methods=['POST'])
def add_product():
    request_data = request.get_json()
    if(valid_request_data(request_data)):
        Product.add_product(request_data['name'], request_data['price'], request_data['identity'])
        #json.dumps({"id": str(request_data['identity'],})
        response = Response("", 201, mimetype='application/json')
        response.headers['Location'] = "/product/" + str(request_data['identity'])
        return response
    else:
        invalidMovieObjectErrorMsg = {
            "error": "Invalid product object passed in request",
        }
        response = Response(json.dumps(invalidmovieObjectErrorMsg), status=400, mimetype='application/json')
        return response


#GET /product/<id>/<tag>
@app.route('/product/<int:identity>/<int:tag>')
def get_product_by_tag(identity, tag):
    return_value = Product.get_product_by_tag(tag)
    return jsonify(return_value)


#GET /product
@app.route('/product')
def get_product():
    tags = request.args.get('tags')
    return_value = Product.get_product_by_tag(tags)
    return jsonify(return_value)


#GET /product/<id>
@app.route('/product/<int:identity>')
def get_product_by_id(identity):
    return_value = Product.get_product(identity)
    return jsonify(return_value)


#PUT /product
@app.route('/product', methods=['PUT'])
def update_product(identity):
    request_data = request.get_json()
    if(not valid_request_data(request_data)):
        invalidMovieObjectErrorMsg = {  
            "error": "Valid movie object must be passed in the request",
            "helpString": "Data passed in similar to this {'name':'moviename', 'price':7.99}"
        }
        response = Response(json.dumps(invalidMovieObjectErrorMsg), status=400, mimetype='application/json')
        return response

    Product.update_product(request_data['name'], request_data['price'], request_data['quantity'])
    response = Response("", status=204)
    return response

app.run(port=5000)