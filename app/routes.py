from flask import request, render_template
from app import app
from app.forms import ConversionForm
from app.converter import get_unit_options, get_possible_conversions, get_conversion_factor

@app.route('/', methods = ["GET", "POST"])
def home():
    form = ConversionForm()
    source = request.form.get("source_unit")
    result = None

    if source:
        possible_targets = get_possible_conversions(source)
        form.target_unit.choices = get_unit_options(possible_targets)

    if form.validate_on_submit():
        if form.submit.data: # submit button pressed
            source = form.source_unit.data
            target = form.target_unit.data
            quantity = float(form.quantity.data)
            result = get_conversion_factor(source, target) * quantity
            result = round(result, 3)

    return render_template("home.html", form = form, result = result)