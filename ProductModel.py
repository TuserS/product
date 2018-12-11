from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app

db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__='products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer)
    tags = db.Column(db.String(100), nullable=True)

    def json(self):
        return {'name': self.name, 'price': self.price, 'identity': self.quantity}

    def add_product(_name, _price, _quantity):
        new_product = Product(name=_name, price=_price, quantity=_quantity)
        db.session.add(new_product)
        db.session.commit()
    
    def get_product(_identity):
        return Product.query.filter_by(identity=_identity).first()
    
    def get_product_by_tag(_tags):
        return Product.query.filter_by(tags=_tags).first()

    def add_product_tag(_identity, _tag):
        product_to_update = Product.query.filter_by(identity=_identity).first()
        product_to_update.tag = _tag
        db.session.commit()

    def update_product(_name, _price,  _quantity):
        product_to_update = Product.query.filter_by(name=_name).first()
        product_to_update.price = _price
        product_to_update.name = _name
        product_to_update.quantity = _quantity
        db.session.commit()