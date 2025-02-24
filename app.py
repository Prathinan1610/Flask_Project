from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Product, Location, ProductMovement
from forms import ProductForm, LocationForm, MovementForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products', methods=['GET', 'POST'])
def products():
    form = ProductForm()
    if form.validate_on_submit():
        new_product = Product(product_id=form.product_id.data, name=form.name.data)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('products'))
    products = Product.query.all()
    return render_template('products.html', form=form, products=products)

@app.route('/locations', methods=['GET', 'POST'])
def locations():
    form = LocationForm()
    if form.validate_on_submit():
        new_location = Location(location_id=form.location_id.data, name=form.name.data)
        db.session.add(new_location)
        db.session.commit()
        return redirect(url_for('locations'))
    locations = Location.query.all()
    return render_template('locations.html', form=form, locations=locations)

@app.route('/movements', methods=['GET', 'POST'])
def movements():
    form = MovementForm()
    if form.validate_on_submit():
        new_movement = ProductMovement(
            product_id=form.product_id.data,
            from_location=form.from_location.data or None,
            to_location=form.to_location.data or None,
            qty=form.qty.data
        )
        db.session.add(new_movement)
        db.session.commit()
        return redirect(url_for('movements'))
    movements = ProductMovement.query.all()
    return render_template('movements.html', form=form, movements=movements)

if __name__ == '__main__':
    app.run(debug=True)
