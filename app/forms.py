from flask_wtf import FlaskForm
from wtforms import DecimalField, SelectField, SubmitField
from app.converter import all_units, get_unit_options

class ConversionForm(FlaskForm):
    source_unit = SelectField(
        "Source Unit",
        choices = get_unit_options(all_units),
        )

    quantity = DecimalField("Quantity")

    update_targets = SubmitField("Update Target Units")

    target_unit = SelectField(
        "Target Unit",
        choices = get_unit_options(all_units),
        )

    submit = SubmitField("Calculate Conversion")