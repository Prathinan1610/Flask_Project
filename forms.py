from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    product_id = StringField('Product ID', validators=[DataRequired()])
    name = StringField('Product Name', validators=[DataRequired()])
    submit = SubmitField('Add Product')

class LocationForm(FlaskForm):
    location_id = StringField('Location ID', validators=[DataRequired()])
    name = StringField('Location Name', validators=[DataRequired()])
    submit = SubmitField('Add Location')

class MovementForm(FlaskForm):
    product_id = StringField('Product ID', validators=[DataRequired()])
    from_location = StringField('From Location')
    to_location = StringField('To Location')
    qty = IntegerField('Quantity', validators=[DataRequired()])
    submit = SubmitField('Move Product')
