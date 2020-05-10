from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app

db = SQLAlchemy(app)


class Fruit(db.Model):
    __tablename__ = 'fruits'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer)

    # commands to create model in console
    # from FruitModel import db
    # db.create_all()

    def json(self):
        return {'name': self.name, 'price': self.price, 'stock': self.stock}

    def add_fruit(_name, _price, _stock):
        new_fruit = Fruit(name=_name, price=_price, stock=_stock)
        db.session.add(new_fruit)
        db.session.commit()

    def get_all_fruits():
        return [Fruit.json(fruit) for fruit in Fruit.query.all()]

    def get_fruit(_stock):
        return Fruit.query.filter_by(stock=_stock).first()

    def delete_fruit(_stock):
        Fruit.query.filter_by(stock=_stock).delete()
        db.session.commit()

    def update_fruit_name(_stock, _name):
        fruit_to_update = Fruit.query.filter_by(stock=_stock).first()
        fruit_to_update.name = _name
        db.session.commit()

    def update_fruit_price(_stock, _price):
        fruit_to_update = Fruit.query.filter_by(stock=_stock).first()
        fruit_to_update.price = _price
        db.session.commit()

    def replace_fruit(_stock, _name, _price):
        fruit_to_replace = Fruit.query.filter_by(stock=_stock).first()
        fruit_to_replace.name = _name
        fruit_to_replace.price = _price
        db.session.commit()

    def __repr__(self):
        fruit_object = {
            'name': self.name,
            'price': self.price,
            'stock': self.stock
        }
        return json.dumps(fruit_object)

    # Test add data to db on console
    # from FruitModel import *
    # Fruit.add_fruit("Avocado", 3.99, 2000)
    # Fruit.get_all_fruits()
    # result: [{"name": "Avocado", "price": 3.99, "stock": 2000}]
