from flask import render_template, flash, redirect, url_for
from app.forms import StartingForm, ProblemForm
from app.calculations import num_solutions
from app import app


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = StartingForm()
    if form.validate_on_submit():
        number_vars = form.number_of_vars.data
        return redirect(url_for('problem'))
    return render_template('index.html', form=form)


@app.route('/problem', methods=['GET', 'POST'])
def problem():
    form = ProblemForm()
    if form.validate_on_submit():
        values = [form.var1.data, form.var2.data, form.var3.data]
        int_solutions = int(num_solutions(values, form.total.data, 3))

        return render_template("problem.html", form=form, int_solutions=int_solutions)

    #  user_addresses = [{"name": "First Address"}, {"name": "Second Address"}]
    #  form = AddressesForm(addresses=user_addresses)

    return render_template("problem.html", form=form)
